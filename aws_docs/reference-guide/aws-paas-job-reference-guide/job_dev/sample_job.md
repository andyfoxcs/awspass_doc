# 简单Job例子 | AWS 定时器开发参考指南

## 简单Job例子

**开发步骤**

  1. 创建您的App Java工程。获得本地开发环境，请[移步这里](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/ide/README.html>)
  2. 实现`com.actionsoft.bpms.schedule.IJob`接口
  3. 将HelloJob类注册到Job
  4. 观察执行结果

### HelloJob.java

该示例在`AWS SDK API接口验证`(com.actionsoft.apps.poc.api)中提供源码。
    
    
    package com.actionsoft.apps.poc.api.local.job;
    
    import org.quartz.JobExecutionContext;
    import org.quartz.JobExecutionException;
    
    import com.actionsoft.bpms.schedule.IJob;
    import com.actionsoft.sdk.local.SDK;
    
    public class HelloJob implements IJob {
    
        public void execute(JobExecutionContext jobExecutionContext)
            throws JobExecutionException {
            // 读管理员配置的扩展参数串，支持简单的@公式
            String param = SDK.getJobAPI().getJobParameter(jobExecutionContext);
            System.out.println("Hello AWS PaaS Job Demo! Param = " + param);
        }
    }
    

JobExecutionContext是Quartz提供的任务执行上下文对象，相关信息可通过[Quartz](<http://quartz-scheduler.org/>)网站了解更多

**相关API**

  * SDK.getJobAPI().getJobParameter 读取维护的扩展参数
  * SDK.getJobAPI().getJobModel 读取Job配置模型

### 将HelloJob类注册到Job

参见[这里](<../scheduler_management/create_job.html>)

### 观察执行结果

当配置的触发策略被执行后，在AWS的后端控制台将打印输出：
    
    
    Hello AWS PaaS Job Demo! Param = Today is 2015-08-19