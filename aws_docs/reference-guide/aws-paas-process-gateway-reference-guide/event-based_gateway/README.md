# 事件网关（Event-Based Gateway） | AWS BPMN2 Gateway参考指南

## 事件网关（Event-Based Gateway）

通常网关根据连线条件来决定后继路径，这就要求条件信息必须存在于流程自身之中。但是，当需要选择的后继路径的条件不能来自该流程时，就可以使用事件网关。事件网关只有分支行为，允许从多个候选分支中选择事件最先到达的分支（如时间事件、消息事件），并取消其他分支。

当候选分支的某个事件到达时，若取消其他分支的事件任务（标记为Cancel）发生异常或事件自身的处理发生异常，该事件的任务实例将被处理成错误（标记为Error），路径将中断于此。可以在AWS控制台的“运行”模块检查和管理这些出错任务。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/event-based_gateway/1.png)

事件网关之后的连线（Sequence Flow）目标必须是一个“中间捕获事件”，事件网关支持以下类型的“中间捕获事件”，而关于如何使用这些捕获类事件请参见相关文档。

BPMN2 | 名称 | 说明  
---|---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/event-based_gateway/2.png) | Timer Intermediate Event  
捕获时间事件 | 时间到达时该分支被选择，其他分支取消  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/event-based_gateway/3.png) | Catch Signal Intermediate Event  
捕获信号事件 | 接收到信号时该分支被选择，其他分支取消  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/event-based_gateway/4.png) | Catch Message Intermediate Event  
捕获消息事件 | 接收到消息时该分支被选择，其他分支取消