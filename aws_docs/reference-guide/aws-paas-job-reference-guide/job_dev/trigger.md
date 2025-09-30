# 自定义触发器 | AWS 定时器开发参考指南

## 自定义触发器

当AWS PaaS提供的`触发定义`不能满足需要时，可以开发自定义的触发器，由程序指定该Job何时被触发。

> [Cron表达式](<http://baike.baidu.com/link?url=asDnHLpO2lVIJvJWQIj7i76Ui90wVEdsDx8hkL4BiJKEOotPhQtclYGtOMAsmHGxOUw0a1FvI3nU57dc8b_kD_>)是一种很灵活的表达式，能够描述足够复杂的调度规则，建议开发者先熟练掌握Cron。当遇到排查节假日等极特殊情况下才建议通过Java代码自定义触发器

**开发步骤**

  1. 创建您的App Java工程。获得本地开发环境，请[移步这里](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/ide/README.html>)
  2. 实现`com.actionsoft.bpms.schedule.ITrigger`接口
  3. 将[HelloJob类](<sample_job.html>)注册到Job，并在`触发定义`中，指定使用HelloTrigger作为触发器
  4. 观察执行结果

### HelloTrigger.java

该示例在`AWS SDK API接口验证`(com.actionsoft.apps.poc.api)中提供源码。
    
    
    package com.actionsoft.apps.poc.api.local.job;
    
    import org.quartz.SimpleTrigger;
    import org.quartz.Trigger;
    
    import com.actionsoft.bpms.schedule.ITrigger;
    
    public class HelloTrigger implements ITrigger {
    
        public Trigger getTrigger(String name, String group) {
            // 执行2次，间隔5秒钟，必须使用参数中name/group为trigger的identity
            SimpleTrigger trigger = TriggerBuilder.newTrigger().withSchedule(SimpleScheduleBuilder.repeatSecondlyForTotalCount(2, 5)).withIdentity(name, group).build();
            return trigger;
        }
    
    }
    

> 有关开发Trigger的细节文档，请参考[Quartz网站](<http://quartz-scheduler.org/documentation>)

### 将HelloJob类注册到Job，并使用HelloTrigger

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/job_dev/2.png)

### 观察执行结果

当配置的触发策略被执行后，将在AWS的后端控制台打印输出三行记录：
    
    
    Hello AWS PaaS Job Demo! Param = Today is 2015-08-19
    Hello AWS PaaS Job Demo! Param = Today is 2015-08-19
    Hello AWS PaaS Job Demo! Param = Today is 2015-08-19