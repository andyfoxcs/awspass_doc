# 连接器 · AWS PaaS文档中心

# 连接器

连接器用于配置HTTP DS要操作的API接口。API接口的根路径来源于连接中已配置的[HTTP连接Web服务](<../tech-adapters/http.html>)。

项 | 说明  
---|---  
名称 | 简要名称  
描述 | 简要描述信息  
连接器 | 可选择当前应用及关联应用中已配置的[HTTP 连接Web 服务](<../tech-adapters/http.html>)  
请求方法 | 该HTTP DS 要操作的Web API的请求方法。支持POST、GET、PUT、DELETE。  
在实际配置中由接口提供方给出  
URL地址 | URL地址根路径来源于所选连接器的URL地址，后面可输入相对路径。   
此种设计有利于当多个HTTP DS，根路径相同时，可以只配置一个连接器，通过后面URL地址区分不同的接口  
请求类型 | 仅在请求方法为POST和PUT时显示，支持application/json 和 application/x-www-form-urlencoded两种  
在实际配置中需由接口提供方给出  
受管信息 | 参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>)  
  
[![](http-lj1.png)](<http-lj1.png>)

> HTTP DS引擎在运行时，可自动继承执行连接器中配置的`验证身份、连接超时、请求超时、最大并发数、请求参数、日志、监控`相关配置。 [![](http18.png)](<http18.png>)