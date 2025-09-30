# PROCESS_BEFORE_CREATE | AWS 流程事件开发参考指南

## PROCESS_BEFORE_CREATE

### 流程创建前被触发

项 | 说明  
---|---  
抽象类 | InterruptListener  
接口 | InterruptListenerInterface  
返回值 | 返回false，流程创建被阻止  
异常 | -如抛出异常时，异常被包装成结果返回，流程创建失败  
-其中抛出BPMNError异常时，若该流程为子流程可被父流程CallActivity定义的  
边界错误事件捕获。如未定义，业务错误信息包装成结果返回  
  
### 常见触发场景

**1.新建流程实例时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/process_event/5.png)

**2.使用SDK API时**
    
    
    //创建流程实例
    ProcessInstance processInst = SDK.getProcessAPI().createProcessInstance(processDefId, processBusinessKey,uid,createUserDeptId,createUserRoleId,title,vars);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListener;
    import com.actionsoft.exception.BPMNError;
    
    public class Test_PROCESS_BEFORE_CREATED extends InterruptListener {
    
        public String getDescription() {
            return "测试用例";
        }
    
        public boolean execute(ProcessExecutionContext ctx) throws Exception {
            info("流程创建前事件被触发");
            String str1 = ctx.getParameterOfString("str1");// 从临时变量中获得，在创建前尚未保存流程变量值
            if (str1 == null || str1.equals("begin")) {
                // 模拟抛出业务异常
                throw new BPMNError("BIZ001", "PROCESS_BEFORE_CREATED事件模拟抛出业务异常");
            } else {
                return true;
            }
        }
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用