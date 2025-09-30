# 审核菜单 · AWS PaaS文档中心

## 审核菜单

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/info3.png)](<info3.png>)

项 | 说明  
---|---  
审核菜单 | 如果关闭此选项，该节点不提供审核菜单功能  
显示位置 | ．表单内  
．执行窗口  
．工具栏  
．工具栏和办理窗口  
留言校验 | 用于设置留言、附件的必填/隐藏选项  
常用审批意见 | 该属性需要启用[审批意见库](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.comments/index.html>)应用  
可选范围 | 该属性需要启用[审批意见库](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.comments/index.html>)应用  
意见往复 | 流程回退至该节点再次办理时是否覆盖上次审批意见，返回值为true或false，支持@公式，默认值为false  
  
**从模板中添加**

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/pl1.png)](<pl1.png>)  
从模板中添加  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/pl2.png)](<pl2.png>)  
  
> 通过拖动可以调整审核菜单显示顺序

### 定义审核菜单

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/shenhe1.png)](<shenhe1.png>)

项 | 说明  
---|---  
审核菜单名称 | 一个易于理解的决策名称，例如`同意、请示领导`，同一节点菜单名称不能重复  
是否默认 | 当用户打开任务表单时，该菜单被默认选中  
是否校验表单  |  如果希望用户在选择该审核菜单后，点击办理按钮时不进行表单校验（如必填字段），可将该项不勾选   
**注意：  
设置不校验表单后，数据将不会保存到数据库中。**  
审核意见校验 | 与留言校验配合使用  
．默认审核意见不控制，按留言校验的配置  
．选择审核意见非必填，按审核意见非必填  
．选择审核意见必填，按审核意见非必填  
．当留言校验选择隐藏时，不校验审核意见必填和非必填   
审核动作 | ．无特殊动作  
．跳转到开始节点  
．跳转到指定节点  
．跳转等待（指定节点处理完再回来）  
．跳转等待（终止当前任务，跳转到父流程节点处理完再回来）  
．退回(当前节点前的历史任务节点)，由办理在运行时自由指定  
．退回（从哪里来回哪里去）  
．退回（前一个节点)，与从哪来回哪去不同的是:如果前后往复几次，该选项总会往前退。场景：逐级不同意返回上个人工任务节点。注意：当逐级退回到流程第一人工任务节点时，要求第一人工任务节点路由方案不允许为`任意指定`，一般可设为 `与流程申请人相关 > 流程申请人`  
．退回（结束指定节点任务），试用于并行或包容网关流出的多个分支，紧邻的人工任务有审核意见退回时，同步结束其它分支未办理的任务，将流程回退至网关前的人工节点，可进阶指定结束的节点，支持多个。仅适用于网关前后紧邻的节点必须是人工任务的场景  
．退回（终止所有子流程实例，退回到父流程节点）  
．自然结束（结束当前分支，如果没有其他活动分支，流程自然结束）  
．终止结束（终止当前分支和其他分支，流程被终止）  
  
  1. 在AWS Portal门户参数中提供了运行时审核菜单展示样式的全局参数配置。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/2.png)](<2.png>)  
---  
  
  1. 在AWS PaaS实例控制台参数中提供了配置审核菜单的全局参数。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/2.1.png)](<2.1.png>)  
---  
  
### 参与连线条件判断

用户选中的审核菜单可用于后继网关连线的判断条件。例如，用户选择不同意，那么将流程分支转移到结束。 [![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/7.png)](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/7.png>) [![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/8.png)](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/8.png>)

### 复用当前审核菜单配置到...

当前节点的审核菜单复用到其他任务节点

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/3.gif)](<3.gif>)

### 延伸阅读

  * [AWS BPMN2 Activity参考指南>人工任务>审核菜单](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/audit_menu.html>)