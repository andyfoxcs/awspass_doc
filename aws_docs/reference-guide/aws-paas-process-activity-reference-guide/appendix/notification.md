# 内置消息通知服务 | AWS BPMN2 Activity参考指南

# 内置消息通知服务

在流程图中编排一个发送通知消息的自动化任务。该服务基于[Notification API](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/NotificationAPI.html>)的系统消息发送服务封装实现。

用户在登录系统时可以从`通知中心`获得该消息，安装手机`移动门户`的用户可以即时接收到Push的消息。

**主要功能**

  * 向指定账户发送一个消息通知
  * 支持info/error/warning三种类型，默认为info

### 使用方法

  1. 在流程图加入一个[Service Task](<../service_task/process_service.html>)
  2. 从流程服务库里选择`消息通知服务`
  3. 完成消息参数的配置

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/appendix/51.png)

参数 | 说明  
---|---  
发送人账户 | 一个合法的AWS账户，可以不填  
接收人账户 | 一个或多个合法的AWS登录账户（多个使用空格隔开）  
消息内容 | 最长2000字符，不支持HTML语法  
消息类型 | 支持info/error/warning三种类型，默认为info  
  
**用户接收到的消息提醒**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/appendix/52.png)

### 延伸阅读

  * [通知中心产品发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.notification/>)
  * [在移动门户接收消息](<https://docs.awspaas.com/emm/aws-pass-portal-user-manual-emm/news/README.html>)