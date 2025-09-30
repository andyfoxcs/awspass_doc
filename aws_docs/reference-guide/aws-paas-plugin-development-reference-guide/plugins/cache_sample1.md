# 不过期缓存示例 · AWS PaaS文档中心

## 不过期缓存示例

这是最常见的缓存设计方案。启动该缓存时，load()方法负责将对象放入缓存中，程序需要时直接从缓存中读取，你的持久层（DAO、XML、File...）在发生变化时（如被更新、被插入、被删除）调用缓存的put和remove方法同步缓存。AWS的Cache框架会自动完成集群各节点的缓存副本同步。

适用于数据规模不大的主数据/配置数据，如在几万条记录之内。如果缓存对象的数量或单一对象字节过大，应合理计算并设置JVM的最大可用内存，以防止内存溢出。

源码见`扩展插件概念验证`应用

### BookCache

> com.actionsoft.apps.poc.plugin.cache.BookCache
    
    
    package com.actionsoft.apps.poc.plugin.cache;
    
    import java.util.ArrayList;
    import java.util.Comparator;
    import java.util.Iterator;
    import java.util.List;
    
    import com.actionsoft.apps.resource.plugin.profile.CachePluginProfile;
    import com.actionsoft.bpms.commons.cache.Cache;
    import com.actionsoft.bpms.commons.cache.CacheManager;
    
    public class BookCache extends Cache<String, BookModel> {
    
        public BookCache(CachePluginProfile profile) {
            super(profile);
        }
    
        /**
         * 让Cache使用者直接访问到内部封装的操作，如put/remove
         *
         * @return
         */
        public static BookCache getCache() {
            return CacheManager.getCache(BookCache.class);
        }
    
        /**
         * 初始化缓存。通常这里从DAO或其他持久数据中完成初始化过程
         */
        protected void load() {
            // 模拟一个持久层数据结构
            List<BookModel> list = new ArrayList<>();
            list.add(new BookModel("001", "北平无战事", 1000, 41.3d, 2014));
            list.add(new BookModel("002", "大江东去", 600, 115.9d, 2013));
            list.add(new BookModel("003", "永恒的终结", 1200, 22.9d, 2014));
            list.add(new BookModel("004", "你总会路过这个世界的美好", 70, 25.9d, 2014));
            list.add(new BookModel("005", "银河系搭车客指南系列", 890, 11.74d, 2012));
            for (BookModel book : list) {
                // 放入本地缓存
                put(book.getId(), book, false);
            }
        }
    }
    

### 将BookCache注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.cache.BookCache;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.CachePluginProfile;
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            // 注册Cache
            list.add(new CachePluginProfile(BookCache.class));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`BookCache`，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/cache-1.png)](<cache-1.png>)

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`CacheSample`，在弹出的对话框中点击`缓存示例`按钮，你会看到页面返回如下类似信息

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/cache-2.png)](<cache-2.png>)

#### 对话框部分的代码示例

> com.actionsoft.apps.poc.plugin.web.SampleWeb#getCacheSampleHome1
>     
>     
>     public String getCacheSampleHome1() {
>         StringBuilder data = new StringBuilder();
>         data.append("<b>BookCache</b><hr>\n");
>         data.append("<b>.size()</b>=" + BookCache.getCache().size()).append("<br/>");
>         long time = System.currentTimeMillis();
>         BookModel book = new BookModel(SDK.getPlatformAPI().getAWSServer().getInstanceName() + "-" + Long.toString(time), "书(" + time + ")", 1, 1d, 2015);
>         data.append("<b>.put()</b><br/>");
>         BookCache.getCache().put(book.getId(), book);
>         data.append("<b>.size()</b>=" + BookCache.getCache().size()).append("<br/>");
>         Iterator<BookModel> iterator = BookCache.getCache().iterator();
>         data.append("<b>.iterator()</b><br/>");
>         while (iterator.hasNext()) {
>             BookModel bookModel = iterator.next();
>             data.append(bookModel.toJson()).append("<br/>");
>         }
>         Map<String, Object> macroLibraries = new LinkedHashMap<String, Object>();
>         macroLibraries.put("data", data.toString());
>         macroLibraries.put("sid", getContext().getSessionId());
>         return HtmlPageTemplate.merge("com.actionsoft.apps.poc.plugin", "cache-sample-dialog.htm", macroLibraries);
>     }
>