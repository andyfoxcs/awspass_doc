# TASK_BEFORE_UNDO | AWS 流程事件开发参考指南

## TASK_BEFORE_UNDO

### 任务收回前被触发

项 | 说明  
---|---  
抽象类 | InterruptListener  
接口 | InterruptListenerInterface  
返回值 | 返回false，任务收回被阻止  
异常 | -如抛出异常时，异常被包装成结果返回  
  
### 常见触发场景

**1.已办的下个任务被收回时,事件需要注册到被收回任务节点**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/usertask_event/4.png)

**2.使用SDK API时**
    
    
    //收回任务
    SDK.getTaskAPI().undoTask(taskInstId, uid, undoReason);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.usertask;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListener;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListenerInterface;
    
    public class Test_TASK_BEFORE_UNDO extends InterruptListener implements InterruptListenerInterface {
    
        public boolean execute(ProcessExecutionContext ctx) throws Exception {
            info("任务收回前可以阻止被触发-->" + ctx.getTaskInstance());
            // throw new BPMNError("UCode01", "User biz error");
            return true;
        }
    
    }
    

> 此时，ctx.getTaskInstance()获得的任务对象是要收回的任务实例对象