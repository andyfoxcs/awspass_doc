# PROCESS_AFTER_CREATE | AWS 流程事件开发参考指南

## PROCESS_AFTER_CREATE

### 流程创建后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
-其中抛出BPMNError异常时，若该流程为子流程可被父流程CallActivity定义的  
边界错误事件捕获。如未定义，业务错误信息包装成结果返回  
  
### 常见触发场景

**1.新建流程实例时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/5.png)

**2.使用SDK API时**
    
    
    //创建流程实例
    ProcessInstance processInst = SDK.getProcessAPI().createProcessInstance(processDefId, processBusinessKey,uid,createUserDeptId,createUserRoleId,title,vars);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    
    public class Test_PROCESS_AFTER_CREATED extends ExecuteListener {
    
        public String getDescription() {
            return "测试用例";
        }
    
        public void execute(ProcessExecutionContext ctx) throws Exception {
            info("流程创建后事件被触发-->" + ctx.getProcessInstance());
        }
    
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用