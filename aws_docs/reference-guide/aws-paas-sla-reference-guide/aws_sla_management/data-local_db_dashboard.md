# 监控本地数据库 | AWS SLA参考指南

# 监控本地数据库

分析某个AWS PaaS实例采集的`本地数据库`类监控数据，包括

  * 告警事件
  * 数据库连接
  * SQL执行耗时
  * SQL执行错误次数
  * 数据库连接池活动连接数
  * 数据库连接池空闲连接数
  * 数据库连接池大小

`本地数据库`是指为运行AWS平台所提供的数据库服务，内部对组织、流程等全部DB操作时，访问该数据库。

当AWS处于集群部署时，每个AWS实例节点都指向该数据库。

## 告警事件

**说明：该AWS实例有关`本地数据库`类指标发生的告警信息，列出最新5条。**

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/51.png)

告警规则Id | 告警标题 | 触发规则  
---|---|---  
(LOCAL DB)Slow SQL | (本地数据库)慢SQL | 大于5秒  
(LOCAL DB)Error | (本地数据库)SQL执行出错 | 发生即触发  
  
告警规则是内置的，高级运维人员也可以修改和添加规则。

  * [平台内置的告警规则](<../appendix1/alarm_rules.html>)
  * [管理和修改告警规则](<setting.html>)

## 数据库连接

**说明：回放该AWS实例数据库连接占用情况，用于辅助分析当性能变差时是否与某些慢SQL有关**

列表通常为空，不会自动刷新，点击右侧`刷新`按钮可抓取最新数据。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/52.png)

点击右侧的耗费时间按钮，会弹出程序调用堆栈，辅助开发人员诊断代码执行位置。

_诊断思路_

  * 如果`耗时`一直不合理的存在，该段程序可能未关闭数据库连接
  * 慢SQL导致该线程长期处于执行状态
  * 如果执行时间超过`conf/db_pool.properties`的`maxWait`设定大小，将强行中断并监控到一次SQL错误

## SQL执行耗时

**说明：回放该AWS实例SQL执行耗时情况，用于辅助分析故障时段的SQL性能波动情况，判断是否该时段数据库存在优化点**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/53.png)

> 通常合理的SQL执行应在1000毫秒内。对于批量sql(batch sql)提交或复杂报表查询处理，存在客观的执行耗时情况，应根据经验情况判断是否为可优化的慢SQL。

_慢SQL的诊断思路_

  * SQL索引/语句结构的合理性
  * 通过程序逻辑避免/降低SQL处理次数
  * 优化代码的SQL场景，数据库的锁机制导致SQL处于竞争等待状态
  * 数据库参数优化、配置增强（如磁盘读写速度、内存、集群），检查数据库级日志
  * 查看SLA相关时段的数据库慢SQL告警信息，了解具体SQL和代码位置
  * 如果执行时间超过`conf/db_pool.properties`的`maxWait`设定大小将强行中断，SLA将监控到一次SQL错误

## SQL执行错误次数

**说明：回放该AWS实例SQL出错情况，用于辅助分析故障时段的SQL出错频率**

  * 最近24小时（5分钟合计数据）
  * 最近15天（1小时合计数据）
  * 最近1年（1天合计数据）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/54.png)

_诊断思路_

  * SQL语法错误，如错误的拼写
  * 数据库层问题，如网络故障、违反数据库配额限制（如超出最大游标数）、数据库内部错误
  * 查看SLA相关时段的数据库错误告警信息，了解具体SQL和代码位置
  * 检查错误发生时段，`logs/aws.log`日志文件内容

## 数据库连接池活动连接数

**说明：回放该AWS实例数据库连接池的活动连接数情况，用于辅助分析故障时段的连接池内部状况**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/55.png)

_诊断思路_

  * 正常情况，SQL处理的并发量越大时，瞬时的活动数越大
  * 正常情况，与`conf/db_pool.properties`的`minIdle`参数有关，当无SQL处理时会降至`minIdle`设定大小
  * 慢SQL、数据库负荷过高等情况，也会使SQL处理拥挤，导致活动数量上升
  * 如果该值已接近`conf/db_pool.properties`的`maxActive`设定大小，分析是否需要调大该参数

## 数据库连接池空闲连接数

**说明：回放该AWS实例数据库连接池的空闲连接数情况，用于辅助分析故障时段的连接池内部状况**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/56.png)

_诊断思路_

  * 正常情况，与`conf/db_pool.properties`的`minIdle`参数有关，当无SQL处理时会降至`minIdle`设定大小
  * 慢SQL、数据库负荷过高等情况，也会使SQL处理拥挤，导致空闲可用连接下降

## 数据库连接池大小

**说明：回放该AWS实例数据库连接池大小情况，用于辅助分析故障时段的连接池内部状况**

  * 最近24小时（5分钟数据）
  * 最近15天（1小时数据）
  * 最近1年（1天数据）
  * 最大值、最小值、平均值

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/57.png)

_诊断思路_

  * 最大连接数不得大于数据库允许的连接数，否则数据库会抛出异常，SLA将监控到一次SQL错误
  * 与`conf/db_pool.properties`的`maxActive`参数有关

## db_pool.properties

AWS使用了Tomcat JDBC Pool，参数文件路径：
    
    
    %AWS-HOME%/bin/conf/db_pool.properties
    

有关参数的详细介绍，请参见官方说明

<http://tomcat.apache.org/tomcat-7.0-doc/jdbc-pool.html>