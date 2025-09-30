# 提供RSA加密的HTTP调用示例 · AWS PaaS文档中心

## 提供RSA加密的HTTP调用示例

这是一种当外部系统通过HTTP请求访问ASLP但无法提供AWS SessionId的业务场景。这时，通过HTTP(S)远程调用一个应用的ASLP接口服务，要求authentication参数提供该App公钥加密处理后的值，以此验证调用方的合法性。
    
    
    http://localhost:8088/portal/r/jd?cmd=API_CALL_ASLP&sourceAppId=com.actionsoft.apps.poc.plugin&aslp=aslp://com.actionsoft.apps.poc.plugin/myName3&params={"yourName":"Tom"}&authentication=CS1pjMug8Wm-Lvlv2iNPieMOiU_SuoJ5-Ib7SRpFv2PhIWsS4p1UEVGrccjsZm2SjDAomiOSLaglOeaSaCE9BoM7pM8j9T5Kh_vuXl69bhsFR-X19bph5VvwzYW7s6bEPapdvkJE3w2FFBN__kBKv_LKW3c0Uay1T6i_mTJoOzA
    

参数 | 说明  
---|---  
sourceAppId | 调用方AppId，且调用方应用设置了依赖服务方的策略  
aslp | 服务地址  
params | 该服务要求提供的参数，一个JSON串  
authentication | 被公钥加密和编码处理的字符串`RSA-KEY`  
  
#### 预期的返回结果
    
    
    {
    msg: "Hi Tom , My name is AWS!",
    id: ":responseobject;",
    result: "ok"
    }
    

#### ASLP服务提供方(AWS App)

  * 使用new HttpASLP(HttpASLP.AUTH_RSA)注册服务
  * 使用AWS提供的rsa-keygen.sh(.bat)，生成名称为该AppId的证书
  * 将生成的.cer（公钥证书）和.pfx（私钥证书）文件移动至该appId的安装目录下

    
    
    //证书生成工具，要求生成的证书文件名为该App的Id
    %AWS-HOME%/bin/rsa-keygen.sh
    %AWS-HOME%/bin/rsa-keygen.bat
    

#### ASLP消费方(HTTP请求)

  * 获得ASLP服务提供方的.cer（公钥证书）文件，供HTTP客户端的发者做加密处理
  * 使用公钥文件对字符串`RSA-KEY`进行RSA加密，并转换成`Base64URL`编码
  * 上述编码后的串作为调用该ASLP URL的authentication参数值

    
    
    //在AWS做RSA加密和编码处理，获得authentication的Sample
    String authentication = new String(Base64.encodeURL(RSA.encrypt( "xxx.cer", "RSA-KEY".getBytes())));