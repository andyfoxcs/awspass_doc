# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 继承com.actionsoft.bpms.commons.cache.Cache类，实现初始化缓存 对象的load方法
  2. 用`CachePluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### Cache抽象类

开发者可继承这个抽象类完成Cache的开发。大部分操作已封装在这个父类中，包括

  * put类操作（缓存对象）
  * get类操作（获取单一缓存对象、全部缓存对象）
  * remove类操作（删除缓存对象）
  * index类操作（注册缓存索引，从缓存索引获取缓存对象）
  * init类操作（初始化缓存）
  * replicate类操作（自定义集群复制）

> 关于该接口的说明，请参见com.actionsoft.bpms.commons.cache.Cache相关的JavaDoc

一个基本的Cache需要实现load()方法，即当你的应用被启动或重启时，对该缓存对象进行初始化。
    
    
    /**
    public abstract class Cache<K, V> implements ReplicateListener, Replicate {
    ...
    
    /**
     * 缓存初始化逻辑。缓存初始化逻辑。你会使用到put方法来缓存对象，注意put使用不同步到其它集群节点的方法。
     * @see #put(Object, Object, false)
     */
    protected void load();
    ...
    

### 注册语法

由`CachePluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册Cache
    list.add(new CachePluginProfile(Class<?> cls));
    

  * `cls`-Cache实现类