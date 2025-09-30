# 流程工作箱 · AWS PaaS文档中心

# 流程工作箱

流程工作箱是普通用户创建、办理流程的窗口，同[流程中心](<https://docs.awspaas.com/apps/com.actionsoft.apps.workbench/>)，流程工作箱仅显示当前流程组的实例数据，而流程中心 会显示当前用户所有的流程数据。

## 流程工作箱入口

实施阶段，运行人员可通过流程设计器上的运行按钮，快速打开流程工作箱。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/worklist/1.png)](<1.png>)

普通用户，可通过[流程发布](<deploy>)的菜单入口，在客户端访问。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/worklist/2.png)](<2.png>)

## 流程工作箱功能介绍

### 待办

显示当前用户的所有待办任务及别人委托过来的任务。

  1. 角标数量为未读任务数量
  2. 当流程标题包含【】或 [] 时，流程标题自动将【】[]内的内容用色块显示
  3. _bpm.portal 应用提供了一系列工作箱配置参数，详细请登录AWS PaaS控制台访问 _bpm.portal应用中相关参数说明

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/worklist/3.png)](<3.png>)

> 委托是指普通用户在[流程中心委托设置](<https://docs.awspaas.com/apps/com.actionsoft.apps.workbench/function/delegatesettion.html>)中委托。[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/worklist/4.png)](<4.png>)

### 待阅

显示当前用户的所有待阅读的传阅类、通知类任务。当用户查看后，将自动从该列表消失，任务将会在已阅中显示。

### 已办

显示当前用户的所有已办任务。

  1. _bpm.portal 应用提供了一系列工作箱配置参数，详细请登录AWS PaaS控制台访问 _bpm.portal应用中相关参数

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/worklist/3.png)](<3.png>)

### 已阅

显示当前用户的所有阅读过的传阅类、通知类任务。

### 已发起

显示由当前用户发起的所有流程实例。