# 人工任务（User Task） | AWS BPMN2 Activity参考指南

# 人工任务（User Task）

人工任务（User Task）用来表示业务流程中由人参与完成的工作。当引擎处理到该节点时，给指定的用户（参与者）或者一组用户（如部门、角色、小组，在AWS里被称为共享任务）创建待处理的任务项，等待用户的处理。

### 图形符号

符号 | 说明  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/1.png) | 单例（只产生一个任务）  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/2.png) | 顺序多例（产生一个或多个任务，按顺序处理）  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/3.png) | 并行多例（产生一个或多个任务，可以同时处理）  
  
### 主要选项

  * 任务办理选项
  * 任务传阅选项
  * 任务委托选项
  * 批量办理选项
  * 特事特办选项
  * 表单打印选项
  * 邮件提醒选项
  * 自由流程选项
  * 自由跳转选项
  * 多例控制选项
  * 审核菜单选项
  * 节点绩效选项

### 进阶设置

一个未做配置的人工任务可以被引擎正常执行，建模人员可以通过增强配置来符合业务流程的处理要求。

  * [参与者](<human_performer.html>)
  * [审核菜单](<audit_menu.html>)
  * [表单应用](<form.html>)
  * [事件触发器](<event.html>)
  * [时限](<monitor.html>)
  * [通知](<notification.html>)
  * [扩展属性](<advance_property.html>)

### 用API创建任务
    
    
    //给指定人创建一个任务实例，流程中断到这里等待完成
    SDK.getTaskAPI().createUserTaskInstance(processInst, parentTaskInstModel, userContext,
    targetActivityDefId, participant, title);
    
    //给指定人创建一个传阅任务实例，流程的执行不受影响
    SDK.getTaskAPI().createUserCCTaskInstance(processInst, parentTaskInstModel,
    userContext, participant, title);
    
    //给当前任务创建一个旁路加签自由任务，流程中断到这里等待外出
    SDK.getTaskAPI().createUserAdHocTaskInstance(processInst, parentTaskInstModel,
    userContext, participant, adHocType, title);
    

### 用API完成任务
    
    
    SDK.getTaskAPI().completeTask(taskInst, vars, userContext);
    

### 用API查询任务列表
    
    
    List<TaskInstance> tasks=SDK.getTaskQueryAPI().activeTask().listPage(firstRow, rowCount);
    

> 全部API文档，[参见这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)