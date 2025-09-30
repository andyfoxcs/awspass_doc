# 互斥Job例子 | AWS 定时器开发参考指南

## 互斥Job例子

在Job类上使用注解org.quartz.DisallowConcurrentExecution可以实现同一时刻只运行一个任务实例。还可以通过注解org.quartz.PersistJobDataAfterExecution持久化上下文中的参数。互斥示例：

**开发步骤**

  1. 创建您的App Java工程。获得本地开发环境，请[移步这里](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/ide/README.html>)
  2. 实现`com.actionsoft.bpms.schedule.IJob`接口
  3. 增加类注解`org.quartz.DisallowConcurrentExecution`
  4. 将LongTimeJob类注册到Job
  5. 观察执行结果

### LongTimeJob.java

该示例在`AWS SDK API接口验证`(com.actionsoft.apps.poc.api)中提供源码。
    
    
    package com.actionsoft.apps.poc.api.local.job;
    
    import java.util.Date;
    
    import org.quartz.JobExecutionContext;
    import org.quartz.JobExecutionException;
    
    import com.actionsoft.bpms.schedule.IJob;
    import com.actionsoft.bpms.util.UtilDate;
    
    @DisallowConcurrentExecution
    public class LongTimeJob implements IJob {
    
        /**
         * 演示互斥操作。该Job模拟运行30秒，但在调度配置上每隔10秒调度一次。运行期望结果是，该Job不会被并发执行
         */
        public void execute(JobExecutionContext jobExecutionContext)
            throws JobExecutionException {
            long times = System.currentTimeMillis();
            System.out.println("Long Time Job Demo (" + times + ")! Begin "
                + UtilDate.datetimeFormat(new Date()));
            // wait 30s
            try {
                Thread.sleep(1000 * 30);
            } catch (Exception e) {
                e.printStackTrace();
            }
            System.out.println("Long Time Job Demo (" + times + ")! End "
                + UtilDate.datetimeFormat(new Date()));
        }
    }
    

JobExecutionContext是Quartz提供的任务执行上下文对象，相关信息可通过[Quartz](<http://quartz-scheduler.org/>)网站了解更多

**相关API**

  * SDK.getJobAPI().getJobParameter 读取维护的扩展参数
  * SDK.getJobAPI().getJobModel 读取Job配置模型

### 将LongTimeJob类注册到Job

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/job_dev/1.png)

> 注意
> 
>   1. 执行间隔要小于30秒，测试并发冲突的场景
> 

### 观察执行结果

当配置的触发策略被执行后，不会出现多个Job实例同时被触发的场景，将在AWS的后端控制台顺序打印输出：
    
    
    Long Time Job Demo (1439957461997)! Begin 2015-08-19 12:11:01
    Long Time Job Demo (1439957461997)! End 2015-08-19 12:11:32