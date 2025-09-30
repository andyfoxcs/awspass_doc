# HTTP · AWS PaaS文档中心

# HTTP

对连接器中[HTTP(连接Web服务)](<../tech-adapters/http.html>)进行数据转换处理。

## 接口要求

  1. 不支持多套业务数据结构-》如500 一套返回数据信息，200一套返回数据信息
  2. 返回内容须为标准json串或一个String串
  3. 返回树中定义的根字段，服务端接口返回数据中要存在

## 快速上手

在进行HTTP连接前，要求准备连接的WEB API接口已经准备完毕。 本例以AWS PaaS平台提供的 `Web API` 中判断指定的应用是否已安装`app.install.check` 为例。

>   1. 有关AWS PaaS平台 Web API的发布详细参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_http_api.html>)。
>   2. 有关使用Postman测试Web API的步骤详细参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/http/postman.html>)。
> 

  1. 准备AWS PaaS平台`APP API`调用接口
  2. 新建身份策略-摘要签名
  3. 新建HTTP连接器
  4. 新建HTTP数据
  5. 配置HTTP数据-数据连接器、请求方法、URL地址
  6. 配置HTTP数据-输入信息
  7. 配置HTTP数据-输出信息
  8. 测试

### 1\. 准备AWS PaaS平台`APP API`调用接口

(1) . 在 `连接服务>策略`页签，创建身份策略，所属应用为`AWS PaaS实例控制台`，类型为`HTTP > 用于发布` ，假设`access_key` 和 `secret` 均为`1`

[![](http3.png)](<http3.png>) [![](http2.png)](<http2.png>)

(2) . 在 `连接服务>发布`页签，发布HTTP API，所属应用为`AWS PaaS实例控制台`，实现类选择`com.actionsoft.sdk.service.AppApi`，并配置身份策略为上步创建的身份策略，至此完成调用接口的准备

[![](http4.png)](<http4.png>) [![](http5.png)](<http5.png>)

### 2\. 新建身份策略-摘要签名

在 `连接服务>策略`页签，创建`身份策略`

  * 类型为`HTTP > 用于连接`
  * 认证方式为`摘要签名`
  * Key和Secret为1 (此值需要与准备APP API时发布是配置的身份策略秘钥一致)
  * 签名详细信息从模板列表中选择`平台发布的API`自动生成即可

[![](http19.png)](<http19.png>)

### 3\. 新建HTTP连接服务

在 `连接服务>连接`页签，创建`HTTP连接Web服务`

  * 开启验证身份，身份策略选择步骤二中创建的摘要签名身份策略

[![](http8.png)](<http8.png>) [![](http7.png)](<http7.png>) [![](http9.png)](<http9.png>) [![](http10.png)](<http10.png>)

### 4\. 新建HTTP数据

在 `连接服务>数据`页签，创建`HTTP连接Web服务`

[![](http11.png)](<http11.png>)

### 5\. 配置数据连接器、请求方法、URL地址

连接器选择步骤3中创建的HTTP连接服务，请求方法勾选POST，URL地址会自动带出所选连接器中配置的URL，因为AWS PaaS平台提供的Web API URl地址前缀一样，所以此示例无需再补充URL后面的信息

[![](http12.png)](<http12.png>)

### 6\. 配置输入信息

在左侧Data Service输入增加String类型的`appId`和`cmd`两个参数， 在右侧请求参数queryParameters下增加String类型的`appId`和`cmd`两个参数。并进行连线

[![](http13.png)](<http13.png>)

[![](http14.png)](<http14.png>)

### 7\. 配置输出信息

在两侧result节点下增加String类型的`result`和`msg`参数、Boolean类型的`ddata`参数，并进行连线 ，点击右下角`保存`按钮进行保存

[![](http17.png)](<http17.png>)

### 8\. 测试

点击左下角`测试一下`按钮，appId输入`_bpm.platform`，cmd输入`app.install.check`，点击`执行`进行测试

[![](http15.png)](<http15.png>) [![](http16.png)](<http16.png>)