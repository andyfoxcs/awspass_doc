# 捕获信号事件 | AWS BPMN2 Event参考指南

# 捕获信号事件（Signal Intermediate Catch Event）

当执行到达`捕获信号事件`时中断在这里，等待`抛出信号事件`或者API发出匹配的信号后结束，流程沿后继路线继续执行。

  * 订阅流程中[抛出信号事件（Signal Intermediate Throwing Event）](<../intermediateevents/signal_intermediate_throwing_event.html>)、[信号结束事件（Signal End Event）](<../endevents/signal_end_event.html>)发出的信号，匹配并完成事件任务，继续后继路线
  * 通过API发出一个指定的信号名，匹配并完成事件任务，继续后继路线

该事件到达后会在WFC_TASK创建一个类型为`catchEvent`、`EXT1`为`signal`、`EXT2`为信号变量名、`EXT3`为捕获规则的记录。完成处理后，状态标记为`complete`归档到历史表。

> 如果流程修改了信号变量名或匹配规则，只对该事件创建的新实例有效

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/21.png)

### 选项开关

**信号**

设置要订阅的信号，并允许通过`数据映射`对接收到的数据（`payload`）进行映射（当前流程变量或者BO存储对象）。

定义信号变量 | 将接收的信号数据初始化给当前流程  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/34.png) |  ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/35.png)  
  
> 要捕获信号，首先在该流程属性的`信号`中定义信号变量名，目前信号变量支持[BO Structure类数据结构](<../appendix/bo_structure.html>)

**关联规则**

一个可选的进阶匹配规则。当捕获的信号名相同时，如果规则不匹配则忽略该信号的处理。

例如，订阅到名为`CRM-Order`且匹配规则值为`vip`的信号，匹配并完成该类事件任务。

### API使用场景

捕获信号事件（Signal Intermediate Catch Event）由引擎自动触发，不需要API。

### 延伸阅读

  * [BO结构对象](<../appendix/bo_structure.html>)
  * [信号数据处理](<../appendix/signal_data.html>)
  * [订阅抛出信号事件（Signal Intermediate Throwing Event）发出的信号](<../intermediateevents/signal_intermediate_throwing_event.html>)
  * [订阅信号结束事件（Signal End Event）发出的信号](<../endevents/signal_end_event.html>)