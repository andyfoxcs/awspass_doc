# 消息数据处理 | AWS BPMN2 Event参考指南

# 消息数据处理

与[信号数据处理](<signal_data.html>)业务场景相似，由于涉及外部接口的互操作，因此在数据处理的方式有所不同。

### 抛出消息时

**基于流程的`抛出消息事件`由引擎自动触发**

  * 如果类型的是`内部消息`，暂不支持业务数据的传递
  * 如果类型的是`外部接口`，支持对接口服务的`数据映射`

**使用`payload`参数，由API编程触发**

  * startByMessage()
  * messageEventReceived()

    
    
    //初始化数据，消息事件启动流程
    Map<String, Object> payload = new HashMap<>();
    payload.put("OrderNo", "008");
    SDK.getProcessAPI().startByMessage(messageName, processBusinessKey, payload);
    
    //初始化数据，完成中断的消息事件
    Map<String, Object> payload = new HashMap<>();
    payload.put("CustomerNo", "888");
    SDK.getTaskAPI().messageEventReceived(messageName, corelation, payload);
    

_`payload`参数_

一个Map类型的Java对象。

Key | Value  
---|---  
流程变量名 | 支持String/Double/Long/Integer/Date/Timestamp类型  
BO存储表名 | List<BO>。每一个BO对象对应一条新建或者更新的表单数据