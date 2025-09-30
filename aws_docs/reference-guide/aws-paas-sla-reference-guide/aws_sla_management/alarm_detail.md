# 告警信息 | AWS SLA参考指南

# 告警信息

对指标收集的数据进行监控，当规则触发时，发生1次记录1次。告警信息包括：

  * 哪个实例
  * 哪个应用
  * 哪个指标
  * 在什么时间（上次发生的时间）
  * 触发的条件是什么
  * 采集到的值是什么
  * 附加的诊断信息

下图为一个“`(本地数据库)慢SQL`”的告警：

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/desc.png)

告警越早的被运维服务人员发现，带来的影响或风险可能就越小。

## 显示最新告警

登录AWS PaaS实例控制台，在首页获知最新告警提醒。（ _未读的告警信息加粗显示_ ）

![首页概览中提供的最新告警事件提醒](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/new-alarms.png)

## 查询历史告警数据

有关介绍请访问[告警日志](<alarm_log.html>)

## 通过API实时捕获告警

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/alarm.png)

  * 开发者可以通过API监听告警信息的到达，触发自己的告警方案（如发短信、发光报警、写入外部系统），参见本文档“[开放接口 > 注册监听器](<../aws_sla_api/listener.html>)”章节
  * [安装`OneAlert监控集成`，在OneAlert统一处理告警信息](<../appendix1/onealert.html>)

## 延伸阅读

  * [内置的监控指标](<../appendix1/resource_metric.html>)
  * [内置的告警规则](<../appendix1/alarm_rules.html>)
  * [OneAlert监控集成](<../appendix1/onealert.html>)