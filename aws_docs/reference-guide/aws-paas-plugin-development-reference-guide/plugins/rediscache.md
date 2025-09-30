# Redis缓存 · AWS PaaS文档中心

## 应用场景

因AWS Cache是进程内缓存，在数据量巨大的场景下并不适用，此时可以使用Redis缓存。AWS Cache内部针对Redis进行了适配，开发者仅需实现RedisAdapter接口即可将缓存迁移到Redis。

## 准备工作

使用Redis缓存需要安装Redis Connector应用（com.actionsoft.apps.cc.connector.redis）。 安装后在应用开发->连接服务中新建一个Redis连接。参见xxx。将该新建的Redis连接的ID填入server.xml中参数redis.cc.id的值中。AWS Cache将默认使用该Redis配置缓存数据。

## 开发步骤

重写父类com.actionsoft.bpms.commons.cache.Cache中的initRedisAdapter方法，在此方法中需返回实现了com.actionsoft.bpms.commons.cache.redis.RedisAdapter接口的对象.

> com.actionsoft.bpms.commons.cache.redis.RedisAdapter
    
    
    package com.actionsoft.bpms.commons.cache.redis;
    
    /**
     * Redis缓存适配器
     */
    public interface RedisAdapter<K,V>{
        /**
         * 在此方法中实现Redis缓存数据初次加载逻辑,需要使用putRedis方法一次将多个对象批量放入Redis
         * @return
         */
        public void load();
    
        /**
         * 获取缓存对象的key
         * @param v
         * @return
         */
        public K getKey(V v);
    
        /**
         * 缓存是否过期。这里如果返回false并不代表永不过期， 如果Redis内存淘汰管理机制设置为allkeys-lru或allkeys-random，缓存数据仍然可能被回收。
         * @return
         */
        public boolean shouldExpire();
    
        /**
         * 缓存过期时间，单位为秒, 0为永久。按需缓存场景下应避免返回相同的过期时间，以减少缓存雪崩的几率。
         */
        public int getExpireTime(V v);
    }
    

#### HistoryNotificationMessageCache代码示例

> com.actionsoft.apps.notification.cache.HistoryNotificationMessageCache
    
    
    public final class HistoryNotificationMessageCache extends Cache<String, NotificationMessageModel>
    
        ...
        //平台启动时默认调用此方法将缓存数据加载到内存;将缓存切换到Redis时内存中的缓存会被释放；将缓存切换到内存时，会再次调用此方法
        //若确定需要使用Redis，此此方法可不实现，当然此时切换到内存操作无效
            @Override
        public void load() {
            List<NotificationMessageModel> list = new NotificationMessageDao().loadMessage(NotificationConst.READED_Y, NotificationDataUtil.maxHistoryCount());
            if (list != null) {
                for (NotificationMessageModel model : list) {
                    put(model.getId(), model, false);
                }
            }
    
            ConsolePrinter.info("Cache加载已读通知 [" + (list == null ? 0 : list.size()) + "个][成功]");
        }
    
        @Override
        protected RedisAdapter<String,NotificationMessageModel> initRedisAdapter(){
            return new RedisAdapter<String,NotificationMessageModel>() {
                @Override
                public  void load(){
                    //先从数据库中读取到需要缓存的已读通知
                    List<NotificationMessageModel> list = new NotificationMessageDao().loadMessage(NotificationConst.READED_Y, NotificationDataUtil.maxHistoryCount());
                    //一次将多条数据放入Redis缓存，如果数据量特别大，可拆分成多个list分批放入
                    putRedis(list);
                }
                @Override
                public String getKey(NotificationMessageModel model){
                    //因putRedis方法一次放入多个对象，此处返回每个缓存对象的key，
                    return model.getId();
                }
    
                @Override
                public boolean shouldExpire() {
                    //一般来说，每天不断产生新数据的业务数据应当过期，通过人工增删改的数据如组织人员可以不过期
                    return true;
                }
                @Override
                public int getExpireTime(NotificationMessageModel model){
                    //缓存5小时，加上1-20分钟的随机过期，避免同时过期可能引起的缓存雪崩
                    return 5 * 60 * 60 + (int)(Math.random() * 20 * 60);
                }
            };
        }
    

## 如何使用

### Redis缓存初始化（缓存预热）

AWS Cache实现RedisAdapter接口后，启动平台时不会自动执行将数据缓存到Redis的操作，而是需要登录到AWS控制台，在工具附加->Redic Connector中点击 “切换到Redis”，此时才会执行RedisAdapter中的load方法将数据加载到Redis中。 `注：应在非工作时间进行切换，以免影响平台使用`

### 添加/更新Redis缓存

添加/更新缓存时依然是调用父类com.actionsoft.bpms.commons.cache.Cache的put(K key, V object)方法
    
    
        public static void putModel(NotificationMessageModel model) {
            getCache().put(model.getId(), model);
        }
    

### 删除Redis缓存

删除缓存依然是调用父类的remove(K key)方法
    
    
        public static void removeById(String id) {
            getCache().remove(id);
        }
    

### 缓存重置

在工具附加->Redis Connector中点击 “重新加载”，此时会将Redis中对应的缓存数据清空，再次执行RedisAdapter中的load方法。 `注：应在非工作时间进行重新加载，以免影响平台使用`

## 缓存清空

在工具附加->Redis Connector中点击 “切换至内存”，此时会将Redis中对应的缓存数据清空，执行Cache中的load方法。

## 注意事项

AWS Cache Redis缓存的底层实现是将Java对象序列化后存储到Redis中。由于AWS Cache 每次从Redis查询缓存后需要将数据反序列化为新的对象，因此应尽量避免一次查询过多缓存而创建太多Java对象导致内存溢出。

### 不支持的方法

实现RedisAdapter后，为避免内存溢出，将不允许调用com.actionsoft.bpms.commons.cache.Cache中的public Iterator iterator()和public Iterator iteratorSorted(final Comparator comparator)方法，强行调用会抛出AWSException。

### 慎用索引

根据索引查询时，会一次返回多条缓存数据，应尽量减少索引中每个key对应的缓存数量，同时避免频繁使用索引查询缓存。