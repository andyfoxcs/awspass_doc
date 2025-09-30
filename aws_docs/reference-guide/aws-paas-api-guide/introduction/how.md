# 如何使用API? · AWS PaaS文档中心

# 如何使用API?

AWS PaaS的API支持四种技术栈的编程模型

  * Web API
  * RESTful API
  * SOAP API
  * Java SDK API

## Web API

适用于外部系统开发者。这类API由开发者发起基于HTTP的请求，返回JSON或XML格式的结果。在调用该类API之前，开发者需要向管理员申请API密钥，该密钥由AWS CC的`秘钥身份`进行管理和分配。秘钥包括访问凭证 ( access_key ) 和 私钥 ( secret，需要被妥善保管，请勿外传或编译到您的源码中泄露)。

  * [签名URL，跨语言调用](<../http/signing.html>)
  * [使用Postman工具](<../http/postman.html>)

## RESTful API

RESTful API 就是REST风格的API。RESTful 是典型的基于HTTP的协议。

  * [使用Postman工具](<../restful/postman.html>)

## SOAP API

又称为WebService，适用于传统企业级应用和SOA架构应用间的接口互操作。 AWS PaaS的WebService注册、秘钥身份、策略配置和服务发布管理由AWS CC提供。

  * [使用SoapUI工具](<../soap/soapui.html>)
  * [使用CXF客户端](<../soap/cxf.html>)
  * [使用JDK客户端](<../soap/java_client.html>)

## Java SDK API

这类API由Java语言直接编写，也是HTTP/SOAP API的后端实现，适用于AWS PaaS本地开发者调用。

  * [在PaaS实例内采用原生Java调用](<../native/java_doc.html>)

AWS PaaS的应用开发环境中已直接提供这些API接口，开发者可以将程序编译的jar包文件存放到apps/install/%appId%/lib下，即可被PaaS容器自动加载和识别。