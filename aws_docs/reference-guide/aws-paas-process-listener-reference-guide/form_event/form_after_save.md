# FORM_AFTER_SAVE | AWS 流程事件开发参考指南

## FORM_AFTER_SAVE

### 表单(或子表)保存后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
通常，该事件用于补偿处理一些业务逻辑

### 常见触发场景

**1.用户在主表单点击保存时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/5.png)

**2.用户在子表单点击保存时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/6.png)

**3.给用户提供一些信息**

流程表单保存后，可针对该表单的业务数据，给用户展示一些信息，这些信息可以是的普通的提醒类消息，也可以是警告，或者错误的消息。通常这些消息仅展示一次，但又不想使用对话框的交互方式时，适用该场景

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/4-1.png)

**该场景仅适用以下事件**

  * FORM_COMPLETE_VALIDATE
  * FORM_AFTER_SAVE
  * FORM_BEFORE_LOAD

开发实例参见[FORM_BEFORE_LOAD](<form_before_load.html>)

### 开发示例

**注意** ：在子表导入后，为了提供性能，会在所有记录导入后执行一下保存后事件，该场景中获取到的参数会和普通的子表保存后事件有所差异，详情请见代码中的说明
    
    
    package com.actionsoft.apps.poc.form.event;
    
    import com.actionsoft.bpms.bo.engine.BO;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    
    public class TestFormAfterSave extends ExecuteListener {
    
        public String getDescription() {
            return "表单保存后的事件测试";
        }
    
        public String getProvider() {
            return "Actionsoft";
        }
    
        public String getVersion() {
            return "1.0";
        }
    
        public void execute(ProcessExecutionContext param) throws Exception {
            //参数获取
            //注意：除特殊说明外，下列参数仅在该事件中场景有效
            //记录ID
            String boId = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BOID);
            //表单ID
            String formId = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_FORMID);
            //BO表名
            String boName = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
            // 保存前的表单数据，注意：该参数针对不同场景获取内容会有所不同
            // 主表场景获取主表数据；普通子表页面的场景获取的是该条子表的数据；获取其他的数据请使用BOQueryAPI获取
            // 注意：这个数据是在保存前放入的，经过保存之后，这些数据和数据库中的数据是一致的
            BO formData = (BO) param.getParameter(ListenerConst.FORM_EVENT_PARAM_FORMDATA);
    
            // 获取Ajax子表在保存时的数据，由于Ajax子表的数据会同主表保存动作一起触发，需要使用该参数获取
            // 在Ajax子表的工具栏上的“保存”动作和主表的“保存”动作中有效
            // 注意：这个数据是在保存前放入的，经过保存之后，这些数据和数据库中的数据是一致的
            List<BO> gridData = (List) param.getParameter(ListenerConst.FORM_EVENT_PARAM_GRIDDATA);
            // 该记录是否新建的状态，由于机制调整，BO对象中的ID是不为空的，不能通过ID判断记录是否处于新建状态还是修改状态
            //注意：该参数仅适用保存前（后）事件中
            boolean isCreate = param.getParameterOfBoolean(ListenerConst.FORM_EVENT_PARAM_ISCREATE);
            //该记录是否通过复制功能创建，用于普通子表的复制时判断该状态
            //注意：该参数仅适用保存前（后）事件中
            boolean isCopy = param.getParameterOfBoolean(ListenerConst.FORM_EVENT_PARAM_ISCOPY);
    
            //注意
            //当该事件处于子表导入后被触发的场景时仅能获取到“ListenerConst.FORM_EVENT_PARAM_BONAME”和“ListenerConst.FORM_EVENT_PARAM_FORMID”
            //参数“ListenerConst.FORM_EVENT_PARAM_ISCREATE”E和“ListenerConst.FORM_EVENT_PARAM_ISCOPY”在该场景不适用
    
            //...
        }
    }