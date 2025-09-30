# 按需缓存示例 · AWS PaaS文档中心

## 按需缓存示例

当需要缓存的数据较大时，可以只将引用过的或使用频率高的缓存到内存中

  * 设置最大缓存个数
  * 设置缓存数据空闲多久后失效
  * 设置缓存数据多长时间后失效
  * 只缓存使用到的数据

### 设置最大缓存个数

当缓存对象容量达到指定值之后，支持基于LRU(Least Recently Used)算法自动删除不使用的缓存。

**在注册缓存插件时设置**
    
    
    List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
    CachePluginProfile cacheProfile=new CachePluginProfile(BookCache.class);
    //只缓存1000个对象
    cacheProfile.maxElements(1000);
    list.add(cacheProfile);
    

**在程序中动态时设置**
    
    
    //只缓存1000个对象
    BookCache.getCache().getConfiguration().maxElements(1000);
    

### 设置缓存数据多长时间后失效

当某个对象超过n秒没有被再次调用后，被标记为失效。

**在注册缓存插件时设置**
    
    
    List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
    CachePluginProfile cacheProfile=new CachePluginProfile(BookCache.class);
    //空闲60秒后失效
    cacheProfile.timeToIdleSeconds(60);
    list.add(cacheProfile);
    

**在程序中动态时设置**
    
    
    //空闲60秒后失效
    BookCache.getCache().getConfiguration()timeToIdleSeconds(60);
    

### 设置缓存数据空闲多久后失效

当某个对象自put到缓存多久后，被标记为失效。

**在注册缓存插件时设置**
    
    
    List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
    CachePluginProfile cacheProfile=new CachePluginProfile(BookCache.class);
    //自put到缓存120秒后失效
    cacheProfile.timeToLiveSeconds(120);
    list.add(cacheProfile);
    

**在程序中动态时设置**
    
    
    //自put到缓存120秒后失效
    BookCache.getCache().getConfiguration()timeToLiveSeconds(120);
    

### 只缓存使用到的数据

这类缓存方案不适用于Query类的集合查询，适用于对单一数据对象的缓存读取。这里提供一种实现思路，开发者可根据需要自行设计：

  * 实现空load()方法，即开始时是一个空缓存结构
  * 封装自己的get()方法，首先从缓存中查询，如果没有命中再从持久层读取并放入缓存
  * 在持久层使用put/remove方法同步对象的新增、修改和删除
  * 适当配合上述的一些参数，如设置maxElements

    
    
    //sample
    public BookModel get(String id) {
        //内存查询
        BookModel book = super.get(id);
        if (book == null) {
            //持久层查询
            book = new BookDao().queryById(id);
              if(book!=null){
               put(book.getId(), book);
              }
        }
        return book;
    }
    

> 当某些缓存数据被标记失效后，Cache.size()会包含正常和失效的对象，这些失效对象在下次执行get或iterator操作时移走