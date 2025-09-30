# CALLACTIVITY_BEFORE_SUBPROCESS_START | AWS 流程事件开发参考指南

# CALLACTIVITY_BEFORE_SUBPROCESS_START

### 子流程实例创建后启动前触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断   
-其中抛出BPMNError异常时，该节点定义的错误边界事件将被捕获，  
若未捕获且该流程为子流程，可被父流程CallActivity定义的  
边界错误事件捕获。如未定义，业务错误信息包装成结果返回  
参数 | CallActivityDefinitionConst.PARAM_CALLACTIVITY_CONTEXT  
  
### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.callactivity;
    
    import com.actionsoft.bpms.bpmn.constant.CallActivityDefinitionConst;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.TaskBehaviorContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    
    public class Test_CALLACTIVITY_BEFORE_SUBPROCESS_START extends ExecuteListener {
    
        @Override
        public void execute(ProcessExecutionContext ctx) throws Exception {
            // 父流程实例对象
            System.out.println("Parent ProcessInstance=" + ctx.getProcessInstance());
            // 子流程实例上下文，此阶段子流程实例已创建，未开始流程（无任务实例）
            TaskBehaviorContext subProcessCtx = (TaskBehaviorContext) ctx.getParameter(CallActivityDefinitionConst.PARAM_CALLACTIVITY_CONTEXT);
            // 子流程实例
            System.out.println("Sub ProcessInstance=" + subProcessCtx.getProcessInstance());
        }
    
    }
    

> 上述源码示例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用