# 内置的告警规则 | AWS SLA参考指南

## 内置的告警规则

告警规则Id | 告警标题 | 触发规则  
---|---|---  
CPU Usage Is Too High | CPU使用率过高 | 连续2次高于90%  
Low Physical Memory | 物理可用内存过低 | 连续2次低于20%  
App Container Error | 应用容器出错 | 发生即触发  
App Container Warn | 应用容器警告 | 发生即触发  
Unauthorized Access | 发生越权访问 | 发生即触发  
Slow Web Response | 有延迟感的用户响应 | 大于10秒  
MVC High Load | MVC负载过高 | 连续2次大于500并发  
Slow ASLP Service | 有延迟感的ASLP服务 | 大于10秒  
Process Listener Is Very Slow | 流程事件业务处理太慢 | 大于5秒  
Process Listener Error | 流程事件业务处理出错 | 发生即触发  
Process HumanPerformer Is Very Slow | 流程路由方案处理太慢 | 大于5秒  
Form Listener Is Very Slow | 表单事件业务处理太慢 | 大于5秒  
Form Listener Error | 表单事件业务处理出错 | 发生即触发  
Form Save Is Very Slow | 表单保存数据处理太慢 | 大于5秒  
(LOCAL DB)Slow SQL | (本地数据库)慢SQL | 大于5秒  
(LOCAL DB)Error | (本地数据库)SQL执行出错 | 发生即触发  
JOB Slow Exec | JOB执行慢 | 大于15秒  
JOB Error | JOB出错 | 发生即触发  
(CC.RDS)Slow SQL | (CC数据库)慢SQL | 大于5秒  
(CC.RDS)Error | (CC数据库)SQL执行出错 | 发生即触发  
(CC.HTTP)Slow Connection | (CC.HTTP)慢连接 | 大于5秒  
(CC.HTTP)Error | (CC.HTTP)出错 | 发生即触发  
(CC.SOAP)Slow Connection | (CC.SOAP)慢连接 | 大于5秒  
(CC.SOAP)Error | (CC.SOAP)出错 | 发生即触发