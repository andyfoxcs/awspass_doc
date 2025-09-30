# 使用定时器 | AWS 定时器开发参考指南

# 使用定时器

AWS PaaS为开发者和运维管理人员提供定时器管理功能，包括

  * 创建Job
  * 设置Job参数
  * 查看调度日志
  * 锁定Job
  * 暂停/启动Job
  * 删除Job

## 访问

  1. 登录您的AWS PaaS实例控制台
  2. 访问“调度服务”页面

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/1.png)

## 创建

  * [创建常规Job](<create_job.html>)
  * [创建SOAP Job](<create_soap_job.html>)
  * [创建HTTP Job](<create_http_job.html>)
  * [创建SQL Job](<create_sql_job.html>)

### 查看调度日志

在定时器页签上提供了查看日志

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/4.png)

  * 执行时间
  * 执行结果（成功与否）
  * 执行耗时
  * 如果是重复类任务，提供下次被执行的时间
  * 默认显示今天全部的日志
  * 可按今天、昨天、最近两周、最近一个月，及全部、成功、失败进行过滤查看日志