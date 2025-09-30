# 时限 | AWS BPMN2 Activity参考指南

# 时限

`时限`是指任务超过指定时间或在一个固定周期时，触发一个指定的动作，并记录到[监控日志](<https://docs.awspaas.com/user-manual/aws-pass-app-user-manual-addons-tasktimeout/appendix/structure.html>)中，供开发者进一步利用。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/15.gif)

时限相当于给节点产生的每个任务绑定了一个闹钟。

> `任务超时监控`是一个平台扩展的商业应用，需要安装该应用支持该特性

### 计时方案

提供两大类方案

  1. 基于某个时刻的开始时间与当前时间做比对，检查是否超时
  2. 基于固定周期频率（例如每月的29日），如果任务在这个时刻存在就会被触发

> 对于第1类方案的`开始时间`，支持任务创建时间、第一次阅读时间或者一个来自业务数据里的日期时间。对于第2类方案，支持按年、季、月、周、天的周期频率

### 执行时间

如果采用第1类计时方案，这里可以指定一个时间KPI值：

  * 当前节点配置的`合理完成时限`
  * 当前节点配置的`宽延警告时限`
  * 指定一个单位是小时的数值，也可以使用公式提取一个来自业务数据里的数字

如果采用第2类计时方案，这里可以指定一个周期时间：

  * 每天的什么时刻
  * 每周第几日的什么时刻
  * 每月第几天的什么时刻
  * 每季第几月第几日的什么时刻
  * 每年第几月第几日的什么时刻

### 业务条件

如果条件成立，真的要执行吗？这里可以通过公式做业务判断，最终返回一个true/false值。

### 执行动作

参见[这里的说明](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.tasktimeout/cfg/task.html>)。

### 扣绩效分

一个数值。当监控规则触发后，写入的[监控日志](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.tasktimeout/manager/README.html>)将含有扣分信息。开发者可以基于这个基础数据表在自己的App应用中进行引用、加工，实现特定绩效分析场景的业务分析

### 延伸阅读

  * [任务超时监控产品发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.tasktimeout/index.html>)
  * [邮件通知产品发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/>)