# ACTIVITY_CONFIRM_PARTICIPANTS | AWS 流程事件开发参考指南

## ACTIVITY_CONFIRM_PARTICIPANTS

### 节点就绪参与者即将产生任务

项 | 说明  
---|---  
抽象类 | ValueListener  
接口 | ValueListenerInterface  
返回值 | \- 一个格式化的字符串值，如果返回null不干涉  
\- 格式：参与者账户，开发者可以在ProcessExecutionContext上下文中调用  
getParameterOfString("$PARTICIPANTS")获得引擎通过路由或ACTIVITY_ADHOC_BRANCH事件获取的参与者账户（多个空格隔开）  
-如果多个账户，将按该节点的多例模式进行处理  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断   
-其中抛出BPMNError异常时，该节点定义的错误边界事件将被捕获，  
若未捕获且该流程为子流程，可被父流程CallActivity定义的  
边界错误事件捕获。如未定义，业务错误信息包装成结果返回  
  
### 常见触发场景

**1.获得下个执行任务路径时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/usertask_event/3.png)

**2.使用SDK API时**
    
    
    //完成任务并向下推进时
    SDK.getTaskAPI().completeTask(tasks.get(0), UserContext.fromUID(optUser), true);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.usertask;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ValueListener;
    import com.actionsoft.bpms.bpmn.engine.listener.ValueListenerInterface;
    
    public class Test_ACTIVITY_CONFIRM_PARTICIPANTS extends ValueListener implements ValueListenerInterface {
    
        public String execute(ProcessExecutionContext ctx) throws Exception {
            info("节点就绪参与者即将产生任务被触发");
            String participants = ctx.getParameterOfString("$PARTICIPANTS");
            info("即将给[" + participants + "]创建人工任务");
            return "admin admin admin";// 不干预当前的委派过程
        }
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用