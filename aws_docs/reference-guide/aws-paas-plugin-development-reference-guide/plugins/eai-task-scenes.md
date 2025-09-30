# 应用场景 · AWS PaaS文档中心

## 应用场景

EAI任务是企业基于AWS PaaS实施`统一待办`的技术方案，同时PaaS开发者也可以利用该接口将任务推送到待办列表，如个人任务、日程。

通常实施`统一待办`解决方案需要关注如下内容：

  * 将[TaskAPI服务](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/http/>)开放给第三方系统，或为第三方系统[开发无session的cmd命令](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/aws_mvc/controller.html>)，接收任务创建、任务完成和任务删除操作
  * 创建EAI任务时，第三方系统提供处理该表单的URL地址
  * 对该URL实施AWS的SSO身份集成，免登录直接处理URL表单
  * 如果手机端需要同步支持该EAI任务，第三方系统提供的URL能够在手机浏览器处理