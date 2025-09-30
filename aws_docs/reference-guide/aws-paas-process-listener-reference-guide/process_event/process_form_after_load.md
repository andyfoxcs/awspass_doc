# PROCESS_FORM_AFTER_LOAD | AWS 流程事件开发参考指南

## PROCESS_FORM_AFTER_LOAD

### 该流程全局的FORM_AFTER_LOAD事件

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
在新版VUE表单引擎中，表单构建前事件会被调用两次：

  * 访问页面触发一次
  * 获取JSON结构时触发一次

通过`$FORM_SOURCE`参数来获取调用的场景
    
    
    String source = ctx.getParameterOfString("$FORM_SOURCE");
    if (source.equals("PAGE")) {
      // 页面触发调用
    }
    if (source.equals("JSON")) {
      // JSON结构触发调用
    }
    

通过`$FORM_ENGINE`参数来判断是新版本VUE引擎调用，还是jQuery引擎调用
    
    
    String engine = ctx.getParameterOfString("$FORM_ENGINE");
    if (engine.equals("VUE")) {
      // VUE引擎
    }
    if (engine.equals("jQuery")) {
      // jQuery引擎
    }
    

### 全局表单构建前事件

仅处理VUE表单的PAGE调用机制触发

通过给`AWS PaaS基础门户`创建参数，参数名：`commonFormAfterLoadEventImpl`，注册一个类，格式：`应用ID:类全路径`

如果该流程某个节点注册了FORM_AFTER_LOAD事件，则对该节点来说，该PROCESS_FORM_AFTER_LOAD事件失效。

### 常见触发场景

**1.用户打开表单时**

### 替换表单模板字段标签

参考`开发示例`小节

### 自定义表单标签

参考`开发示例`小节

### 开发示例
    
    
    public class TestFormAfterLoad extends ExecuteListener {
    
        public void execute(ProcessExecutionContext param) throws Exception {
            //参数获取
            //注意：除特殊说明外，下列参数仅在该事件中场景有效
            //记录ID
            String boId = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BOID);
            //表单ID
            String formId = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_FORMID);
            //BO表名
            String boName = param.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
    
            //表单引擎的数据结构
            JSONObject formContext = param.getParameterOfMap(ListenerConst.FORM_EVENT_PARAM_FORM_CONTEXT);
    
            // formContext对象中有以下几项：
            // formConfig：表单相关的描述信息，子表描述信息，子表描述信息
            // data：当前表单的BO表数据描述
            // dataExtends：针对data数据的扩展描述，如字段的显示值信息
            // 
        }
    
    }