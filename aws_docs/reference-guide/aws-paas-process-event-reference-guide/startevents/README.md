# 开始事件（Start Events） | AWS BPMN2 Event参考指南

# 开始事件（Start Events）

开始事件用来指明流程从哪里开始。开始事件启动一个流程的新实例，它只有一个唯一的无条件输出[顺序流](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/sequence_flow/README.html>)，没有输入连线。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/10.png)

当它被触发后，BPM引擎会产生一个Token并顺着它的输出连线实例化后继路线上的流程对象（例如[网关](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/index.html>)、[节点](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/index.html>)、[中间事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/README.html>)、[结束事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/README.html>)）。AWS支持的开始事件类型包括：

  * [开始事件](<none_start_event.html>)
  * [时间开始事件](<timer_start_event.html>)
  * [信号开始事件](<signal_start_event.html>)
  * [消息开始事件](<message_start_event.html>)

开始事件将流程实例的状态标记为`active`值。
    
    
    //流程开始后的状态常量
    ProcessRuntimeConst.INST_STATE_ACTIVE