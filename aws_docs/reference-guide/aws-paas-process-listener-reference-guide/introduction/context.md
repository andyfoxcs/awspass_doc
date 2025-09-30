# 上下文对象 | AWS 流程事件开发参考指南

## ProcessExecutionContext上下文对象

对于所有流程事件，开发者可以从接口中获取一个类型为ProcessExecutionContext的流程执行上下文对象，用来访问当前流程引擎的内部数据。（详细参见[JavaDoc](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/core/delegate/ProcessExecutionContext.html>)）

  * 获取当前流程实例、任务实例
  * 获取当前流程定义、节点定义、前置汇聚分支定义、后继连线分支定义
  * 流程变量读、写
  * 设置表单字段权限

    
    
        ...
        public boolean execute(ProcessExecutionContext ctx) throws Exception {
            info("流程完成前事件被触发-->" + ctx.getProcessInstance());
            return true;
        }
        ...
    

### ctx常用方法

  * getProcessInstance 获得当前流程实例对象
  * getTaskInstance 获得当前任务实例对象
  * getUserContext 获得当前用户上下文对象
  * getVariable 读取指定的流程变量
  * isChoiceActionMenu 当前人工任务是否选中了指定的审核菜单
  * execAtScript 执行@公式脚本
  * addFormReadOnlyPolicy 程序指定BO操作只读（优先级最高）
  * addFormEditablePolicy 程序指定BO可编辑（优先级最高）
  * addFormHiddenPolicy 程序指定BO字段隐藏（优先级最高）
  * addFormDisplayPolicy 程序指定BO字段显示（优先级最高）
  * addGridHiddenPolicy 程序指定子表列的BO字段隐藏（优先级最高）
  * addGridDisplayPolicy 程序指定子表列的BO字段显示（优先级最高）
  * addFormNotNullPolicy 程序指定BO字段必填（优先级最高）
  * addFormNullablePolicy 程序指定BO字段选填（优先级最高）
  * addGridColumnPolicy 程序指定子表列头的字段信息（可控制显示顺序，优先级最高，高于子表列字段的显示隐藏策略）

    
    
    //获取流程实例Id
    String processInstId=ctx.getProcessInstance().getId();
    
    //注意：除特殊说明外，下列参数仅在特定事件中的场景有效，不是所有事件都可以获取
    //获取操作的BO记录ID
    String boId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BOID);
    //获取操作的BO对象名
    String boName = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
    //获取当前表单模型Id
    String fromDefId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_FORMID);
    
    
    //从数据库读当前表单数据源数据
    BO custBO = SDK.getBOAPI().query("BO_ACT_XXX").detailByBindId(ctx.getProcessInstance().getId());
    

### 常用SDK API

  * DBSql 本地数据库操作
  * SDK.getBOAPI BO表读、写、查操作
  * SDK.getRuleAPI 执行规则脚本
  * SDK.getCCAPI 执行CC连接
  * SDK.getProcessAPI 流程实例控制
  * SDK.getProcessQueryAPI 流程实例查询
  * SDK.getTaskAPI 任务实例控制
  * SDK.getTaskQueryAPI 任务查询
  * SDK.getHistoryTaskQueryAPI 历史任务查询
  * SDK.getAppAPI 应用API，如执行ASLP
  * SDK.getORGAPI 组织结构查询、处理
  * SDK.getFormAPI 表单接口
  * ...