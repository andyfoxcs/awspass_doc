# PROCESS_BEFORE_DELETE | AWS 流程事件开发参考指南

## PROCESS_BEFORE_DELETE

### 流程删除前被触发

项 | 说明  
---|---  
抽象类 | InterruptListener  
接口 | InterruptListenerInterface  
返回值 | 返回false，流程删除被阻止  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
### 常见触发场景

**1.使用流程运维管理时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/process_event/11.png)

**2.使用SDK API时**
    
    
    //创建流程实例
    ProcessInstance processInst = SDK.getProcessAPI().createProcessInstance(processDefId, processBusinessKey,uid,createUserDeptId,createUserRoleId,title,vars);
    //从默认的开始事件启动流程
    List<TaskInstance> tasks = SDK.getProcessAPI().start(processInst, null).fetchActiveTasks();
    
    //删除一个流程实例时
    SDK.getProcessAPI().delete(processInst,UserContext.fromUID(deleteUser));
    

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
            info("流程删除前事件被触发-->" + ctx.getProcessInstance());
            String str1 = (String) ctx.getVariable("str1");
            if (UtilString.isEmpty(str1) || !str1.equals("remove yes")) {
                info("流程删除前事件-->测试str1必须为remove yes值才可以删除");
                return false;
            } else {
                info("流程删除前事件-->str1=" + str1);
            }
            return true;
        }
    
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用