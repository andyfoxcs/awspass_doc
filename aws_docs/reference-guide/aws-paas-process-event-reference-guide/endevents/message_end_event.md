# 消息结束事件 | AWS BPMN2 Event参考指南

# 消息结束事件（Message End Event）

在消息事件结束之前，引擎向系统内部（又叫`内部消息`）发出一条消息或者调用外部系统接口（注册到AWS CC的服务），随即事件结束，所在流程分支结束。如果当前分支是最后一个活动分支，流程实例结束。

### 图形符号

单结束 | 多结束  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/41.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/42.png)  
  
### 选项开关

**消息类型**

  * 内部消息
  * 外部接口

**1\. 内部消息**

发出一个内部消息。要正确抛出消息，首先在该流程属性的`消息`中定义消息变量名，并确保消息变量名与订阅消息的事件名、关联规则一致。

**2\. 外部接口**

调用外部服务接口。要正确调用外部服务，首先在AWS CC中完成服务注册，并在`数据映射`中对该服务的参数进行值初始化。

> 目前AWS的`抛出消息事件`只支持Web Service类外部接口和简单参数格式，对于复杂参数格式的重要服务处理，建议使用[Service Task](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/README.html>)。

### API使用场景

消息结束事件（Message End Event）由引擎自动触发，不需要API。

### 延伸阅读

  * [消息数据处理](<../appendix/message_data.html>)
  * [让消息开始事件（Message Start Event）接收消息](<../startevents/message_start_event.html>)
  * [让捕获消息事件（Message Intermediate Catch Event）接收消息](<../intermediateevents/message_intermediate_catch_event.html>)
  * [让边界消息事件（Message Boundary Interrputing Event）接收消息](<../boundaryevents/message_boundary_interrputing_event.html>)