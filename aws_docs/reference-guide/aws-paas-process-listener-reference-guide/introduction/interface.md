# 编程接口 | AWS 流程事件开发参考指南

## 编程接口

当流程实例或任务实例（即将）发生状态转换时，AWS流程引擎的[事件总线（EventBus）](<../appendix/listener_handler.html>)会根据事件类型捕获开发者实现的Java代码，这些Java代码被开发者基于要求的监听接口实现，并注册在流程或节点的相应事件中。监听接口被分为四类：

  * 中断类（布尔值）
  * 取值类（字符串值）
  * 处理类（Void）
  * 特殊类（基于上述三类接口的自定义）

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/introduction/1.png)

接口 | 说明  
---|---  
InterruptListenerInterface | -返回Boolean，中断操作  
\- 开发者继承**InterruptListener** 抽象类  
ValueListenerInterface | -返回String，取值操作  
-开发者继承**ValueListener** 抽象类  
ExecuteListenerInterface | -逻辑处理  
-开发者继承**ExecuteListener** 抽象类  
  
**InterruptListener** 例子
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListener;
    
    public class Test_PROCESS_BEFORE_COMPLETED extends InterruptListener {
    
        public String getDescription() {
            return "测试用例";
        }
    
        public boolean execute(ProcessExecutionContext ctx) throws Exception {
            info("流程完成前事件被触发-->" + ctx.getProcessInstance());
            return true;
        }
    
    }