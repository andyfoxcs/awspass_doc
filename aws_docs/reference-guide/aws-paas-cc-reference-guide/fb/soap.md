# Web Service - 发布SOAP服务 | AWS CC连接中心参考指南

# Web Service - 发布SOAP服务

## 发布

本节以发布AWS PaaS平台官方Web API为例，进行发布。 操作步骤：

  1. 登录AWS PaaS控制台，进入`连接服务 > 发布`
  2. 点击新建，在弹出窗口中选择应用名称为`AWS PaaS实例控制台`，服务类型选择`Web Service`
  3. 点击确定按钮，弹出侧边栏，填写相关信息，点击保存，完成发布

名称 | 便于识别的名称  
---|---  
实现 | 选择需要发布的类名  
服务ID | 默认为开发者代码类中注解的serviceName，修改后，保存升效  
访控策略 | 在[访控策略](<../service-center/access.html>)中维护，且策略类型为`用于发布`，并勾选`可用于Web Service`  
身份策略 | 在[身份策略](<../service-center/service_policy.html>)中维护，且类型为`SOAP`  
当身份策略处于关闭状态时，表示不再校验接口权限  
开启时，如果不配置策略则在调用时，可传AWS PaaS平台内存在的任意一个身份策略  
开启时，配置策略后，则仅支持当前配置的策略。  
流控策略 | 在[流控策略](<../service-center/flow.html>)中维护  
  
> 发布SOAP API示例及调用详细参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_soap_api.html>)。

## 日志

开启相关开关后，将记录相关日志。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/fb/web3.png)

### 审计日志

打开`记录访问请求到审计日志`开关后，当调用发布的SOAP API时，会记录日志，该日志存储在SYS_AUDIT_LOG表中，可在`日志`页签查看。日志信息最多显示1000个字符。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/fb/log.png)

### 文件日志

文件日志存储在AWS PaaS平台%AWS_HOME%/logs/目录下，默认每个文件日志最大为20M，最多存储20个文件，超出将自动清除最早日期文件。 log文件个数及单文件最大值可在%AWS_HOME%/bin/conf/aws-log4j.xml文件中配置。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log1.png)

## 监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`开启SLA服务质量监控`后，当调用发布的SOAP API时，将自动对`调用次数、出错次数、限流次数、访控次数、熔断次数、流出流量、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/fb/web5.png)

## 上线下线

  1. 当Web Service服务绑定的访控策略发生变化时，需要重新上线，才升效
  2. 下线的API， 不允许调用。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/fb/online.png)

## 应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>