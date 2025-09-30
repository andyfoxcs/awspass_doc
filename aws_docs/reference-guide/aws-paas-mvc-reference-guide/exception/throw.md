# 异常抛出 · AWS PaaS文档中心

## 异常抛出

AWS平台提供的异常对象都是`uncheck`类型，开发者可以根据处理的需要进行捕获，如果开发者非常明确的要抛出这些异常，那么可以不对其处理。

除`AWSAPIException`外，所有AWS内部异常的父类都是`AWSExceptione`，常见异常如下：

Exception | 说明  
---|---  
AWSAPIException | API调用异常（uncheck）  
AWSException | AWS平台异常（以下均内部使用，uncheck）【通用】  
AWSClassLoaderException | 类加载异常  
AWSEngineException | 引擎内部异常（流程、表单、报表等，见该类常量）  
BPMNDefException | BPMN定义异常（设计阶段）  
BPMNError | BPMN规范要求捕获的异常抛出（运行阶段）  
AWSDataAccessException | 数据操作异常。如数据库操作、JSON数据操作  
AWSIllegalArgumentException | 参数校验异常【通用】  
AppStoreServiceException | 访问AWS企业应用商店异常  
  
### 常用异常

虽然AWS平台定义了很多异常对象，但是对于应用开发者，只需要熟练掌握以下几个，即可满足大部分开发场景的需要：

  * AWSIllegalArgumentException(400)
  * AWSForbiddenException(403)
  * AWSObjectNotFindException(404)
  * AWSException(500)

    
    
    //参数合法性异常
    throw new AWSIllegalArgumentException("参数1", AWSIllegalArgumentException.FORMAT,"参数必须是0-9数字");
    throw new AWSIllegalArgumentException("参数1", AWSIllegalArgumentException.EMPT);
    throw new AWSIllegalArgumentException("参数1不能为空");
    
    //操作被拒绝
    throw new AWSForbiddenException("流程已经挂起，操作被拒绝");
    throw new AWSForbiddenException("ctx类型不当，应给定begin()返回的上下文对象");
    
    //对象不存在
    throw new AWSObjectNotFindException("App文件不存在[" + appFile.getPath() + "]");
    throw new AWSObjectNotFindException("流程定义未找到。processDefinitionId:" + processDefinitionId);
    

### 注意事项

  * 4类异常，通常可以直接抛出给前端处理
  * 5类异常，除非开发者捕获该异常也无法提供解决方案，否则应在上层逻辑捕获并处理
  * 7和8类异常属于底层非预期信息，开发者不必捕获可直接抛出
  * 在捕获异常时，不建议直接捕获Exception，除非你的意图是处理掉所有异常的抛出
  * 如果开发者的程序捕获了所有异常，应当使用e.printStackTrace(System.err)记录日志