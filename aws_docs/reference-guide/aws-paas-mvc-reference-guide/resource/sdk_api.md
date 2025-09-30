# SDK API · AWS PaaS文档中心

## SDK API

AWS PaaS作为App运行的容器环境和资源平台，为App开发者提供了丰富的API，这些API可以直接在你的Java程序中使用。

[![SDK结构](https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/resource/sdk.png)](<sdk.png>)

对于API详细说明及用法，参见**aws-api-doc**(一个Java API Doc)。

### MVC编程常用API

类 | 说明  
---|---  
SDK | SDK API的总入口  
ActionWeb | Web(View)请求处理的父类  
ModelBean | 业务实体对象父类  
DaoObject | DAO对象父类  
ResponseObject | 返回JSON、XML结构化数据，如操作状态、业务数据  
UserContext | 用户会话，获得用户会话串、登录IP、语言、设备类型、用户组织等  
AppAPI | 多语言处理、跨应用的ASLP调用、应用日志  
ORGAPI | 访问组织结构相关接口  
PermAPI | 访问AWS权限相关接口  
PortalAPI | 访问或构建门户应用相关接口  
RuleAPI | 规则处理接口  
DCAPI | 文件处理接口  
  
### 平台系统常用API

类 | 说明  
---|---  
PlatformAPI | 查询平台及服务状态接口  
ConfAPI | 查询平台常用配置参数接口  
SLAAPI | 监控告警接口  
  
### BPM引擎常用API

类 | 说明  
---|---  
ProcessAPI | 流程实例控制接口  
TaskAPI | 任务实例控制接口  
ProcessExecuteQuery | 引擎执行结果查询接口  
ProcessQueryAPI | 流程实例查询接口  
TaskQueryAPI | 任务查询接口  
HistoryTaskQueryAPI | 历史任务查询接口  
DelegationAPI | 任务委托/代理接口  
RepositoryAPI | 模型资源库访问接口  
BOAPI | BO操作接口  
BOQueryAPI | BO查询接口  
  
### 监听器常见接口（事件编程）

类 | 说明  
---|---  
ValueListener | 取值类监听器父类  
ExecuteListener | 执行类监听器父类  
InterruptListener | 中断类监听器父类  
  
### 注意事项

  * 不推荐直接调用**aws-api-doc** 未提供的接口方法
  * SDK API适用于在AWS Server端执行，不能用于Web层开发。如果你在Web层使用了不符合AWS MVC框架的开发模式，可以通过AWS CC发布Server API或封装ASLP服务来访问AWS Server端操作