# 日志架构 · AWS PaaS文档中心

# 日志架构

AWS的日志架构在设计上要求满足开发者、运维管理员和企业安全审计人员。

其目标主要为AWS PaaS内部的原生应用提供日志服务，不包括硬件、操作系统、数据库以及与AWS不相干的日志管理，因此，您不能将AWS LOG日志作为完整的日志管理系统进行使用。

  * 程序开发
  * 场景操作审计
  * 服务质量监控

在使用层、配置层和持久层都留有API接口，适应企业客户对日志运维和安全审计的管理要求。

> 可以将AWS产生的日志和告警与专业日志服务厂商的产品进行集成，本文档将详细介绍每类日志文件的位置、结构。如配置基于Linux的`rsyslog`或`syslog-ng`实现日志数据的统一采集，使用OneAlert实现AWS SLA的告警集成 <https://blog.awspaas.com/app-onealert/>

[![](https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/architecture/log-architecture.png)](<log-architecture.png>)

## 程序开发

AWS日志架构采用了流行的slf4j日志接口标准，屏蔽了对特定日志系统的依赖。为开发者封装了比传统日志系统（如log4j）更简单的编程模式，包括程序的debug、错误日志记录。

**例如**
    
    
    //应用`com.abc.apps.xyz`输出一个`hi`日志
    SDK.getLogAPI().getLogger(this.getClass()).debug("hi");
    

> 点击这里阅读API接口 <https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/appendix/api.html>

## 场景操作审计

这类日志主要满足运维人员和安全审计对系统运行状况的检查，系统内置了[`专项审计`、`控制台`和`客户端`三个大类和十余项小类审计场景](<https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/audit_log>)，为这些专项审计记录提供了查询界面。

通常对安全保密要求较高的系统应用访问、敏感操作均需要被日志系统记录。AWS的日志架构为这里用户提供了灵活的[自定义配置](<https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/appendix/audit_config.html>)，无需编写任何代码即可对AWS平台内任何的场景操作进行拦截记录。

## 服务质量监控

无论AWS平台服务运行在私有部署环境还是云中，企业都依赖一种可靠的7X24小时服务监控系统，对应用服务质量进行评估和改进，并期望在第一时间获得告警和应对措施。

AWS SLA是AWS PaaS针对高可用性用户提供的一套服务质量监控高级组件，目的在于通过对PaaS资源/服务指标的连续监控和分析，帮助客户的技术团队及时发现服务质量隐患，并为解决或改善问题提供诊断线索。

详细介绍请访问 <https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/index.html>