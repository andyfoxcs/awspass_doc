# JavaScript脚本 | AWS BPMN2 Activity参考指南

# JavaScript脚本

JavaScript 语法具有强大的用户基础，很容易上手。与大家熟悉的浏览器JavaScript不同，在脚本任务中编写的JavaScript运行在Server端。

AWS BPMN2使用了Mozilla的Rhino，Rhino是一种使用Java 语言编写的JavaScript的开源实现。Rhino是一种动态类型的、基于对象的脚本语言，它可以简单地访问各种Java类库。Rhino从 JavaScript 中借用了很多语法，让程序员可以快速编写功能强大的程序。

  * AWS BPMN2引擎支持的版本 JavaScript 1.5

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/javascript.png)

### 常用变量

通过js访问Java包：
    
    
    importPackage(包路径)
    

为了简化编程，我们封装了3个常用的入口变量，可在脚本中直接使用。

变量名 | 说明  
---|---  
ctx | [com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/core/delegate/ProcessExecutionContext.html>)  
sdk | [com.actionsoft.sdk.local.SDK](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/SDK.html>)  
dbsql | [com.actionsoft.bpms.util.DBSql](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/util/DBSql.html>)  
  
### 脚本示例

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/script3.png)

假如测试流程定义了`v1`变量，以下代码演示了`ctx`、`sdk`、`dbsql`变量的使用
    
    
    var hello = "Hello World, JavaScript! - Script1"
    
    //引擎上下文对象测试
    var processInstId=ctx.getProcessInstance().getId()
    var taskInstId=ctx.getTaskInstance().getId()
    print("processInstId="+processInstId)
    print("taskInstId="+taskInstId)
    ctx.setVariable("v1", hello);
    print("v1="+ctx.getVariable("v1"))
    
    //SDK测试
    print("AWSVersion="+sdk.getPlatformAPI().getAWSServer().getAWSVersion())
    
    //DBSql测试
    var param = {'ID':taskInstId}
    print("taskTitle= "+dbsql.getString("SELECT TASKTITLE FROM WFC_TASK WHERE ID=:ID","TASKTITLE",param))
    //query records
    var rows = dbsql.getList("SELECT * FROM WFC_TASK WHERE ID=:ID",param)
    print("taskTitle= "+rows.get(0).get("TASKTITLE"))
    print(rows)
    

运行时打印如下结果
    
    
    processInstId=d8262d2d-cd37-47d4-89d6-55e0e0073611
    taskInstId=2e42f216-adbd-4961-9e60-5e2fc0b641e7
    v1=Hello World, JavaScript! - Script1
    AWSVersion=6.1.1.0318
    taskTitle= XXXXXXX
    taskTitle= XXXXXXX
    [{ID=2e42f216-adbd-4961-9e60-5e2fc0b641e7,
    PARENTTASKINSTID=269032c9-c295-4a20-a0fe-2edc1d7b8b95,
    SCOPEID=269032c9-c295-4a20-a0fe-2edc1d7b8b95,
    ACTIVITYTYPE=scriptTask,
    ACTIVITYDEFID=obj_c73a377d2ff00001193c12a015f0ccd0,
    PROCESSINSTID=d8262d2d-cd37-47d4-89d6-55e0e0073611,
    PROCESSDEFID=obj_6cec36d47250400185446190d5ff54e3,
    PROCESSDEFVERID=obj_6cec36d47250400185446190d5ff54e3,
    PROCESSGROUPID=obj_723fdbae7f2848a985f775a86a083745,
    DISPATCHID=0, TASKTITLE=()AAAAA, TASKSTATE=0,
    CONTROLSTATE=active, PRIORITY=1, OWNER=, TARGET=,
    CLAIMTYPE=0, CLAIMRESOURCEID=0, DUETIME=null,
    BEGINTIME=2016-09-18 11:56:49.0,
    BEGINENGINENODE=localhost:10008, READTIME=null,
    OWNERDEPTID=0, TARGETDEPTID=0, TARGETCOMPANYID=0,
    TARGETROLEID=0, ISMONITOR=0, ISASYNC=0,
    EXCEPTIONERR=null, IOBD=, IOR=, IOS=, IOC=, EXT1=,
    EXT2=, EXT3=, REMINDTIMES=0, DELAYTIMES=0, READSTATE=0}]
    

### 异常处理

可以像Java代码一样，抛出错误异常。下面我们用示例抛出[BPMNError](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/exception/BPMNError.html>)业务异常，并捕获进行处理。
    
    
    importPackage(com.actionsoft.exception)
    
    throw new BPMNError("ERR110","业务代码错误");
    

流程图如下 ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/script2.png)