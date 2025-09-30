# PROCESS_BEFORE_RESTART | AWS 流程事件开发参考指南

## PROCESS_BEFORE_RESTART

### 流程重置前被触发

项 | 说明  
---|---  
抽象类 | InterruptListener  
接口 | InterruptListenerInterface  
返回值 | 返回false，流程重置被阻止  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
### 常见触发场景

**1.使用流程运维管理时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/process_event/restart.png)

**2.在发起列表撤销任务时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/process_event/restart1.png)

**2.使用SDK API时**
    
    
    //重置流程实例
     SDK.getProcessAPI().restart( processInst,  restartReason);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListener;
    import com.actionsoft.bpms.util.UtilString;
    
    public class Test_PROCESS_BEFORE_DELETED extends InterruptListener {
    
        public String getDescription() {
            return "测试用例";
        }
    
        public boolean execute(ProcessExecutionContext ctx) throws Exception {
            info("流程重置前事件被触发-->" + ctx.getProcessInstance());
            return true;
        }
    
    }
    

> 该事件仅在6.3.GA及后续版本提供