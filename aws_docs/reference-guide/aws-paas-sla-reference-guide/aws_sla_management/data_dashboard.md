# 监控分析 | AWS SLA参考指南

# 监控分析

  * [实时看板](<data-realtime-dashboard.html>)
  * [监控计算资源](<data-infrastructure_dashboard.html>)
  * [监控本地数据库](<data-local_db_dashboard.html>)
  * [监控MVC框架](<data-mvc_dashboard.html>)
  * [监控流程引擎](<process.html>)
  * [监控表单引擎](<form.html>)
  * [监控应用容器](<container.html>)
  * [监控安全风险](<risk.html>)
  * [监控缓存对象](<cache.html>)

## 集群多节点

登录实例控制台时，系统会随机分配一个可用节点，并将管理员的Session会话黏贴到该节点，此后管理员的所有Web请求都会默认分发到该节点，包括访问`SLA服务质量监控`模块。

_如当前为集群部署，可以在实例控制台左侧菜单的右上角相关菜单，切换AWS节点。见下图_

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/00.png)

## 某历史时段无数据

当指标的历史数据在某个时间段没有数据，可能是

  * 正常情况，该时段KPI收集的数据为0
  * 异常情况，该时段可能AWS服务暂停或SLA服务暂停，造成数据未采集到

_如下图，15天内有两次停机造成内存数据未记录_

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/26.png)