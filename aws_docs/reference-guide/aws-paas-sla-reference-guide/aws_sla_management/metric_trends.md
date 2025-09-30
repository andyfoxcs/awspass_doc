# 指标趋势 | AWS SLA参考指南

# 指标趋势

SLA将指标收集的数据按时间维度进行处理，存放在[数据库中](<../appendix1/table.html>)，高级运维人员可以通过综合查询工具，对任意指标的历史数据进行调阅。

> 当性能故障发生后，该图表能够真实回放各指标在平台内部的运行情况

**时段范围**

  * 24小时内的5分钟片段
  * 15天内的1小时片段
  * 1年内的1天片段

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/301.png)

## 延伸阅读

  * [内置的监控指标](<../appendix1/resource_metric.html>)
  * [存储SLA数据的表](<../appendix1/table.html>)
  * [通过API查询日志](<../aws_sla_api/query.html>)