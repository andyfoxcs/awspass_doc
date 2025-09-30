# 使用本地原生API · AWS PaaS文档中心

# 使用本地原生Java API

这是AWS PaaS对Java开发者提供的原生API，大部分被封装在`%AWS-HOME%/bin/lib/aws-sdk-local.jar`里，对于获得本地AWS开发环境的用户，该jar文件已随平台提供。这些API能够直接的与AWS实例进行交互，AWS PaaS的各种官方客户端应用也是基于这些原生API构建。

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/1.png)](<1.png>)

> **注意**
> 
>   * 原生Java API不适用于异构系统的程序调用（例如，你希望在一个外部环境中使用这些API）
>   * 基于这些接口开发的jar包编译文件，必须存放在`%AWS-HOME%/apps/install/%appId%/lib`目录下，其中`%appId%`是开发者的应用Id
> 

## 使用AWS SDK for Java API

为简化开发者的使用，大部分API都可以直接通过一个名为SDK的类作为调用入口，例如
    
    
    //获得AWS流程引擎的接口，执行挂起操作
    SDK.getProcessAPI().suspend(processInstId);
    

**进阶参考**

  * [浏览AWS SDK for Java API的Java Doc](<java_doc.html>)
  * [了解API的异常处理策略](<exception.html>)