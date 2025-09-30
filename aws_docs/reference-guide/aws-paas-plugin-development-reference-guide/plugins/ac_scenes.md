# 应用场景 · AWS PaaS文档中心

## 应用场景

AC(Access Control)通用访问控制是AWS平台提供给应用开发者的一种简单、灵活的RBAC(Role-Based Access Control, 基于角色访问控制)授权模型，可以通过对资源对象(Resource,被保护的资源)、分配对象(Assignment Object)和访问模式（Access Mode)的定义，创建应用场景所需的权限体系。

[![RBAC](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/ac-1.png)](<ac-1.png>)

AC的主要结构

  * 定义资源（业务对象）
  * 定义分配对象的范围
  * 定义许可（访问控制模式）

> 上述三要素组合成一句话即：你要为一个业务场景（资源）设置多少种权限(访问控制模式)，允许授权给哪些用户（分配对象）

### 使用

  * 某订单记录允许一个特定范围的用户执行`取消`操作
  * 为`投票调查`设定一个投票范围
  * 设置某`文件夹`读、写的用户范围

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/ac-2.png)](<ac-2.png>)