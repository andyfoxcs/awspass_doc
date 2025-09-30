# 消息开始事件 | AWS BPMN2 Event参考指南

# 消息开始事件（Message Start Event）

当接受到特定的消息后`消息开始事件`被触发，启动一个流程实例。与[信号开始事件](<signal_start_event.html>)不同，每个消息只允许有一个订阅者（subscriber）。

> `Message Start Event`是一种模式基础，如果处理外部系统消息（如JMS、HTTP、SOAP），则需要开发人员使用AWS CC结合API编程完成流程的启动和数据初始化。例如，当接收到一个JMS消息订阅时，在Java代码中调用SDK.getProcesAPI().startByMessage()完成流程的启动

  * 订阅流程中[抛出消息事件（Message Intermediate Throwing Event）](<../intermediateevents/message_intermediate_throwing_event.html>)、[消息结束事件（Message End Event）](<../endevents/message_end_event.html>)发出的`内部消息`，匹配并启动流程
  * 收到外部事件（如JMS、自行发布的HTTP/SOAP服务）后，通过API启动流程
  * 作为[普通开始](<none_start_event.html>)事件，启动流程

### 图形符号

单开始 | 多开始  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/41.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/42.png)  
  
### 选项开关

**消息**

设置要订阅的消息。要正确监听消息，首先在该流程属性的`消息`中定义消息变量名，并确保消息变量名的全局唯一性。

> 如果当前引擎中部署的流程文件存在多个`Message Start Event`且消息变量名重复，只允许其中一个作为有效订阅者。

例如，当捕获到`内部消息`名为`Alibaba-B2B-Order`时，自动启动X订单流程。

### API使用场景

也可以使用以下代码直接向消息开始事件发送内部消息
    
    
    //发送一个名为Alibaba-B2B-Order的内部消息，当匹配捕获规则时自动启动流程
    SDK.getProcessAPI().startByMessage("Alibaba-B2B-Order");
    
    //初始化数据
    Map<String, Object> payload = new HashMap<>();
    payload.put("OrderNo", "008");
    SDK.getProcessAPI().startByMessage("Alibaba-B2B-Order", null, payload);
    

### 延伸阅读

  * [消息数据处理](<../appendix/message_data.html>)
  * [订阅抛出消息事件（Message Intermediate Throwing Event）发出的消息](<../intermediateevents/message_intermediate_throwing_event.html>)
  * [订阅消息结束事件（Message End Event）发出的消息](<../endevents/message_end_event.html>)
  * [封装和发布自己的HTTP API接收外部信息](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_http_api.html>)
  * [封装和发布自己的SOAP API接收外部信息](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_soap_api.html>)
  * [启动流程对版本的选择](<../appendix/process_model_version.html>)