# Groovy脚本 | AWS BPMN2 Activity参考指南

# Groovy脚本

Groovy的语法与Java非常相似，是Java平台上设计的面向对象编程语言。这门动态语言拥有类似Python、Ruby和Smalltalk中的一些特性，可以作为Java平台的脚本语言使用。

<https://zh.wikipedia.org/wiki/Groovy>

  * AWS BPMN2引擎支持的版本 Groovy 2.2

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/groovy.png)

### 常用变量

开发者可以像使用Java一样import库资源。为了简化编程，我们封装了3个常用的入口变量，可在脚本中直接使用。

变量名 | 说明  
---|---  
ctx | [com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/core/delegate/ProcessExecutionContext.html>)  
sdk | [com.actionsoft.sdk.local.SDK](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/SDK.html>)  
dbsql | [com.actionsoft.bpms.util.DBSql](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/util/DBSql.html>)  
  
### 脚本示例

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/script1.png)

假如测试流程定义了`v1`变量，以下代码演示了`ctx`、`sdk`、`dbsql`变量的使用
    
    
    def hello = "Hello World, Groovy! - Script1"
    
    //引擎上下文对象测试
    def processInstId=ctx.getProcessInstance().getId()
    def taskInstId=ctx.getTaskInstance().getId()
    println "processInstId= $processInstId"
    println "taskInstId= $taskInstId"
    ctx.setVariable("v1", hello);
    println "v1="+ctx.getVariable("v1")
    
    //SDK测试
    println "AWSVersion="+sdk.getPlatformAPI().getAWSServer().getAWSVersion()
    
    //DBSql测试
    def param = [ID:taskInstId]
    println "taskTitle= "+dbsql.getString("SELECT TASKTITLE FROM WFC_TASK WHERE ID=:ID","TASKTITLE",param)
    //query records
    def rows = dbsql.getList("SELECT * FROM WFC_TASK WHERE ID=:ID",param)
    println "taskTitle= "+rows.get(0).get("TASKTITLE")
    println rows
    

运行时打印如下结果
    
    
    processInstId= 1011726d-9574-4b11-9e81-c7bbf97ca5a5
    taskInstId= ca2a9bf9-027c-49ce-8b8f-34806ed8d5b0
    v1=Hello World, Groovy! - Script1
    AWSVersion=6.1.1.0318
    taskTitle= XXXXXX
    taskTitle= XXXXXX
    [[ID:ca2a9bf9-027c-49ce-8b8f-34806ed8d5b0,
    PARENTTASKINSTID:254346bd-1ac7-41b9-8e54-70359839a59d,
    SCOPEID:254346bd-1ac7-41b9-8e54-70359839a59d,
    ACTIVITYTYPE:scriptTask,
    ACTIVITYDEFID:obj_c73a377d2ff00001193c12a015f0ccd0,
    PROCESSINSTID:1011726d-9574-4b11-9e81-c7bbf97ca5a5,
    PROCESSDEFID:obj_6cec36d47250400185446190d5ff54e3,
    PROCESSDEFVERID:obj_6cec36d47250400185446190d5ff54e3,
    PROCESSGROUPID:obj_723fdbae7f2848a985f775a86a083745,
    DISPATCHID:0, TASKTITLE:()AAAAA, TASKSTATE:0,
    CONTROLSTATE:active, PRIORITY:1, OWNER:, TARGET:,
    CLAIMTYPE:0, CLAIMRESOURCEID:0, DUETIME:null,
    BEGINTIME:2016-09-18 10:36:39.0,
    BEGINENGINENODE:localhost:10008, READTIME:null,
    OWNERDEPTID:0, TARGETDEPTID:0, TARGETCOMPANYID:0,
    TARGETROLEID:0, ISMONITOR:0, ISASYNC:0,
    EXCEPTIONERR:null, IOBD:, IOR:, IOS:, IOC:, EXT1:,
    EXT2:, EXT3:, REMINDTIMES:0, DELAYTIMES:0, READSTATE:0]]
    

### 异常处理

可以像Java代码一样，抛出错误异常。下面我们用示例抛出[BPMNError](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/exception/BPMNError.html>)业务异常，并捕获进行处理。
    
    
    import com.actionsoft.exception.BPMNError
    
    throw new BPMNError("ERR110","业务代码错误");
    

流程图如下 ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/script2.png)