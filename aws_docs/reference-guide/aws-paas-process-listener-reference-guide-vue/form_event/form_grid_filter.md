# FORM_GRID_FILTER | AWS 流程事件开发参考指南

## FORM_GRID_FILTER

### 表单子表过滤(支持普通子表、Ajax子表)

项 | 说明  
---|---  
抽象类 | FormGridFilterListener  
接口 | ValueListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
**注意**

节点注册该事件后，流程全局的`PROCESS_FORM_GRID_FILTER`将失效。

常见开发场景以及开发实例参见[PROCESS_FORM_GRID_FILTER](<../process_event/process_form_grid_filter.html>)