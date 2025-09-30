# 应用场景 · AWS PaaS文档中心

## 应用场景

全局事件监听器能够时时捕获BPMS引擎中人工任务的处理动作，当产生任务或任务发生状态变化时事件被触发。

  * 任务到达提醒（如IM工具、移动设备）
  * 为企业已建的员工统一工作台服务提供AWS任务的推送

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/process-1.png)](<process-1.png>)

**以下事件发生时，被全局事件监听器监听**

事件名称 | 说明  
---|---  
PROCESS_CREATE | 流程实例创建后  
PROCESS_UPDATE | 流程实例标题更新后触发  
PROCESS_COMPLETE | 流程实例完成后（包括终止，取消）  
PROCESS_BEFORE_RESTART | 流程实例重置前  
PROCESS_RESTART | 流程实例重置后  
PROCESS_BEFORE_DELETE | 流程实例删除前，事件只是一个补偿，不会阻止流程实例的删除  
PROCESS_DELETE | 流程实例删除后  
\-- | \--  
TASK_CREATE | 任务创建后，新任务到达  
TASK_UPDATE | 任务标题更新后触发  
TASK_READ | 任务阅读后，未读被标记已读  
TASK_COMPLETE | 任务执行完，转成历史任务（已办）  
TASK_DELETE | 任务删除后，转成历史任务（已删除）  
TASK_SUSPEND | 任务挂起后，仅任务状态发生改变  
TASK_RESUME | 任务恢复后，仅任务状态发生改变  
TASK_TRANSFER | 任务移交时触发，如由A交接给B时  
TASK_DELEGATE | 任务转办  
TASK_TERMINATE | 任务终止  
  
> 注意：流程任务批量转移APP 中批量移交任务不会被全局事件监听器监听