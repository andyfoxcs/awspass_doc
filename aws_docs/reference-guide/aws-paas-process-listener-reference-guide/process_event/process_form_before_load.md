# PROCESS_FORM_BEFORE_LOAD | AWS 流程事件开发参考指南

## PROCESS_FORM_BEFORE_LOAD

### 该流程全局的FORM_BEFORE_LOAD事件

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
如果该流程某个节点注册了FORM_BEFORE_LOAD事件，则对该节点来说，该PROCESS_FORM_BEFORE_LOAD事件失效。

参见[FORM_BEFORE_LOAD](<../form_event/form_before_load.html>)事件