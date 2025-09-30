# 抛出消息事件 | AWS BPMN2 Event参考指南

# 抛出消息事件（Message Intermediate Throwing Event）

当执行到达`抛出消息事件`时，引擎向系统内部（又叫`内部消息`）发出一条消息或者调用外部系统接口（注册到AWS CC的服务），随即该事件结束，流程沿后继路线继续执行。

该事件到达后会在WFC_TASK创建一个类型为`throwEvent`、`EXT1`为`message`的记录。被正常触发后，状态标记为`complete`归档到历史表。

> 同一个消息只允许一个subscriber（订阅者）

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/51.png)

### 选项开关

**消息接口**

  * 内部消息
  * 外部接口

**1\. 内部消息**

发出一个内部消息。要正确抛出消息，首先在该流程属性的`消息`中定义消息变量名，并确保消息变量名与订阅消息的事件名、关联规则一致

**2\. 外部接口**

调用外部服务接口。要正确调用外部服务，首先在AWS CC中完成服务注册，并在`数据映射`中对该服务的调用参数进行值初始化。

> 目前AWS的`抛出消息事件`只支持Web Service类外部接口和简单参数格式，对于复杂参数格式的重要服务处理，建议使用[Service Task](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/README.html>)。

### API使用场景

也可以使用以下代码直接向订阅事件发送内部消息
    
    
    //发送一个名为Alibaba-B2B-Order的内部消息，匹配并完成订单编号为201702040007的中断任务
    SDK.getTaskAPI().messageEventReceived("Alibaba-B2B-Order", "201702040007");
    
    //初始化数据
    Map<String, Object> payload = new HashMap<>();
    payload.put("CustomerNo", "888");
    SDK.getTaskAPI().messageEventReceived("Alibaba-B2B-Order", "201702040007", payload);
    

### 延伸阅读

  * [消息数据处理](<../appendix/message_data.html>)
  * [让消息开始事件（Message Start Event）接收消息](<../startevents/message_start_event.html>)
  * [让捕获消息事件（Message Intermediate Catch Event）接收消息](<../intermediateevents/message_intermediate_catch_event.html>)
  * [让边界消息事件（Message Boundary Interrputing Event）接收消息](<../boundaryevents/message_boundary_interrputing_event.html>)
  * [封装和发布自己的HTTP API接收外部信息](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_http_api.html>)
  * [封装和发布自己的SOAP API接收外部信息](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_soap_api.html>)