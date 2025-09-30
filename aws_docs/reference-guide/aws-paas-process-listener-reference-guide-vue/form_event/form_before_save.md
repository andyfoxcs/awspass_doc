# FORM_BEFORE_SAVE | AWS 流程事件开发参考指南

## FORM_BEFORE_SAVE

### 表单(或子表)保存前被触发

项 | 说明  
---|---  
抽象类 | InterruptListener  
接口 | InterruptListenerInterface  
返回值 | 返回false，表单保存被阻止  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
通常，该事件用于在保存前的最后一次校验，可以用来阻止保存

### 常见触发场景

**1.用户在主表单点击保存时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/form_event/5.png)

**2.用户在子表单点击保存时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/form_event/6.png)

### 开发示例
    
    
    package com.actionsoft.apps.poc.form.event;
    
    import com.actionsoft.bpms.bo.engine.BO;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.InterruptListener;
    import com.actionsoft.sdk.local.SDK;
    
    public class TestFormBeforeSave extends InterruptListener {
    
        public String getDescription() {
            return "表单保存前的事件测试";
        }
    
        public String getProvider() {
            return "Actionsoft";
        }
    
        public String getVersion() {
            return "1.0";
        }
    
        public boolean execute(ProcessExecutionContext param) throws Exception {
            //参数获取
            //注意：除特殊说明外，下列参数仅在该事件中场景有效
            //记录ID
            String boId = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BOID);
            //表单ID
            String formId = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_FORMID);
            //BO表名 ，当表单中有主子表多个表时，该事件会执行多次，开发人员需要判断当前执行换取到的表名，进一步进行业务处理
            String boName = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
    
            // 保存前的表单数据，注意：该参数针对不同场景获取内容会有所不同
            // 主表中的保存场景获取主表数据；普通子表页面的保存场景获取的是该条子表的数据；如果需要获得其他数据请使用BOQueryAPI获取
            BO formData = (BO) param.getParameter(ListenerConst.FORM_EVENT_PARAM_FORMDATA);
    
            // 获取Ajax子表的数据，由于Ajax子表的数据会同主表保存动作一起触发，需要使用该参数获取
            // 在Ajax子表的工具栏上的“保存”动作和主表的“保存”动作中有效
            // 注意：该数据并不是从数据库中获取，获取的数据取决于表单上对Ajax子表新增的数据与修改的数据的和
            List<BO> gridData = (List) param.getParameter(ListenerConst.FORM_EVENT_PARAM_GRIDDATA);
            //遍历子表的数据
            for (BO rowData : gridData) {
                //下面一行示例代码，可以获取Ajax子表的每行记录的新建状态
                boolean rowDataIsCreate = Boolean.parseBoolean(rowData.getString("isCreate"));//注意：isCreate并不是BO的一个字段，该字段是有接口上层赋值的
            }
    
            // 该记录是否新建的状态，由于机制调整，BO对象中的ID是不为空的，不能通过ID判断记录是否处于新建状态还是修改状态
            //注意：该参数仅适用保存前（后）事件中，该参数仅能获取主表的是否新建状态
            boolean isCreate = param.getParameterOfBoolean(ListenerConst.FORM_EVENT_PARAM_ISCREATE);
    
            //该记录是否通过复制功能创建，用于普通子表的复制时判断该状态
            //注意：该参数仅适用保存前（后）事件中
            boolean isCopy = param.getParameterOfBoolean(ListenerConst.FORM_EVENT_PARAM_ISCOPY);
    
            return true;//返回true可以正常保存表单
            //return false;//可阻止表单保存
            //或者直接抛出BPMNErr异常
            //throw new BPMNError("0313","数据不完整，不能进行保存操作");
        }
    }