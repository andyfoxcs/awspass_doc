# FORM_AFTER_LOAD | AWS 流程事件开发参考指南

## FORM_AFTER_LOAD

### 表单构建后被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/form_event/4.png)

**注意**

节点注册该事件后，流程全局的`PROCESS_FORM_AFTER_LOAD`将失效。

常见开发场景以及开发实例参见[PROCESS_FORM_AFTER_LOAD](<../process_event/process_form_after_load.html>)