# AWS API与AWS ASLP的区别 · AWS PaaS文档中心

# AWS API与AWS ASLP的区别

AWS API是指本文档中介绍的三种API；AWS ASLP（Application Service Locator Protocol，应用服务访问定位协议）是AWS平台App PaaS容器为解决PaaS应用间互操作和安全访问控制定义的一套私有协议和实现，用于统一管控企业PaaS平台的应用服务接口，简化和标准化应用与应用间的互操作。

有关ASLP的开发，请[移步这里](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/aslp_scenes.html>)。

比较项 | AWS Web/SOAP API | AWS ASLP(开启HTTP服务)  
---|---|---  
定位 | 第三方系统与AWS平台间的集成，  
例如某外部系统访问AWS平台的引擎API | AWS应用与AWS应用间的互操作，  
例如移动端访问AWS服务端的应用接口  
服务提供 | AWS平台类API为主，例如流程引擎 | AWS应用类API为主，例如移动端下订单  
安全机制 | 基于访问凭证 ( access_key )和私钥   
( secret )的签名摘要验证，操作与AWS用户会话无关 | 基于AWS用户的Session，操作与AWS用户会话有关  
协议 | HTTP(s)/SOAP | HTTP(s)  
结果 | JSON/XML | JSON/XML/自定义  
适用于 | 异构系统间的集成 | 统一AWS用户身份的跨应用集成