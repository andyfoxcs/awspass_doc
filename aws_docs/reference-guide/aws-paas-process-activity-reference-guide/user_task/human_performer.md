# 参与者 | AWS BPMN2 Activity参考指南

# 参与者

人工任务的实例由流程引擎自动分配给用户，也可以由用户或开发者在运行时刻动态指定。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/9.png)

如果人工任务设定了`宽延警告时限`或者开发者使用API为任务实例设置了逾期时间，将进入`任务超时监控`的监控范围，[详细参见这里](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.tasktimeout/index.html>)。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/13.png)
    
    
    //使用API设定过期时间
    SDK.getTaskAPI().setDueTime(taskInstId, dueTime);
    

### 两种参与者类型

  * 分配到一个账户（私有任务）
  * 共享给一群账户（共享任务）

#### 1\. 分配到一个账户（私有任务）

大部分的流程审批场景，一个任务被具体到一个账户。

#### 2\. 共享给一群账户（共享任务）

在一些业务处理场景，一个任务可以被共享给多个人。这类任务在流程引擎只创建一个任务实例，所有被共享的人都可以查询，最终只有一个人通过领用完成该任务。

**共享任务支持**

  * 共享给一个部门
  * 共享给一个角色
  * 共享给一个小组

API用法示例
    
    
    //查询tom个人待办和共享给tom的任务
    SDK.getTaskQueryAPI().activeTask().target("tom").supportClaimTask("tom")
    .listPage(firstRow, rowCount);
    
    //查询共享给某个部门的全部待办任务
    SDK.getTaskQueryAPI().activeTask().claimToDepartment(departmentId)
    .listPage(firstRow, rowCount);
    
    //查询共享给某个角色的全部待办任务
    SDK.getTaskQueryAPI().activeTask().claimToRole(roleId)
    .listPage(firstRow, rowCount);
    
    //查询共享给某个小组的全部待办任务
    SDK.getTaskQueryAPI().activeTask().claimToTeam(teamId)
    .listPage(firstRow, rowCount);
    

### 路由方案

路由方案从一组规则中动态寻找任务参与者。参与者可能是私有任务，也可能是共享任务，由路由方案实现的功能决定。

AWS的BPM引擎内置了三十余种路由方案，开发者也可以[扩展新的路由方案](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/performer.html>)。

  * 由办理者动态指定
  * 与流程或上个任务办理人相关
  * 与角色相关
  * 与部门相关
  * 与单位相关
  * 与小组相关
  * 与外部的API服务相关
  * 其他类型

### 路由参数

为`路由方案`提供进阶的参数配置。

### 限定范围

控制参与该节点的用户必须在指定的用户范围之内，从而确保该节点的执行人范围是完全受控的，无论是采用哪种路由方案还是由用户任意指定。

### 限定人数

控制参与该节点的用户数量必须指定的范围之内。例如从25个候选专家账户中，最多选出3个账户参与评审。

### 历史参与者优先

这是一个附加选项，用于提高节点在多次往返时的用户体验。当同一流程实例往返多次时，如果被退回的节点是从一批候选人确定的，那么当开启该选项时，该节点已办人账户将直接被推荐。

### 跳过选项

如果该参与者身份与特定规则重复时，可选择忽略跳过（如填单节点和审核节点是同一个人，忽略审核节点）。

**支持的规则**

  * 与上个任务参与者相同时
  * 找不到办理人时
  * 与指定节点任务参与者相同时

> 跳过的节点不产生任务实例，不会触发相关事件

**以下场景时该配置失效**

  * 该节点是流程的最后一个节点
  * 该节点的后继网关不是`排他网关`
  * 该节点的后继节点不是`人工节点`

### 用API获取路由方案的结果
    
    
    //获得指定节点路由方案配置的参与者。
    //该方法调用路由方案接口的getHumanPerformer（执行人）+getPotentialOwner（候选人 ），然后去重
    SDK.getTaskAPI().getParticipants(uid, processInstId, taskInstId, nextUserTaskDefId);
    
    //获得指定节点路由方案配置的执行人
    SDK.getTaskAPI().getParticipantsOfPerformer(uid, processInstId, taskInstId, nextUserTaskDefId);
    
    //获得指定节点路由方案配置的候选人
    SDK.getTaskAPI().getParticipantsOfPotential(uid, processInstId, taskInstId, nextUserTaskDefId);
    

### 用API创建和领取共享任务

AWS允许将参与者指派到一个部门、小组或者角色，这类任务被称为`公共人工任务`。公共人工任务只产生1条任务，可以共享给一组人。
    
    
    //创建共享任务实例，认领类型由claimType指定
    //1-部门，2-角色，3-小组
    SDK.getTaskAPI().createUserClaimTaskInstance(processInstId, parentTaskInstId, uid,
    targetActivityDefId, claimType, claimResourceId, title);
    
    //将共享任务变为私有任务。认领后其他人再次认领抛出异常
    SDK.getTaskAPI().claimTask(taskInstId, uid);
    
    //退回认领，其他人可以继续认领。
    SDK.getTaskAPI().unclaimTask(taskInstId);
    

> 全部API文档，[参见这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)

### 延伸阅读

  * [ACTIVITY_ADHOC_BRANCH事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/usertask_event/activity_adhoc_branch.html>)
  * [ACTIVITY_CONFIRM_PARTICIPANTS事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/usertask_event/activity_confirm_participants.html>)
  * [PROCESS_ACTIVITY_ADHOC_BRANCH事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/process_event/process_activity_adhoc_branch.html>)
  * [扩展新的路由方案](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/performer.html>)