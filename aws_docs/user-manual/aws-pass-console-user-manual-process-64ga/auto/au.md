# 修改新增数据 · AWS PaaS文档中心

## 修改/新增数据

修改新增数据就是当触发类型和触发条件满足时，按照配置过滤条件进行目标表数据修改，当过滤条件查询不到相应数据时，进行新增动作。 新增支持同步创建新实例或在已有实例添加。

该动作主要用于对子表数据的修改、新增。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/au1.gif)](<au1.gif>)

### 应用举例

员工职称、职业资格证书变动或新增后同步更新员工档案库。

#### 配置触发类型

配置员工信息变更流程，在审批通过后，同步修改员工档案表 （因为员工职称可以有多个，所以为子表数据，在变更时，如果职称已存在，且有变动（如有效期有变动）则修改原数据; 如果职称原来不存在，则新增加到档案库）。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/au2.png)](<au2.png>)  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/au2.1.png)](<au2.1.png>)  
  
#### 配置修改/数增的数据

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/au3.png)](<au3.png>)  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/au3.1.png)](<au3.1.png>)  
  
### 效果预览

#### 变更前员工档案信息

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/au4.png)](<au4.png>)

#### 要变更的信息

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/au5.png)](<au5.png>)

#### 变更档案库信息

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/au6.png)](<au6.png>)