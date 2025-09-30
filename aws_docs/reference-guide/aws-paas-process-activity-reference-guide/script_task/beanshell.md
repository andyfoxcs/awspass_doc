# BeanShell脚本 | AWS BPMN2 Activity参考指南

# BeanShell脚本

BeanShell是一种小巧、嵌入式的Java脚本语言。

<http://www.beanshell.org/>

  * AWS BPMN2引擎支持的版本 BeanShell2.0

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/beanshell.png)

### 常用变量

常规Java类型beanshell已经帮你引入，可以通过import引入特定的Java包
    
    
    import 包路径
    

为了简化编程，我们封装了3个常用的入口变量，可在脚本中直接使用。

变量名 | 说明  
---|---  
ctx | [com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/core/delegate/ProcessExecutionContext.html>)  
sdk | [com.actionsoft.sdk.local.SDK](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/SDK.html>)  
dbsql | [com.actionsoft.bpms.util.DBSql](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/util/DBSql.html>)  
  
### 脚本示例

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/script4.png)

假如测试流程定义了`v1`变量，以下代码演示了`ctx`、`sdk`、`dbsql`变量的使用
    
    
    var hello = "Hello World, BeanShell! - Script1";
    
    //引擎上下文对象测试
    var processInstId=ctx.getProcessInstance().getId();
    var taskInstId=ctx.getTaskInstance().getId();
    print("processInstId="+processInstId);
    print("taskInstId="+taskInstId);
    ctx.setVariable("v1", hello);
    print("v1="+ctx.getVariable("v1"));
    
    //SDK测试
    print("AWSVersion="+sdk.getPlatformAPI().getAWSServer().getAWSVersion());
    
    //DBSql测试
    var param = new HashMap();
    param.put("ID",taskInstId);
    print("taskTitle= "+dbsql.getString("SELECT TASKTITLE FROM WFC_TASK WHERE ID=:ID","TASKTITLE",param));
    //query records
    var rows = dbsql.getList("SELECT * FROM WFC_TASK WHERE ID=:ID",param);
    print("taskTitle= "+rows.get(0).get("TASKTITLE"));
    print(rows);
    

运行时打印如下结果
    
    
    processInstId=50c973dc-2638-41b3-b58e-2389d048cdf4
    taskInstId=54c312f0-5958-4ba5-92a3-4b1be283ca9f
    v1=Hello World, BeanShell! - Script1
    AWSVersion=6.1.1.0318
    taskTitle= XXXXXX
    taskTitle= XXXXXX
    [{ID=54c312f0-5958-4ba5-92a3-4b1be283ca9f,
    PARENTTASKINSTID=34a68366-3a8c-416c-b5c3-1756531a5c8b,
    SCOPEID=34a68366-3a8c-416c-b5c3-1756531a5c8b,
    ACTIVITYTYPE=scriptTask,
    ACTIVITYDEFID=obj_c73a377d2ff00001193c12a015f0ccd0,
    PROCESSINSTID=50c973dc-2638-41b3-b58e-2389d048cdf4,
    PROCESSDEFID=obj_6cec36d47250400185446190d5ff54e3,
    PROCESSDEFVERID=obj_6cec36d47250400185446190d5ff54e3,
    PROCESSGROUPID=obj_723fdbae7f2848a985f775a86a083745,
    DISPATCHID=0, TASKTITLE=()AAAAA, TASKSTATE=0,
    CONTROLSTATE=active, PRIORITY=1, OWNER=, TARGET=,
    CLAIMTYPE=0, CLAIMRESOURCEID=0, DUETIME=null,
    BEGINTIME=2016-09-18 19:16:47.0,
    BEGINENGINENODE=localhost:10008, READTIME=null,
    OWNERDEPTID=0, TARGETDEPTID=0, TARGETCOMPANYID=0,
    TARGETROLEID=0, ISMONITOR=0, ISASYNC=0,
    EXCEPTIONERR=null, IOBD=, IOR=, IOS=, IOC=, EXT1=,
    EXT2=, EXT3=, REMINDTIMES=0, DELAYTIMES=0, READSTATE=0}]
    

### 异常处理

可以像Java代码一样，抛出错误异常。下面我们用示例抛出[BPMNError](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/exception/BPMNError.html>)业务异常，并捕获进行处理。
    
    
    import com.actionsoft.exception.BPMNError;
    
    throw new BPMNError("ERR110","业务代码错误");
    

流程图如下 ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/script_task/script2.png)