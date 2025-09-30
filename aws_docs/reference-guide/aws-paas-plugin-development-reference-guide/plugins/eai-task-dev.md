# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 为EAI任务提供的一组API
  2. 用`AppExtensionProfile`描述这个插件，绑定应用扩展点(见本文档[插件开发 > 绑定应用扩展点](<../app-extension.html>)章节)
  3. 一个提供getBehaviors()方法的类，负责该EAI任务的工作台列表行为处理
  4. 场景模拟，调试

>   1. 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。
>   2. 开发的代码所在应用，应用配置中必须关联`流程中心(com.actionsoft.apps.workbench)`应用
> 

### 为EAI任务提供的一组API

#### createEAITaskInstance(创建EAI任务)

可以有多种封装方式向AWS的流程引擎创建一个EAI任务，例如通过本地的Java程序、外部的服务接口。这些方式最终都是通过调用[createEAITaskInstance()](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/TaskAPI.html#createEAITaskInstance%28java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20int%29>)方法完成。
    
    
    SDK.getTaskAPI().createEAITaskInstance(...);
    

例如有个名叫`百度`的系统，`张三`向`李四`创建一个打开百度首页的待办任务，代码看起来如下：
    
    
    EAITaskInstance baiduTask = SDK.getTaskAPI().createEAITaskInstance("百度", "0001", "张三", "李四", "这是百度的首页", "http://www.baidu.com", 1);
    

点击这里[查看API JavaDoc](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/TaskAPI.html#createEAITaskInstance%28java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20int%29>)

参数 | 说明  
---|---  
applicationName | 应用系统简称，最长36个字符，全平台应唯一  
outerId | 该信息在外部系统的ID，最长64个字符  
createUid | 创建人账户，一个合法的AWS用户登录账户  
targetUid | 执行人账户，一个合法的AWS用户登录账户  
title | 任务标题，最长255个字符  
actionParameter | 该参数是私有格式， 被对应的EAITaskAction实现类处理，最长255个字符  
priority | 任务优先级 （0：低；1：无；2：中；3：高）  
  
创建成功返回[EAITaskInstance](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/model/run/delegate/EAITaskInstance.html>)对象

#### completeEAITask(标记完成任务)

使用以下API，将EAI任务状态从待办转为已办
    
    
    SDK.getTaskAPI().completeEAITask("百度", "0001");
    

  * [completeEAITask(eaiTaskInstId)](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/TaskAPI.html#completeEAITask%28java.lang.String%29>)
  * [completeEAITask(applicationName,outerId)](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/TaskAPI.html#completeEAITask%28java.lang.String,%20java.lang.String%29>)

#### deleteEAITask(标记删除任务)

使用以下API，将EAI任务标记为已删除
    
    
    SDK.getTaskAPI().deleteEAITask("百度", "0001");
    

### 注册语法

如果需要EAI任务在`我的工作台`、移动端列表中响应用户的点击行为，或则标记特定的背景色，则需要为`我的工作台`绑定应用扩展点。

由`AppExtensionProfile`类完成向`我的工作台`的注册。
    
    
    // 注册应用扩展点
    Map<String, Object> params3 = new HashMap<String, Object>();
    params3.put("applicationName", "百度");
    params3.put("behaviorClass", BaiduEAIBehavior.class.getName());
    list.add(new AppExtensionProfile("我的工作台->百度任务行为", "aslp://com.actionsoft.apps.workbench/registerEAIBehavior", params3));
    

要成功注册，必须设置该应用依赖`com.actionsoft.apps.workbench`，即在该应用的`manifest.xml`声明依赖
    
    
      <requires>
        <require appId="com.actionsoft.apps.workbench" notActiveHandler="error"/>
      </requires>
    

  * notActiveHandler=error，表示高度依赖。如果服务提供方被停用，该应用将收到错误
  * notActiveHandler=warning，表示中度依赖。如果服务提供方被停用，该应用将收到警告
  * notActiveHandler=none，表示智能依赖。如果服务提供方被停用，该应用不会收到任何信息

### behaviorClass

一个提供getBehaviors()方法的普通Java类
    
    
    //用户显示的待办或则已办任务含有该EAI任务时
    //将该系统的EAI任务组织到instances
    public ResponseObject getBehaviors(UserContext user, List<EAITaskInstance> instances) {
        Map<String, Map<String, String>> behaviors = new HashMap<>();
        ...
        return ResponseObject.newOkResponse().put("behaviors", behaviors);
    
    }
    

该方法要求返回一个ResponseObject对象，该对象含有一个名为behaviors的Map，包含了这些EAI任务的用户行为属性：

  * font-color 字体颜色
  * background-color 背景色
  * icon 图标
  * icon-title 鼠标提示文字
  * title 标题，如不提供默认创建的任务标题
  * url 点击时打开的URL地址，支持@公式
  * type 任务分组，如不提供默认该系统名