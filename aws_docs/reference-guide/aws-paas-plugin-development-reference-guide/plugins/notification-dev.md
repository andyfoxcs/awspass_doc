# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 用`AppExtensionProfile`描述这个插件，绑定应用扩展点(见本文档[插件开发 > 绑定应用扩展点](<../app_plugin/pluginlistener.html>)章节)
  2. 注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### 注册语法

由`AppExtensionProfile`类完成向`通知中心`的注册。
    
    
    // 注册通知中心
    Map<String, Object> params1 = new HashMap<String, Object>();
    params1.put("systemName", MyFormatter.DEMO_NAME);
    params1.put("icon", "../apps/com.actionsoft.apps.poc.plugin/img/icon96.png");
    params1.put("formatter", MyFormatter.class.getName());
    list.add(new AppExtensionProfile(MyFormatter.DEMO_NAME, "aslp://com.actionsoft.apps.notification/registerApp", params1));
    

要成功注册，必须设置该应用依赖`com.actionsoft.apps.notification`，即在该应用的`manifest.xml`声明依赖
    
    
      <requires>
        <require appId="com.actionsoft.apps.notification" notActiveHandler="error"/>
      </requires>
    

  * notActiveHandler=error，表示高度依赖。如果服务提供方被停用，该应用将收到错误
  * notActiveHandler=warning，表示中度依赖。如果服务提供方被停用，该应用将收到警告
  * notActiveHandler=none，表示智能依赖。如果服务提供方被停用，该应用不会收到任何信息

### formatterClass

一个提供parser()方法的Java类，继承`NotificationMessageFormatter`父类
    
    
    /**
     * @param user 通知查看人
     * @param content 发送的原始内容，可能是简单信息也可能是开发者约定的json串
     * @return ResponseObject，包含content和buttons两个变量
    */
    public ResponseObject parser(UserContext user, String content) {
        // 封装结果
        ResponseObject ro = ResponseObject.newOkResponse();
        ...
        return ro;
    }
    

该方法要求返回一个ResponseObject对象，该对象含有一个名为`content`的字符串和`buttons`的ArrayList（非必须）。ArrayList是一个Map结构，每个Map用来描述一个button的定义，包含属性：

  * name 按钮名称
  * action url地址
  * target 只允许三个常量：_blank/mainFrame/ajax
  * color 只允许三个常量：blue/white/red