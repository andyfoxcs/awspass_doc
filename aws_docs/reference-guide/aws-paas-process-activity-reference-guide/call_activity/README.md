# 调用子流程（Call Activity） | AWS BPMN2 Activity参考指南

# 调用子流程（Call Activity）

`调用子流程（Call Activity）`（又称为`子流程任务`）是一个特殊的自动化容器任务，其内在包含了对子流程(Sub Process)的创建、启动和调度管理。

当流程到达子流程任务时，按照配置策略自动启动子流程实例，父流程的该分支中断在这里等待子流程实例全部结束后继续执行后继路线。

子流程模型可以再包含`调用子流程（Call Activity）`，成为层层嵌套的多级流程。

### 图形符号

符号 | 说明  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/8.png) | 调用外部流程，该流程实例全部结束后，任务执行完成  
  
**主流程示例**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/mainProcess.png)

### 进阶设置

一个未做配置的子流程任务不可以被引擎正常执行，需要指定要调用的子流程模型和启动者账户。

  * [配置子流程](<subprocess_config.html>)
  * [事件触发器](<event.html>)
  * [扩展属性](<advance_property.html>)

### 用API创建任务
    
    
    //创建子流程任务实例，并自动启动预配置的子流程实例
    SDK.getTaskAPI().createCallActivityTaskInstance( processInst,
    parentTaskInstModel, targetActivityDefId, title);