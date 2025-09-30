# 内置的监控指标 | AWS SLA参考指南

## 内置的监控指标

### 计算资源

指标Id | 说明  
---|---  
Infrastructure.cpu | CPU使用率  
Infrastructure.maxJVMMemory | JVM总内存  
Infrastructure.maxPhysicalMemory | 总物理内存  
Infrastructure.freePhysicalMemory | 剩余可用物理内存  
  
### 应用容器服务

指标Id | 说明  
---|---  
AppContainer.error | 应用容器错误次数  
AppContainer.warn | 应用容器警告次数  
  
### 安全风险

指标Id | 说明  
---|---  
SecurityRisk.accountLocked | 账户冻结次数  
SecurityRisk.unauthorizedAccess | 越权访问次数  
  
### MVC框架服务

指标Id | 说明  
---|---  
MVCFramework.cmd | cmd总请求次数  
MVCFramework.webCmd | Web请求耗时  
MVCFramework.loginTime | 用户登录耗时  
MVCFramework.dataCmd | Data请求（JSON/XML）耗时  
MVCFramework.upfileCmd | 文件上传耗时  
MVCFramework.downfileCmd | 文件下载耗时  
MVCFramework.aslpExecute | ASLP执行耗时  
MVCFramework.activeUsers | 活跃用户数  
MVCFramework.activeSesssion | 有效会话数  
MVCFramework.concurrentRequests | 并发请求数  
  
### 流程引擎服务

指标Id | 说明  
---|---  
ProcessEngine.listener | 流程事件耗时  
ProcessEngine.listenerFailing | 流程事件错误次数  
ProcessEngine.createProcess | 创建流程实例耗时  
ProcessEngine.startProcess | 启动流程实例耗时  
ProcessEngine.createTask | 创建任务实例耗时  
ProcessEngine.humanPerformer | 流程路由方案耗时  
  
### 表单引擎服务

指标Id | 说明  
---|---  
FormEngine.listener | 表单事件耗时  
FormEngine.formBuilding | 表单构建耗时  
FormEngine.gridBuilding | 子表数据集构建耗时  
FormEngine.save | 保存数据耗时  
FormEngine.excelDownload | 下载Excel数据耗时  
FormEngine.excelUpload | 上传Excel数据耗时  
  
### 本地数据库服务

指标Id | 说明  
---|---  
LocalDatabase.sqlExecute | SQL执行耗时  
LocalDatabase.poolSize | 数据库连接池大小  
LocalDatabase.idleSize | 数据库连接池空闲连接数  
LocalDatabase.activeSize | 数据库连接池活动连接数  
LocalDatabase.dbFailing | SQL执行错误次数  
  
### CC连接服务

指标Id | 说明  
---|---  
CC.JDBC.sqlExecute | CC JDBC SQL执行耗时  
CC.JDBC.failing | CC JDBC SQL执行错误次数  
CC.HTTP.execute | CC HTTP处理时间  
CC.HTTP.failing | CC HTTP调用错误次数  
CC.SOAP.execute | CC SOAP处理时间  
CC.SOAP.failing | CC SOAP调用错误次数  
JMS.execute | JMS处理时间  
JMS.failing | JMS调用错误次数  
FTP.execute | FTP处理时间  
FTP.failing | FTP调用错误次数  
NC.execute | NativeCall处理时间  
NC.failing | NativeCall调用错误次数  
LDAP.execute | LDAP处理时间  
LDAP.failing | LDAP调用错误次数  
SR.failing | Service Regist调用错误次数  
PS.execute | Process Service处理时间  
PS.failing | Process Service调用错误次数  
  
### Job调度服务

指标Id | 说明  
---|---  
JOB.execute | JOB执行耗时  
JOB.failing | JOB错误次数