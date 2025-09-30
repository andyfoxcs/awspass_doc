# TASK_AFTER_COMPLETE | AWS 流程事件开发参考指南

## TASK_AFTER_COMPLETE

### 任务完成（结束）后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断   
-其中抛出BPMNError异常时，该节点定义的错误边界事件将被捕获，  
若未捕获且该流程为子流程，可被父流程CallActivity定义的  
边界错误事件捕获。如未定义，业务错误信息包装成结果返回  
  
### 常见触发场景

**1.执行任务并向后推进时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/activity_event/3.png)

**2.使用SDK API时**
    
    
    //完成任务并向下推进时
    SDK.getTaskAPI().completeTask(taskInst, UserContext.fromUID(optUser), true);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.usertask;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListenerInterface;
    
    public class Test_TASK_AFTER_COMPLETE extends ExecuteListener implements ExecuteListenerInterface {
    
        public void execute(ProcessExecutionContext ctx) throws Exception {
            info("任务结束后可以补偿被触发-->" + ctx.getTaskInstance());
            // throw new BPMNError("UCode02", "User biz error");
        }
    
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用