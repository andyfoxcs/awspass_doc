# 内置邮件发送服务 | AWS BPMN2 Activity参考指南

# 内置邮件发送服务

在流程图中编排一个发送电子邮件的自动化任务。

**主要功能**

  * 向指定账户发送一封电子邮件
  * 支持邮件抄送

### 使用方法

  1. 在流程图加入一个[Service Task](<../service_task/process_service.html>)
  2. 从流程服务库里选择`邮件发送服务`
  3. 完成邮件参数的配置

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/appendix/41.png)

参数 | 说明  
---|---  
收件人email账户 | 一个或多个合法的email地址，多个用分号分割，支持@公式  
接收人账户 | 一个或多个合法的AWS登录账户（多个使用空格隔开）  
抄送人email账户 | 一个或多个合法的email地址，多个用分号分割，支持@公式  
邮件标题 | 邮件标题，支持@公式  
邮件正文 | 邮件标题，支持@公式  
邮件标题 | 邮件正文，支持@公式和特定变量（任务办理URL）  
  
### 注意事项

这是一个AWS企业应用商店附加的商业应用。为BPM流程和开发者提供邮件通知服务，包括提供任务到达、任务催办、任务超时的邮件提醒。

邮件通知 | 配置SMTP服务  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/appendix/43.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/appendix/42.png)  
  
### 延伸阅读

  * [邮件通知产品发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/>)