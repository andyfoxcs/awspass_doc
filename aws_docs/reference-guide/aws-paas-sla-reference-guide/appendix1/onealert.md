# OneAlert监控集成 | AWS SLA参考指南

# OneAlert监控集成

OneAlert是北京蓝海讯通提供的一站式告警管理平台。

AWS PaaS提供了一个工具附加应用，可以将AWS SLA的告警实时接入到OneAlert中，实现企业内各种告警的统一展现、统一通知和统一处理。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/1.png)

**集成配置步骤**

  * 在OneAlert创建“REST API”应用，并获得自动生成的“应用Key”

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/2.png)

  * 登录AWS的控制台，在“工具附加”找到“OneAlert监控集成”，配置对应的“应用 Key”选项

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/3.png)

  * 该应用处于启动时，将自动拦截SLA的告警并发往OneAlert；该应用处于暂停或卸载时集成被停止

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/4.png)