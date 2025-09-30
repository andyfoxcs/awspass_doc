# 按单位 · AWS PaaS文档中心

## 按单位

### 方案27：单位/固定单位

一个或多个单位的人员合并。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa19.png)](<fa19.png>)

项 | 说明  
---|---  
单位 | ．实体单位  
．虚拟单位  
组织ID | 对应单位的ID，支持@公式  
支持兼任 | 勾选后，支持兼任的人员  
  
### 方案28：单位/来自公式

使用@公式指定单位（通过@公式解析获取单位ID）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa19-1.png)](<fa19-1.png>)

项 | 说明  
---|---  
单位 | ．实体单位  
．虚拟单位  
公式 | 使用@公式指定单位  
支持兼任 | 勾选后，支持兼任的人员  
  
### 方案29：单位/来自表单

获取表单上某个字段来指定单位（通过表单字段的值获取单位ID）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa19-2.png)](<fa19-2.png>)

项 | 说明  
---|---  
单位 | ．实体单位  
．虚拟单位  
字段名称 | 获取表单上某个字段来指定单位，仅支持主表单字段  
支持兼任 | 勾选后，支持兼任的人员  
  
### 方案30：单位/来自变量

从当前流程变量来指定单位（通过流程变量的值获取单位ID）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa19-3.png)](<fa19-3.png>)

项 | 说明  
---|---  
单位 | ．实体单位  
．虚拟单位  
流程变量 | 从当前流程变量来指定单位  
支持兼任 | 勾选后，支持兼任的人员  
  
### 方案31：单位/动态单位

由规则动态指定单位。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa20.png)](<fa20.png>)

项 | 说明  
---|---  
单位类型 | ．实体单位  
．虚拟单位  
单位ID | 对应单位的ID，支持@公式  
支持兼任 | 勾选后，支持兼任的人员