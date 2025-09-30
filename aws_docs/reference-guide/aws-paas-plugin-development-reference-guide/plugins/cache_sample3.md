# 缓存索引示例 · AWS PaaS文档中心

## 缓存索引示例

AWS的Cache本质上是基于键/值的ConcurrentHashMap，通过哈希快速命中缓存对象（值）。如果你需要遍历缓存并从值对象的某个属性中匹配查询，AWS Cache还提供一种更高效的索引模式。

  * 缓存唯一索引
  * 缓存多值索引

> 在某种查询频繁且遍历的数据量较大时，建立缓存索引能明显改善性能，同时AWS Cache也会为维护索引增加一定的开销。因此，为缓存建立索引应保持适度、合理的原则。

AWS Cache自动维护索引的主要开销

  * put/remove等发生结构变化时，同步维护Index结构
  * 每个Index会增加一份链表结构，但不会增加值副本

源码见`扩展插件概念验证`应用

### 缓存唯一索引

继承`SingleValueIndex`父类，要求这类查询的业务key值必须不能重复。

> com.actionsoft.apps.poc.plugin.cache.BookIndex1
    
    
    package com.actionsoft.apps.poc.plugin.cache;
    
    import com.actionsoft.bpms.commons.cache.SingleValueIndex;
    
    /**
     * 索引示例。为“书名”字段建立缓存唯一索引。要求“书名”字段值不能有重复的
     */
    public class BookIndex1 extends SingleValueIndex<String, BookModel> {
    
        /**
         * 返回该索引的键值
         */
        public String key(BookModel model) {
            return model.getName();
        }
    
    }
    

### 缓存多值索引

继承`ListValueIndex`父类。

> com.actionsoft.apps.poc.plugin.cache.BookIndex2
    
    
    package com.actionsoft.apps.poc.plugin.cache;
    
    import com.actionsoft.bpms.commons.cache.ListValueIndex;
    
    /**
     * 索引示例。为“出版年份”字段建立缓存多值索引，快速索引到某年份的书
     */
    public class BookIndex2 extends ListValueIndex<String, BookModel> {
    
        /**
         * 返回该索引的键值
         */
        public String key(BookModel model) {
            return Integer.toString(model.getYear());
        }
    
    }
    

### BookCache

> com.actionsoft.apps.poc.plugin.cache.BookCache
    
    
    public class BookCache extends Cache<String, BookModel> {
    
        public BookCache(CachePluginProfile profile) {
            super(profile);
            // 注册索引，为“书名”字段建立缓存唯一索引。要求“书名”字段值不能有重复的
            registeIndex(BookIndex1.class, new BookIndex1());
            // 注册索引，为“出版年份”字段建立缓存多值索引，快速索引到某年份的书
            registeIndex(BookIndex2.class, new BookIndex2());
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
         * 索引示例。从“书名”获得缓存对象
         *
         * @param name 书名
         * @return
         */
        public static BookModel getByName(String name) {
            return getCache().getByIndexSingle(BookIndex1.class, name);
        }
    
        /**
         * 索引示例。从“出版年份”获得多个缓存对象
         *
         * @param year
         * @return
         */
        public static Iterator<BookModel> listByYear(int year) {
            return getCache().getByIndex(BookIndex2.class, Integer.toString(year));
        }
    
        ...
    

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`CacheSample`，在弹出的对话框中点击`索引示例`按钮，你会看到页面返回如下类似信息

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/cache-3.png)](<cache-3.png>)

#### 对话框部分的代码示例

> com.actionsoft.apps.poc.plugin.web.SampleWeb#getCacheSampleHome2
>     
>     
>     public String getCacheSampleHome2() {
>         StringBuilder data = new StringBuilder();
>         data.append("<b>BookCache ==> BookIndex1/BookIndex2</b><hr>\n");
>         data.append("<b>BookCache.getByName(\"你总会路过这个世界的美好\")</b><br/>" + BookCache.getByName("你总会路过这个世界的美好").toJson()).append("<br/>");
>         Iterator<BookModel> iterator = BookCache.listByYear(2014);
>         data.append("<b>BookCache.getByYear(2014)</b><br/>");
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