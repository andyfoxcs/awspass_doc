# 系统任务（Service Task） | AWS BPMN2 Activity参考指南

# 系统任务（Service Task）

系统任务（Service Task）是一个自动化任务。当流程到达系统任务时，自动执行编写的Java程序，完毕后继续执行后继路线。

### 图形符号

符号 | 说明  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/2.png) | 一个Java Service，可以执行AWS内部或外部服务  
  
### 调度模式

当流程到达系统任务时，采取何种执行策略。

  * **同步** ，等待逻辑处理完毕后再执行后继路线。如果执行过程抛出异常，按`异常处理`策略进行控制
  * **异步** ，不用等待逻辑处理的结果，同时执行后继路线。如果执行过程抛出异常，不会中断和影响流程的处理路线

> 对于需要大量运算，其结果不会干涉流程处理路线的服务，建议使用`异步`调度模式

### 进阶设置

一个未做配置的系统任务可以被引擎正常执行，建模人员可以通过增强配置来符合业务流程的处理要求。

  * [调用普通Java服务](<java_service.html>)
  * [调用公共流程服务](<process_service.html>)
  * [异常处理](<exception.html>)
  * [事件触发器](<event.html>)
  * [扩展属性](<advance_property.html>)

### 用API创建任务
    
    
    //创建系统任务实例，并自动执行
    SDK.getTaskAPI().createServiceTaskInstance(processInst, parentTaskInstModel, targetActivityDefId,
    title, isAsync);
    

### 用API完成任务
    
    
    //与人工任务
    SDK.getTaskAPI().completeTask(taskInst, vars, userContext);
    

### 用API查询任务列表
    
    
    List<TaskInstance> tasks=SDK.getTaskQueryAPI().activeTask().listPage(firstRow, rowCount);
    

> 全部API文档，[参见这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)