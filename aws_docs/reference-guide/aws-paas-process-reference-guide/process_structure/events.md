# 事件（Events） | AWS BPMN2 Process参考指南

# 事件（Events）

事件用来表明流程的生命周期中发生了什么事。事件总是画成一个圆圈， 在BPMN 2.0中事件有两大分类：

  * 捕获（Catching）事件。当流程执行到该事件, 它会中断执行，等待被触发
  * 抛出（Throwing)）事件。当流程执行到该事件, 抛出一个结果

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/event.png)

### 清单

BPMN2示例 | 名称  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/10.png) | [开始事件  
None Start Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/none_start_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/12.png) | [时间开始事件  
Timer Start Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/timer_start_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/13.png) | [信号开始事件  
Signal Start Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/signal_start_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/11.png) | [消息开始事件  
Message Start Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/message_start_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/21.png) | [捕获时间事件  
Timer Intermediate Catch Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/timer_intermediate_catch_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/22.png) | [捕获消息事件  
Message Intermediate Catch Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/message_intermediate_catch_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/23.png) | [捕获信号事件  
Signal Intermediate Catch Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/signal_intermediate_catch_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/24.png) | [抛出消息事件  
Message Intermediate Throwing Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/message_intermediate_throwing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/25.png) | [抛出信号事件  
Signal Intermediate Throwing Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/signal_intermediate_throwing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/26.png) | [抛出补偿事件  
Compensate Intermediate Throwing Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/compensate_intermediate_throwing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/31.png) | [边界消息事件  
Message Boundary Interrputing Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/message_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/32.png) | [边界时间事件  
Timer Boundary Interrputing Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/timer_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/33.png) | [边界信号事件  
Signal Boundary Interrputing Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/signal_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/34.png) | [边界补偿事件  
Compensate Boundary Interrputing Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/compensate_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/35.png) | [边界错误事件  
Error Boundary Interrputing Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/error_boundary_interrputing_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/41.png) | [结束事件  
End Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/42.png) | [终止事件  
Terminate End Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/terminate_end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/43.png) | [消息结束事件  
Message End Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/message_end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/44.png) | [信号结束事件  
Signal End Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/signal_end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/45.png) | [错误结束事件  
Error End Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/error_end_event.html>)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/events/46.png) | [补偿结束事件  
Compensate End Event](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/compensate_end_event.html>)