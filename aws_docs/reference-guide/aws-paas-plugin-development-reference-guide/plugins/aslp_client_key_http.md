# 提供Key口令的HTTP调用示例 · AWS PaaS文档中心

## 提供Key口令的HTTP调用示例

这是一种当外部系统通过HTTP请求访问ASLP但无法提供AWS SessionId的业务场景。这时，通过HTTP(S)远程调用一个应用的ASLP接口服务，要求authentication参数提供一个固定的Key口令。这种方式缺乏更高的安全性，因此被限定调用方的固定IP，适合处于防火墙内的服务器间访问。
    
    
    http://localhost:8088/portal/r/jd?cmd=API_CALL_ASLP&sourceAppId=com.actionsoft.apps.poc.plugin&aslp=aslp://com.actionsoft.apps.poc.plugin/myName2&params={"yourName":"Tom"}&authentication=hehe
    

参数 | 说明  
---|---  
sourceAppId | 调用方AppId，且调用方应用设置了依赖服务方的策略  
aslp | 服务地址  
params | 该服务要求提供的参数，一个JSON串  
authentication | ASLP服务提供方应用提供的一个暗号口令  
  
#### 预期的返回结果
    
    
    {
    msg: "Hi Tom , My name is AWS!",
    id: ":responseobject;",
    result: "ok"
    }
    

#### ASLP服务提供方(AWS App)

  * 使用new HttpASLP(HttpASLP.AUTH_KEY, "MY_KEY")注册服务
  * `MY_KEY`是该应用定义的一个App参数名，其值格式为{"key":"你的暗号口令","ip":"调用方IP地址"}
  * `MY_KEY`命名可任意指定，只要注册和配置匹配即可

**设置应用变量**

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/aslp-2.png)](<aslp-2.png>)