# 边界错误事件 | AWS BPMN2 Event参考指南

# 边界错误事件（Error Boundary Interrputing Event）

当`边界错误事件`依附的节点任务抛出[BPMNError](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/exception/BPMNError.html>)业务异常时中断该任务，`边界错误事件`自动被激活，执行错误事件后继路线上的任务。

  * 边界错误事件不捕获和处理非BPMNError异常
  * 抛出的BPMNError异常代码与边界错误事件的`异常代码`匹配成功，才会激活后继路线
  * 如果边界错误事件的`异常代码`未设置，表示匹配所有的BPMNError异常

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/51.png)

### 选项开关

  * **异常代码** 用来匹配抛出BPMNError的错误代码

### API使用场景

边界错误事件（Error Boundary Interrputing Event）由捕获的错误自动触发，不需要API。