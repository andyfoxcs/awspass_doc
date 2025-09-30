# 监控计算资源 | AWS SLA参考指南

# 监控计算资源

分析某个AWS PaaS实例采集的`计算资源`类监控数据，包括

  * 告警事件
  * 实时线程/进程
  * CPU使用情况
  * 内存使用情况

`计算资源`是运行AWS实例的服务器资源。当AWS处于集群部署时，每个AWS实例节点分别拥有自己的`计算资源`。

## 告警事件

**说明：该AWS实例有关`计算资源`类指标发生的告警信息，列出最新5条。**

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/21.png)

告警规则Id | 告警标题 | 触发规则  
---|---|---  
CPU Usage Is Too High | CPU使用率过高 | 连续2次高于90%  
Low Physical Memory | 物理可用内存过低 | 连续2次低于20%  
  
告警规则是内置的，高级运维人员也可以修改和添加规则。

  * [平台内置的告警规则](<../appendix1/alarm_rules.html>)
  * [管理和修改告警规则](<setting.html>)

## 抓取线程信息

**说明：该节点JVM正在处理的操作，只显示持续执行时间大于3秒的线程。**

列表通常为空，不会自动刷新，点击右侧`刷新`按钮可抓取最新线程数据。AWS服务器对每次接收到的Web请求从线程池分配一个可用线程，**执行时间大于3秒的线程是性能改善的重点排查对象** 。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/22.png)

点击右侧的耗费时间按钮，会弹出程序调用堆栈，辅助开发人员诊断代码执行位置。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/23.png)

## 抓取进程信息

**说明：该AWS实例所在操作系统的进程信息。**

CPU和内存列支持点击排序。列表不会自动刷新，点击右侧`刷新`按钮可抓取最新进程数据。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/24.png)

## CPU使用情况

**说明：回放该AWS实例历史时段的CPU使用率，用于辅助分析故障时段的CPU波动**

  * 最近24小时（5分钟平均数据）
  * 最近15天（1小时平均数据）
  * 最近1年（1天平均数据）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/25.png)

## 内存使用情况

**说明：回放该AWS实例历史时段的内存分配情况，用于辅助分析故障时段的内存波动**

  * 最近24小时（5分钟平均数据）
  * 最近15天（1小时平均数据）
  * 最近1年（1天平均数据）
  * `总物理内存` = 部署该节点的操作系统全部内存（G)
  * `剩余可用物理内存` = 部署该节点的操作系统剩余可用内存（G)
  * `JVM总内存` = 分配给该节点JVM的最大可用内存（G)

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/26.png)