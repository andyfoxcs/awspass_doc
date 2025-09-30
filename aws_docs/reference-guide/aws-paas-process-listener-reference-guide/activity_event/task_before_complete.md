# TASK_BEFORE_COMPLETE | AWS 流程事件开发参考指南

## TASK_BEFORE_COMPLETE

### 任务完成（结束）前被触发

项 | 说明  
---|---  
抽象类 | InterruptListener  
接口 | InterruptListenerInterface  
返回值 | 返回false，任务完成被阻止  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断   
-其中抛出BPMNError异常时，该节点定义的错误边界事件将被捕获，  
若未捕获且该流程为子流程，可被父流程CallActivity定义的  
边界错误事件捕获。如未定义，业务错误信息包装成结果返回  
  
### 常见触发场景

**1.执行任务并向后推进时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/activity_event/3.png)

**2.使用SDK API时**
    
    
    //完成任务并向下推进时
    SDK.getTaskAPI().completeTask(taskInst, UserContext.fromUID(optUser), true);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.usertask;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListener;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListenerInterface;
    
    public class Test_TASK_BEFORE_COMPLETE extends InterruptListener implements InterruptListenerInterface {
    
        public boolean execute(ProcessExecutionContext ctx) throws Exception {
            info("任务结束前可以阻止被触发-->" + ctx.getTaskInstance());
            // throw new BPMNError("UCode01", "User biz error");
            return true;
        }
    
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用