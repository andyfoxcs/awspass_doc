# 实时看板 | AWS SLA参考指南

# 实时看板

实时监控某个AWS PaaS实例的总体运行状况，包括

  * 活跃用户
  * 告警事件
  * 实时性能
  * 实时压力
  * 实时CPU使用
  * 实时内存使用

## 活跃用户

**说明：在一段时间内有操作的用户。`活跃用户` <= 实际登录的用户**

  * 手机用户（来自手机移动门户App、微信企业号等移动端）
  * 平板用户（来自平板移动门户App）
  * 台式机和笔记本（来自PC浏览器）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/11.png)

在server.xml配置了`活跃`时间，默认为20分钟内有请求的用户为活跃用户。
    
    
    %AWS-HOME%/bin/conf/server.xml#connector#sessionIdleTime
    

## 告警事件

**说明：该节点发生的所有告警信息，列出最新5条。**

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/12.png)

告警规则是内置的，高级运维人员也可以修改和添加规则。

  * [平台内置的告警规则](<../appendix1/alarm_rules.html>)
  * [管理和修改告警规则](<setting.html>)

## 实时性能

**说明：该节点最近60秒内，处理Web 请求的平均处理时间（不含用户与Web Server之间的网络传输时间和Web Server自身处理时间），每隔5秒钟采集一次**

  * `处理时间` = 该节点返回Web结果时的时间-接收Web 请求时的时间
  * 请求类型包括：/w的页面请求，/jd的JSON请求，/xd的XML请求

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/13.png)

## 实时压力

**说明：该节点最近12分钟（每隔1分钟采集1次）和最近60秒（每隔5秒采集1次）内，来自Web的请求次数**

  * `压力` = Web Server向该节点提交的请求次数
  * 请求包括：/w的页面请求，/jd的JSON请求，/xd的XML请求

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/14.png)

## 实时CPU使用

**说明：该节点在最近一段时间的CPU使用率**

  * 每分钟采集一次
  * 每5秒采集一次

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/15.png)

### 实时内存使用

**说明：该节点在最近一段时间的内存分配情况**

  * 每分钟采集一次
  * 每5秒采集一次
  * `总物理内存` = 部署该节点的操作系统全部内存（G)
  * `剩余可用物理内存` = 部署该节点的操作系统剩余可用内存（G)
  * `JVM总内存` = 分配给该节点JVM的最大可用内存（G)

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/16.png)