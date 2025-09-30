# 启动流程对版本的选择 | AWS BPMN2 Event参考指南

# 启动流程对版本的选择

引擎会根据当前[AWS PaaS的运行环境](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/version/README.html>)，智能选择流程版本。

  * 当开发者使用`ProcessAPI`创建指定的流程实例时
  * 当[信号开始事件](<../startevents/signal_start_event.html>)、[消息开始事件](<../startevents/message_start_event.html>)被触发时

### 相关API清单

  * [ProcessAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/ProcessAPI.html>).createShortProcessInstance
  * [ProcessAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/ProcessAPI.html>).createProcessInstance
  * [ProcessAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/ProcessAPI.html>).createSubProcessInstance
  * [ProcessAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/ProcessAPI.html>).signalStartEventReceived
  * [ProcessAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/ProcessAPI.html>).startByMessage

### API参数`processDefId`场景

**当前是DEV开发环境时：**

参数`processDefId`给定的值 | 说明  
---|---  
流程模型Id且不同于流程版本Id | \- 如果版本可用，使用该模型  
\- 如果版本停用，抛出错误  
流程版本Id | \- 优先使用`设计`版  
\- 候选使用`正式`版  
\- 如果没有可用版本，抛出错误  
  
**当前是PRD生产环境、QAS测试环境、TEST压测环境时：**

参数`processDefId`给定的值 | 说明  
---|---  
流程模型Id且不同于流程版本Id | \- 如果版本可用，使用该模型  
\- 如果版本停用，抛出错误  
流程版本Id | \- 优先使用`正式`版  
\- 候选使用`设计`版  
\- 如果没有可用版本，抛出错误  
  
开发者也可以使用[RepositoryAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/RepositoryAPI.html>)获得可用的流程模型Id
    
    
    //根据当前AWS PaaS的运行环境，智能返回可启动的流程版本Id
    //@param id 一个流程模型Id或流程版本Id
    String processDefId= SDK.getRepositoryAPI().getProcessDefIdOfWork(String id);
    //@return 一个流程定义Id，没有可用流程返回空串
    if(!UtilString.isEmpty(processDefId)){
        //...
    }
    

### 信号开始、消息开始场景

**当前是DEV开发环境时：**

  * 优先使用`设计`版
  * 候选使用`正式`版
  * 如果没有可用版本，抛出错误

**当前是PRD生产环境、QAS测试环境、TEST压测环境时：**

  * 优先使用`正式`版
  * 候选使用`设计`版
  * 如果没有可用版本，抛出错误