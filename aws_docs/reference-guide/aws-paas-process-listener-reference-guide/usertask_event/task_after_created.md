# TASK_AFTER_CREATED | AWS 流程事件开发参考指南

## TASK_AFTER_CREATED

### 任务创建后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回  
  
### 常见触发场景

**1.任务创建后**

**2.使用SDK API时**
    
    
    // 创建任务
    SDK.getTaskAPI().createUserTaskInstance(processInst, parentTaskInstModel, userContext,targetActivityDefId,participant,title);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.usertask;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListenerInterface;
    
    public class Test_TASK_AFTER_CREATED extends ExecuteListener implements ExecuteListenerInterface {
    
        public void execute(ProcessExecutionContext ctx) throws Exception {
            info("任务创建后可以补偿被触发-->" + ctx.getTaskInstance());
            // throw new BPMNError("UCode02", "User biz error");
        }
    
    }
    

> 该事件仅在6.3.GA及后续版本提供