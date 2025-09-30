# 为什么要用AWS MVC · AWS PaaS文档中心

## 为什么要用AWS MVC？

作为一种编程框架，AWS MVC与传统开源的Spring MVC、Strusts2或商业开发框架相比有众多优势：

  * 清晰、干净、`请求驱动`（请求-响应）的轻量级Web编程框架
  * 学习难度远小于[Spring MVC](<http://docs.spring.io/spring/docs/current/spring-framework-reference/html/mvc.html>)和[Strusts2](<http://struts.apache.org/development/2.x/>)，很容易写出性能优秀、体验性强的程序
  * `No Servlet`、`No JSP`，`Just J2SE`，更容易的开发调试和问题追踪
  * 与AWS平台架构兼容的会话安全、DAO、I18N国际化、日志、审计和SLA告警机制
  * 没有值栈、[OGNL表达式](<http://baike.baidu.com/view/1347280.htm?fr=aladdin>)、繁琐标签库等增加代码复杂度和性能下降的架构缺陷
  * 优于Strusts2的注解编程和方法拦截，能够直接根据注解绑定Request参数，代码更简洁
  * 对处理结果是HTML、JSON、XML数据结构和错误码的统一处理，避免业务架构缺陷
  * 提供了一套基于[JQuery](<http://jquery.com/>)和[JQuery Mobile](<http://jquerymobile.com/>)的AWS UI库，针对企业级需求进行了增强封装
  * 内核采用了`NIO`通信和多线程池化管理，能够充分对计算资源的扩容做出适应，实现纵向扩展（Scale Up）
  * 为多个集群节点提供自我发现和自我纠正能力，简化部署和运维，轻松实现弹性的横向扩展（Scale Out）

### 提高生产环境下的SLA服务可用性

使用AWS MVC框架开发的应用在向目标环境安装或升级时，被AWS PaaS容器监控、调度和管理。可以确保业务生产环境在不中断服务的情况下完成新旧程序版本的切换，对每次请求的性能和问题进行监控。

**与MVC直接相关的AWS SLA指标**

Metric Id | 说明  
---|---  
MVCFramework.cmd | cmd总请求次数  
MVCFramework.webCmd | Web请求耗时  
MVCFramework.loginTime | 用户登录耗时  
MVCFramework.dataCmd | Data请求（JSON/XML）耗时  
MVCFramework.upfileCmd | 文件上传耗时  
MVCFramework.downfileCmd | 文件下载耗时  
MVCFramework.aslpExecute | ASLP执行耗时  
MVCFramework.activeUsers | 活跃用户数  
MVCFramework.activeSesssion | 有效会话数  
  
> 有关SLA部分，请阅读《AWS SLA参考指南》

### 应用的分发、安装和卸载

如果你是AWS PaaS的独立软件开发者(ISV)或集成服务提供商(SI)，选择使用AWS MVC的一个商业目标，是能够让所开发的应用顺畅分发到其他AWS PaaS客户环境中，实现应用产品化。通过`AWS企业应用商店`的上架审核标准，还有机会直接向更大群体的AWS PaaS企业用户提供应用和服务。

> 有关应用开发规范和上架审核，请阅读《AWS App开发与发布指南》

### 对计算资源的扩容做出适应，实现纵向扩展（Scale Up）

当提高服务器配置时，可以获得更高的性能。我们在24核CPU的Linux(CentOS)环境中进行MVC框架的压测实验，可无错误的达到16,800/TPS（每秒可以处理完1.6万个请求），平均每个请求能够在32毫秒完成处理。

> AWS MVC提供了一个用于基线压力测程序
>     
>     
>     %AWS-HOME%/bin/benchmark.sh(或benchmark.bat)
>     
> 
> 可以执行如下命令，测试你的部署环境MVC性能（该测试用例模拟真实的Web请求，测试MVC框架I/O通信和对请求的传参、接参处理）
>     
>     
>     cd %AWS-HOME%/bin/
>     benchmark.sh cmd
>     

### 获得线性的横向扩展（Scale Out）

当采用集群模式，部署更多AWS节点时，性能上可以获得线性提升（2-5个节点）。持续增加更多节点时，数据库、网络流量和共享存储的I/O将成为瓶颈。