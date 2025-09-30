# 附录4-微信企业号通信 · AWS PaaS文档中心

# 微信企业号框架

微信企业号框架基于AWS MVC框架，将请求根据请求类型（URL跳转、消息/事件）交由不同的Servlet处理，再根据请求的映射规则分发给相应的后端逻辑控制器进行处理。

[![AWS MVC编程架构](https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/wechat/wechat.png)](<wechat.png>)

上图中的三个Servlet（AWS Web Server / 一般请求Servlet，WS Web Server /重定向Servlet，WS Web Server /回调Servlet），`后端处理控制`（AWS App Server / Controller）和`微信企业号管理平台`是微信企业号的核心通信框架，AWS微信App是开发者实现业务逻辑的区域，主要元素描述如下：

项 | 说明  
---|---  
AWS Web Server | 安装有AWS Portal的标准Servlet容器，例如：Tomcat、WebLogic  
AWS App Server | 安装有AWS Server的应用服务器，所有的业务逻辑在这里处理  
一般请求Servlet | 接收URL跳转请求，收到请求后会检查是否带有包含用户认证信息的Cookie，如果包含则封装后转发给后端控制器，若不包含则构造微信OAuth验证链接，重定向到下面的`重定向Servlet`  
重定向Servlet | 处理微信OAuth验证请求，封装后转发给后端控制器，最终交由微信管理平台处理并返回验证结果。如果验证通过，将验证信息写入Cookie，最后重定向到原始URL  
回调Servlet | 微信企业号应用的回调地址指向此处。处理微信消息/事件请求，封装后转发给后端控制器，再由微信管理平台转发到指定的AWS微信App处理请求  
后端处理控制器 | 通过注解拦截到方法，绑定逻辑处理程序  
微信企业号管理平台 | 管理微信企业号应用，可为企业号应用设置、绑定菜单和指定处理消息/事件的AWS 微信App  
AWS微信App | 实现业务逻辑，一般包含H5页面（View视图组装,Model/Dao/Cache模型，Template模板），和消息/事件处理实现类。