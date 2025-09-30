# 如何输出业务对话 | AWS 流程事件开发参考指南

## 如何输出业务对话

### 抛出BPMNError

遵循BPMN2的标准，当开发者需要在表单事件或有人工交互的场景，给用户输出业务提示信息时，可使用如下方法
    
    
    //业务异常代码（自定义）
    //业务异常信息（自定义）
    throw new BPMNError("ERR0312","订单尚未审核，不能进行支付操作");
    

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/appendix/alert.png)

> 当上述场景发生在流程引擎内部时，如果流程使用了`边界错误事件（Error Boundary Interrputing Event）`进行异常建模，那么将按照错误捕获事件去执行，如下图

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/appendix/2.png)

### 使用AlertMessage

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/appendix/3.png)

**仅适用以下事件**

  * FORM_COMPLETE_VALIDATE
  * FORM_AFTER_SAVE
  * FORM_BEFORE_LOAD

    
    
    //以下是表单横幅消息的示例代码，多条消息顺序按照添加的顺序展示
    //第一个参数是BO名称，第二个参数是消息内容，这是一个默认的消息
    ctx.addAlertMessage(boName, "测试横幅警告消息");
    ctx.addAlertMessage(boName, "第二个消息");
    ctx.addAlertMessageInfo(boName, "我是第三个提醒消息");//这是一个普通的消息
    ctx.addAlertMessageWarn(boName, "我是第四个警告消息");//这是一个警告的消息
    ctx.addAlertMessageError(boName, "我是第五个错误消息");//这是一个错误的消息
    //另外提供了自定义外观的消息，第三个参数指定背景色，第四个参数指定文字颜色
    ctx.addAlertMessage(boName, "消息", "bgColor", "fontColor");