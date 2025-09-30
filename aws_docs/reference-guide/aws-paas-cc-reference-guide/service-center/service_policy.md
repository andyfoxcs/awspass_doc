# Secret Identity - 身份策略(6.4.2) | AWS CC连接中心参考指南

# Secret Identity - 身份策略 (6.4.2)

为HTTP和SOAP提供认证秘钥信息。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/1.gif)

## 配置

项 | 说明  
---|---  
名称 | 服务名称，用于开发人员区分服务  
类型 | HTTP， 用于发布[HTTP API](<../fb/http.html>)和[Restful API](<../fb/restful_api_-_restful.html>)服务时身份验证  
SOAP，用于发布[Web Service](<../fb/soap.html>)服务时身份验证  
access_key(访问凭证) | 任意字符串，支技@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
secret(私钥) | 任意字符串，支技@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
描述 | 描述信息  
  
## API绑定列表

当该策略被已发布的HTTP或SOAP服务绑定后，此处可展示相应API列表。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/sf.png)

## 应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>

## 上线下线

在策略列表，可以切换身份策略的状态。处于上线状态的策略，在HTTP和SOAP服务中引擎可以正常应用该策略，处于下线状态的策略，引擎将自动不执行该策略。 如果发布的HTTP 和SOAP API服务绑定的身份策略，全部处于下线状态，则调用API服务时，可传入AWS PaaS平台存在的任意一个身份信息均可调用成功。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/3.gif)

## 删除

在策略列表，光标移至需要删除的模型上，点击右侧删除按钮，按照提示进行删除。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/1.png)