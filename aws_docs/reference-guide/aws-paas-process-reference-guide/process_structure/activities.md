# 活动（Activities） | AWS BPMN2 Process参考指南

# 活动（Activities）

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activity.png)

活动（Activities）是业务流程定义的核心元素，中文可称为“活动”、“节点”、“步骤”。一个活动可以是流程中一个基本处理单元（如人工任务、服务任务），也可以是一个组合单元（如外部子流程、嵌套子流程）。

### 清单

BPMN2 | 名称 | 说明  
---|---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/1.png) | [User Task  
人工任务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/README.html>) | 人工任务是一个典型的“工作流”处理，需要人的参与  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/2.png) | [Service Task  
系统任务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/README.html>) | 一个Java Service，可以执行AWS内部或外部服务。  
开发人员可以将外部SOAP/REST或任意的处理逻辑  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/3.png) | [Script Task  
脚本任务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/README.html>) | 脚本任务能够执行指定的程序脚本。当前支持的语言  
包括：JavaScript、BeanShell、Groovy  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/8.png) | [Call SubProcess Activity  
调用子流程](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/README.html>) | 调用外部流程，该流程实例全部结束后，任务执行完成  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/7.png) | [Manual Task  
手工任务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/manual_task/README.html>) | 手工任务主要用于完善流程结构描述，不被引擎执行