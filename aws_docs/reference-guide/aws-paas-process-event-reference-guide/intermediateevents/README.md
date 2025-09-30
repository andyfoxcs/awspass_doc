# 中间事件（Intermediate Events） | AWS BPMN2 Event参考指南

# 中间事件（Intermediate Events）

在`开始事件`和`结束事件`之间发生的事件都称为中间事件。中间事件会影响流程的流转路线，但不会启动或直接终止流程的执行。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/1.png)

本小节只介绍直接出现在流程连线上的中间事件，这类事件即可以捕获触发器又可以抛出结果。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/2.png)

  * **捕获（Catching）事件** 。当流程执行到该事件（Token到达并创建一个持久化的任务实例）, 它会中断执行，等待触发器。当触发条件被捕获后，事件执行完毕，并自动执行后继的路线
  * **抛出（Throwing)）事件** 。当流程执行到该事件（Token到达并创建一个持久化的任务实例）, 抛出一个结果

  * [捕获时间事件](<timer_intermediate_catch_event.html>)

  * [捕获消息事件](<message_intermediate_catch_event.html>)
  * [捕获信号事件](<signal_intermediate_catch_event.html>)
  * [抛出消息事件](<message_intermediate_throwing_event.html>)
  * [抛出信号事件](<signal_intermediate_throwing_event.html>)
  * [抛出补偿事件](<compensate_intermediate_throwing_event.html>)