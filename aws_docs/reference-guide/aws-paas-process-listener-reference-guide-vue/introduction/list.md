# 事件清单 | AWS 流程事件开发参考指南

## 事件清单

### 1.Process Event

#### 流程通用事件

无论是人工流程还是系统短流程，都被触发的事件

事件名称 | 说明  
---|---  
[PROCESS_BEFORE_CREATE](<../process_event/process_before_create.html>) | 流程创建前  
[PROCESS_AFTER_CREATE](<../process_event/process_after_create.html>) | 流程创建后  
[PROCESS_START](<../process_event/process_start.html>) | 流程启动  
[PROCESS_SUSPEND](<../process_event/process_suspend.html>) | 流程挂起  
[PROCESS_RESUME](<../process_event/process_resume.html>) | 流程恢复  
[PROCESS_BEFORE_COMPLETE](<../process_event/process_before_complete.html>) | 流程完成前  
[PROCESS_AFTER_COMPLETE](<../process_event/process_after_complete.html>) | 流程完成后  
[PROCESS_BEFORE_TERMINATE](<../process_event/process_before_terminate.html>) | 流程终止前  
[PROCESS_AFTER_TERMINATE](<../process_event/process_after_terminate.html>) | 流程终止后  
[PROCESS_BEFORE_CANCEL](<../process_event/process_before_cancel.html>) | 流程取消前  
[PROCESS_AFTER_CANCEL](<../process_event/process_after_cancel.html>) | 流程取消后  
[PROCESS_BEFORE_DELETE](<../process_event/process_before_delete.html>) | 流程删除前  
[PROCESS_AFTER_DELETE](<../process_event/process_after_delete.html>) | 流程删除后  
[PROCESS_BEFORE_REACTIVATE](<../process_event/process_before_reactivate.html>) | 流程复活前  
[PROCESS_AFTER_REACTIVATE](<../process_event/process_after_reactivate.html>) | 流程复活后  
  
#### 人工流程专有事件

含有人工节点的流程范围内全局事件

事件名称 | 说明  
---|---  
[PROCESS_ACTIVITY_ADHOC_BRANCH](<../process_event/process_activity_adhoc_branch.html>) | 程序指定后继路线和参与者。如果节点定义了ACTIVITY_ADHOC_BRANCH事件，则优先应用节点的实现  
[PROCESS_FORM_GRID_FILTER](<../process_event/process_form_grid_filter.html>) | 全局表单子表过滤。如果节点定义了FORM_GRID_FILTER事件，则优先应用节点实现  
[PROCESS_FORM_BEFORE_LOAD](<../process_event/process_form_before_load.html>) | 全局表单加载前事件。如果节点定义了FORM_BEFORE_LOAD事件，则优先应用节点实现  
[PROCESS_FORM_AFTER_LOAD](<../process_event/process_form_after_load.html>) | 全局表单加载后事件。如果节点定义了FORM_AFTER_LOAD事件，则优先应用节点实现  
  
#### 子流程专有事件

含有子流程节点的流程范围内全局事件

事件名称 | 说明  
---|---  
[CALLACTIVITY_BEFORE_SUBPROCESS_START](<../callactivity_event/callactivity_before_subprocess_start.html>) | 子流程实例创建后启动前事件  
[CALLACTIVITY_AFTER_SUBPROCESS_COMPLETE](<../callactivity_event/callactivity_after_subprocess_complete.html>) | 子流程实例结束后事件  
  
### 2.Activity Event

#### 节点通用事件

流程中各种节点都会触发的事件

事件名称 | 说明  
---|---  
[TASK_BEFORE_COMPLETE](<../activity_event/task_before_complete.html>) | 任务完成前  
[TASK_AFTER_COMPLETE](<../activity_event/task_after_complete.html>) | 任务完成后  
[TASK_SUSPEND](<../activity_event/task_suspend.html>) | 任务挂起  
[TASK_RESUME](<../activity_event/task_resume.html>) | 任务恢复  
[ACTIVITY_BEFORE_LEAVE](<../activity_event/activity_before_leave.html>) | 节点离开前  
[ACTIVITY_AFTER_LEAVE](<../activity_event/activity_after_leave.html>) | 节点离开后  
  
#### UserTask节点专有事件

当该节点为“UserTask”类型时，以下事件被触发

事件名称 | 说明  
---|---  
[ACTIVITY_ADHOC_BRANCH](<../usertask_event/activity_adhoc_branch.html>) | 程序指定后继路线和参与者  
[ACTIVITY_CONFIRM_PARTICIPANTS](<../usertask_event/activity_confirm_participants.html>) | 节点就绪参与者即将产生任务  
[TASK_BEFORE_UNDO](<../usertask_event/task_before_undo.html>) | 任务收回前被触发  
[TASK_AFTER_UNDO](<../usertask_event/task_after_undo.html>) | 任务收回后被触发  
[FORM_COMPLETE_VALIDATE](<../form_event/form_complete_validate.html>) | 流程表单办理前校验  
[FORM_TOOLBAR_BUILD](<../form_event/form_toolbar_build.html>) | 表单工具栏构建  
[FORM_BEFORE_LOAD](<../form_event/form_before_load.html>) | 表单加载前  
[FORM_AFTER_LOAD](<../form_event/form_after_load.html>) | 表单加载后  
[FORM_BEFORE_SAVE](<../form_event/form_before_save.html>) | 表单保存前  
[FORM_AFTER_SAVE](<../form_event/form_after_save.html>) | 表单保存后  
[FORM_BEFORE_REMOVE](<../form_event/form_before_remove.html>) | 表单删除前  
[FORM_AFTER_REMOVE](<../form_event/form_after_remove.html>) | 表单删除后  
[FORM_GRID_FILTER](<../form_event/form_grid_filter.html>) | 表单子表过滤  
[FORM_GRID_EXCEL_TRANSFORM](<../form_event/form_grid_excel_transform.html>) | 表单子表Excel转换处理  
  
### 3.全局事件

以下事件被引擎全局捕获

事件名称 | 说明  
---|---  
TASK_CREATE | 任务创建后  
TASK_READ | 任务阅读后  
TASK_COMPLETE | 任务执行完  
TASK_DELETE | 任务删除后  
TASK_SUSPEND | 任务挂起后  
TASK_RESUME | 任务恢复后