# 前言 · AWS PaaS文档中心

# AWS PaaS API参考指南

欢迎阅读这个文档！

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/api.gif)](<api.gif>)

AWS PaaS向所有开发者开放编程接口。基于这些API接口，开发者可以为AWS PaaS平台和上层的AWS商业应用进行功能扩展，通过程序的组合完成复杂的自动化任务。

**AWS PaaS支持的API协议类型**

  * HTTP(s) API（基于访问凭证/access_key和私钥/secret的URL签名访问）
  * RESTful API（基于访问凭证/access_key和私钥/secret的URL签名访问）
  * SOAP API（基于用户名/密码和x509证书身份的SOAP访问）
  * Java SDK API（原生接口，开放给本地开发者）

这些API能够支持不同场景和不同编程语言的调用需求，包括业务逻辑处理、Web应用程序后端编程、移动端应用编程等。

> **AWS PaaS同时也是一个强大的企业服务集成平台，本文仅涉及由AWS PaaS对外提供的编程接口，不涉足如何调用第三方系统的集成服务。若了解 AWS PaaS如何集成三方服务或应用，请参阅流程服务编排、AWS CC组件等文档**

本文档适用于AWS PaaS应用开发者和第三方应用开发者阅读。

## 声明

  * `炎黄盈动`、`Actionsoft`、`AWS`、`AWS CC`、`CoE`是北京炎黄盈动科技发展有限责任公司在中国的注册商标或产品字号
  * 本文档出现的一些商业产品名称、公司商号版权归相关拥有人，除非另行说明，本文档范例中涉及的公司、组织、产品、人物或事件均属虚构，并无意联系或暗示任何真实的公司、组织、产品、人物或事件