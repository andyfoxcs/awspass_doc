# 监控MVC框架 | AWS SLA参考指南

# 监控MVC框架

分析某个AWS PaaS实例采集的`MVC框架`类监控数据，包括

  * 告警事件
  * MVC压力
  * 用户/会话
  * MVC性能
  * Web页面性能
  * 身份验证性能
  * Data请求性能
  * ASLP执行性能
  * 文件上传性能
  * 文件下载性能

> 注意：MVC的耗时类指标值，是AWS App Server内部的处理时间，不包含Web Server向用户端传输和客户端页面渲染时间

当AWS处于集群部署时，每个AWS实例节点的MVC框架性能表现可能是不一样的。

## 告警事件

**说明：该AWS实例有关`MVC框架`类指标发生的告警信息，列出最新5条。**

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/31.png)

告警规则Id | 告警标题 | 触发规则  
---|---|---  
Slow Web Response | 有延迟感的用户响应 | 大于10秒  
MVC High Load | MVC负载过高 | 连续2次大于500并发  
Slow ASLP Service | 有延迟感的ASLP服务 | 大于10秒  
  
告警规则是内置的，高级运维人员也可以修改和添加规则。

  * [平台内置的告警规则](<../appendix1/alarm_rules.html>)
  * [管理和修改告警规则](<setting.html>)

## MVC压力

**说明：回放该AWS实例MVC框架处理次数情况（接收Web服务器发送的请求）。用于辅助分析当性能变差时，是否与用户或API请求量增大有关**

  * 最近24小时（5分钟合计数据）
  * 最近15天（1小时合计数据）
  * 最近1年（1天合计数据）
  * `压力` = Web Server向该节点提交的请求次数
  * 请求包括：/w的页面请求，/jd的JSON请求，/xd的XML请求，/uf附件上传请求，/df附件下载请求

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/32.png)

_诊断思路_

  * 请求可能来自用户页面操作，也可能来自外部系统的API调用
  * 在不增加集群节点时，扩大用户访问范围或部署新应用，可能会导致压力数据增大
  * 压力变化波动不大时，增加集群节点可以分散单一节点的处理请求数，间接减小压力

## 用户/会话

**说明：回放该AWS实例活跃用户和会话数情况（集群多个AWS实例数据相同），用于辅助分析近期时段用户在线情况。`活跃用户` <= 实际登录的用户**

  * 最近24小时（5分钟平均数据）
  * 最近15天（1小时平均数据）
  * 最近1年（1天平均数据）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/33.png)

_诊断思路_

  * `活跃用户数`越高，说明系统的使用率越频繁
  * 用户每次登录系统时，一个有效会话被创建。如果用户未正常离开系统，该会话在超出`conf/server.xml`的`sessionTimeout`设定大小时被自动销毁。`有效会话数`总是高于`活跃用户数`（偶尔峰值100倍内合理），在晚间登录量下降时自然回落
  * 如果`有效会话数`持续高于百倍的`活跃用户数`，一定是有开发者实施SSO类场景时未利用某用户可用会话所致。发生这类情况会在较短时期内产生大量Session，并导致系统性能变缓，必须进行代码检查和调整

## MVC性能

**说明：回放该AWS实例MVC框架处理请求耗时情况，用于辅助分析MVC框架各种场景对操作等待的体验度**

  * 最近24小时（5分钟平均数据）
  * 最近15天（1小时平均数据）
  * 最近1年（1天平均数据）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/34.png)

_诊断思路_

  * 内部关键场景的处理变缓时（如慢SQL、集成外部系统的网络编程），最终都可能直接导致MVC性能变差
  * 查看SLA相关时段的告警信息（如慢SQL、延迟感警告），根据详细信息寻找线索，解决问题
  * 如果瓶颈来自请求数陡增，增加集群节点也可以分散计算压力
  * 这是一个总览分析，下面的分项图表提供了更详细的数据

## Web页面性能

**说明：回放该AWS实例处理Web页面类请求的耗时情况，用于辅助感知用户在PC或移动端等待返回页面的体验度**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/35.png)

_诊断思路_

  * 查看SLA相关时段的告警信息（如`有延迟感的用户响应`），根据详细信息寻找线索，解决问题
  * 排查级联的告警线索，如产生`有延迟感的用户响应`的原因是发生了一次`慢SQL`导致
  * 减少SQL操作次数和适当索引

## 身份验证性能

**说明：回放该AWS实例处理用户身份验证耗时情况，用于辅助分析内部身份鉴权环节所消耗的时间。尤其在实施LDAP或第三方身份验证后，用户登录变差时应重点关注该指标**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/36.png)

_诊断思路_

  * 排查和改善第三方LoginAdapter代码逻辑，定位是否由第三方登录验证的API性能或网络延迟造成，制定优化方案
  * 减少SQL操作次数和适当索引
  * 参见`用户/会话`诊断思路
  * 如果该指标正常，但用户登录依旧反应迟钝，分析用户登录后的门户首页加载信息量，重点优化或减少首页提供的数据项即可大大改善用户登录体验

## Data请求性能

**说明：回放该AWS实例处理JSON/XML类HTTP请求的耗时情况，用于辅助分析Ajax类请求的处理速度（如为前端页面Grid加载数据）**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/37.png)

_诊断思路_

  * 参见`Web页面性能`诊断思路
  * 参见`SQL执行耗时`诊断思路

## ASLP执行性能

**说明：回放该AWS实例处理ASLP请求的耗时情况，辅助分析移动端或其他应用调用ASLP场景的性能**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/38.png)

_诊断思路_

  * 查看SLA相关时段的告警信息（如`有延迟感的ASLP服务`），根据详细信息寻找线索，解决问题
  * 参见`Web页面性能`诊断思路
  * 参见`SQL执行耗时`诊断思路

## 文件上传性能

**说明：回放该AWS实例处理文件上传的耗时情况，用于辅助分析用户上传文件时存储/加密所消耗的时间。注意，该指标不能分析用户从客户端到Web服务器的传输时间**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/39.png)

_诊断思路_

  * 限制附件上传大小，降低存储盘I/O
  * 企业网管分析Web服务总出口的网络流量，分配更高的出口带
  * 企业网管分析存储盘I/O的性能表现，通过硬件方案提高磁盘I/O速度
  * 如果客户方案为密集型文档处理业务，建议为该节点适当增加CPU（或增加新的集群节点），提高加密的运算速度

## 文件下载性能

**说明：回放该AWS实例处理文件下载的耗时情况，用于辅助分析用户下载文件时读取/解密所消耗的时间。注意，该指标不能分析用户从客户端到Web服务器的传输时间**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/40.png)

_诊断思路_

  * 限制附件上传大小，降低存储盘I/O
  * 企业网管分析Web服务总出口的网络流量，分配更高的出口带
  * 企业网管分析存储盘I/O的性能表现，通过硬件方案提高磁盘I/O速度
  * 如果客户方案为密集型文档处理业务，建议为该节点适当增加CPU（或增加新的集群节点），提高解密的运算速度