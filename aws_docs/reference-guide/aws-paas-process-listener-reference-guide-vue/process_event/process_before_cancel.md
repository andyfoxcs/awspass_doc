# PROCESS_BEFORE_CANCEL | AWS 流程事件开发参考指南

## PROCESS_BEFORE_CANCEL

### 流程取消前被触发

项 | 说明  
---|---  
抽象类 | InterruptListener  
接口 | InterruptListenerInterface  
返回值 | 返回false，流程取消被阻止，该分支被孤立中断  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断   
-其中抛出BPMNError异常时，若该流程为子流程可被父流程CallActivity定义的  
边界错误事件捕获。如未定义，业务错误信息包装成结果返回  
  
### 常见触发场景

**1.使用流程运维管理时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/10.png)

**2.使用SDK API时**
    
    
    //创建流程实例
    ProcessInstance processInst = SDK.getProcessAPI().createProcessInstance(processDefId, processBusinessKey,uid,createUserDeptId,createUserRoleId,title,vars);
    //从默认的开始事件启动流程
    List<TaskInstance> tasks = SDK.getProcessAPI().start(processInst, null).fetchActiveTasks();
    
    //取消一个流程实例时
    SDK.getProcessAPI().cancel(processInst,UserContext.fromUID(cancelUser));
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListener;
    import com.actionsoft.bpms.util.UtilString;
    
    public class Test_PROCESS_BEFORE_CANCEL extends InterruptListener {
    
        public String getDescription() {
            return "测试用例";
        }
    
        public boolean execute(ProcessExecutionContext ctx) throws Exception {
            info("流程取消前事件被触发-->" + ctx.getProcessInstance());
            String str1 = (String) ctx.getVariable("str1");
            if (UtilString.isEmpty(str1) || !str1.equals("cancel yes")) {
                info("流程取消前事件-->测试str1必须为cancel yes值才可以取消");
                return false;
            } else {
                info("流程取消前事件-->str1=" + str1);
            }
            return true;
        }
    
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用