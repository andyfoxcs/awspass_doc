# 通过模拟压测学会看图 | AWS SLA参考指南

# 通过模拟压测学会看图

在本章节，我们通过一次模拟压测，了解SLA监控指标的回放分析方法。

## 环境准备

_在青云，模拟了如下配置的云实例环境：_

AWS单实例服务 | SQLServer数据库服务  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/51.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/52.png)  
16核/32G/Windows 2012/AWS 6.2 | 16核/48G/Windows 2012/SQLServer2014  
  
_测试用例：_

项 | 说明  
---|---  
并发用户 | 200人  
测试时间 | 1小时20分钟  
给压计划 | 初始规模100并发，在第10秒增加100至200并发，之后持续200并发。  
1小时20分10秒时减少100并发，在1小时20分20秒并发数将至0  
login | 模拟用户登录AWS平台，完成身份鉴权，创建Session会话  
create-process | 创建流程实例，并创建一个待办任务给自己  
  
_测试结果：_

  * Maximum Running Vusers:200
  * Total Throughput (bytes):1,913,580,151
  * Average Throughput (bytes/second):396,844
  * Total Hits:188,862

事务 | 最小(秒) | 平均(秒) | 最大(秒) | 90%(秒)  
---|---|---|---|---  
create-process | 0.016 | 0.087 | 3.25 | 0.156  
login | 0.006 | 0.167 | 1.013 | 0.7  
  
## SLA总体概览

压测期间AWS平均每5分钟接收处理1.2万次请求，压力平滑，符合测试用例的`给压计划`。（见下图）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/sla-mvc.png)

我们通过`指标趋势`，回放该时段的`cmd请求总次数`，可以看到更清晰的压力分布情况。（见下图）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/sla-hits.png)

该压测过程，AWS创建了188,662个流程实例和188,662个任务实例，没有产生错误和SLA告警事件。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/sla-summary.png)

## 分析内部细节的耗时分布情况

访问`指标趋势`，可以分析`create-process`时更细的分解指标。回放该时段的`创建流程实例耗时`、`启动流程实例耗时`的时间分布，了解相关指标耗时情况。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/sla-process.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/sla-summary.png)

期间所有Web请求，平均在100毫秒内完成处理。 ![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/sla-response.png)

## 分析外部并发200时，内部实际的并发情况

访问`指标趋势`，通过回放该时段的`并发请求数`可以分析出，由于外部200并发用户设置了思考等待时间（类似于在线用户），真正对系统产生的高峰并发压力在10-40之间（约5:1）。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/sla-user.png)

## 分析资源使用情况

访问`指标趋势`，回放该时段的`CPU资源使用率`、`数据库连接池大小`、`数据库连接池空闲连接数`、`数据库连接池活动连接数`的最大值分布，了解内部资源指标的使用情况。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/sla-db.png)

随着200用户持续创建流程，数据库活动连接数平稳保持在10-20个之间。在初期CPU使用率有个55%的小高峰，后平稳保持在20%水平。

运行一段时间后，AWS的数据库连接池发现不需要预留100个连接资源，根据实际数据库活动连接数，数据库连接池大小逐渐降低到20-40之间。完成压测没有数据库压力后，数据库连接池大小保持在10水平。

从上图分析，AWS能够随着压力上升使用更多资源，随着压力的下降自动释放资源。

## 延伸阅读

  * [SLA对平台性能的损耗](<performance.html>)
  * [常见的分析场景](<question.html>)