# PROCESS_AFTER_REACTIVATE | AWS 流程事件开发参考指南

## PROCESS_AFTER_REACTIVATE

### 流程复活后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
### 常见触发场景

**1.使用流程运维管理时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/12.png)

**2.使用SDK API时**
    
    
    //复活一个已结束的流程实例时
    SDK.getProcessAPI().reactivate(processInst,targetActivityId,isClearHistory,optUser,targetUser,"原因是要求重新执行");
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    
    public class Test_PROCESS_AFTER_REACTIVATE extends ExecuteListener {
    
        public String getDescription() {
            return "测试用例";
        }
    
        public void execute(ProcessExecutionContext ctx) throws Exception {
            info("流程激活后事件被触发-->" + ctx.getProcessInstance());
        }
    
    }