# 内置SQLScript服务 | AWS BPMN2 Activity参考指南

# 内置SQLScript服务

在流程图中编排一个可执行SQL自动化任务。

**主要功能**

  * 执行本地数据库或一个CC JDBC指定的外部数据源
  * SQL语句支持INSERT/UPDATE/DELETE
  * SQL语句支持@公式
  * 支持多条语句（换行隔开）
  * 多语句执行在一个事务内完成

### 使用方法

  1. 在流程图加入一个[Service Task](<../service_task/process_service.html>)
  2. 从流程服务库里选择`SQLScript`
  3. 完成SQL脚本的配置

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/appendix/31.png)

参数 | 说明  
---|---  
数据源 | 可输入CC JDBC的ID，空值表示当前数据库  
SQL语句 | 支持@公式的UPDATE/INSERT/DELETE，多条SQL语句使用回车