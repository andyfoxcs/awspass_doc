# 开发定时器 | AWS 定时器开发参考指南

# 开发定时器

调度代码听起来很复杂，实际上开发和测试却很简单，开发者几乎只需专注于自己的处理代码。

### IJob接口

将Java代码封装到实现`com.actionsoft.bpms.schedule.IJob`接口的execute方法中，抛出JobExecutionException异常。

**一个示例**
    
    
    public class YourClass implements IJob {
    
        public void execute(JobExecutionContext jobExecutionContext)
            throws JobExecutionException {
            ...
        }
    }
    

### 开发示例

  * [简单Job例子](<sample_job.html>)
  * [互斥Job例子](<concurrently_job.html>)
  * [自定义触发器](<trigger.html>)