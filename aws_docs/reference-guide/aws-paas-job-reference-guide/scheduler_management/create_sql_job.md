# 创建SQL Job | AWS 定时器开发参考指南

## 创建SQL Job

在指定的触发条件执行一次或周期重复执行指定的数据库SQL。

### 步骤1：新建Job

  1. 访问“调度服务”页面
  2. 点击“新建”按钮
  3. 选择“SQL Job // 定时执行数据库SQL”
  4. 点击“确定”按钮，完成新建

> 任务的配置信息将创建在选择的应用

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/15.png)

### 步骤2：完成配置

**如下图所示** ![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/16.png)

项 | 说明  
---|---  
任务名称 | 易于运维人员了解的Job名，如`转移60天后的日志数据`  
DB连接 | 数据源列表，由AWS CC提供的JDBC技术适配器  
开启事务 | SQL操作要么全部成功，要么全部回滚  
SQL | INSERT/UPDATE/DELETE语句，多个按顺序执行，支持简单@公式  
触发规则 | 执行该Job的循环策略  
通知规则 | 执行该Job的通知规则，支持邮件通知、企业微信、钉钉通知，详见[邮件通知](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/appendix/scenes.html#a>)