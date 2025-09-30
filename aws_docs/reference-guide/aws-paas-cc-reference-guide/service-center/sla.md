# SLA Alarm - SLA告警监控 | AWS CC连接中心参考指南

# SLA Alarm - SLA告警监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控

当CC连接器、发布的服务API被调用时，满足相应规则后，出发告警并给相关人员发送通知。如当某API服务连续5分钟内调用次数大于10次时，触发告警，并给管理员发送短信、邮件通知。

## 监控指标

### 执行耗时

调用连接器API方法和发布的服务时，执行的耗时时长。

支持RDS、LDAP、Elasticsearch、Redis、MongoDB、HBase、FTP、HTTP、SOAP连接器和发布的HTTP API、Web Servcie服务。

### 调用次数

调用连接器API方法和发布的服务的次数。

支持RDS、LDAP、Elasticsearch、Redis、MongoDB、HBase、FTP、HTTP、SOAP连接器和发布的HTTP API、Web Servcie服务。

### 出错次数

调用连接器API方法和发布的服务时出错次数。

支持RDS、LDAP、Elasticsearch、Redis、MongoDB、HBase、FTP、HTTP、SOAP、ActiveMQ、RabbitMQ、RocketMQ、Kafka、Zookeeper连接器和发布的HTTP API、Web Servcie服务。

### 流入流量

调用HTTP连接器、SOAP连接器时，流入流量。

支持HTTP、SOAP连接器。

### 流出流量

调用发布的API服务时，流出的流量。

支持发布的HTTP API、Web Servcie服务。

### 限流次数

触发[流控策略](<flow.html>)的次数。

支持发布的HTTP API、Web Servcie服务。

### 访控次数

触发[访控策略](<access.html>)的次数。

支持发布的HTTP API、Web Servcie服务。

### 熔断次数

触发流控策略中断路器的次数。

支持发布的HTTP API、Web Servcie服务。

## 监控范围

不同监控指标，可选择不同监控范围。详见上方各指标说明。

  1. 监控范围，为多个时，每个监控对象的监控数据为独立计算，不会在多个监控对象间累计
  2. 列表中灰色不可选择的对象，表示当前对象未开启SLA监控

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/4.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/5.png)

## 监控规则

配置监控规则和告警级别、告警范围。

### 时段

  1. 指标为调用次数、出错次数、限流次数、访控次数、熔断次数时，即时，表示只要触发相关指标则告警。 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/6.png)

  2. 指标为调用次数、出错次数、限流次数、访控次数、熔断次数时，5分钟/1小时/1天，表示间隔相应时间段且连续触发次数大于等于设置的连续次数后，才告警。 次数累计规则：只要触发相应指标则会一直累计，只有当AWS PaaS服务重启后，才会清零，重新开始计算。 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/7.png)

  3. 指标为执行耗时、流入流量、流出流量时，即时，表示触发时，采集到的值满足相应条件时则告警。 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/9.png)

  4. 指标为执行耗时、流入流量、流出流量时，，5分钟/1小时/1天，表示间隔相应时间段且连续每次触发时采集到的值满足设置的值，并且采集值连续满足条件下触发次数大于等于设置的连续次数，则告警。 次数累计规则：当触发时，采集值满足条件时，则次数器累计加1，当不满足条件时，则次数器清零。 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/10.png)

>   1. 指标为执行耗时时，采集值单位为毫秒ms
>   2. 指标为流入流量、流出流量时，采集值单位为KB
> 

### 告警级别

告警级别，分为三种：通知、重要、紧急。触发相应告警后，在监控页签可查看相应级别的告警数据。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/11.png)

### 通知

触发相应告警时，可给相关人员发送短信、邮件、微信、钉钉、飞书通知(需要安装对应通知应用)。通知列表可在[系统通知列表](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/appendix/scenes.html>)中进行配置。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/12.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/13.png)

#### 短信

短信通知模板配置参见<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.sms/model/sla.html>

#### 邮件

邮件通知模板配置参见<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/model/sla.html>

#### 微信

当正常安装配置[`](<https://docs.awspaas.com/reference-guide/aws-paas-wechat-reference-guide/appendix/scenes.html>)企业微信集成(com.actionsoft.apps.wechat)`应用后，且在系统通知列表配置了企业微信账号时，当触发告警时，可发送企业微信通知。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/wx.png)

#### 钉钉

当正常安装配置[`钉钉集成(com.actionsoft.apps.dingding)`](<https://docs.awspaas.com/apps/com.actionsoft.apps.dingding/index.html>)应用后，且在系统通知列表配置了钉钉账号时，当触发告警时，可发送钉钉通知。 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/dd.png)

#### 飞书

当正常安装配置[`飞书集成(com.actionsoft.apps.feishu.open)`](<https://docs.awspaas.com/apps/com.actionsoft.apps.feishu.open/index.html>)应用后，且在系统通知列表配置了飞书账号时，当触发告警时，可发送飞书通知。

## 应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>

## 上线下线

在策略列表，可以切换SLA告警监控的状态。处于上线状态的策略，在HTTP和SOAP服务中引擎可以正常应用该策略，处于下线状态的策略，引擎将自动不执行该策略。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/s1.png)

## 删除

在策略列表，光标移至需要删除的模型上，点击右侧删除按钮，按照提示进行删除。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/s2.png)