# PROCESS_AFTER_RESTART | AWS 流程事件开发参考指南

## PROCESS_AFTER_RESTART

### 流程重置后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
### 常见触发场景

**1.使用流程运维管理时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/restart.png)

**2.在发起列表撤销任务时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/restart1.png)

**3.使用SDK API时**
    
    
    //重置流程实例
     SDK.getProcessAPI().restart( processInst,  restartReason);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    
    public class Test_PROCESS_AFTER_CANCEL extends ExecuteListener {
    
        public String getDescription() {
            return "测试用例";
        }
    
        public void execute(ProcessExecutionContext ctx) throws Exception {
            info("流程重置后事件被触发-->" + ctx.getProcessInstance());
        }
    
    }
    

> 该事件仅在6.3.GA及后续版本提供