# 提供AWS会话的HTTP调用示例 · AWS PaaS文档中心

## 提供AWS会话的HTTP调用示例

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