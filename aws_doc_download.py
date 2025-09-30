import os
import requests
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urljoin, urlparse
import time
import re
import json

class StructuredAWSDocsCrawler:
    def __init__(self, base_url, output_dir="aws_docs"):
        self.base_url = base_url
        self.output_dir = output_dir
        self.visited_urls = set()
        self.url_mapping = {}
        self.navigation_structure = []
        
        # 配置html2text
        self.h = html2text.HTML2Text()
        self.h.ignore_links = False
        self.h.ignore_images = False
        self.h.body_width = 0
        self.h.protect_links = True
        
        # 创建输出目录
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def is_awspaas_domain(self, url):
        """检查URL是否属于awspaas.com域名"""
        parsed = urlparse(url)
        return parsed.netloc.endswith('awspaas.com')
    
    def get_site_base(self):
        """获取站点基础URL"""
        parsed = urlparse(self.base_url)
        return f"{parsed.scheme}://{parsed.netloc}"
    
    def get_full_url(self, url):
        """将相对URL转换为绝对URL"""
        if url.startswith('http'):
            return url
        return urljoin(self.base_url, url)
    
    def extract_navigation_structure(self, soup):
        """提取完整的导航结构"""
        navigation = []
        summary = soup.find('ul', class_='summary')
        
        if summary:
            for item in summary.find_all('li', recursive=False):
                nav_item = self._parse_nav_item(item)
                if nav_item:
                    navigation.append(nav_item)
        
        return navigation
    
    def _parse_nav_item(self, li_element):
        """解析单个导航项"""
        link = li_element.find('a', href=True)
        if not link:
            return None
        
        # 清理标题文本
        title = link.get_text().strip()
        # 移除标题中的数字前缀（如 "1. "）
        title = re.sub(r'^\d+\.\s*', '', title)
        
        full_url = self.get_full_url(link['href'])
        
        # 只处理awspaas.com域名的链接
        if not self.is_awspaas_domain(full_url):
            return None
        
        item = {
            'title': title,
            'url': full_url,
            'level': li_element.get('data-level', '0'),
            'path': li_element.get('data-path', ''),
            'children': []
        }
        
        # 处理子项
        sub_ul = li_element.find('ul', class_='articles')
        if sub_ul:
            for sub_li in sub_ul.find_all('li', recursive=False):
                sub_item = self._parse_nav_item(sub_li)
                if sub_item:
                    item['children'].append(sub_item)
        
        return item
    
    def get_all_navigation_urls(self, navigation):
        """从导航结构中获取所有URL"""
        urls = []
        
        def extract_urls(items):
            for item in items:
                # 只添加awspaas.com域名的URL
                if self.is_awspaas_domain(item['url']):
                    urls.append(item['url'])
                if item['children']:
                    extract_urls(item['children'])
        
        extract_urls(navigation)
        return urls
    
    def get_local_filepath(self, url):
        """根据URL生成本地文件路径"""
        parsed = urlparse(url)
        path = parsed.path
        
        # 移除开头的斜杠
        if path.startswith('/'):
            path = path[1:]
        
        # 如果路径为空或者是目录，使用index.md
        if not path or path.endswith('/'):
            path = os.path.join(path, "index.md") if path else "index.md"
        elif path.endswith('.html'):
            path = path[:-5] + '.md'
        else:
            path = path + '.md'
        
        # 确保路径在输出目录内
        full_path = os.path.join(self.output_dir, path)
        return full_path
    
    def create_directory_structure(self, filepath):
        """创建目录结构"""
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
    
    def safe_find(self, element, selector, method='select_one', default=None):
        """安全地查找元素，避免NoneType错误"""
        try:
            if method == 'select_one':
                result = element.select_one(selector)
            elif method == 'find':
                result = element.find(selector)
            elif method == 'find_all':
                result = element.find_all(selector)
            else:
                return default
                
            return result if result is not None else default
        except Exception:
            return default
    
    def extract_page_content(self, soup, url):
        """直接提取page-inner下的内容，包含图片链接"""
        try:
            # 获取页面标题
            title_tag = self.safe_find(soup, 'title', method='find')
            page_title = title_tag.get_text().strip() if title_tag else "未命名文档"
            
            print(f"提取页面: {page_title}")
            
            # 直接获取page-inner内容
            page_inner = self.safe_find(soup, 'div.page-inner', method='select_one')
            
            if not page_inner:
                print(f"警告: 无法找到page-inner内容区域")
                # 尝试其他内容区域
                content_selectors = [
                    'section.normal',
                    'div.body-inner',
                    'div.book-body',
                    '.page-wrapper',
                    '.content'
                ]
                
                for selector in content_selectors:
                    page_inner = self.safe_find(soup, selector, method='select_one')
                    if page_inner:
                        print(f"使用备选选择器找到内容: {selector}")
                        break
            
            
            if not page_inner:
                print(f"错误: 无法找到任何内容区域")
                return None, page_title
            
            # 创建主要内容副本
            main_content = page_inner
            
            
            # 移除不需要的元素
            unwanted_selectors = [
                'script', 'style', 'nav', 'header', 'footer',
                '.navbar', '.book-header', '.book-summary', 
                '.navigation', '.toggle-search', '.sharing-link', 
                '.toggle-dropdown', '.book-search', '.gitbook-link', 
                '.font-settings-wrapper'
            ]
            
            for selector in unwanted_selectors:
                elements = self.safe_find(main_content, selector, method='find_all', default=[])
                for element in elements:
                    if element:
                        element.decompose()
            
            # 先移除AWS特定的元素（在延伸阅读清理之前）
            aws_classes = [
                'aws_header',
                'aws_m_link', 
                'aws_content',
                'aws_i_main',
                'aws_i_user',
                'aws_i_telephone',
                'aws_i_mail',
                'aws_i_inner',
                'aws_i_img'
            ]
            
            for aws_class in aws_classes:
                # 直接使用select方法清理AWS元素
                elements = main_content.select(f'.{aws_class}')
                for element in elements:
                    if element:
                        element.decompose()
            
            # 精确移除【延伸阅读】部分
            try:
                # 查找包含"延伸阅读"的h3标题
                extended_reading_headers = main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'], 
                                                               string=re.compile(r'延伸阅读'))
                
                for header in extended_reading_headers:
                    # 找到包含延伸阅读内容的容器
                    current_element = header
                    elements_to_remove = [header]
                    
                    # 查找直到下一个同级标题或容器结束的所有元素
                    while True:
                        current_element = current_element.find_next_sibling()
                        if current_element is None:
                            break
                        
                        # 如果遇到下一个标题，停止
                        if current_element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                            break
                        
                        # 将元素添加到移除列表
                        elements_to_remove.append(current_element)
                    
                    # 移除所有相关元素
                    for element in elements_to_remove:
                        if element and element in main_content:
                            element.decompose()
                    
                    print(f"已移除延伸阅读部分: {header.get_text().strip()}")
                    
            except Exception as e:
                print(f"移除延伸阅读时出错: {e}")
            
            # 额外处理：移除空元素（但保留img标签）
            empty_elements = main_content.find_all(lambda tag: (
                not tag.get_text().strip() and 
                not tag.find_all() and 
                tag.name not in ['img', 'br', 'hr', 'input', 'area', 'base', 'col', 'embed', 'link', 'meta', 'source', 'track', 'wbr']
            ))
            for element in empty_elements:
                if element:
                    element.decompose()
            
            return main_content, page_title
            
        except Exception as e:
            print(f"提取页面内容失败: {e}")
            import traceback
            traceback.print_exc()
            return None, "提取失败"
    
    def convert_html_to_markdown_with_images(self, html_content, url):
        """将HTML转换为Markdown，确保图片链接正确写入"""
        try:
            if not html_content:
                return ""
            
            # 确保我们有BeautifulSoup对象
            soup = BeautifulSoup(str(html_content), 'html.parser') if not hasattr(html_content, 'find_all') else html_content
            
            # 首先处理所有图片 - 这是最重要的部分
            images = soup.find_all('img')
            print(f"找到 {len(images)} 张图片需要处理")
            
            
            for img in images:
                src = img.get('src', '')
                alt = img.get('alt', '')
                
                if src:
                    # 转换为绝对URL
                    if not src.startswith('http'):
                        src = urljoin(url, src)
                    
                    print(f"图片原始路径: {img.get('src', '')} -> 转换后路径: {src}")
                    
                    # 更新img标签的src属性为绝对URL
                    img['src'] = src
            
            # 使用html2text处理HTML，它会自动处理图片
            html_string = str(soup)
            content_md = self.h.handle(html_string)
            
            # 清理格式
            content_md = re.sub(r'\n{3,}', '\n\n', content_md)
            content_md = content_md.strip()
            
            return content_md
            
        except Exception as e:
            print(f"Markdown转换失败: {e}")
            import traceback
            traceback.print_exc()
            
            # 如果失败，回退到直接使用html2text
            try:
                html_string = str(html_content)
                content_md = self.h.handle(html_string)
                content_md = re.sub(r'\n{3,}', '\n\n', content_md)
                content_md = content_md.strip()
                return content_md
            except:
                return ""
    
    def convert_to_markdown(self, html_content, url, title):
        """将HTML内容转换为Markdown，确保图片链接正确写入"""
        if html_content is None:
            return f"# {title}\n\n> 此页面内容无法正常提取。"
        
        try:
            # 使用转换方法
            content_md = self.convert_html_to_markdown_with_images(html_content, url)
            
            # 添加标题
            markdown = f"# {title}\n\n{content_md}"
            
            return markdown
            
        except Exception as e:
            print(f"转换Markdown失败: {e}")
            import traceback
            traceback.print_exc()
            return f"# {title}\n\n> 页面处理失败: {str(e)}"
    
    def crawl_page(self, url):
        """爬取单个页面"""
        if url in self.visited_urls:
            return
        
        # 只处理awspaas.com域名的页面
        if not self.is_awspaas_domain(url):
            print(f"跳过非awspaas.com域名: {url}")
            return
        
        print(f"正在爬取: {url}")
        self.visited_urls.add(url)
        
        try:
            # 发送请求
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
            
            response = requests.get(url, headers=headers, timeout=15)
            response.encoding = 'utf-8'
            
            if response.status_code != 200:
                print(f"请求失败: {url}, 状态码: {response.status_code}")
                # 保存错误信息
                filepath = self.get_local_filepath(url)
                self.create_directory_structure(filepath)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# 页面获取失败\n\n状态码: {response.status_code}\nURL: {url}")
                return
            
            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取主要内容和标题
            content, title = self.extract_page_content(soup, url)
            
            # 生成本地文件路径
            filepath = self.get_local_filepath(url)
            
            # 创建目录结构
            self.create_directory_structure(filepath)
            
            # 转换为markdown
            markdown_content = self.convert_to_markdown(content, url, title)
            
            # 保存文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            # 保存URL映射
            self.url_mapping[url] = filepath
            
            print(f"已保存: {filepath}")
            
        except Exception as e:
            print(f"爬取失败 {url}: {str(e)}")
            import traceback
            traceback.print_exc()
            
            # 即使失败也创建一个占位文件
            try:
                filepath = self.get_local_filepath(url)
                self.create_directory_structure(filepath)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# 页面爬取失败\n\n错误: {str(e)}\nURL: {url}")
                self.url_mapping[url] = filepath
            except:
                pass
    
    def save_navigation_structure(self):
        """保存导航结构"""
        nav_file = os.path.join(self.output_dir, "navigation.json")
        
        with open(nav_file, 'w', encoding='utf-8') as f:
            json.dump(self.navigation_structure, f, ensure_ascii=False, indent=2)
        
        print(f"导航结构已保存: {nav_file}")
    
    def save_url_mapping(self):
        """保存URL映射"""
        mapping_file = os.path.join(self.output_dir, "url_mapping.json")
        
        with open(mapping_file, 'w', encoding='utf-8') as f:
            json.dump(self.url_mapping, f, ensure_ascii=False, indent=2)
        
        print(f"URL映射已保存: {mapping_file}")
    
    def create_readme_index(self):
        """创建README索引文件"""
        readme_content = """# AWS BPMN2 Event参考指南

本文档是通过爬虫自动生成的AWS PaaS BPMN2事件参考指南的本地副本。

## 文档结构

"""
        
        def build_index(nav_items, level=0):
            content = ""
            for item in nav_items:
                indent = "  " * level
                local_path = self.get_local_filepath(item['url'])
                relative_path = os.path.relpath(local_path, self.output_dir)
                
                if os.path.exists(local_path):
                    content += f"{indent}- [{item['title']}]({relative_path})\n"
                else:
                    content += f"{indent}- {item['title']} (未爬取)\n"
                
                if item['children']:
                    content += build_index(item['children'], level + 1)
            return content
        
        readme_content += build_index(self.navigation_structure)
        
        # 添加统计信息
        readme_content += f"\n## 统计信息\n\n"
        readme_content += f"- 总页面数: {len(self.visited_urls)}\n"
        readme_content += f"- 生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        readme_content += f"- 源地址: {self.base_url}\n"
        
        # 保存README文件
        readme_file = os.path.join(self.output_dir, "README.md")
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"索引文件已创建: {readme_file}")
    
    def crawl_by_navigation(self):
        """根据导航结构爬取所有页面"""
        print("正在获取导航结构...")
        
        try:
            # 获取首页来提取导航
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
            
            response = requests.get(self.base_url, headers=headers, timeout=15)
            response.encoding = 'utf-8'
            
            if response.status_code != 200:
                print(f"无法获取首页，状态码: {response.status_code}")
                return
            
            # 解析导航结构
            soup = BeautifulSoup(response.text, 'html.parser')
            self.navigation_structure = self.extract_navigation_structure(soup)
            
            if not self.navigation_structure:
                print("无法提取导航结构")
                return
            
            print("导航结构提取成功，开始爬取页面...")
            
            # 从导航结构中获取所有URL
            all_urls = self.get_all_navigation_urls(self.navigation_structure)
            print(f"发现 {len(all_urls)} 个页面需要爬取")
            
            # 爬取所有页面
            for i, url in enumerate(all_urls, 1):
                print(f"\n进度: {i}/{len(all_urls)}")
                self.crawl_page(url)
                time.sleep(1)  # 添加延迟避免请求过快
            
            # 保存元数据
            self.save_navigation_structure()
            self.save_url_mapping()
            self.create_readme_index()
            
            print(f"\n爬取完成! 共爬取 {len(self.visited_urls)} 个页面")
            
        except Exception as e:
            print(f"爬取过程出错: {str(e)}")
            import traceback
            traceback.print_exc()

