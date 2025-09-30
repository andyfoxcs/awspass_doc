# PROCESS_SUSPEND | AWS 流程事件开发参考指南

## PROCESS_SUSPEND

### 流程挂起后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
### 常见触发场景

**1.使用流程运维管理时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/process_event/6.png)

**2.使用SDK API时**
    
    
    //创建流程实例
    ProcessInstance processInst = SDK.getProcessAPI().createProcessInstance(processDefId, processBusinessKey,uid,createUserDeptId,createUserRoleId,title,vars);
    //从默认的开始事件启动流程
    List<TaskInstance> tasks = SDK.getProcessAPI().start(processInst, null).fetchActiveTasks();
    //挂起流程实例
    SDK.getProcessAPI().suspend(processInst);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    
    public class Test_PROCESS_SUSPEND extends ExecuteListener {
    
        public String getDescription() {
            return "测试用例";
        }
    
        public void execute(ProcessExecutionContext ctx) throws Exception {
            info("流程挂起后事件被触发-->" + ctx.getProcessInstance());
        }
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用