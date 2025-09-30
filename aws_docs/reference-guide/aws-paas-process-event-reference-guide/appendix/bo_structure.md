# BO结构对象 | AWS BPMN2 Event参考指南

# BO结构对象

BO结构（BO Structure）是AWS BO模型的一种，用来描述一个业务对象的数据结构，但不做持久化操作。主要应用在以下场景的参数传递：

  * [信号开始事件（Signal Start Event）](<../startevents/signal_start_event.html>)
  * [捕获信号事件（Signal Intermediate Catch Event）](<../intermediateevents/signal_intermediate_catch_event.html>)
  * [抛出信号事件（Signal Intermediate Throwing Event）](<../intermediateevents/signal_intermediate_throwing_event.html>)
  * [边界信号事件（Signal Boundary Interrputing Event）](<../boundaryevents/signal_boundary_interrputing_event.html>)
  * [信号结束事件（Signal End Event）](<../endevents/signal_end_event.html>)

与其他AWS模型相同，在不同环境中，支持AWS PaaS的模型`受管(Managed)`控制。

> 版本环境文档：<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

支持的数据类型主要包括：

  * 字符类（String）
  * 数值类（Double、Long、Intger）
  * 日期类（Date、Timestamp）