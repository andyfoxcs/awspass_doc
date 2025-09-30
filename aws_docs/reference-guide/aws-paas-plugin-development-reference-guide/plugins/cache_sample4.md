# 缓存排序示例 · AWS PaaS文档中心

## 缓存排序示例

Cache默认提供的迭代器返回无序的结果，如
    
    
    Iterator<BookModel> iterator = BookCache.getCache().iterator();
    

AWS Cache对查询全部缓存和索引缓存支持Comparator（排序比较器），开发者可以通过自定义的排序比较器获得有序的Iterator结果。

### 按书名排序比较

> com.actionsoft.apps.poc.plugin.cache.BookCache#SORT_BOOK_NAME
    
    
    private static Comparator<BookModel> SORT_BOOK_NAME = new Comparator<BookModel>() {
        public int compare(BookModel o1, BookModel o2) {
            if (o1 == null || o2 == null) {
                return 0;
            }
            return o1.getName().compareTo(o2.getName());
        }
    };
    

### 按图书数量排序比较

> com.actionsoft.apps.poc.plugin.cache.BookCache#SORT_BOOK_QUANTITY
    
    
    private static Comparator<BookModel> SORT_BOOK_QUANTITY = new Comparator<BookModel>() {
        public int compare(BookModel o1, BookModel o2) {
            if (o1 == null || o2 == null) {
                return 0;
            }
    
            return o1.getQuantity() - o2.getQuantity();
        }
    };
    

### 排序在BookCache中封装

  * getByIndex，适用于排序CacheIndex索引的缓存对象
  * iteratorSorted，适用于排序Cache的全部缓存对象

> com.actionsoft.apps.poc.plugin.cache.BookCache
    
    
    /**
     * 排序示例。按图书名排序索引的结果
     *
     * @param year
     * @return
     */
    public static Iterator<BookModel> listSortByName(int year) {
        return getCache().getByIndex(BookIndex2.class, Integer.toString(year), SORT_BOOK_NAME);
    }
    
    /**
     * 排序示例。按图书库存量排序全部缓存
     *
     * @return
     */
    public static Iterator<BookModel> listSortByQuantity() {
        return getCache().iteratorSorted(SORT_BOOK_QUANTITY);
    }
    

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`CacheSample`，在弹出的对话框中点击`排序示例`按钮，你会看到页面返回如下类似信息

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/cache-4.png)](<cache-4.png>)

#### 对话框部分的代码示例

> com.actionsoft.apps.poc.plugin.web.SampleWeb#getCacheSampleHome3
>     
>     
>     public String getCacheSampleHome3() {
>         StringBuilder data = new StringBuilder();
>         data.append("<b>BookCache ==> SORT_BOOK_NAME/SORT_BOOK_QUANTITY</b><hr>\n");
>         Iterator<BookModel> iterator = BookCache.listSortByName(2014);
>         data.append("<b>SORT_BOOK_NAME/BookCache.listSortByName(2014)</b><br/>");
>         while (iterator.hasNext()) {
>             BookModel bookModel = iterator.next();
>             data.append(bookModel.getName()).append(" ==> ").append(bookModel.toJson()).append("<br/>");
>         }
>         iterator = BookCache.listSortByQuantity();
>         data.append("<b>SORT_BOOK_QUANTITY/BookCache.listSortByQuantity()</b><br/>");
>         while (iterator.hasNext()) {
>             BookModel bookModel = iterator.next();
>             data.append(bookModel.getQuantity()).append(" ==> ").append(bookModel.toJson()).append("<br/>");
>         }
>         Map<String, Object> macroLibraries = new LinkedHashMap<String, Object>();
>         macroLibraries.put("data", data.toString());
>         macroLibraries.put("sid", getContext().getSessionId());
>         return HtmlPageTemplate.merge("com.actionsoft.apps.poc.plugin", "cache-sample-dialog.htm", macroLibraries);
>     }
>