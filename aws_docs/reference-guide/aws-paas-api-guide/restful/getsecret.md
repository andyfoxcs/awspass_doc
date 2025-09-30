# 获取秘钥 · AWS PaaS文档中心

# 获取秘钥

秘钥由AWS CC的`身份策略`进行管理，开发者可以向管理员申请API密钥，包括访问凭证 ( access_key ) 和 私钥 ( secret )。

## 创建秘钥

  1. 登录您的AWS PaaS实例控制台
  2. 访问“连接服务”页面
  3. 进入策略页签
  4. 创建身份策略
  5. 策略类型选择HTTP

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/8.png)](<8.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/9.png)](<9.png>)

项 | 说明  
---|---  
类型 | 此处选择`HTTP`  
access_key | 访问凭证  
secret | 私钥  
  
> 如果被调用的API设置了身份策略，则获取的秘钥，请确保为对应身份策略的秘钥信息 [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/10.png)](<10.png>)