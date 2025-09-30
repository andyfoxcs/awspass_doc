# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 为`主应用`开发`ASLP`服务，实现相关框架逻辑
  2. 在`关联应用`，用`AppExtensionProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### 注册语法

由`AppExtensionProfile`类完成向AWS PaaS的注册。
    
    
    //注册应用扩展点
    list.add(new AppExtensionProfile(name, aslp, params));
    

  * `name`-实现该扩展点的名称，例如`PAL报告->RACI流程说明`
  * `aslp`-主应用的ASLP地址，例如`aslp://com.actionsoft.apps.notification/registerApp`。
  * `params`-调用该ASLP的参数(Map< String,Object >)

### 注意事项

要成功绑定`主应用`，必须在`关联应用`的`manifest.xml`声明依赖
    
    
      <requires>
        <require appId="主应用的AppId" notActiveHandler="error"/>
      </requires>
    

  * notActiveHandler=error，表示高度依赖。如果服务提供方被停用，该应用将收到错误
  * notActiveHandler=warning，表示中度依赖。如果服务提供方被停用，该应用将收到警告
  * notActiveHandler=none，表示智能依赖。如果服务提供方被停用，该应用不会收到任何信息

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`绑定应用扩展点`，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/app-extend-2.png)](<app-extend-2.png>)