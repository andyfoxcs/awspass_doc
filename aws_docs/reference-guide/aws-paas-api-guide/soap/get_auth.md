# 获取身份 · AWS PaaS文档中心

# 获取身份

秘钥由AWS CC的`身份策略`进行管理，开发者可以向管理员申请API密钥，包括用户名和密码。

## 获取用户名密码身份

  1. 登录您的AWS PaaS实例控制台
  2. 访问“连接服务”页面
  3. 进入策略页签
  4. 创建身份策略
  5. 策略类型选择SOAP

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/5.png)](<5.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/4.png)](<4.png>)

项 | 说明  
---|---  
类型 | 此处选择`SOAP`  
access_key | 访问凭证  
secret | 私钥。开发者应妥善保管  
  
> 如果被调用的SOAP API设置了身份策略，则获取的秘钥，请确保为对应身份策略的秘钥信息 [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/6.png)](<6.png>)