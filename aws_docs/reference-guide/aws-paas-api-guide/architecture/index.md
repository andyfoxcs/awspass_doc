# API架构 · AWS PaaS文档中心

# API架构

AWS 对每次API请求都进行一次完整的安全验证，验证处理过程与开发者选择的API技术协议有关（如选择HTTP或SOAP）。下图是一个抽象的API架构图：

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/architecture/1.png)](<1.png>)

**请求处理过程：**

  1. 发起请求
  2. 因安全或请求非法被拒绝
  3. 调用AWS PaaS的本地接口封装
  4. 将处理结果以JSON/XML文档返回

## API客户端安全

API客户端是指调用API的请求方程序。

项 | Web API | RESTful API | SOAP API | Java SDK  
---|---|---|---|---  
鉴权 | access_key/secret | access_key/secret | 用户名/口令 | 原生本地调用  
保护 | 私钥串建议加密存放 | 私钥串建议加密存放 | 口令串建议加密存放 | 无  
  
>   1. 开发者应妥善保管AWS PaaS提供的私钥/口令字符串，建议在调用端加密后存至配置文件，源码中禁止含有私钥/口令信息
>   2. 对于测试、生产环境，应设置不同的私钥/口令
>   3. 一旦发现secret存在泄露隐患，应重设私钥/口令
> 

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/architecture/2.png)](<2.png>)

## API网络安全

网络安全是指调用方在和AWS PaaS服务间网络传输的通讯安全，一个基本的安全要求是AWS PaaS的Web层只允许接受SSL(Secure Sockets Layer 安全套接层)的处理请求。（AWS PaaS云实例已开启SSL）

API类型 | 网络层采取的安全控制  
---|---  
[HTTP(s)](<../http/README.html>) | \- 每次对参数用私钥签名，防止中途篡改、恶意拼凑  
\- 对请求的timestamp进行检查，控制url存活有效期  
  
[SOAP](<../soap/README.html>) | \- 对入站参数进行解密、签名验证  
\- 对出站结果进行加密、签名计算  
\- 控制服务请求的有效期  
[Java SDK](<../native/README.html>) | 本地处理，无需处理网络层安全隐患  
  
## API处理结果

API类型 | 返回的数据结果  
---|---  
[HTTP(s)](<../http/README.html>) | 由请求的format参数指定，支持json和xml两种格式  
[SOAP](<../soap/README.html>) | 由服务的实现者指定，标准API返回XML文档格式  
[Java SDK](<../native/README.html>) | Java对象  
  
## API错误码

当请求发生错误时，服务器会返回错误码 ( errCode ) 和错误信息 ( msg )，完整的错误码参见<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/error-code.html>