# 信号开始事件（Signal Start Event）

当接收到特定的信号后`信号开始事件`被触发，启动一个流程实例。如果多个流程含有相同信号名称的`信号开始事件`，那么它们可能被同时启动。

- 订阅流程中[抛出信号事件（Signal Intermediate Throwing Event）](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/signal_intermediate_throwing_event.html)、[信号结束事件（Signal End Event）](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/signal_end_event.html)发出的信号，匹配并启动流程
- 通过API抛出一个信号，匹配并启动流程
- 作为[普通开始](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/none_start_event.html)事件，启动流程

### 图形符号

| 单开始                                                       | 多开始                                                       |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/31.png) | ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/32.png) |

### 选项开关

**信号**

设置要订阅的信号，可进阶通过`数据映射`对接收到的数据（`payload`）进行映射（当前流程变量或者BO存储对象）。

| 定义信号变量                                                 | 将接收的信号数据初始化给当前流程                             |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/34.png) | ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/35.png) |

> 要捕获信号，首先在该流程属性的`信号`中定义信号变量名，目前信号变量支持[BO Structure类数据结构](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/appendix/bo_structure.html)。如下图

![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/33.png)

**关联规则**

一个可选的进阶匹配规则。当捕获的信号名相同时，如果规则不匹配则忽略该信号的处理。

例如，当捕获到信号名为`B2B-Order`时，忽略不是`vip`的信号处理。

### API使用场景

也可以使用以下代码直接向信号开始事件发送信号

```java
//传播一个名为B2B-Order的信号，当匹配捕获规则为vip时自动启动流程
SDK.getProcessAPI().signalStartEventReceived("B2B-Order", "vip", null);

//初始化指定BO Structure的OrderNo数据项
Map<String, Object> payload = new HashMap<>();
payload.put("OrderNo", "008");
SDK.getProcessAPI().signalStartEventReceived("B2B-Order", "vip", payload);
```

### 延伸阅读

- [BO结构对象](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/appendix/bo_structure.html)
- [信号数据处理](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/appendix/signal_data.html)
- [订阅抛出信号事件（Signal Intermediate Throwing Event）发出的信号](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/signal_intermediate_throwing_event.html)
- [订阅信号结束事件（Signal End Event）发出的信号](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/signal_end_event.html)
- [封装和发布自己的HTTP API接收外部信息](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_http_api.html)
- [封装和发布自己的SOAP API接收外部信息](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_soap_api.html)
- [启动流程对版本的选择](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/appendix/process_model_version.html)