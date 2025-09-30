# 错误结束事件 | AWS BPMN2 Event参考指南

# 错误结束事件（Error End Event）

当执行到达`错误结束事件`时抛出BPMNError业务异常，表示流程或分支在发生业务错误后结束。如果抛出的异常未被捕获，该流程不会结束（状态仍然为`active`）。

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/51.png)

### 选项开关

**异常代码**

抛出的错误代码，如`ORDER-ERR-002`。如果未给定，运行到该事件时会抛出如下错误：
    
    
    Error Code must not be empty.
    

### 适用的模式

`错误结束事件`只适用于子流程结束，由父流程的[边界错误事件](<../boundaryevents/error_boundary_interrputing_event.html>)捕获。

父流程使用边界错误事件捕获错误 | 子流程使用错误结束事件抛出错误  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/52.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/53.png)  
  
如果父流程未捕获该错误，运行到该事件时会抛出如下错误：
    
    
    No catching boundary event found for error with errorCode 'xxx' ,
    neither in same process nor in parent process
    

### API使用场景

错误结束事件（Error End Event）由引擎自动触发，不需要API。

### 延伸阅读

[边界错误事件（Error Boundary Interrputing Event）](<../boundaryevents/error_boundary_interrputing_event.html>)