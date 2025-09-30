# 日志保留期限 | AWS LOG日志参考指南

# 日志保留期限

  * 存放在物理表中的日志记录
  * 存放在系统中的日志文件
  * SLA服务质量指标处理数据

## 存放在物理表中的日志记录

AWS平台对各种日志类数据定时清理，提供了通用规则配置。

配置文件： _%AWS-HOME%/bin/conf/aws-audit.xml_
    
    
    <!-- fieldtype：字段类型，支持long为数值型，date日期型-->
    <!-- expire：过期时间，单位月-->
    <purge table='SYS_SESSION' field="STARTTIME" fieldtype="long" expire="3" />
    <purge table='SYS_AUDIT_LOG' field="OP_TIME" fieldtype="date" expire="3" />
    <purge table='SYS_SLA_ALARM' field="EVENTTIME" fieldtype="date" expire="6" />
    ...
    

**PurgeJob定时器**

![](https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/appendix/1.png)

  * 每个周日凌晨执行一次

**默认配置的过期清理规则**

表 | 说明  
---|---  
SYS_AUDIT_LOG（审计日志表） | 保留3个月数据  
SYS_SESSION（用户会话表） | 保留3个月数据  
SYS_SLA_ALARM（SLA告警表） | 保留6个月数据  
  
## 存放在系统中的日志文件

AWS基于slf4j日志框架的log4j实现，按默认的参数配置，您需要为1个AWS实例预留至少420M磁盘空间。以此类推，如果计划部署5个集群节点需要预留至少2.1G的磁盘空间。
    
    
    //日志文件目录
    %AWS-HOME%/logs
    

  * 每个日志文件最大20M
  * 滚动保留最新20个历史

    
    
    //default 20000KB
    %AWS-HOME%/bin/conf/aws-log4j.xml#MaxFileSize
    
    //default 20
    %AWS-HOME%/bin/conf/aws-log4j.xml#MaxBackupIndex
    

## SLA服务质量指标处理数据

这些数据以时间为切片，滚动存放在特定的数据库表中（如分钟维度数据，只滚动保留某一指标最近24小时的数据），详细请访问 <https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/table.html>