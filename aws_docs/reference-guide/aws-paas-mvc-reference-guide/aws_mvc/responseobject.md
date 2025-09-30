# 非HTML结构 · AWS PaaS文档中心

## 非HTML结果

一些来自前端Ajax操作或服务请求通常需要响应一个结构化数据：

  * 一个操作结果是否成功
  * 一个被封装的数据结构

类型支持：

  * JSON
  * XML

### ResponseObject
    
    
    com.actionsoft.bpms.commons.mvc.view.ResponseObject
    

`ResponseObject`对象是AWS为开发者提供的一个通用数据对象封装，用于封装一个结构化处理结果。`ResponseObject`支持三种处理状态：

常量 | 值 | 说明  
---|---|---  
ResponseObject.SUCCESS | ok | 被成功处理。对应AWS UI中simpleAlertd的ok或info提示  
ResponseObject.WARNING | warning | 操作发生警告。对应AWS UI中simpleAlertd的warning提示  
ResponseObject.ERROR | error | 操作发生错误。对应AWS UI中simpleAlertd的error提示  
  
> 状态值可在返回结果的`result`项检查，这是一个必须结构

## msg-信息

当处理成功或发生失败时，应该将进阶的信息反馈给调用者。
    
    
    //success msg
    return ResponseObject.newOkResponse("a订单被取消").toString();
    //或者
    ResponseObject ro=ResponseObject.newOkResponse();
    ro.msg("a订单被取消");
    return ro.toString();
    
    //warning msg
    return ResponseObject.newWarnResponse("a订单已经发出").toString();
    //或者
    ResponseObject ro=ResponseObject.newWarnResponse();
    ro.msg("a订单已经发出");
    return ro.toString();
    
    //error msg
    return ResponseObject.newErrResponse("a订单取消失败，原因是xxxx").toString();
    //或者
    ResponseObject ro=ResponseObject.newErrResponse();
    ro.msg("a订单取消失败，原因是xxxx");
    return ro.toString();
    

> 补充信息可在返回结果的`msg`项检查，这是一个附加结构

### data-数据

以key/value形式由开发者自定义，value可以是一个简单Java对象也可以是一个集合对象。
    
    
    Map<String, Object> orderDetails = new HashMap<>();
    orderDetails.put("orderId", "001");
    orderDetails.put("customerId", "999");
    orderDetails.put("customerName", "Actionsoft");
    orderDetails.put("amount", Double.valueOf("980.01"));
    ResponseObject ro = ResponseObject.newOkResponse();
    ro.put("enabled", true);
    ro.put("orderDetails", orderDetails);
    return ro.toString();
    

> 数据可在返回结果的`data`项检查，这是一个附加结构

### 处理成JSON

默认`ResponseObject`的`toString()`将数据结构拼装成JSON串。
    
    
    return ro.toString();
    

**含有状态信息的JSON结构**
    
    
    {
        data: {
            enabled: true,
            orderDetails: {
                amount: 980.01,
                customerName: "Actionsoft",
                customerId: "999",
                orderId: "001"
            }
        },
        msg: "",
        result: "ok"
    }
    
    
    
    return ro.toDataString();
    

**只有数据的JSON结构**
    
    
    {
        enabled: true,
        orderDetails: {
            amount: 980.01,
            customerName: "Actionsoft",
            customerId: "999",
            orderId: "001"
        }
    }
    

### 处理成XML
    
    
    return ro.toXML();
    

**含有状态的XML Document片段**
    
    
    <result type="ok" errorCode="" msg="" />
    

### 数据来自文件系统

如果你的Java程序读取本地文件系统的文件，建议文件名和内容强制以utf-8读和写。这样做的原因是中文系统的Window默认是`936`字符集（可以使用`chcp`命令查看和设置），而大部分OS Server以utf-8进行编码。

如果程序强制以utf-8处理文件，当AWS PaaS在部署一段时间后，客户希望在Windows和Linux之间做迁移时，能够确保用户数据编码格式的一致性。