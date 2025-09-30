# 异常处理 | AWS BPMN2 Activity参考指南

# 异常处理

程序在任何时候都可能抛出异常。AWS流程引擎可以处理两类异常：

  * [BPMNError](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/exception/BPMNError.html>)业务异常
  * 系统异常

使用[边界错误事件（Error Boundary Interrputing Event）](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/error_boundary_interrputing_event.html>)对异常进行建模，可以捕获[BPMNError](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/exception/BPMNError.html>)业务异常。当业务异常代码未被匹配时：如果当前有人工交互界面，那么将信息组织成对话框输出，如果是服务器端自动处理，信息被记录日志。

BPMNError业务异常对话框 | 系统异常对话框  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/alert1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/alert2.png)  
使用边界错误事件（Error Boundary Interrputing Event）对异常进行建模  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/catch-errorcode.png)  
  
## 异常策略

任务发生异常后流程被中断在这里，任务实例在`WFC_TASK`表中的`CONTROLSTATE`字段更新为`error`状态。此类场景可以在建模时选择如下策略：

  1. 等待人工干预
  2. 忽略
  3. 单步退回
  4. 回退到上个人工任务
  5. 按路径退回

> 如果抛出开发者的`BPMNError`业务异常且使用[边界错误事件（Error Boundary Interrputing Event）](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/error_boundary_interrputing_event.html>)对异常进行建模，引擎优先对边界错误事件设定的错误码进行匹配，匹配成功则激活`边界错误`的后继路线，以上异常策略不再执行。

### 1.等待人工干预

这是默认的一种策略。发生异常时，流程中断在这里。运维人员可以在`控制台>实例运行管理`对发生错误的任务进行跟踪和处理。

  * **跟踪** ，查看流程图和执行轨迹
  * **重试** ，尝试手工执行一次服务，如果成功则激活后继路线继续执行
  * **忽略** ，取消该任务（Cancel），激活后继路线继续执行

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/1.png)

### 2.忽略

发生异常时，当前任务实例被自动终止(Terminate)，激活后继路线继续执行。

被终止的任务已成为历史，可以在`控制台>实例运行管理`中跟踪： ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/2.png)

### 3.单步退回

发生异常时，当前任务实例被取消执行(Cancel)，重新激活上个任务实例（从哪里来回哪里去）。

> 注意：如果回退的目标节点是一个系统类自动化节点，要防止再次执行时抛出异常进而进入死循环，除非建模人员已知晓异常会被解除。采用`4.回退到上个人工任务`可规避。

被取消的任务已成为历史，可以在`控制台>实例运行管理`中跟踪： ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/3.png)

如果回退的目标节点使用[边界补偿事件（Compensate Boundary Interrputing Event）](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/compensate_boundary_interrputing_event.html>)对业务进行了补偿建模，引擎会激活`边界补偿事件`的后继路线。

> 当补偿操作完成后，回退的目标节点任务才被创建执行

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/4.png)

发生异常的任务被取消，补偿的任务被执行，可以在`控制台>实例运行管理`中跟踪： ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/5.png)

### 4.回退到上个人工任务

与`3.单步退回`相似。发生异常时，当前任务实例被取消执行(Cancel)，重新激活到上个任务实例是人工任务的节点。

### 5.按路径退回

发生异常时，当前任务实例被取消执行(Cancel)，回退到指定的节点。从指定节点到发生异常节点间的历史节点（自动计算，可能有多个节点），如果这些节点有使用[边界补偿事件（Compensate Boundary Interrputing Event）](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/compensate_boundary_interrputing_event.html>)对业务进行了补偿建模，引擎会激活`边界补偿事件`的后继路线。

> 当补偿操作完成后，回退的目标节点任务才被创建执行

### 延伸阅读

  * [边界补偿事件（Compensate Boundary Interrputing Event）](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/compensate_boundary_interrputing_event.html>)
  * [抛出补偿事件（Compensate Intermediate Throwing Event）](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/compensate_intermediate_throwing_event.html>)
  * [在事件Java代码中如何输出业务对话](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/appendix/message.html>)
  * [AWS MVC的异常处理框架](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/README.html>)