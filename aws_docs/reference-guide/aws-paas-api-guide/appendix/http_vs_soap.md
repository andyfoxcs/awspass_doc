# Web API与SOAP API的区别 · AWS PaaS文档中心

# Web API与SOAP API的区别

总的来说，Web API比SOAP API有优势，多数情况下SOAP API的优势仅在消息结构的描述上。因此在三方集成时，当对方的集成工具仅支持根据WSDL来构建调用时，才建议考虑发布SOAP API。

## 1.请求消息格式不同

Web API的消息规格为URL请求；SOAP API的消息格式为SOAP规范。从消息封装、编码/解码上，Web API有明显的并发性能优势。

由于SOAP消息格式在发布时声明，可以方便一些高级工具调用方实现可视化的参数映射、配置化的调用。

**例如，一个Web API请求消息**
    
    
    https://b2b.awspaas.com/openapi
    ?timestamp=1439277618461
    &sig_method=HmacMD5
    &cmd=app.install.check
    &appId=com.actionsoft.apps.notification
    &access_key=Salesforce#1
    &format=json
    &sig=DE90336BEDB0C3D3FE6DEE2FF0DF11AC
    

**例如，一个SOAP API请求消息**
    
    
    <soap:Envelope xmlns:ser="http://service.sdk.actionsoft.com/"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
       <soapenv:Header
       xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"/>
       <soap:Body>
          <ser:isInstalled>
             <appId>com.actionsoft.apps.notification</appId>
          </ser:isInstalled>
       </soap:Body>
    </soap:Envelope>
    

## 2.响应消息格式不同

Web API可以返回JSON/XML结果，尤其是JSON数据格式是当今Web和移动端开发的首选规范；SOAP API返回一个XML的消息对象。从数据结果封装、编码/解码上，Web API有明显的并发性能优势，同时JSON结构有助于减少网络流量。

由于SOAP响应格式在发布时声明，可以方便一些高级工具调用方实现可视化的结果映射、配置化的调用。

**例如，一个Web API响应消息**
    
    
    {
      "data" : true,
      "result" : "ok"
    }
    

或
    
    
    <?xml version="1.0" encoding="utf-8" standalone="yes"?>
    <boolResponse>
        <data>true</data>
    </boolResponse>
    

**例如，一个SOAP API响应消息**
    
    
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <ns1:isInstalledResponse
            xmlns:ns1="http://service.sdk.actionsoft.com/">
                <return
                xmlns:ns2="http://service.sdk.actionsoft.com/">
                    <data>true</data>
                </return>
            </ns1:isInstalledResponse>
        </soap:Body>
    </soap:Envelope>
    

## 3.安全机制不同

  1. Web API可以基于HTTPS，而SOAP API可以基于WS-Security规范对消息加密时也可以使用HTTPS
  2. Web API的认证基于访问凭证 ( access_key )和私钥 ( secret )的签名摘要验证，而SOAP API的认证基于WS-Security规范的用户名密码或者x509

## 4.客户端调用方式不同

SOAP API需要一个比较重的SOAP协议栈，会遇到跨语言、版本的SOAP互操作问题；Web API仅需要客户端支持HTTP(s)传输协议。

> 综上，Web API和SOAP API在请求、响应、安全和编程调用模式上有很大差异。AWS PaaS开发者可根据实际情况和上述差异，启用和配置合适的API协议。

## 5.并发处理能力的不同

**测试环境**

项 | 说明  
---|---  
AWS PaaS服务器 | 16核、16G内存、Centos 7.1 64 位、AWS PaaS(6.1.2.0830)  
数据库服务器 | 16核、16G内存、Centos 7.1 64 位、 Oracle11.2g 64位  
模拟客户机 | 2核、4G内存、Windows 7 32位、 LoadRunner 11  
  
**测试用例**

方法 | 说明  
---|---  
demo.say | 测试返回简单值  
demo.calc | 测试返回简单对象  
  
> 测试用例可与我们技术支持联系，获得com.actionsoft.apps.poc.api应用

**测试结果**

  1. Web API最大TPS(Trasaction per second事务数/秒)值为2137.529
  2. SOAP API最大TPS(Trasaction per second事务数/秒)值为219.706

**结论** ：Web API与SOAP API相比较，有明显的并发性能优势