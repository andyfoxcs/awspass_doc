# 监控应用容器 | AWS SLA参考指南

# 监控应用容器

分析某个AWS PaaS实例采集的`应用容器`类监控数据，包括

  * 告警事件
  * 错误次数
  * 警告次数

当AWS处于集群部署时，每个AWS实例节点的容器监控数据不一样的。

## 告警事件

**说明：该AWS实例有关`应用容器`类指标发生的告警信息，列出最新5条。**

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/81.png)

告警规则Id | 告警标题 | 触发规则  
---|---|---  
App Container Error | 应用容器出错 | 发生即触发  
App Container Warn | 应用容器警告 | 发生即触发  
  
告警规则是内置的，高级运维人员也可以修改和添加规则。

  * [平台内置的告警规则](<../appendix1/alarm_rules.html>)
  * [管理和修改告警规则](<setting.html>)

## 错误次数

**说明：回放该AWS实例应用容器发生错误的情况，用于辅助分析应用在安装、启动、暂停、卸载过程中发生的重要问题。**

  * 最近24小时（5分钟合计数据）
  * 最近15天（1小时合计数据）
  * 最近1年（1天合计数据）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/82.png)

_诊断思路_

  * 如果是重启父应用时，子应用被级联重启抛出的告警信息，可以忽略
  * 查看SLA相关时段`应用容器出错`的告警信息，了解具体应用和详细信息说明
  * 检查错误发生时段，`logs/aws.log`日志文件内容

## 警告次数

**说明：回放该AWS实例应用容器发生警告的情况，用于辅助分析应用在安装、启动、暂停、卸载过程中发生的次要问题。**

  * 最近24小时（5分钟合计数据）
  * 最近15天（1小时合计数据）
  * 最近1年（1天合计数据）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/83.png)

_诊断思路_

  * 如果是重启父应用时，子应用被级联重启抛出的告警信息，可以忽略
  * 查看SLA相关时段的`应用容器警告`的告警信息，了解具体应用和详细信息说明
  * 检查错误发生时段，`logs/aws.log`日志文件内容