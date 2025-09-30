# 创建常规Job | AWS 定时器开发参考指南

## 创建常规Job

在指定的触发条件执行一次或周期重复执行指定的Java程序。

### 步骤1：编码准备

参照`IJob`编程接口，完成Job实现类的编写。详细开发过程，请[移步到这里](<../job_dev/sample_job.html>)。

### 步骤2：新建

  1. 登录您的AWS PaaS实例控制台
  2. 访问“调度服务”页面
  3. 点击“新建”按钮
  4. 输入Java程序所在的应用，并选择“Job 常规定时任务”
  5. 点击“确定”按钮，完成新建

> 任务的配置信息将创建在选择的应用。同时，您编译的Java代码必须部署在该应用下，即%AWS-HOME%/apps/install/%your appId%/lib

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/2.png)

### 步骤3：完成配置

**如下图所示** ![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/3.png)

项 | 说明  
---|---  
任务名称 | 易于运维人员了解的Job名，如`异常交易监控`  
任务执行类 | Java类路径，请[移步到这里](<../job_dev/sample_job.html>)  
顺序执行 | 选中后，上下文参数被持久化，Job不会并行执行。等同于[互斥Job](<../job_dev/concurrently_job.html>)  
自定义参数 | 自定义的串（可选），开发者可以在程序中读取该值，支持基本的@公式  
触发规则 | 执行该Job的循环策略  
通知规则 | 执行该Job的通知规则，支持手机短信、邮件通知、企业微信、钉钉、飞书通知，详见[邮件通知-系统通知](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/appendix/scenes.html#a>)