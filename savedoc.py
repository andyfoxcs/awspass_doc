import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import re
from collections import deque

class AsyncJavadocScraper:
    def __init__(self, base_url, max_concurrent=20, delay=0.1):
        self.base_url = base_url.rstrip('/') + '/'
        self.max_concurrent = max_concurrent
        self.delay = delay
        self.visited_urls = set()
        self.url_queue = deque()
        self.all_content = []
        self.semaphore = asyncio.Semaphore(max_concurrent)
        
        # 添加起始URL
        self.url_queue.append(self.base_url + "index.html")

    async def scrape_all(self, output_file="async_javadoc_llms.txt"):
        """异步爬取所有页面"""
        print(f"开始异步爬取，最大并发数: {self.max_concurrent}")
        start_time = time.time()
        
        # 创建会话
        connector = aiohttp.TCPConnector(limit=self.max_concurrent, limit_per_host=10)
        timeout = aiohttp.ClientTimeout(total=30)
        
        async with aiohttp.ClientSession(
            connector=connector, 
            timeout=timeout,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            }
        ) as session:
            
            # 创建任务列表
            tasks = []
            processed_count = 0
            max_pages = 500  # 限制最大页面数，避免无限爬取
            
            while self.url_queue and processed_count < max_pages:
                # 控制并发数量
                current_tasks = []
                for _ in range(min(self.max_concurrent, len(self.url_queue))):
                    if self.url_queue:
                        url = self.url_queue.popleft()
                        if url not in self.visited_urls:
                            self.visited_urls.add(url)
                            task = asyncio.create_task(self.process_url(session, url))
                            current_tasks.append(task)
                
                # 等待当前批次任务完成
                if current_tasks:
                    results = await asyncio.gather(*current_tasks, return_exceptions=True)
                    for result in results:
                        if isinstance(result, Exception):
                            print(f"异步任务出错: {result}")
                        elif result:
                            content, new_links = result
                            if content:
                                self.all_content.append(content)
                                processed_count += 1
                            
                            # 添加新链接到队列
                            for link in new_links:
                                if link not in self.visited_urls and link not in self.url_queue:
                                    self.url_queue.append(link)
                    
                    # 控制请求频率
                    await asyncio.sleep(self.delay)
            
            # 保存结果
            self.save_to_file(output_file)
            elapsed_time = time.time() - start_time
            print(f"异步爬取完成！共处理 {len(self.all_content)} 个页面，耗时 {elapsed_time:.2f} 秒")

    async def process_url(self, session, url):
        """处理单个URL"""
        async with self.semaphore:
            try:
                async with session.get(url) as response:
                    if response.status != 200:
                        print(f"页面 {url} 返回状态码: {response.status}")
                        return None, []
                    
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # 提取内容
                    content = self.extract_content(soup, url)
                    
                    # 发现新链接
                    new_links = self.find_links(soup, url)
                    
                    return content, new_links
                    
            except Exception as e:
                print(f"处理URL {url} 时出错: {e}")
                return None, []

    def find_links(self, soup, base_url):
        """发现页面中的所有相关链接"""
        links = set()
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            
            # 过滤不需要的链接
            if any(skip in href for skip in ['javascript:', 'mailto:', '#']):
                continue
            
            # 处理相对链接
            full_url = urljoin(base_url, href)
            
            # 只关注本站点内的HTML页面
            if (self.base_url in full_url and 
                href.endswith('.html') and
                not any(skip in full_url.lower() for skip in ['index.html', 'help-doc.html'])):
                links.add(full_url)
        
        return list(links)

    def extract_content(self, soup, url):
        """提取页面内容"""
        content_lines = []
        
        # 提取页面标题
        title = soup.find('title')
        if title:
            content_lines.append(f"# PAGE: {title.text.strip()}")
        
        content_lines.append(f"# URL: {url}")
        
        # 智能内容提取
        content_lines.extend(self.smart_content_extraction(soup))
        
        return "\n".join(content_lines)

    def smart_content_extraction(self, soup):
        """智能内容提取，针对Javadoc结构优化"""
        content = []
        
        # 1. 提取类/接口信息
        class_elements = soup.find_all(['h1', 'h2'], class_=lambda x: x and 'title' in x)
        for elem in class_elements:
            text = elem.get_text(strip=True)
            if text and len(text) > 5:
                content.append(f"[TITLE] {text}")
        
        # 2. 提取描述性文本
        desc_blocks = soup.find_all('div', class_=lambda x: x and any(cls in x for cls in ['description', 'block']))
        for block in desc_blocks:
            text = block.get_text(separator=' ', strip=True)
            if text and len(text) > 20:  # 过滤太短的描述
                content.append(f"[DESCRIPTION] {text}")
        
        # 3. 提取方法签名（Javadoc特定）
        method_signatures = soup.find_all('code')
        for code in method_signatures:
            text = code.get_text(strip=True)
            if text and '(' in text and ')' in text:  # 可能是方法签名
                content.append(f"[METHOD_SIGNATURE] {text}")
        
        # 4. 提取表格内容
        tables = soup.find_all('table')
        for i, table in enumerate(tables):
            caption = table.find('caption')
            table_title = caption.get_text(strip=True) if caption else f"Table_{i+1}"
            
            rows = table.find_all('tr')
            if len(rows) > 1:  # 至少有标题行和数据行
                content.append(f"[TABLE] {table_title}")
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    row_text = ' | '.join(cell.get_text(strip=True) for cell in cells)
                    if row_text:
                        content.append(f"  {row_text}")
        
        return content

    def save_to_file(self, output_file):
        """保存结果到文件"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# AWS Javadoc 异步爬取结果\n")
            f.write(f"# 源地址: {self.base_url}\n")
            f.write(f"# 生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# 总页面数: {len(self.all_content)}\n\n")
            
            for i, content in enumerate(self.all_content):
                f.write(f"=== 页面 {i+1} ===\n")
                f.write(content)
                f.write("\n\n" + "="*80 + "\n\n")

# 使用示例
async def main():
    base_url = "https://docs.awspaas.com/api/aws-api-javadoc/"
    scraper = AsyncJavadocScraper(base_url, max_concurrent=25, delay=0.05)
    await scraper.scrape_all("async_aws_javadoc.txt")

if __name__ == "__main__":
    # 运行异步爬虫
    asyncio.run(main())