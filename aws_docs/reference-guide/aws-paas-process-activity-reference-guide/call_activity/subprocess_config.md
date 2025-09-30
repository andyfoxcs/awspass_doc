# 配置子流程 | AWS BPMN2 Activity参考指南

# 配置子流程

激活`调用子流程`节点时，引擎会首先在`WFC_TASK`创建一个类型为`callActivity`的任务实例，基于设计阶段配置好的子流程策略，自动完成子流程的创建、启动和调度。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/callactivity.png)

  * 选择子流程
  * 子流程版本管理
  * 实例控制选项
  * 处理子流程的业务异常
  * 挂起和恢复子流程
  * 用API动态控制子流程实例

### 选择子流程

一个`调用子流程（Call Activity）`节点只允许配置一个子流程，该子流程可以是当前AWS PaaS平台任何有效的流程模型。

如果要引用当前应用和父应用之外的流程模型，需设置当前应用与对方应用的关联依赖。

##### 子流程管理

提供可引用的流程列表 _(该列表不显示`流程属性 > 流程级别` 为`顶级流程`的流程)_，由建模人员确定要使用的流程。当流程有多版本时，流程引擎将自动根据[规则](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/appendix/process_model_version.html>)，智能选择流程版本。

> 6.2.GA(不含)版本以前版本
> 
>   1. 提供可供引用的流程及版本列表，由建模人员确定要使用的版本。当子流程模型版本号发生变化后，应根据实际业务场景更改父流程启动子流程的对应版本。
>   2. 如果已引用的子流程模型处于`停用`状态，在激活`调用子流程`节点时，引擎会抛出`错误的参数请求(400)，子流程已经停用，请检查配置`
> 

### 实例控制选项

##### 确定子流程的启动者

将启动者账户映射到`子流程启动者`选项。这是一个必选配置，通常可以通过@公式动态指定启动者。

**可以使用如下格式指定多个账户**

  * 多账户间空格隔开
  * 多账户间逗号隔开
  * 多账户间分号隔开
  * 一个JSON数组

>   1. 如果启动的子流程是一个无需人工干预的系统短流程，可以`admin`账户替代
>   2. 当实例控制项用于映射子流程实例数据时，这时子流程实例启动者可通过`流程启动者`属性控制，只允许填写一个账户，子流程实例第一节点任务参与者可通过子流程节点路由方案确定
> 

##### 确定子流程标题

配置`子流程标题`属性后，优先级高于子流程模型默认标题。

##### 多例时的处理方式

当指定多个启动者账户时，每个账户会对应启动一个子流程实例（允许账户重复，如两个`tom`,`tom`账户也会启动2次子流程）。

  * **并行** ，同时启动多个子流程实例。所有子流程都结束后，父流程的`调用子流程（Call Activity）`任务结束，自动激活后继路线的流程对象
  * **串行** ，按给定账户的顺序依次启动子流程实例。上一个子流程结束后，自动创建下一个子流程实例，最后一个子流程实例结束后，自动激活后继路线的流程对象

### 处理子流程的业务异常

父流程可以捕捉子流程的错误结束事件，对异常进行处理。

父流程使用边界错误事件捕获错误 | 子流程使用错误结束事件抛出错误  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/2.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/1.png)  
  
### 挂起和恢复子流程

  * 如果`挂起`某个主流程实例，其相关的子流程实例也被挂起
  * 如果`挂起`某一个子流程实例，其他子流程实例和主流程实例不受影响
  * `恢复`操作亦是如此

下图示意一个主流程挂起后，相关的2个子流程实例也被挂起

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/3.png)

### 用API动态控制子流程实例

可以对一个正在运行的`调用子流程（Call Activity）`任务动态增加子流程实例。
    
    
    ProcessInstance subProcessInst = SDK.getProcessAPI().createSubProcessInstance("启动人账户",
    "标题", "调用子流程（Call Activity）节点的任务实例ID", null);
    //启动流程
    SDK.getProcessAPI().start(subProcessInst);
    

开发者也可以调用ProcessAPI对在执行的子流程进行终止操作。

## 延伸阅读

  * [边界错误事件（Error Boundary Interrputing Event）](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/error_boundary_interrputing_event.html>)
  * [错误结束事件（Error End Event）](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/error_end_event.html>)
  * [SDK ProcessAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/ProcessAPI.html>)
  * [SDK TaskAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/TaskAPI.html>)