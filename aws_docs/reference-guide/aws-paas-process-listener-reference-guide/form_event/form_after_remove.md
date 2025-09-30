# FORM_AFTER_REMOVE | AWS 流程事件开发参考指南

## FORM_AFTER_REMOVE

### 表单子表记录删除后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
### 常见触发场景

**1.用户删除子表记录时**

删除后执行补偿动作

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/7.png)

**注意**

由于删除操作在底层代码中使用了数据库事务，如果在事件中需要对数据库进行操作，需要使用系统参数提供的数据库连接。否则，会出现数据库事务的问题。

**该参数仅在表单子表记录删除前（后）有效**
    
    
    Connection conn = (Connection) param.getParameter(ListenerConst.FORM_EVENT_PARAM_CONNECTION);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.form.event;
    
    import com.actionsoft.bpms.bo.engine.BO;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    
    public class TestFormAfterRemove extends ExecuteListener {
    
        public String getDescription() {
            return "表单子表记录删除后的事件测试";
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
            //子表单项ID
            String formItemId = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_FORMID);
            //BO表名
            String boName = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
    
            //被删除的记录，可读取该信息，进行删除后的补偿操作
            BO bo = (BO) param.getParameter(ListenerConst.FORM_EVENT_PARAM_REMOVED_BO);
    
            //注意：由于使用了事务，操作数据库需要使用如下方式获取的Connection连接
            //该参数仅在表单子表记录删除前（后）有效
            Connection conn = (Connection) param.getParameter(ListenerConst.FORM_EVENT_PARAM_CONNECTION);
    
            //执行删除后的业务补偿
        }
    }