# 应用场景 · AWS PaaS文档中心

## 应用场景

这是一个安全处理机制扩展应用，通过该应用，可调整以下场景的算法：

  * 平台附件加密、解密的算法
  * BO存储的加密、解密的算法
  * 登录密码的摘要算法
  * BO表记录摘要算法

> 如果替换平台安全处理机制，可修改`AWS BPMS平台`的参数配置`安全处理机制(SecurityProcessorId)`。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/security-1.png)](<security-1.png>)

** 当AWS PaaS平台已产生业务数据后，修改平台安全处理机制，会影响历史数据展示，因此当已有业务数据后，不能修改该配置。**