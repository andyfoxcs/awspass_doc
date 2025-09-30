# FORM_TOOLBAR_BUILD | AWS 流程事件开发参考指南

## FORM_TOOLBAR_BUILD

### 表单工具栏构建

项 | 说明  
---|---  
抽象类 | FormToolbarBuilderListener  
接口 | ValueListenerInterface  
返回值 | List<ButtonModel>  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
### 按钮执行动作

项 | 说明  
---|---  
抽象类 | ValueListener  
接口 | ValueListenerInterface  
返回值 | String  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
### 常见触发场景

**1.用户打开任务表单时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/3.png)

### 按钮定义与设置

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/3-1.gif)

> 触发后端事件：response的JSON结构说明
    
    
    {
        "msg": "一个服务器端放入的消息",
        "id": ":RO;",//系统自动生成
        "result": "ok"//系统根据服务器端代码ResponseObject的类型生成，可能是ok、error
    }
    

### 工具条格式化事件例子
    
    
    public class TestFormToolbarBuild extends FormToolbarBuilderListener {
    
        public String getDescription() {
            return "表单扩展按钮工具栏构建事件测试";
        }
    
        public String getProvider() {
            return "Actionsoft";
        }
    
        public String getVersion() {
            return "1.0";
        }
    
        /**
         * 人工任务节点自定义按钮构建前方法，该方法可用于自定义按钮过滤，添加属性，修改属性等行为
         *
         * @param ctx 流程引擎提供给监听器的上下文对象
         * @param initButs 默认的自定义列表
         * @return 处理过的按钮列表
         */
        @Override
        public JSONArray buttonFactory(ProcessExecutionContext ctx, JSONArray initButs) {
            if(initButs != null && !initButs.isEmpty()){
                initButs.stream().forEach(item ->{
                    //自定义按钮配置
                    String customBtnObj = ((JSONObject)item).toJSONString();
                });
            }
            return initButs;
        }
    }
    

### 触发后端程序在Server端实现

Java事件注册方式：

> 应用id:类全路径

示例代码
    
    
    package com.actionsoft.apps.poc.form.event;
    
    import java.util.HashMap;
    import java.util.Map;
    
    import com.actionsoft.apps.AppsConst;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ValueListener;
    import com.actionsoft.bpms.commons.htmlframework.HtmlPageTemplate;
    import com.actionsoft.bpms.commons.mvc.view.ResponseObject;
    import com.actionsoft.bpms.server.UserContext;
    
    public class MyBtnActionImpl extends ValueListener {
    
        @Override
        public String execute(ProcessExecutionContext ctx) throws Exception {
            //参数获取
            //记录ID
            String boId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BOID);
            //表单ID
            String formId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_FORMID);
            //BO表名
            String boName = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
    
            // Ajax方式
            ResponseObject ro = ResponseObject.newOkResponse();
            boolean r = true;// 针对业务进行处理
            // 处理业务逻辑成功时
            if (r) {
                ro.msg("成功");// 返回给服务器的消息
                ro.put("key1", "value1").put("key2", "value2");// 放入前端需要的参数
                return ro.toString();
            } else {
                // 错误时
                ro = ResponseObject.newErrResponse();
                ro.msg("错误");
                return ro.toString();
            }
        }
    }