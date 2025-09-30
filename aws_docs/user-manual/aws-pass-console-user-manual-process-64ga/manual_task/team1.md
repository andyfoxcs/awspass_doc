# 按群组 · AWS PaaS文档中心

## 按群组

### 方案32：群组/固定群组

一个或多个群组的人员合并。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa21.png)](<fa21.png>)

项 | 说明  
---|---  
群组 | 选择一个或多个团队群组  
  
### 方案33：群组/来自公式

使用@公式指定群组（通过@公式解析获取群组ID，多个逗号隔开）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa21-1.png)](<fa21-1.png>)

项 | 说明  
---|---  
公式 | 使用@公式指定群组（通过@公式解析获取群组ID，多个逗号隔开）  
  
### 方案34：群组/来自表单

获取表单上某个字段来指定账户（通过表单字段的值获取群组ID，多个逗号隔开）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa21-2.png)](<fa21-2.png>)

项 | 说明  
---|---  
字段名称 | 获取表单上某个字段来指定账户，仅支持主表单字段  
  
### 方案35：群组/来自变量

从当前流程变量来指定账户（通过流程变量的值获取群组ID，多个逗号隔开）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa21-3.png)](<fa21-3.png>)

项 | 说明  
---|---  
流程变量 | 从当前流程变量来指定账户（通过流程变量的值获取群组ID，多个逗号隔开）  
  
### 方案36：群组/动态小组

由规则动态指定小组。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa22.png)](<fa22.png>)

项 | 说明  
---|---  
群组ID | 一个团队群组ID，支持@公式  
  
### 方案37：群组/共享任务

该任务共享给一个特定的小组，该小组的用户可以通过认领完成该任务。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa23.png)](<fa23.png>)

项 | 说明  
---|---  
团队群组ID | 一个团队群组ID，支持@公式  
  
> 更多信息参见 [方案18：(角色/岗位)/共享任务](<orgrole.html#12>)

#### 延伸阅读

  * [组织服务>团队群组](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-org-vue/organization/team.html>)