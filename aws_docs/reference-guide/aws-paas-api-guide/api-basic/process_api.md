# 流程 · AWS PaaS文档中心

# 流程

AWS PaaS为开发者提供的流程引擎操作接口。

  * 流程实例查询/操作
  * 任务实例查询/操作
  * 任务委托/代理凭证

> 以下给出该类API的常用部分，但不完整，请以相关文档为准

## 流程实例查询/操作（Process Instance）

  * 创建和启动流程实例
    * 创建系统流程实例（短流程）
    * 创建人工流程实例（人工和系统混合流程）
    * 创建仅存储实例（DW）
    * 创建子流程实例
    * 启动流程实例
  * 控制流程实例
    * 终止
    * 取消
    * 挂起
    * 恢复
    * 重置
    * 复活
  * 操作流程变量和高级属性
    * 赋值变量
    * 读取变量
    * 设置实例关联的高级分类（IoX，Instance Of XXX）
    * 设置流程实例扩展参数值
  * 查询
    * 获得流程实例的审批记录
    * 获得流程实例的历史参与者账户列表
    * 获得一个流程实例对象
    * 流程实例高级查询（Query）

## 任务查询/操作（Task Instance）

  * 完成任务
    * 完成流程类任务
    * 完成EAI类外部任务
  * Ad-Hoc类
    * 跳到指定节点
    * 模拟后继路线
    * 创建任务
    * 删除任务
  * 控制任务实例
    * 取消
    * 挂起
    * 恢复
    * 收回
    * 回退
    * 认领
    * 委托
    * 已读
  * 操作实例属性
    * 设置任务实例关联的高级分类（IoX，Instance Of XXX）
    * 设置任务实例扩展参数值
    * 设置任务实例处理时限
  * 审核菜单
    * 暂存审核留言
    * 提交审核留言
    * 判断审核菜单
  * 参与者
    * 获得指定节点路由方案配置的参与者
    * 执行人、候选人
  * 查询
    * 获得任务实例
    * 查询历史路径的任务实例
    * 查询子任务实例
    * 任务实例高级查询（Query）

## 任务委托/代理凭证（Delegation Profile）

  * 创建委托凭证
  * 删除委托凭证
  * 修改委托凭证
  * 查询委托凭证

## API索引

API类型 | 说明  
---|---  
[HTTP(s)](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/http/>) | cmd=process.xxx(如`process.create`)   
cmd=task.xxx(如`task.complete`)  
cmd=delegation.xxx(如`delegation.create`)  
[SOAP](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/>) | service=`processApi`  
service=`taskApi`  
service=`delegationApi`  
[Java SDK](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/>) | SDK.getProcessAPI()  
SDK.getProcessQueryAPI()  
SDK.getTaskAPI()  
SDK.getTaskQueryAPI()  
SDK.getHistoryTaskQueryAPI()  
SDK.getDelegationAPI()