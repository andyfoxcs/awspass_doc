# AWS MVC架构 · AWS PaaS文档中心

# AWS MVC架构

AWS MVC框架也是一个基于请求驱动的Web框架，使用了前端控制器模式来进行设计，再根据请求映射规则分发给相应的后端逻辑控制器（动作/处理器）进行处理。

[![AWS MVC编程架构](https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/aws_mvc/mvc.png)](<mvc.png>)

在上图中，`前端控制器`（AWS Web Server / Front Controller）和`后端处理控制`（AWS App Server / Controller）是AWS MVC的核心通信框架，黄色区域（视图组装、模型、模版）是开发者实现业务逻辑的区域，主要元素描述如下：

项 | 说明  
---|---  
AWS Web Server | 安装有AWS Portal的标准Servlet容器，例如：Tomcat、WebLogic  
AWS App Server | 安装有AWS Server的应用服务器，所有的业务逻辑在这里处理  
Servlet 前端控制器 | 接收所有来自用户的请求，封装后转发给AWS App服务器  
后端处理控制器 | 通过注解拦截到方法，绑定逻辑处理程序  
View视图组装 | 实现业务逻辑，返回处理的结果  
Model模型 | 资源处理对象，如处理逻辑、对象、国际化、Dao处理、缓存  
Template模版 | 基于静态模版的渲染，处理成动态页面结果  
  
AWS MVC编程框架的主要组成部分：

  * 提交请求(submit)
  * 前端参数解析
  * 后端控制器(controller)
  * 业务对象封装(ModelBean)
  * DAO封装
  * Cache缓存
  * View视图(返回结果)
  * 页面模版渲染(Template)