# 边界补偿事件 | AWS BPMN2 Event参考指南

# 边界补偿事件（Compensate Boundary Interrputing Event）

当`边界补偿事件`依附的节点触发`回退`操作时，`边界补偿事件`自动被激活，执行补偿事件后继路线上的任务。

  * 如果此事件依附节点尚未产生历史任务，不会被触发
  * 补偿被触发的次数与依附节点的历史任务的成功完成次数相等（如`批准订单`被执行过2次任务，那么会触发2次补偿动作）
  * 补偿被触发的次数与依附节点的循环多例任务的成功完成次数相等

`边界补偿事件`被激活后，在`WFH_TASK`创建一个标题为`Boundary Event Subscription-xxx`的记录，类型为`catchEvent`。

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/41.png)

### 选项开关

无

### 由`异常策略`触发

在系统类节点(如[系统任务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/README.html>)、[脚本任务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/README.html>))采取如下异常策略时会触发边界补偿事件。

  * 单步回退
  * 回退到上个人工任务
  * 按路径回退

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/42.png)

### 由`抛出补偿事件`触发

当执行到达[抛出补偿事件（Compensate Intermediate Throwing Event）](<../intermediateevents/compensate_intermediate_throwing_event.html>)时会触发边界补偿事件。

### 由`补偿结束事件`触发

当执行到达[补偿结束事件（Compensate End Event）](<../endevents/compensate_end_event.html>)时会触发边界补偿事件。

### API使用场景

在调用TaskAPI.rollbackTask时会触发边界补偿事件。`taskInstId`是执行回退的当前任务（例如Y节点），`targetActivityId`是要回退的目标节点（例如X节点）。X节点到Y节点如果产生了历史任务，且历史任务的节点有使用边界补偿事件（Compensate Boundary Interrputing Event）对业务反向处理进行了补偿建模，引擎会激活边界补偿事件的后继路线。
    
    
    //执行回退操作
    SDK.getTaskAPI().rollbackTask(taskInstId, targetActivityId, uid,
    isCompensation, rollbackReason)
    

> 可以在后台的`实例运行管理`管理事件的任务实例

### 延伸阅读

  * [系统类任务的异常处理](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/exception.html>)
  * [抛出补偿事件（Compensate Intermediate Throwing Event）](<../intermediateevents/compensate_intermediate_throwing_event.html>)
  * [补偿结束事件（Compensate End Event）](<../endevents/compensate_end_event.html>)