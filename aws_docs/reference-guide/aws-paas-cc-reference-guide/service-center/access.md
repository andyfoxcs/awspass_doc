# Access Control - 访控策略 | AWS CC连接中心参考指南

# Access Control - 访控策略

访控策略（访问控制）可以允许或禁止访问者IP，对访问资源数据提供细粒度的权限保护。访控策略和发布的API是相互独立的，只有将API绑定访控策略后，访问控制策略才对该API生效。如果暂停访控策略，随之相关的API也将暂停访问控制。

访问范围对访问资源数据提供细粒度的权限保护，默认只提供“自定义”模式，由服务提供者通过读取自定义内容（如JSON）自定义实现。平台预制了对单位、部门、角色、人、群组、流程、应用的细粒度权限，可在封装API服务时通过注解声明，CC API为服务开发者提供了读取该访控配置的相关API。

## 配置

项 | 说明  
---|---  
名称 | 策略服务名称  
策略类型 | 用于发布，该访控策略用于[API服务发布](<../fb>)   
用于连接器，该访控策略用于[SOAP连接器](<../tech-adapters>)  
  
## 连接器类型

### Web Service策略

验证方法，支持用户名密码、HTTP两种。HTTP表示HTTP Basic验证，比如SAP的对接默认是这种方式。

身份，设置身份策略，列表数据来源于[身份策略](<../service-center/service_policy.html>)

### 出站安全

密码加密，请求消息中密码是否是加密的

时间戳，是否添加时间戳，指定消息过期时间

有效期，指定消息的有效期

## 发布类型

### Web Service策略

当勾选`可用于Web Service`时显示。如果不勾选`可用于Web Service`，则该策略仅可用于发布HTTP API和发布Restful API。 当勾选`可用于Web Service`后，则该策略可同时用于发布HTTP API、Restful API和Web Servcie API。

验证方式，只支持用户名密码验证方式

### 入站安全

密码加密，请求消息中密码是否是加密的 时间戳，是否添加时间戳，指定消息过期时间

> 相关配置与SOAPUI工具里的对应参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/soapui.html#soap>)。

### IP策略

控制调用者IP。支持IP白名单、IP黑名单 ，多个IP用半角英文逗号隔开。

### 访问范围

默认只提供“自定义”模式，仅当策略被已发布的服务绑定后，由绑定服务的注解声明类型，可提供单位、部门、角色、人、群组、流程、应用的细粒度权限。

### API绑定列表

已绑定该策略的API服务列表。

有关服务的发布参见[发布](<../fb>)章节。

## 应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>

## 上线下线

在策略列表，可以切换访控策略的状态。处于上线状态的策略，在HTTP和SOAP服务中引擎可以正常应用该策略限制，处于下线状态的策略，引擎将自动不执行该策略。更新该策略状态后，必须重新上下线相关绑定该策略的服务。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/f1.png)

## 删除

在策略列表，光标移至需要删除的模型上，点击右侧删除按钮，按照提示进行删除。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/f2.png)