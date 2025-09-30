# 基本概念 | AWS BPMN2 Process参考指南

# 基本概念

流程引擎是BPMN2行为控制的内部实现。包括BPMN规定的基本行为（BPMN2 Spec p. 425 13-BPMN Execution Semantics）和AWS扩展行为。

# 词汇表

  * 实例
  * 多例
  * 单例
  * 串签
  * 并签
  * 并签完成率
  * 长流程
  * 短流程
  * 子流程
  * 启动流程
  * 撤销流程
  * 复活流程
  * 终止流程
  * 取消流程
  * 挂起流程
  * 激活流程
  * 多开始
  * 多结束
  * 完成任务
  * 收回任务
  * 取消任务
  * 任务回退
  * 任务委派
  * 任务认领
  * 交回认领
  * 挂起任务
  * 激活任务
  * 动态任务
  * 传阅任务
  * 通知任务

## 实例

Instance。流程引擎根据流程定义产生的若干具体结果。实例是一个代名词，例如，流程引擎在启动一个流程时会产生一个具体的流程实例（ProcessInstance），在执行过程中会产生若干任务实例（TaskInstance）。

## 多例

是指在同一个Activity（活动、节点）执行过程中，产生多于一个任务的情形。多例通常需要附加模式的支持，如顺序执行（串签）、并发执行（并签）。

多例也适用于子流程。

## 单例

多例的反义词。是指在同一个Activity（活动、节点）执行过程中，仅产生一个任务。

## 串签

是指在同一个人工节点，产生多例任务。多个任务按照参与者的顺序分配给办理者。如A，B两个人办理，A完毕后B会自动收到任务，B完毕后激活后继路线。

## 并签

是指在同一个人工节点，产生多例任务。多个任务同时分配给办理者。如A，B两个人办理，则A、B会同时收到任务，最后一个人完毕后激活后继路线。

## 并签完成率

是指在同一个人工节点，产生多例并签任务时，只要符合完成条件就结束其他未完成的任务，激活后继路线。

## 长流程

Process。也简称“流程”，在AWS BPM PaaS中指流程由人工任务或人工任务与系统任务混合的流程，这类流程一定有人的干预，不会执行即结束。

**引擎API示例**
    
    
    //创建流程实例
    ProcessInstance processInst=SDK.getProcessAPI().createProcessInstance(processDefId, uid, title);
    

## 短流程

Short Process。也简称“集成流”、“逻辑流”，与ESB的服务编排相似。在AWS BPM PaaS中指全部是由各种系统任务组合的流程，没有人工的干预，可能无需等待瞬间执行完毕。

**引擎API示例**
    
    
    //创建短流程实例
    ProcessInstance processInst=SDK.getProcessAPI().createShortProcessInstance(processDefId);
    

## 子流程

子流程使流程的设计与执行形成层次关系，在AWS BPM PaaS中子流程由[CallActivity](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/README.html>)实现。子流程与父流程拥有等同的行为，可以从子流程上下文中获得父流程信息。

## 启动流程

Start Process。将创建就绪状态的流程实例正式启动。如果该流程为短流程，可从返回的执行堆栈中获知流程的自动化执行结果；如果该流程为长流程，遇到人工节点并创建人工任务完毕后中断执行。

**引擎API示例**
    
    
    //启动流程，获得执行结果的查询器
    ProcessExecuteQuery q=SDK.getProcessAPI().start(processInst);
    
    //启动流程，获得创建的活动任务
    List<TaskInstance> list=SDK.getProcessAPI().start(processInst).fetchActiveTasks();
    

## 撤销流程

Restart Process。是指流程在未结束前，将流程重置到开始状态，从新处理。

**引擎API示例**
    
    
    //撤销重办
    SDK.getProcessAPI().restart(processInst, restartReason);
    

## 复活流程

Reactivate Process。又称为流程激活，是指流程在结束后，重新激活流程进入运行状态。

**引擎API示例**
    
    
    //结束重新复活
    SDK.getProcessAPI().reactivate(processInst, targetActivityId,
    isClearHistory, uid, targetUID, reactivateReason);
    

## 终止流程

Terminate Process。在非自然结束的状态下，终止流程的运行。终止流程在业务上不一定是发生了异常，这取决于[结束事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/README.html>)的使用。

**引擎API示例**
    
    
    //强制终止，结束流程
    SDK.getProcessAPI().terminate(processInst, userContext);
    

## 取消流程

Cancel Process。放弃正在执行的流程。

**引擎API示例**
    
    
    //强制取消，结束流程
    SDK.getProcessAPI().cancel(processInst, userContext);
    

## 挂起流程

Suspend Process。暂停流程的执行，挂起的流程不会显示到用户任务列表，属于管理员操作或API级操作。

**引擎API示例**
    
    
    //挂起流程
    SDK.getProcessAPI().suspend(processInst);
    

## 激活流程

Resume Process。将处于暂停的流程激活，继续执行。

