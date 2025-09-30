# 应用场景 · AWS PaaS文档中心

## 应用场景

ASLP（Application Service Locator Protocol，应用服务访问定位协议）是AWS平台App PaaS容器为解决应用间互操作和安全访问控制定义的一套私有协议和实现，用于统一管控企业PaaS平台的应用服务接口，简化和标准应用与应用间的互操作。在AWS中每个ASLP都拥有一个唯一的访问地址和自描述元数据，便于开发者识别和使用。
    
    
    aslp://%appId%/%serviceName%
    

> 例如：aslp://com.actionsoft.apps.poc.plugin/myName

ASLP调用者不必了解ASLP提供者的具体实现，也不必处理相关应用的JVM ClassLoader依赖关系，只需一行Java代码或一个HTTP（如为移动客户端提供HTTP服务）请求即可完成对依赖应用的ASLP服务调用。当该服务以跨JVM的形式访问时，提供了三种鉴权策略：

鉴权策略 | 说明  
---|---  
Session会话 | 安全的鉴权模式，要求HTTP调用者提供AWS会话  
Key | 不安全的鉴权模式，要求HTTP调用者提供约定的Key口令串  
RSA | 安全的鉴权模式，要求HTTP调用者提供特定公钥加密的串  
  
> ASLP在设计上具有很多优势，比如可以无状态的解决A、B、C应用的交叉关联，提供关联依赖策略和依赖程度定义，如高度依赖、中度依赖还是智能依赖。

### 使用

  * 在同一个AWS PaaS中，实现A应用调用B应用提供的接口
  * 为移动开发者封装服务接口

### 注意事项

要成功调用某应用提供的ASLP，必须在该应用的`manifest.xml`声明依赖
    
    
      <requires>
        <require appId="服务提供方的AppId" notActiveHandler="error"/>
      </requires>
    

  * notActiveHandler=error，表示高度依赖。如果服务提供方被停用，该应用将收到错误
  * notActiveHandler=warning，表示中度依赖。如果服务提供方被停用，该应用将收到警告
  * notActiveHandler=none，表示智能依赖。如果服务提供方被停用，该应用不会收到任何信息