# Secret Identity - 身份策略(6.4.3) | AWS CC连接中心参考指南

# Secret Identity - 身份策略(6.4.3)

为HTTP和SOAP提供认证秘钥信息。

从6.4.3版本起身份策略分为HTTP和SOAP两种类型，HTTP类型又支持用于连接和用于发布两种场景。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/cl.gif)

## 用于SOAP的身份策略

SOAP类型策略用于发布[Web Service API](<../fb/soap.html>)时的策略身份配置。`access_key(访问凭证)`和 `secret(私钥)`为调用发布的SOAP API时需要传入 的身份策略。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/cl1.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/cl2.png)

> 有关Web Service API的发布参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_soap_api.html>)。

## 用于HTTP发布的身份策略

HTTP类型发布用于发布[WEB API](<../fb/http.html>)和[Restful API](<../fb/restful_api_-_restful.html>)时的策略身份配置。`access_key(访问凭证)`和 `secret(私钥)`为调用发布的SOAP API时需要传入 的身份策略。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/cl3.png)

> 有关Web API和Restful API的发布参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/>)。

## 用于HTTP连接的身份策略

HTTP类型连接用于[HTTP连接](<../tech-adapters/http.html>)的身份策略配置。认证方式支持`Basic Auth、Token、API Key、摘要签名`。

### Basic Auth

Basic Auth简单点说明就是每次请求API时都提供用户的username和password， 简言之，Basic Auth是配合RESTful API 使用的最简单的认证方式，只需提供用户名密码即可。

  * 勾选开启控制台调试日志后，在调用相关使用该策略的连接服务时，会有相应调试日志输出在log文件中

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic1.png)

**示例：**

此示例以通过Basic认证方式调用AWS PaaS平台的应用是否安装接口。准备:

  1. 在AWS PaaS实例控制台(_bpm.platform)增加未发布的服务也可以调用参数`api.noprofile.access`，参数值为`true`
  2. 在AWS PaaS实例控制台(_bpm.platform)增加Web API认证方案`webapi.auth.scheme` 参数值设为`Basic` ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic6.png)
  3. 创建HTTP 发布类型的身份策略，假设。`access_key(访问凭证)`和 `secret(私钥)`均为testcc2 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic5.png)

**步骤：**

  1. 创建Basic Auch认证的身份策略，用户名、密码与上面准备步骤3中配置相同

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic1.png)

  2. 创建连接服务，并开启验证身份，身份策略选择步骤1中创建的Basic Auch认证的身份策略

Http(s) URL地址为 <http://localhost:8088/portal/api>

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic2.png)

  3. 创建数据服务，连接器选择步骤2中创建的连接服务

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic3.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic7.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic8.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic9.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/basic10.png)

### Token

基于token的鉴权机制类似于http协议也是无状态的，它不需要在服务端去保留用户的认证信息或者会话信息。这就意味着基于token认证机制的应用不需要去考虑用户在哪一台服务器登录了，这就为应用的扩展提供了便利。流程：

  1. 用户使用用户名密码来请求服务器
  2. 服务器进行验证用户的信息
  3. 服务器通过验证发送给用户一个token
  4. 客户端存储token，并在每次请求时附送上这个token值
  5. 服务端验证token值，并返回数据

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/token1.png)

项 | 说明  
---|---  
认证方式 | 请选择Token  
Token API服务 | 需选择一个DS数据模型  
Token位置 | 选择DS数据模型用于存储Token的输出参数  
扩展字段 | 可添加扩展字段  
缓存时间 | 获取Token值后在AWS PaaS平台是否需要缓存以及缓存时间，当超过缓存时间后再次调用时会创建新的Token，如果设置为不缓存，则每次调用均重新获取Token,。 配置方式支持固定时间、动态字段   
动态字段，选择DS数据模型用于存储一个时长的输出参数   
固定时间，设置一个固定时长  
开启控制台调试日志 | 开启后，在调用相关使用该策略的连接服务时，会有相应调试日志输出在log文件中  
  
**示例：**

以[微盟云](<https://cloud.weimob.com/>)接口为例。微盟云在调用所有接口时都必须传入Token参数，此例先创建Token值后，然后再继续调用其它API接口。

  1. 创建获取微盟云Token的链接 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/token2.png)
  2. 创建DS数据服务，配置输出参数Token ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/token3.png) ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/token4.png)
  3. 创建Token身份策略 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/token5.png)
  4. 再次创建微盟云某个具体接口的连接，并开启验证身份，身份策略选择步骤3中配置的Token身份策略 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/token6.png)
  5. 创建DS数据服务，配置输入输出参数模拟调用即可 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/token7.png) ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/token8.png)

> 以上方式只是将每个DS的Token参数变成由系统自动生成，并且这时Token的有效性、有效时长等将自动根据步骤3策略中配置有效， 如果不是这种方式，而是手动添加token参数，这时是每次都会重新请求token值，性能上会有影响 5中自动生成的token参数，也可手动删除，删除后，再次手动添加回来也可以，就算不用该种方式添加，而是手动自己完全添加，按照 @ccIdentity公式规则配置也是可以的，@ccIdentity公式就相当于是系统内置了一个@公式获取相应数据

### API Key

API Key是一种简单的授权方式，一般用于测试，可以在请求头或查询参数中向API发送一个用于校验的键值对。 对计划要调用的接口为API Key认证方式的，可创建该策略后，过再创建连接服务时，开启身份验证选择该策略即可。

认证key value参数支持存在Header和Query两种。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/apikey1.png)

### 摘要签名

摘要签名是一种可用于生产的授权方式，服务端颁发key和secret秘钥，客户端利用秘钥将必要字符串按照约定的逻辑组装和签名，然后传输到服务端验签。该方式比较安全，如果控制好秘钥分发时的安全性，则不惧怕传输过程中被监听和篡改。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/zhaiyao1.png)

平台提供了常用服务的签名模板：`平台发布的API`、 `阿里云API网关` 、`腾讯云API网关` 、 `华为云API网关`，您也可根据自己实际情况进行配置。

### 平台发布的API

AWS PaaS平台发布的Web API，即为[签名认证](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/http/signing.html>)。通过此签名模板，即可调通AWS Web 服务接口。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/zhaiyao2.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/zhaiyao3.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/zhaiyao4.png)

> 其它签名模板，仅为当前各服务的签名认证参数，后期各服务商如有变动，使用者请根据各服务商实际情况进行调整即可。 详细的签名认证过程参见各服务商官方文档说明。