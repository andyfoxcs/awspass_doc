# 通知 | AWS BPMN2 Activity参考指南

# 通知

`通知`是指任务在结束时，向指定用户发送消息。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/16.gif)

### 触发规则

系统支持两类场景

  * 当该节点的任务结束时，即触发
  * 当该节点的任务结束且用户选择指定的审核菜单时，才会触发

> 例如，当用户选择`已出库`后，给采购商发送一封提醒邮件

### 消息类型

系统支持两类消息

  * 通知类任务。这类消息可以出现在通知用户的工作台的`未阅通知`列表中，点击可只读查看表单。如果安装了`任务超时监控`应用，这类通知可以实现[逾期未读自动消除](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.tasktimeout/cfg/clear_task.html>)的功能
  * 邮件。这类消息可以给特定用户发送一封邮件，邮件内容由事先设计的模板自动生成

> `邮件发送`是一个平台扩展的商业应用，需要安装该应用支持该特性

### 通知范围

系统支持两类范围

  * 该流程特定节点的已办人员
  * 直接指定

### 延伸阅读

  * [任务超时监控产品发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.tasktimeout/index.html>)
  * [邮件通知产品发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/>)