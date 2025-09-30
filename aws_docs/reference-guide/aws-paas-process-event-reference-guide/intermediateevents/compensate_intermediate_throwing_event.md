# 抛出补偿事件 | AWS BPMN2 Event参考指南

# 抛出补偿事件（Compensate Intermediate Throwing Event）

当执行到达`抛出补偿事件`时触发该流程已完成任务的[边界补偿事件（Compensate Boundary Interrputing Event）](<../boundaryevents/compensate_boundary_interrputing_event.html>)，完成补偿操作后自动执行后继路线。

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/61.png)

例如，当客户拒收货物后，执行`付款`节点的`边界补偿事件`，在完成退款操作后继续执行该事件的后继路线，给客服人员创建`满意度调查`任务。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/62.png)

### 选项开关

无

### API使用场景

抛出补偿事件（Compensate Intermediate Throwing Event）由引擎自动触发，不需要API。

### 延伸阅读

  * [边界补偿事件（Compensate Boundary Interrputing Event）](<../boundaryevents/compensate_boundary_interrputing_event.html>)