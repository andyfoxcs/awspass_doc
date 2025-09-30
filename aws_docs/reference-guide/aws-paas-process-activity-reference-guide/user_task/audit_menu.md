# 审核菜单 | AWS BPMN2 Activity参考指南

# 审核菜单

一组为用户提供的审批/处理选项，例如`同意`、`不同意`。

**场景1：处理选项、填写意见**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/5.png)

**场景2：查看审批记录**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/6.png)

### 主要配置项

项 | 说明  
---|---  
提供人工审核菜单 | 如果关闭此选项，该节点不提供审核菜单功能  
审核菜单显示位置 | 表单内/执行窗口/工具栏，三选一  
审批留言 | 用于设置留言、附件的必填/隐藏选项  
显示历史审批记录 | 当任务到达该节点时，是否显示审批记录  
  
### 定义审核菜单

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/4.png)

如果希望用户在选择某项审核菜单后，点击`办理`按钮时不进行表单校验（如必填字段），可将`是否校验表单`设置为否

**特殊动作**

  * 跳转到开始节点
  * 跳转等待（指定节点处理完再回来）
  * 退回（从哪里来回哪里去）
  * 退回（前一个节点）

> 若特殊动作被触发，该节点的后继连线将不被执行

### 参与连线条件判断

用户选中的审核菜单可用于后继网关连线的判断条件。例如，用户选择`不同意`，那么将流程分支转移到结束。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/7.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/8.png)

### 在节点事件中进行程序判断

开发者可以在流程节点事件代码中，通过API判断用户选中的审核菜单，继而提供对应的逻辑处理。例如，当用户选择`订单已发出`选项后，完成任务时更新订单数据状态。

> 有关事件开发，[请点击这里](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/index.html>)
    
    
    ...
    
    public boolean execute(ProcessExecutionContext ctx) throws Exception {
        //使用事件上下文，直接判断
        Boolean c1 = ctx.isChoiceActionMenu("订单已发出");
    
        //使用SDK，对指定的任务实例进行判断
        Boolean c2 = SDK.getTaskAPI().isChoiceActionMenu(ctx.getTaskInstance(), "订单已发出");
        ...
    }
    

### 用API模拟用户的处理

可以使用API模拟用户选择审核菜单、填写意见的操作过程。
    
    
    //为任务提交一个审批留言到历史记录
    SDK.getTaskAPI().commitComment(taskInst, user, actionName,
    commentMsg, isIgnoreDefaultSetting);
    

### 用API获取流程的审批意见记录
    
    
    //通过流程实例Id，获取审批留言列表
    List<TaskCommentModel>  comments1 = SDK.getProcessAPI().
    getCommentsById(processInstId);
    
    //通过业务关键字，获取审批留言列表
    List<TaskCommentModel>  comments2 = SDK.getProcessAPI().
    getCommentsByBusinessKey(businessKey);
    

> 全部API文档，[参见这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)