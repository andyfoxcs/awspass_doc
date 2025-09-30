# 活动（Activities） | AWS BPMN2 Activity参考指南

# 活动（Activities）

活动（Activities）是业务流程定义的核心元素，中文称为“活动”、“节点”、“步骤”。一个活动可以是流程的基本处理单元（如人工任务、服务任务），也可以是一个组合单元（如外部子流程、嵌套子流程）。

### 使用

从面板拖放一个活动 | 创建连线时选择一个活动  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/10.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/11.png)  
改变活动类型 | 复制活动  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/12.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/13.png)  
  
**如何快速修改活动的名称？**

  * 鼠标选中活动
  * 按空格键，输入或编辑名称

### 清单

BPMN2 | 名称 | 说明  
---|---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/1.png) | [User Task  
人工任务](<../user_task/README.html>) | 人工任务是一个典型的“工作流”处理，需要人的参与  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/2.png) | [Service Task  
系统任务](<../service_task/README.html>) | 一个Java Service，可以执行AWS内部或外部服务。  
开发人员可以将外部接口或任意的处理逻辑封装成CC的`流程服务`，实现复用  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/3.png) | [Script Task  
脚本任务](<../script_task/README.html>) | 脚本任务能够执行指定的程序脚本。当前支持的语言  
包括：JavaScript、BeanShell、Groovy  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/8.png) | [Call SubProcess Activity  
调用子流程](<../call_activity/README.html>) | 调用外部流程，该流程实例全部结束后，任务执行完成  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/7.png) | [Manual Task  
手工任务](<../manual_task/README.html>) | 手工任务主要用于完善流程结构描述，不被引擎执行  
  
### 专业分级

AWS PaaS为降低BPMN建模的复杂度，提供了三个级别的能力配置，其中level0（默认）适合普通企业建模用户。

  * level0 核心
  * level1 专业
  * level2 实验室

> 这是一个BPMN引擎的高级配置项，如调高级别，需专业人员提供协助

**ENGINE_BPMN_LEVEL_0** [startEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/none_start_event.html>),[userTask](<../user_task/README.html>),[serviceTask](<../service_task/README.html>),[callActivityCallingProcess](<../call_activity/README.html>),[exclusiveGateway](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/exclusive_gateway/README.html>),[inclusiveGateway](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/inclusive_gateway/README.html>),[parallelGateway](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/parallel_gateway/README.html>),[endEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/end_event.html>),[terminateEndEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/terminate_end_event.html>),[group](<https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_structure/other.html>),[textAnnotation](<https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_structure/other.html>),[verticalPool](<https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_structure/other.html>),[verticalLane](<https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_structure/other.html>),[horizontalPool](<https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_structure/other.html>),[horizontalLane](<https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_structure/other.html>)

**ENGINE_BPMN_LEVEL_1** [timerStartEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/timer_start_event.html>),[signalStartEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/signal_start_event.html>),[messageStartEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/message_start_event.html>),[manualTask](<../manual_task/README.html>),[scriptTask](<../script_task/README.html>),[complexGateway](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/complex_gateway/README.html>),[eventBasedGateway](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/event-based_gateway/README.html>),[timerIntermediateCatchEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/timer_intermediate_catch_event.html>),[messageIntermediateCatchEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/message_intermediate_catch_event.html>),[signalIntermediateCatchEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/signal_intermediate_catch_event.html>),[messageIntermediateThrowingEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/message_intermediate_throwing_event.html>),[signalIntermediateThrowingEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/signal_intermediate_throwing_event.html>),[compensateIntermediateThrowingEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/compensate_intermediate_throwing_event.html>),[messageBoundaryInterrputingEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/message_boundary_interrputing_event.html>),[timerBoundaryInterrputingEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/timer_boundary_interrputing_event.html>),[signalBoundaryInterrputingEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/signal_boundary_interrputing_event.html>),[compensateBoundaryInterrputingEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/compensate_boundary_interrputing_event.html>),[errorBoundaryInterrputingEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/error_boundary_interrputing_event.html>),[messageEndEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/message_end_event.html>),[signalEndEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/signal_end_event.html>),[errorEndEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/error_end_event.html>),[compensateEndEvent](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/compensate_end_event.html>)