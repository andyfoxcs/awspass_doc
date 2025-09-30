# 边界事件（Boundary Events） | AWS BPMN2 Event参考指南

# 边界事件（Boundary Events）

边界事件属于[中间事件](<../intermediateevents/README.html>)的一类。边界事件附加在活动（任务）的边界上，此时的事件只能捕获触发器。根据捕获后对路线影响的不同行为，又分为两种：边界中断事件和边界非中断事件。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/1.png)

  * 边界中断事件。附加的活动（任务）实例被终止，执行该事件的后继路线
  * 边界非中断事件。附加的活动（任务）实例继续执行，同时执行该事件的后继路线

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/2.png)

  * [边界消息事件](<message_boundary_interrputing_event.html>)
  * [边界时间事件](<timer_boundary_interrputing_event.html>)
  * [边界信号事件](<signal_boundary_interrputing_event.html>)
  * [边界补偿事件](<compensate_boundary_interrputing_event.html>)
  * [边界错误事件](<error_boundary_interrputing_event.html>)