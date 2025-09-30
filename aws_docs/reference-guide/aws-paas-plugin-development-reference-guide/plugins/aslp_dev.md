# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现ASLP接口，完成一个互操作接口的实现
  2. 用`ASLPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### ASLP接口

开发者可实现这个接口完成ASLP的开发。

> com.actionsoft.apps.resource.interop.aslp.ASLP
    
    
    /**
     * <p>ASLP(Application Service Locator Protocol缩写)应用服务访问定位协议接口对象，在AWS
     * PaaS容器中为每个封装的互操作方法分配一个唯一的ASLP地址。ASLP用于实现同一AWS
     * PaaS中跨App的接口互操作，也支持跨网络服务的互操作（如为移动客户端提供http接口服务）</p>
    
     * @see AppAPI#callASLP(com.actionsoft.apps.resource.AppContext, String, Map)
     *      同步调用
     * @see AppAPI#asynCallASLP(com.actionsoft.apps.resource.AppContext, String,
     *      Map) 异步调用
     */
    public interface ASLP {
    
    /**
     * 服务方法
     *
     * @param params
     *            一个key/value的参数传递定义，其中一定会传递一个名为caller的AppContext对象。如果该请求来自HTTP
     *            ，会传递一个名为http的变量，值为true，如果调用类型为Session验证，会传递一个名为sid的字符串变量，
     *            值为调用方用户会话 。注意value只允许使用Java基本类型和AWS的公共对象，如String、Integer
     *            、Boolean、UserContext
     *            、ProcessInstance等，但如果该服务允许被以http方式调用，Value仅支持String类型
     * @return 通用数据结构对象
     * @see AppAPI#callASLP(com.actionsoft.apps.resource.AppContext, String,
     *      Map)
     * @see AppAPI#asynCallASLP(com.actionsoft.apps.resource.AppContext, String,
     *      Map)
     */
    public abstract ResponseObject call(Map<String, Object> params);
    

### @Meta注解

call接口支持@Meta注解，可以描述该接口的参数规格和说明。注解中允许的变量名如下：

变量名 | 说明 | 值类型  
---|---|---  
name | 参数标题 | String，例如"Hi"  
required | 调用时是否必须给定 | Boolean，例如true  
allowEmpty | 给定的值是否允许空串 | Boolean，例如true  
minLen | 给定值的最小长度 | Integer，例如12  
maxLen | 给定值的最大长度 | Integer，例如36  
      
    
    //sample
    @Meta(parameter = { "name:'yourName',required:true,allowEmpty:fasle,desc:'你的名字'" })
    

### 注册语法

由`ASLPPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册ASLP
    list.add(new ASLPPluginProfile(serviceName, clazz, desc, httpService));
    

  * `serviceName`-服务名，不允许包含怪字符和空格，建议使用英文和数字组合
  * `clazz`-类名称，该类必须实现了ASLP接口
  * `desc`-描述
  * `httpService`-该协议是否开放http(s)直接调用，如果支持需要给定安全策略，如果不开放该参数为null

**`httpService`参数说明**

  * `null`-只允许调用者在PaaS内部使用SDK API访问（APPAPI）
  * new HttpASLP(HttpASLP.`AUTH_AWS_SID`)-允许调用者提供AWS会话。通过http访问
  * new HttpASLP(HttpASLP.`AUTH_KEY`, "MY_KEY")-允许调用者提供一个暗号口令，这个值定义该App的`MY_KEY`变量的`key`项中。通过http访问
  * new HttpASLP(HttpASLP.`AUTH_RSA`)-允许调用者有应用服务提供方提供的cer公钥文件。通过http访问