# ACTIVITY_ADHOC_BRANCH | AWS 流程事件开发参考指南

## ACTIVITY_ADHOC_BRANCH

### 程序指定后继路线和参与者，上一节点准备离开时触发

项 | 说明  
---|---  
抽象类 | ValueListener  
接口 | ValueListenerInterface  
返回值 | -一个格式化的字符串值，如果返回null不干涉  
\- 格式：节点定义Id:参与者账户  
-如果指定节点定义Id，后继路线跳转到该节点  
-如果指定参与者账户（多个空格隔开），后继节点的参与者以该值为准  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断   
-其中抛出BPMNError异常时，该节点定义的错误边界事件将被捕获，  
若未捕获且该流程为子流程，可被父流程CallActivity定义的  
边界错误事件捕获。如未定义，业务错误信息包装成结果返回  
  
### 常见触发场景

**1.点击办理按钮校验通过后**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/usertask_event/2.png)

**2.使用SDK API时**
    
    
    //完成任务并向下推进时
    SDK.getTaskAPI().completeTask(tasks.get(0), UserContext.fromUID(optUser), true);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.usertask;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ValueListener;
    import com.actionsoft.bpms.bpmn.engine.listener.ValueListenerInterface;
    
    public class Test_ACTIVITY_ADHOC_BRANCH extends ValueListener implements ValueListenerInterface {
    
        public String execute(ProcessExecutionContext ctx) throws Exception {
            info("程序指定后继路线和参与者-->" + ctx.getTaskInstance());
            if (ctx.getProcessElement().getName().equals("U1")) {
                return "obj_c649377f56b000012274a6807f401783:admin";
            } else {
                return null;
            }
        }
    
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用