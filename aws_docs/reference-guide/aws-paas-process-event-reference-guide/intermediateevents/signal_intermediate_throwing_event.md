# 抛出信号事件 | AWS BPMN2 Event参考指南

# 抛出信号事件（Signal Intermediate Throwing Event）

当执行到达`抛出信号事件`时，引擎向系统内部发出一个信号，信号发出后事件结束，流程沿后继路线继续执行。

该事件到达后会在WFC_TASK创建一个类型为`throwEvent`、`EXT1`为`signal`的记录。被正常触发后，状态标记为`complete`归档到历史表。

> 同一个信号可以有多个subscriber（订阅者）

抛出的信号可以被[信号开始事件（Signal Start Event）](<../startevents/signal_start_event.html>)、[中间捕获信号事件（Signal Intermediate Catch Event）](<../intermediateevents/signal_intermediate_catch_event.html>)、[边界信号事件（Signal Boundary Interrputing Event）](<../boundaryevents/signal_boundary_interrputing_event.html>)订阅处理。

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/41.png)

### 选项开关

**信号**

设置要抛出的信号，并确保信号变量名与订阅信号的事件名一致。作为进阶设置，可以通过`数据映射`对抛出的业务数据（`payload`）进行值映射。

定义信号变量 | 将抛出的信号数据初始化给当前流程  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/34.png) |  ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/35.png)  
  
> 要抛出信号，首先在该流程属性的`信号`中定义信号变量名，目前信号变量支持[BO Structure类数据结构](<../appendix/bo_structure.html>)

**关联规则**

一个可选的进阶匹配规则。当抛出的信号名相同时，如果规则不匹配则忽略该信号的处理。

例如，订阅到名为`CRM-Order`且匹配规则值为`vip`的信号，匹配并完成该类事件任务。

### API使用场景

也可以使用以下代码直接向订阅事件发送信号
    
    
    //传播一个名为CRM-Order的信号，当匹配捕获规则为vip时完成该中断的任务，并继续向下执行
    SDK.getTaskAPI().signalEventReceived("CRM-Order", "vip", null);
    
    //初始化指定BO Structure的OrderNo数据项
    Map<String, Object> payload = new HashMap<>();
    payload.put("OrderNo", "009");
    SDK.getTaskAPI().signalEventReceived("CRM-Order", "vip", payload);
    

### 延伸阅读

  * [BO结构对象](<../appendix/bo_structure.html>)
  * [信号数据处理](<../appendix/signal_data.html>)
  * [让信号开始事件（Signal Start Event）接收信号](<../startevents/signal_start_event.html>)
  * [让捕获信号事件（Signal Intermediate Catch Event）接收信号](<../intermediateevents/signal_intermediate_catch_event.html>)
  * [让边界信号事件（Signal Boundary Interrputing Event）接收信号](<../boundaryevents/signal_boundary_interrputing_event.html>)
  * [封装和发布自己的HTTP API接收外部信息](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_http_api.html>)
  * [封装和发布自己的SOAP API接收外部信息](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_soap_api.html>)