def main():
    # 首页地址
    # AWS BPMN2 Event参考指南
    # https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/index.html
    
    # AWS 流程事件开发参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/index.html"
    
    # AWS 流程事件开发参考指南 6.4GA
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/index.html"
    
    # 定时器开发指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/index.html"
    
    # AWS CC连接中心参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/"
    
    # AWS PaaS API参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-api-guide/index.html"
    
    # AWS MVC框架参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/index.html"
    
    # AWS 移动开发参考指南
    # base_url ="https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/index.html"

    # AWS 插件扩展开发参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/index.html"
    
    # AWS PaaS多语言开发参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-language-reference-guide/index.html"
    
    # AWS BPMN2 Process参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/index.html"
    
    # AWS BPMN2 Event参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/index.html"
    
    # AWS BPMN2 Gateway参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/index.html"

    # AWS BPMN2 Activity参考指南
    # base_url ="https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/index.html"

    # AWS PAL流程梳理到执行参考指南
    # base_url ="https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/index.html"
    
    # AWS SLA参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/index.html"
    
    # AWS LOG日志参考指南
    # base_url ="https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/index.html"
    
    # AWS PaaS应用容器与资源控制参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/index.html"
    
    # AWS 流程引擎对WCP的支持评估
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-wcp-reference-guide/index.html"
    
    # 表单模型
    # base_url ="https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/index.html"

    # 存储模型
    # base_url = "https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/"
    
    # 流程模型
    # base_url = "https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/"
    
    # 数据窗口
    # base_url = "https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/"

    # AWS 定时器开发参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/index.html"
    
    # AWS CC连接中心参考指南 
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/"
    
    # 服务编排(Dataflow)
    # base_url = "https://docs.awspaas.com/apps/com.actionsoft.apps.dataflow/"

    # AWS @公式参考指南
    # base_url = "https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html"

    # AWS UI组件参考指南
    base_url = "https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/index.html"

    # 创建爬虫实例
    crawler = StructuredAWSDocsCrawler(base_url, "aws_docs")
    
    # 开始爬取
    crawler.crawl_by_navigation()

if __name__ == "__main__":
    main()