**引擎API示例**
    
    
    //激活挂起的流程
    SDK.getProcessAPI().resume(processInst);
    

## 多开始

传统流程只有一个开始事件，在BPMN2.0规范中流程可以支持多开始。若使用多个开始，开发者在调用API时指定[开始事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/none_start_event.html>)。 **引擎API示例**
    
    
    //指定从`abcde`开始事件启动流程
    SDK.getProcessAPI().start(processInst, "abcde");
    

## 多结束

传统流程只有一个结束事件，在BPMN2.0规范中流程可以支持多结束。若使用多个[普通结束(NoneEndEvent)](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/end_event.html>)，每个结束事件只结束当前分支，如果没有其他活动的分支，流程自然结束。

## 完成任务

Complete Task。是指执行一个任务，不同Activity的任务，其对应的执行操作不同。对于人工任务，Complete操作表示任务办理通过；对于系统任务，Complete操作表示执行完毕。

**引擎API示例**
    
    
    //各类任务都通用的complete方法
    //--------------------------------
    //简单完成任务，不激活后继路线
    SDK.getTaskAPI().completeTask(taskInst, userContext);
    
    //使用高级参数完成任务
    SDK.getTaskAPI().completeTask(taskInst, userContext, isBranch, isBreakUserTask);
    

## 收回任务

Undo Task。是指收回已结束的任务，流程激活到被收回的节点。任务收回仅限于人工任务。

**引擎API示例**
    
    
    //收回已完成的任务（能否收回受策略配置控制）
    SDK.getTaskAPI().undoTask(taskInstId, uid, undoReason);
    

## 取消任务

Cancel Task。放弃正在执行的任务，如果此时该节点为单例状态，开发者应通过API创建一个新任务或继续流程的执行，防止取消任务后流程被中断。

**引擎API示例**
    
    
    //放弃任务的执行
    SDK.getTaskAPI().cancelTask(taskInst, uid, cancelReason);
    

## 任务回退

Rollback Task。是指将当前执行的任务回退到历史路径的某个节点，回退触发[边界补偿事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/compensate_boundary_interrputing_event.html>)。 **引擎API示例**
    
    
    //回退到指定节点
    SDK.getTaskAPI().rollbackTask(taskInst, targetActivityId, userContext,
    isCompensation, rollbackReason);
    

## 任务委托

Delegate Task。是指将某个任务主动委托给其他人处理，适用于人工任务。

**引擎API示例**
    
    
    //将单个任务委托给其他人
    SDK.getTaskAPI().delegateTask(taskInst, userContext, targetUser, delegateReason);
    

## 任务代理（委托）

Delegation Profile（委托凭据）。A把全部或部分任务委托给B，在有效期间内，AB均可以查询和处理该类Task（实例只有1个）。凭据失效后，A仍然可以查询和处理。委托凭据是一组流程、时间和代理人的策略组合。

**引擎API示例**
    
    
    //为A创建一个委托凭据
    SDK.getDelegationAPI().create(delegationModel);
    

## 任务认领

Claim Task。是指将共享任务转换成领取人私有任务，任务认领后其他人不能再认领。

**引擎API示例**
    
    
    //认领公共任务
    SDK.getTaskAPI().claimTask(taskInstId, uid);
    

## 交回认领

Un-claim Task。是指将已认领的任务返还给公共任务池。

**引擎API示例**
    
    
    //反悔操作，退回成公共任务
    SDK.getTaskAPI().unclaimTask(taskInstId);
    

## 挂起任务

Suspend Task。暂停任务的执行，挂起的任务不会显示到用户任务列表，属于管理员操作或API级操作。

**引擎API示例**
    
    
    //挂起任务
    SDK.getTaskAPI().suspend(taskInstId);
    

## 激活任务

Resume Task。将处于暂停的任务激活，继续执行。

**引擎API示例**
    
    
    //激活挂起的任务
    SDK.getTaskAPI().resume(taskInstId);
    

## 动态任务

Ad-Hoc Task，或者Ad-Hoc Process。是AWS BPM PaaS人工节点的一种增强特性，动态任务不在定义阶段设计，可在运行时刻动态决定，例如加签路径、协作处理等。动态任务会挂起当前任务，待动态任务处理完毕后当前任务会自动激活。

**引擎API示例**
    
    
    //动态创建一个自由旁路分支任务
    SDK.getTaskAPI().createUserAdHocTaskInstance(processInst, parentTaskInstModel,
    userContext, participant, adHocType, title);
    

## 传阅任务

不影响流程主干执行的知会任务，如将会议纪要传阅给与会人员。

**引擎API示例**
    
    
    //创建一个传阅任务
    SDK.getTaskAPI().createUserCCTaskInstance(processInst, parentTaskInstModel,
    userContext, participant, title);
    

## 通知任务

不影响流程主干执行的信息通知任务，如流程结束通知、某节点执行完毕通知。