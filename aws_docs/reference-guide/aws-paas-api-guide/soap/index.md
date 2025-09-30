# 使用SOAP访问API · AWS PaaS文档中心

# SOAP API

> 使用本章节内容要求你的AWS PaaS平台 bin/conf/aws-portal.xml中 url属性值为实际的AWS PaaS平台访问地址[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/0.png)](<0.png>)

SOAP API即Web Service。开发者可以通过HTTP传输协议发送SOAP格式的请求消息获得XML结构的处理结果。

在调用这类API之前，开发者需要向管理员申请API密钥，该秘钥由AWS CC的`身份策略`进行管理。包括用户名和密码及增强安全策略。

用户名和密码的传输需要遵循WS-Security的用户名密码类型令牌规范，**密码需要妥善保管，请勿外传** 。

## 技术规格

项 | 说明  
---|---  
Transports | 
* HTTPS/HTTP  
JSR | 
* Java API for XML-Based Web Services (JAX-WS) 2.0 - JSR-224
* Web Services Metadata for the Java Platform - JSR-181
* SOAP with Attachments API for Java (SAAJ) - JSR-67  
WS-*和相关规范 | 
* WS-I Basic Profile 1.1
* WS-Reliable Messaging
* WSDL 1.1
* WS-Security
* SOAP 1.1, SOAP 1.2
* Message Transmission Optimization Mechanism (MTOM)
* JAXB 2.x  
  
## SOAP请求

项 | 说明  
---|---  
API入口 | Portal URL + /r/s，例如：<https://b2b.awspaas.com/api>  
查询参数 | \- service 值为服务ID(必须)，例如`appApi`  
\- wsdl true/false，是否返回WSDL(可选)  
业务参数 | XML，结构参考WSDL定义文档  
  
## SOAP请求样例

一个典型的API请求如下所示

**这是一个 isInstalled 的SOAP API请求**
    
    
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
    

## SOAP返回结构

项 | 说明  
---|---  
result | 状态码。ok代表成功，error代表失败  
errorCode | 错误码。如果result值为error时，提供[错误代码](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/error-code.html>)  
msg | 结果信息。如果result值为error时，提供错误描述信息  
data | 业务数据  
  
## SOAP返回样例

一个典型的SOAP API请求返回结果如下所示

**这是一个 isInstalled 的SOAP API服务返回结果**
    
    
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
    

> 如结果中无errorCode标签项，等同于执行成功  
>  如结果中无result标签项，等同于result值为ok