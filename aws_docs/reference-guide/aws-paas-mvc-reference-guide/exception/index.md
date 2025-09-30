# 异常处理 · AWS PaaS文档中心

# 异常处理框架

AWS MVC框架的异常处理过程如下所示

[![异常处理框架](https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/exception.png)](<exception.png>)

在上图中，请求者（用户或服务API）被前端控制器封装成指令并传输至AWS服务器，当图中红色、橙色和黄色区域异常发生后，由AWS的顶层异常拦截器捕获，向请求者返回错误消息。

在这个章节中，你将了解如下内容：

  * 错误码定义
  * 抛出异常
  * 处理异常