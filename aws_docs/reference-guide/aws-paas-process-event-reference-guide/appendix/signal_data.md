# 信号数据处理 | AWS BPMN2 Event参考指南

# 信号数据处理

在发送或接收信号时，除了实现跨任务间的联动，还需要传输关键业务数据，实现业务层的联动。

### 抛出信号时

首先，基于业务场景定义`BO Structure`类型的[BO结构模型](<bo_structure.html>)。

**基于流程的`抛出信号事件`由引擎自动触发**

  * 在抛出信号事件的流程中，定义`信号`变量并引用`BO Structure`结构模型
  * 在抛出信号事件的`数据映射`中，将要传递的数据/规则映射到`BO Structure`结构字段

**使用`payload`参数，由API编程触发**

  * signalStartEventReceived()
  * signalEventReceived()

    
    
    //初始化指定BO Structure的OrderNo数据项，信号事件启动流程
    Map<String, Object> payload = new HashMap<>();
    payload.put("OrderNo", "008");
    SDK.getProcessAPI().signalStartEventReceived(signalName,corelation, payload);
    
    //初始化指定BO Structure的OrderNo数据项，完成中断的信号事件
    Map<String, Object> payload = new HashMap<>();
    payload.put("OrderNo", "009");
    SDK.getTaskAPI().signalEventReceived(signalName, corelation, payload);
    

_`payload`参数_

一个Map类型的Java对象。

Key | Value  
---|---  
BO Structure的字段名 | 支持String/Double/Long/Integer/Date/Timestamp类型  
  
### 订阅信号时

  * 在捕获类信号事件的流程中，定义`信号`变量并引用相同的`BO Structure`结构模型
  * 在捕获信号事件的`数据映射`中，将`BO Structure`结构字段映射到当前流程的流程变量或BO表