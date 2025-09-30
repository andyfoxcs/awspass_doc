# 信号结束事件 | AWS BPMN2 Event参考指南

# 信号结束事件（Signal End Event）

在信号事件结束之前引擎向系统内部发出一个信号，随即结束该事件，所在流程分支结束。如果当前分支是最后一个活动分支，流程实例结束。

> 同一个信号可以有多个subscriber（订阅者）

抛出的信号可以被[信号开始事件（Signal Start Event）](<../startevents/signal_start_event.html>)、[中间捕获信号事件（Signal Intermediate Catch Event）](<../intermediateevents/signal_intermediate_catch_event.html>)、[边界信号事件（Signal Boundary Interrputing Event）](<../boundaryevents/signal_boundary_interrputing_event.html>)订阅处理。

### 图形符号

单结束 | 多结束  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/31.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/32.png)  
  
### 选项开关

**信号**

设置要抛出的信号，并确保信号变量名与订阅信号的事件名一致。作为进阶设置，可以通过`数据映射`对抛出的业务数据（`payload`）进行值映射。

> 要抛出信号，首先在该流程属性的`信号`中定义信号变量名，目前信号变量支持[BO Structure类数据结构](<../appendix/bo_structure.html>)

**关联规则**

一个可选的进阶匹配规则。当抛出的信号名相同时，如果规则不匹配则忽略该信号的处理。

例如，订阅到名为`CRM-Order`且匹配规则值为`vip`的信号，匹配并完成该类事件任务。

### API使用场景

信号结束事件（Signal End Event）由引擎自动触发，不需要API。

### 延伸阅读

  * [BO结构对象](<../appendix/bo_structure.html>)
  * [信号数据处理](<../appendix/signal_data.html>)
  * [让信号开始事件（Signal Start Event）接收信号](<../startevents/signal_start_event.html>)
  * [让捕获信号事件（Signal Intermediate Catch Event）接收信号](<../intermediateevents/signal_intermediate_catch_event.html>)
  * [让边界信号事件（Signal Boundary Interrputing Event）接收信号](<../boundaryevents/signal_boundary_interrputing_event.html>)