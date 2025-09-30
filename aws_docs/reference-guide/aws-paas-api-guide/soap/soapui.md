# 使用SoapUI工具 · AWS PaaS文档中心

# 使用SoapUI工具

[SoapUI](<http://baike.baidu.com/link?url=sG1MiNpKIPbtkF4p6ooOOCrtHqQ7wC6vBASmgudh7rUAUEyF2pDjpJBTYdh3XPuPvnmvA8g4OEldCcPEmuJ--K>)是一个开源测试工具，希望快速熟悉SOAP API的开发者，也可以使用这个客户端测试每个API。

## 环境准备

  * [SoapUI工具](<http://www.soapui.org/downloads/soapui/open-source.html>)

## 场景

调用`appApi`服务的`isInstalled`方法判断AWS PaaS是否安装了某个应用。

## 步骤

### 1.在AWS PaaS控制台创建身份策略

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/5.png)](<5.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/4.png)](<4.png>)

### 2.在AWS PaaS控制台获取WSDL地址

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/7.png)](<7.png>)

### 3.创建soapUI工程,File > new soapUI Project

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/soapui2.png)](<soapui2.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/soapui1.png)](<soapui1.png>)

### 4.配置参数及认证用户名密码

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/soapui3.png)](<soapui3.png>)

>   1. AWS PaaS出厂提供的官方SOAP API，默认提供了密码加密的认证方式。[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/8.png)](<8.png>) [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/9.png)](<9.png>)
>   2. 发布的SOAP API，没有配置身份策略时，在调用该SOAP API时，可以使用AWS PaaS平台存在的任何一个身份策略秘钥信息 [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/10.png)](<10.png>)
> 

### 5.运行查看结果

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/soapui4.png)](<soapui4.png>)

更详细的soapUI配置请参见<http://www.soapui.org/soap-and-wsdl/authenticating-soap-requests.html>

## SOAP API客户端身份认证安全机制

访控策略可为SOAP API提供几种安全机制验证方式。

> 有关Web Services Security UsernameToken详细介绍可参见<https://www.oasis-open.org/committees/download.php/13392/wss-v1.1-spec-pr-UsernameTokenProfile-01.htm>

下面将详细介绍这几种安全机制验证方式对应SoapUI工具里的配置。

以下介绍当访控策略配置发生变化，或发布的SOAP API绑定的访控策略改变时，SOAP API需要重新上下线升效。 [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/12.png)](<12.png>)

### 1.密码明文

**AWS PaaS平台访控策略配置**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/y1.png)](<y1.png>)

**SoapUI配置**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/su1.png)](<su1.png>)

### 2.密码加密

**AWS PaaS平台访控策略配置**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/y2.png)](<y2.png>)

**SoapUI配置**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/su2.png)](<su2.png>)

### 3.密码加密+时间戳

**AWS PaaS平台访控策略配置**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/y3.png)](<y3.png>)

**SoapUI配置**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/su3.png)](<su3.png>)

### 4.当发布的SOAP API未绑定访控策略和身份策略

此种配置，从安全解度非常不建意使用。

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/y4.png)](<y4.png>)

**SoapUI配置**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/su0.png)](<su0.png>)