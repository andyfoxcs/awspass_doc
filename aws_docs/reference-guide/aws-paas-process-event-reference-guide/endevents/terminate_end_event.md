# 终止事件 | AWS BPMN2 Event参考指南

# 终止事件（Terminate End Event）

表示流程被强制终止，什么都不做。当流程有多个分支路线被激活时，这些分支上的活动任务也被终止。

终止操作将流程实例和任务实例的状态标记为`terminate`值。
    
    
    //流程终止后的状态常量
    ProcessRuntimeConst.INST_STATE_TERMINATE
    
    //任务终止后的状态常量
    TaskRuntimeConst.INST_STATE_TERMINATE
    

### 图形符号

混合结束示意  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/21.png)  
  
### 选项开关

  * 无

### API使用场景

对于静态的流程结构，终止事件（TerminateEndEvent）不需要特定的API创建或结束，该类事件等待前置连线被激活（如前置连线的任务完成、网关决策通过），自动触发。

也可以使用API对运行中的流程执行终止操作，作用与终止事件相同。
    
    
    //终止一个流程实例
    SDK.getProcessAPI().terminate(processInst,userContext);
    SDK.getProcessAPI().terminateById(processInstId,uid);
    SDK.getProcessAPI().terminateByBusinessKey(processBusinessKey,uid);
    

### 客户端使用场景

  * 当流程终止时，提示`流程结束`

执行终止事件，人工任务2被强行终止  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/22.png)