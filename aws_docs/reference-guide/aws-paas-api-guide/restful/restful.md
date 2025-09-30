# 使用RESTful访问API · AWS PaaS文档中心

# 使用RESTful访问API

> 使用本章节内容要求你的AWS PaaS平台 bin/conf/aws-portal.xml中 url属性值为实际的AWS PaaS平台访问地址[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/0.png)](<0.png>)

REST是URL定位资源，用HTTP动词（GET，POST，DELETE，PUSH等）描述操作，基于REST构建的API就是Restful风格。。 Restful可以通过一套统一的接口为PC、微信(H5)、IOS和Android提供服务，这样的接口不需要前端样式，只提供数据。

在调用这类API之前，开发者需要向管理员申请API密钥，该秘钥由AWS CC的`身份策略`进行管理。包括访问凭证 ( access_key ) 和 私钥 ( secret )。