# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现`WechatProcessor`接口handleMessage()方法
  2. 用`WechatPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### WechatProcessor接口

开发者可实现这个接口，实现该应用的全部微信消息处理程序。通常您应该对消息类型进行判断，以能够针对不同的事件类型和消息类型作出准确的处理响应。

> com.actionsoft.bpms.commons.wechat.WechatProcessor
    
    
    public interface WechatProcessor {
    
        /**
         * 事件处理
         *
         * @param msg 接收到的微信消息对象
         * @return 如果返回null表示不响应消息
         */
        public WechatOutMessage handleMessage(WechatInMessage msg);
    }
    

### 注册语法

由`WechatPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册企业微信事件处理接口
    list.add(new WechatPluginProfile(XXX.class.getName(), "这里是说明"));
    

  * `clazz`-`WechatProcessor`接口的实现类路径

> 注意，注册成功后平台还不具备将事件分发到该处理器的条件，需要通过`企业微信管理开发平台`对某个[应用的菜单进行关联引用](<https://docs.awspaas.com/reference-guide/aws-paas-wechat-reference-guide/sync_wechat_app/setting_app.html>)，建立"微信应用<\-->本地应用"的配对关系。