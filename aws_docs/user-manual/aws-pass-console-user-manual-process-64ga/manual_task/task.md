# 规则设置 · AWS PaaS文档中心

## 规则设置

### 通知规则

通知策略是一项在管理中行使‘知晓权’的流程工具，在不影响流程执行的同时让需要知晓进展的人及时了解到流程执行状态的变化，例如 _【当总监审批报价单‘同意’时，为销售员发送一封电子邮件】_ 。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/tongzhi.gif)](<tongzhi.gif>)

项 | 说明  
---|---  
触发规则 | ．当任务办理完毕时  
．当节点向下一节点推进时  
．当沟通任务办理完毕时  
．当用户选择"XXX"菜单时（当前节点配置的人工审核菜单）  
消息类型 | ．系统通知，给接收者发送一个`未阅通知`类任务，任务标题来源于`通知标题`项的配置   
．邮件，发送邮件  
．短信，发送短信  
．企业微信，发送企业微信通知  
．阿里钉钉，发送钉钉通知  
．飞书，发送飞书通知  
  
通知标题 | 通知类任务标题，支持@公式。  
邮件模板 | 需安装并启用[邮件通知](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/index.html>)应用  
通知范围 | ．指定节点的已办用户   
．指定的用户  
．发起沟通的用户  
．自定义范围事件  
Java类名 | ．填写类名全路径   
．返回指定用户的UID，多个用空格隔开  
．继承com.actionsoft.bpms.bpmn.engine.listener.ValueListener  
  
>   1. 系统通知在`流程中心 > 未阅任务`列表中显示 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/nose2.png)](<nose2.png>)
>   2. 邮件通知需正确配置邮件服务, 主要配置项包括：  
> 
>      * 正确配置[邮件服务](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/index.html>)  
> 
>      * 参与提醒的用户正确配置了个人外部邮箱
>   3. 短信通知需正确配置短信服务, 主要配置项包括：  
> 
>      * 正确配置[短信服务](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.sms/index.html>)  
> 
>      * 参与提醒的用户正确配置了个人手机号码
>   4. 企业微信通知需安装并启用`企业微信集成`应用，主要配置项包括：  
> 
>      * 正确配置[企业微信应用](<https://docs.awspaas.com/reference-guide/aws-paas-wechat-reference-guide/sync_wechat_app/README.html>)  
> 
>      * 在`企业微信应用-系统通知`的参数中配置企业corpId及企业号应用agentId  
> 
>      * 在平台组织中添加企业微信账号[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/nose3.2.png)](<nose3.2.png>)
>   5. 阿里钉钉通知需安装并启用钉钉集成`应用，主要配置项包括：  
> 
>      * 正确配置[钉钉集成应用](<https://docs.awspaas.com/apps/com.actionsoft.apps.dingding/index.html>)  
> 
>      * 在`钉钉集成应用-系统通知`的参数中corpId及企业号应用agentId  
> 
>      * 在平台组织中添加阿里钉钉账号[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/nose3.png)](<nose3.png>)
>   6. 飞书通知需安装并启用`飞书集成`应用，主要配置项包括：  
> 
>      * 正确配置[飞书集成应用](<https://docs.awspaas.com/apps/com.actionsoft.apps.feishu.open/index.html>)  
> 
>      * 在`飞书集成`的参数中配置用于发送飞书消息时的飞书应用ID
>      * 在平台组织中添加飞书账号[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/nose3.1.png)](<nose3.1.png>)
> 

任务办理完毕通知展示

邮件 | 短信  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/email-nose4.png)](<email-nose4.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/sms-nose7.png)](<sms-nose7.png>)  
企业微信 | 阿里钉钉信  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/weixin-nose5.png)](<weixin-nose5.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/dingding-nose6.png)](<dingding-nose6.png>)  
飞书  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/feishu-nose5.png)](<feishu-nose5.png>)  
  
### 监控规则

时限策略是一项流程监控服务，在任务超过指定时间或在一个固定周期时，触发一个指定的动作，并记录到监控日志中，供开发者进一步利用。该功能需要安装并启用[邮件通知](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/index.html>)应用、[短信通知](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.sms/model/create.html>)应用、[企业微信集成](<https://docs.awspaas.com/reference-guide/aws-paas-wechat-reference-guide/index.html>)应用、[钉钉集成](<https://docs.awspaas.com/apps/com.actionsoft.apps.dingding/index.html>)应用、[飞书集成](<https://docs.awspaas.com/apps/com.actionsoft.apps.feishu.open/index.html>)应用或[任务超时监控](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.tasktimeout/index.html>)应用。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/sx1.gif)](<sx1.gif>)

### 延伸阅读

  * [任务超时监控发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.tasktimeout/index.html>)

### 表单归档

在流程结束时将当前节点激活的表单数据入库到KMS知识管理系统，默认不入库。该功能需要安装并启用[KMS知识管理](<https://docs.awspaas.com/apps/com.actionsoft.apps.kms/>)应用。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/kms1.1.png)](<kms1.1.png>)

项 | 说明  
---|---  
入库方式 | ．不入库（默认）  
．表单附件  
．表单链接和表单附件  
知识目录 | KMS知识管理系统中维度  
知识名称 | 自动入知识库后显示的知识名称，不支持模型类、流程定义类、任务实例相关等@公式  
知识创建人 | 知识创建人  
  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/kms0.png)](<kms0.png>)