# ASLP服务 | AWS 移动开发参考指南

### ASLP服务

[ASLP（Application Service Locator Protocol，应用服务访问定位协议）](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/aslp.html>)是AWS平台App PaaS容器为解决应用间互操作和安全访问控制定义的一套私有协议和实现，用于统一管控企业PaaS平台的应用服务接口，简化和标准应用与应用间的互操作。ASLP服务可通过Http请求的方式被移动端调用。

#### 提供AWS会话的HTTP调用示例

通过HTTP(S)远程调用一个应用的ASLP接口服务，要求authentication参数提供一个合法的AWS账户会话。
    
    
    http://localhost:8088/portal/r/jd?cmd=API_CALL_ASLP&sourceAppId=com.actionsoft.apps.poc.plugin&aslp=aslp://com.actionsoft.apps.poc.plugin/myName1&params={"yourName":"Tom"}&authentication=%sessionId%
    

参数 | 说明  
---|---  
sourceAppId | 调用方AppId，且调用方应用设置了依赖服务方的策略  
aslp | 服务地址  
params | 该服务要求提供的参数，一个JSON串  
authentication | 有效的AWS Session会话  
  
#### 预期的返回结果
    
    
    {
    msg: "Hi Tom , My name is AWS!",
    id: ":responseobject;",
    result: "ok"
    }
    

#### ASLP服务提供方(AWS App)

  * 使用new HttpASLP(HttpASLP.AUTH_SID)注册服务

有关ASLP服务的详情， 请[参考这里](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/aslp_scenes.html>)