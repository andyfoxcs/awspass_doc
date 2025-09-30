# 事件（Events） | AWS BPMN2 Event参考指南

# 事件（Events）

事件用来描述流程的生命周期中发生了什么事。事件总是画成一个圆圈， 在BPMN 2.0中事件有两大分类：

  * 捕获（Catching）事件。当流程执行到该事件, 它会中断执行，等待被触发
  * 抛出（Throwing)事件。当流程执行到该事件, 抛出一个结果

基于事件对流程的影响，定义了三种事件：

  1. [开始事件](<../startevents/README.html>)
  2. 中间事件（包括[中间事件](<../intermediateevents/README.html>)和[边界事件](<../boundaryevents/README.html>)）
  3. [结束事件](<../endevents/README.html>)

### 使用

从面板拖放一个事件 | 创建连线时选择一个事件  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/2.png)  
改变事件类型 | 复制事件  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/3.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/4.png)  
  
### 清单

BPMN2示例 | 名称  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/10.png) | [开始事件  
None Start Event](<../startevents/none_start_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/12.png) | [时间开始事件  
Timer Start Event](<../startevents/timer_start_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/13.png) | [信号开始事件  
Signal Start Event](<../startevents/signal_start_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/11.png) | [消息开始事件  
Message Start Event](<../startevents/message_start_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/21.png) | [捕获时间事件  
Timer Intermediate Catch Event](<../intermediateevents/timer_intermediate_catch_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/22.png) | [捕获消息事件  
Message Intermediate Catch Event](<../intermediateevents/message_intermediate_catch_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/23.png) | [捕获信号事件  
Signal Intermediate Catch Event](<../intermediateevents/signal_intermediate_catch_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/24.png) | [抛出消息事件  
Message Intermediate Throwing Event](<../intermediateevents/message_intermediate_throwing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/25.png) | [抛出信号事件  
Signal Intermediate Throwing Event](<../intermediateevents/signal_intermediate_throwing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/26.png) | [抛出补偿事件  
Compensate Intermediate Throwing Event](<../intermediateevents/compensate_intermediate_throwing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/31.png) | [边界消息事件  
Message Boundary Interrputing Event](<../boundaryevents/message_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/32.png) | [边界时间事件  
Timer Boundary Interrputing Event](<../boundaryevents/timer_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/33.png) | [边界信号事件  
Signal Boundary Interrputing Event](<../boundaryevents/signal_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/34.png) | [边界补偿事件  
Compensate Boundary Interrputing Event](<../boundaryevents/compensate_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/35.png) | [边界错误事件  
Error Boundary Interrputing Event](<../boundaryevents/error_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/41.png) | [结束事件  
End Event](<../endevents/end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/42.png) | [终止事件  
Terminate End Event](<../endevents/terminate_end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/43.png) | [消息结束事件  
Message End Event](<../endevents/message_end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/44.png) | [信号结束事件  
Signal End Event](<../endevents/signal_end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/45.png) | [错误结束事件  
Error End Event](<../endevents/error_end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/46.png) | [补偿结束事件  
Compensate End Event](<../endevents/compensate_end_event.html>)  
  
### 专业分级

AWS PaaS为降低BPMN建模的复杂度，提供了三个级别的能力配置，其中level0（默认）适合普通企业建模用户。

  * level0 核心
  * level1 专业
  * level2 实验室

> 这是一个BPMN引擎的高级配置项，如调高级别，需专业人员提供协助。有关不同等级的差异，请参考这里<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/README.html>