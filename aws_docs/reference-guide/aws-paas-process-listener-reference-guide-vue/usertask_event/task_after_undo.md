# TASK_AFTER_UNDO | AWS 流程事件开发参考指南

## TASK_AFTER_UNDO

### 任务收回后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回  
  
### 常见触发场景

**1.已办的下个任务被收回后**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/usertask_event/4.png)

**2.使用SDK API时**
    
    
    //收回任务
    SDK.getTaskAPI().undoTask(taskInstId, uid, undoReason);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.usertask;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListenerInterface;
    
    public class Test_TASK_AFTER_UNDO extends ExecuteListener implements ExecuteListenerInterface {
    
        public void execute(ProcessExecutionContext ctx) throws Exception {
            info("任务收回后可以补偿被触发-->" + ctx.getTaskInstance());
            // throw new BPMNError("UCode02", "User biz error");
        }
    
    }
    

> 此时，ctx.getTaskInstance()获得的任务对象是新的任务实例对象