# 边界消息事件 | AWS BPMN2 Event参考指南

# 边界消息事件（Message Boundary Interrputing Event）

当执行到达`边界消息事件`依附的任务时（如[人工任务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/README.html>)、[子流程](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/README.html>)），引擎会创建一个捕获事件，在其依附的任务的生命周期内等待一个`抛出消息`，该消息来自`消息抛出事件`或者API，被触发后后继路线继续执行。如果该边界事件设置为`中断`，依附的任务将中断执行。

  * 订阅流程中[抛出消息事件（Message Intermediate Throwing Event）](<../intermediateevents/message_intermediate_throwing_event.html>)、[消息结束事件（Message End Event）](<../endevents/message_end_event.html>)发出的`内部消息`，匹配并完成事件任务，继续后继路线
  * 收到外部事件（如JMS、自行发布的HTTP/SOAP服务）后，匹配并完成事件任务，继续后继路线

该事件到达后会在WFC_TASK创建一个类型为`catchEvent`、`EXT1`为`message`、`EXT2`为消息变量名、`EXT3`为捕获规则的记录。完成处理后，状态标记为`complete`归档到历史表。

> 如果流程修改了消息变量名或匹配规则，只对该事件创建的新实例有效

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/31.png)

### 选项开关

**消息**

设置要订阅的消息。要正确监听消息，首先在该流程属性的`消息`中定义消息变量名。

**关联规则**

一个必选的进阶匹配规则。当订阅到匹配的消息后，通过`捕获规则`确定唯一的事件任务（如果匹配了多个中断的事件任务，只允许其中一个作为有效订阅者）。

例如，接收到名为`Alibaba-B2B-Order`，`捕获规则`为`201702040007`的消息，匹配并完成该事件任务。

> 每个消息只允许有一个订阅者（subscriber），在实施策略上，请遵循`消息名`+`捕获规则`的全局唯一性

**是否中断**

如果中断，主活动（任务）实例被终止，但该事件的后继路线继续执行。

### API使用场景

边界消息事件（Message Boundary Interrputing Event）由引擎自动触发，不需要API。

### 延伸阅读

  * [消息数据处理](<../appendix/message_data.html>)
  * [订阅抛出消息事件（Message Intermediate Throwing Event）发出的消息](<../intermediateevents/message_intermediate_throwing_event.html>)
  * [订阅消息结束事件（Message End Event）发出的消息](<../endevents/message_end_event.html>)