# 监控缓存对象 | AWS SLA参考指南

# 监控缓存对象

分析某个AWS PaaS实例采集的内存Cache数据。该功能主要适合开发者，用于了解缓存对象的使用情况。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/100.png)

_诊断思路_

  * 开发者应自我评估，缓存对象数量过多对服务器内存、CPU的开销影响
  * 开发者应自我评估，是否存在无效的缓存定义，应删除作废
  * 基于缓存对象总大小，适当调大JVM分配的最大内存