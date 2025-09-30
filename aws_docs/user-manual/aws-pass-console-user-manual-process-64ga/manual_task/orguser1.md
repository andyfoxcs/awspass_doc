# 按账户 · AWS PaaS文档中心

## 按账户

### 方案1：账户/任意指定

由上个任务的办理者指定该节点的执行人

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/luyou1.png)](<luyou1.png>)

项 | 说明  
---|---  
地址簿选项 | 打开后，可通过[地址簿](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/dzb.html>)的高级选项配置人员选择范围  
分类方式 | ．组织  
．岗位  
．角色  
．群组  
显示兼任 | 参见[地址簿](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/dzb.html>)  
过滤范围 | 参见[地址簿](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/dzb.html>)  
单位列表 | 参见[地址簿](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/dzb.html>)  
数据源接口 | 参见[地址簿](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/dzb.html>)  
过滤事件 | 参见[地址簿](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/dzb.html>)  
  
>   * 数据源过滤示例参数[UI-地址簿](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/dzb.html>)
> 
>   * 除方案1以外的其他方案没找到办理人时，可以由上一任务的办理人手动从地址簿中任意指定人，在AWS Portal门户中有参数控制 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/luyou1-1.png)](<luyou1-1.png>)
> 
>   * 在AWS Portal门户中有参数控制隐藏不需要使用的路由方案 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/luyou1-2.png)](<luyou1-2.png>)
> 

### 方案2：账户/固定账户

执行人来自特定的账户 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/luyou2.png)](<luyou2.png>)

项 | 说明  
---|---  
固定参与者 | 执行人来自特定的账户，多个用空格隔开  
  
> 输入值是@公式后，地址簿禁用

### 方案3：账户/来自公式

使用@公式指定账户（通过@公式解析获取账户UID，多个空格隔开）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/luyou3.png)](<luyou3.png>)

项 | 说明  
---|---  
公式 | 支持@公式及手动输入账户UID，多个用空格隔开  
  
### 方案4：账户/来自表单

获取表单上某个字段来指定账户（通过表单字段的值获取账户UID，多个空格隔开）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/luyou4.png)](<luyou4.png>)

项 | 说明  
---|---  
字段名称 | 仅支持主表单上的字段，通过表单字段的值获取账户UID，多个用空格隔开  
  
### 方案5：账户/来自变量

从当前流程变量来指定账户（通过流程变量的值获取账户UID，多个空格隔开）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/luyou5.png)](<luyou5.png>)

项 | 说明  
---|---  
流程变量 | 从当前流程变量来指定账户（通过流程变量的值获取账户UID，多个空格隔开）  
  
### 方案6：账户/与上个任务办理人相关

账户与上个任务的办理人相关。例如获取上个任务的办理人，或者该办理人的部门主管。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa3.png)](<fa3.png>)

项 | 说明  
---|---  
上个任务的 | ．办理者  
．办理者的部门主管  
．办理者的上级部门主管  
该部门无主管是否继续向上找(仅向上找一次) | 勾选后当该部门无主管时自动向上寻找一级  
支持兼任 | 勾选后，支持兼任的部门主管  
  
### 方案7：账户/与指定任务办理人相关

账户与指定任务的办理人相关。例如获取指定任务的办理人，或者该办理人的部门主管。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa4.png)](<fa4.png>)

项 | 说明  
---|---  
任务ID | 支持@公式,一个任务ID  
该任务的 | ．办理者  
．办理者的部门主管  
．办理者的上级部门主管  
该部门无主管是否继续向上找(仅向上找一次) | 勾选后当该部门无主管时自动向上寻找一级  
支持兼任 | 勾选后，支持兼任的部门主管  
  
### 方案8：账户/与指定节点办理人相关

账户与指定节点的办理人相关，如果在该流程实例中，这个节点已有多人执行，给出相关所有人员。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa5.png)](<fa5.png>)

项 | 说明  
---|---  
节点ID | 选择已办理的节点  
  
### 方案9：账户/与流程申请人相关

账户与流程的创建人相关。例如获取流程创建人的部门主管账户。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa6.png)](<fa6.png>)

项 | 说明  
---|---  
该流程的 | ．流程申请人  
．上个任务的办理者的部门主管  
．上个任务的办理者的上级部门主管  
．流程申请人的部门主管   
．流程申请人的上级部门主管  
该部门无主管是否继续向上找(仅向上找一次) | 勾选后当该部门无主管时自动向上寻找一级  
支持兼任 | 勾选后，支持兼任的部门主管  
  
### 方案：与业务汇报线相关

账户与业务汇报线相关。例如获取指定业务线的被汇报人账户

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa6-1.png)](<fa6-1.png>)

项 | 说明  
---|---  
业务线 | 详见应用[多业务线汇报规则](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mreporter/install/README.html>)  
  
> 方案6,7,9中选项为`办理者的部门主管`时，如果前一任务办理人设置了[直属上级](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-org-vue/organization/creat_people.html>)则直属上级相当于部门主管。