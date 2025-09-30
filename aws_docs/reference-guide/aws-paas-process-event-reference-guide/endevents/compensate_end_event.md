# 补偿结束事件 | AWS BPMN2 Event参考指南

# 补偿结束事件（Compensate End Event）

当执行到达`补偿结束事件`时触发该流程已完成任务的[边界补偿事件（Compensate Boundary Interrputing Event）](<../boundaryevents/compensate_boundary_interrputing_event.html>)，表示流程或分支在发生业务补偿后结束。如果执行业务补偿时抛出的异常，该流程不会结束（状态仍然为`active`）。

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/61.png)

例如，当客户拒收货物后，执行`付款`节点的`边界补偿事件`，自动完成退款操作。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/62.png)

### 选项开关

**是否等待补偿完毕**

如果不等待，触发`边界补偿事件`后不等待事件是否已处理完毕，直接结束流程。

**补偿范围**

指定要触发`边界补偿事件`的节点。如果未设置默认该流程全部含有`边界补偿事件`的任务实例。

### API使用场景

补偿结束事件（Compensate End Event）由引擎自动触发，不需要API。

### 延伸阅读

  * [边界补偿事件（Compensate Boundary Interrputing Event）](<../boundaryevents/compensate_boundary_interrputing_event.html>)