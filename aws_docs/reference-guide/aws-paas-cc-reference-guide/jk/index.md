# 监控 · AWS PaaS文档中心

# 监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控

当连接器和发布的服务开启`开启SLA服务质量监控`开关后，调用连接器相应方法和发布的服务时，会将监控信息统一显示在监控页签。 这里的数据会有延迟，因为系统会有5分钟切片时间。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/jk/sla1.png)](<sla1.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/jk/sla2.png)](<sla2.png>)

## 监控数量

显示相应监控数量，点击可按时间查看分布图。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/jk/sla3.png)](<sla3.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/jk/sla5.png)](<sla5.png>)

### 调用次数

开启`开启SLA服务质量监控`开关后，每**成功** 调用一次RDS、LDAP、Elasticsearch、Redis、MongoDB、HBase、FTP、HTTP、SOAP连接器相关方法和发布的HTTP API、Web Servcie服务，就记录一次调用次数。

### 出错次数

开启`开启SLA服务质量监控`开关后，每调用一次RDS、LDAP、Elasticsearch、Redis、MongoDB、HBase、FTP、HTTP、SOAP、ActiveMQ、RabbitMQ、RocketMQ、Kafka、Zookeeper连接器相关方法和发布的HTTP API、Web Servcie服务**出错** 时，就记录一次出错次数。

### 成功率

成功率 = 调用次数 / (调用次数 + 出错次数)

### 紧急事件次数

触发[SLA告警监控策略](<../service-center/sla.html>)，告警级别为紧急的事件次数。

### 重要事件次数

触发[SLA告警监控策略](<../service-center/sla.html>)，告警级别为重要的事件次数。

### 通知事件次数

触发[SLA告警监控策略](<../service-center/sla.html>)，告警级别为通知的事件次数。

### 限流次数

调用发布的HTTP API、Web Servcie服务时触发流控策略的次数。

### 访控次数

调用发布的HTTP API、Web Servcie服务时触发访控策略的次数。

### 熔断次数

调用发布的HTTP API、Web Servcie服务时触发流控策略中断路器的次数。

### 流入数据总量

调用HTTP连接器、SOAP连接器时，流入流量。

### 流出数据总量

调用发布的HTTP API、Web Servcie服务时，流出流量。

## 告警事件

触发SLA告警监控事件列表。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/jk/sla4.png)](<sla4.png>)

## 查看某对象监控数据

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/jk/sla6.gif)](<sla6.gif>)