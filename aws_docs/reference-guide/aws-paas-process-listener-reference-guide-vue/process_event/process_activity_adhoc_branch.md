# PROCESS_ACTIVITY_ADHOC_BRANCH | AWS 流程事件开发参考指南

## PROCESS_ACTIVITY_ADHOC_BRANCH

### 该流程全局的ADHOC_BRANCH事件，见ACTIVITY_ADHOC_BRANCH说明

如果该流程某个节点注册了ACTIVITY_ADHOC_BRANCH事件，则对该节点来说，该PROCESS_ACTIVITY_ADHOC_BRANCH事件失效。

### 常见触发场景

**1.点击办理按钮校验通过后**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/8.png)

**2.使用SDK API时**
    
    
    //创建流程实例
    ProcessInstance processInst = SDK.getProcessAPI().createProcessInstance(processDefId, processBusinessKey,uid,createUserDeptId,createUserRoleId,title,vars);
    //从默认的开始事件启动流程
    List<TaskInstance> tasks = SDK.getProcessAPI().start(processInst, null).fetchActiveTasks();
    
    //完成任务并向下推进时
    SDK.getTaskAPI().completeTask(tasks.get(0), UserContext.fromUID(optUser), true);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ValueListener;
    
    public class Test_PROCESS_ACTIVITY_ADHOC_BRANCH extends ValueListener {
    
        public String getDescription() {
            return "测试用例";
        }
    
        // 规则activityDefId:执行人
        public String execute(ProcessExecutionContext ctx) throws Exception {
            if (ctx.getProcessElement().getName().equals("U1")) {
                info("流程全局跳转事件被触发-->" + ctx.getProcessInstance());
                return "obj_c60c1e1780900001d21d59391c441b54:admin";
            } else {
                return null;
            }
        }
    
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用