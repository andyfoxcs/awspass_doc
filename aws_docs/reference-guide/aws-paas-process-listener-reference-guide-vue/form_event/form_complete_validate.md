# FORM_COMPLETE_VALIDATE | AWS 流程事件开发参考指南

## FORM_COMPLETE_VALIDATE

### 流程表单办理前校验,流程办理前被触发

项 | 说明  
---|---  
抽象类 | InterruptListener  
接口 | InterruptListenerInterface  
返回值 | 返回false，流程办理被阻止  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断   
-其中抛出BPMNError异常时，该节点定义的错误边界事件将被捕获，  
若未捕获且该流程为子流程，可被父流程CallActivity定义的  
边界错误事件捕获。如未定义，业务错误信息包装成结果返回  
  
### 常见触发场景

**1.用户点击办理按钮时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/form_event/2.png)

**注意**

  * DW数据窗口模型中，该事件使用保存前事件替代
  * BPMNError异常是事件处理过程中的一个特殊异常，通过该异常，用户可以在事件中进行特殊场景的信息输出。信息会使用带有确定按钮的对话框提示进行展示，以便于区别于其他的错误。

    
    
    //模拟子表记录数不能为0的场景
    if (count <= 0) {
        throw new BPMNError("5001", "子表未录入数据，不能提交");
        //第一个参数可根据需求随意定义，但不能为空串或者null
        //第二个参数为前端界面提示的内容
    }
    

**2.给用户提供一些信息**

流程表单办理前，可针对该表单的业务数据，给用户展示一些信息，这些信息可以是的普通的提醒类消息，也可以是警告，或者错误的消息。通常这些消息仅展示一次，但又不想使用对话框的交互方式时，适用该场景

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/form_event/4-1.png)

**该场景仅适用以下事件**

  * FORM_COMPLETE_VALIDATE
  * FORM_AFTER_SAVE
  * FORM_BEFORE_LOAD

开发实例参见[FORM_BEFORE_LOAD](<form_before_load.html>)

### 开发示例
    
    
    package com.actionsoft.apps.poc.api.local.process.listener.usertask;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListener;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListenerInterface;
    
    public class Test_FORM_COMPLETE_VALIDATE extends InterruptListener implements InterruptListenerInterface {
    
        public boolean execute(ProcessExecutionContext ctx) throws Exception {
            //业务异常代码（自定义）
            //业务异常信息（自定义）
            throw new BPMNError("0312","订单尚未审核，不能进行支付操作");
        }
    
    }