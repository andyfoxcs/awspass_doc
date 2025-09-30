# 变量命名词汇 · AWS PaaS文档中心

## 变量命名词汇表

为规范App开发者对专业变量的命名和识别，在这里给出一个词汇表参考。

### 设计期

项 | 命名参考  
---|---  
存储模型ID | boDefId  
表单模型ID | formDefId  
表单子表模型ID | formItemDefId  
流程模型ID | processDefId  
节点模型ID | 通用：activityDefId  
特定：userTaskDefId、serviceTaskDefId..  
报表模型ID | reportDefId  
DW模型ID | dwDefId  
各种Context对象 | 如UserContext、TaskBehaviorContext...  
  
建议：单独出现时命名变量为ctx或context，同时出现多个不同类型的Context时，使用userContext、taskContext区分  
登录账户名 | uid、uids（多个），对应ORGUSER的USERID字段  
单位ID | companyId  
部门ID | departmentId  
角色ID | roleId  
小组ID | teamId  
小组成员ID | teamMemberId  
  
### 运行期

项 | 命名参考  
---|---  
流程实例ID | 建议processInstId，可以使用processInstanceId  
流程实例对象 | 建议processInst，可以使用processInstance  
任务实例ID | 建议taskInstId，可以使用taskId、taskInstanceId  
任务实例对象 | 通用：建议taskInst，可以使用task、taskInstance  
特定：建议historyTaskInst，可以使用historyTask、historyTaskInstance  
BO表ID | boId  
BO表与流程实例绑定 | 通用：bindId  
特定：纯流程驱动场景下，也可使用processInstId