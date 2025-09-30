# CALLACTIVITY_AFTER_SUBPROCESS_COMPLETE | AWS 流程事件开发参考指南

# CALLACTIVITY_AFTER_SUBPROCESS_COMPLETE

### 子流程实例结束后触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
异常 | 抛出异常时，如果该子流程实例是单例或多例的最后一个子流程实例，流程将中断在父流程的`子流程任务`  
参数 | CallActivityDefinitionConst.PARAM_CALLACTIVITY_CONTEXT  
  
### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.callactivity;
    
    import com.actionsoft.bpms.bpmn.constant.CallActivityDefinitionConst;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.TaskBehaviorContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    
    public class Test_CALLACTIVITY_AFTER_SUBPROCESS_COMPLETE extends ExecuteListener {
    
        @Override
        public void execute(ProcessExecutionContext ctx) throws Exception {
            // 父流程实例对象
            System.out.println("Parent ProcessInstance=" + ctx.getProcessInstance());
            // 子流程实例上下文
            TaskBehaviorContext subProcessCtx = (TaskBehaviorContext) ctx.getParameter(CallActivityDefinitionConst.PARAM_CALLACTIVITY_CONTEXT);
            // 子流程实例
            System.out.println("Sub ProcessInstance=" + subProcessCtx.getProcessInstance());
        }
    
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用