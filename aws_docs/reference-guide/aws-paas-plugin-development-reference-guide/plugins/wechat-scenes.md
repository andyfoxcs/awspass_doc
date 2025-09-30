# 应用场景 · AWS PaaS文档中心

## 应用场景

企业微信事件，是指当成员在企业微信上的某些操作行为发生时（比如关注、取消关注、上报地理位置、点击菜单、进入应用等），企业微信会将事件以消息的方式通知到相应每个应用。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/wechat-3.png)](<wechat-3.png>)

如果基于AWS PaaS的`企业微信管理开发平台`开发微信应用，AWS PaaS将负责监听并传递这些事件给相应的本地App，触发开发者的处理程序。在架构上，从接收到微信消息到触发处理器的代码，这个过程是同步的。

上图中，微信应用和AWS PaaS并不一定是一对一的处理关系。

> 如果启用该项服务，可从`AWS企业应用商店`安装`企业微信管理开发平台`应用。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/wechat-1.png)](<wechat-1.png>)

#### AWS企业微信管理开发平台参考指南

完整的微信应用开发文档，请访问以下链接：

<https://docs.awspaas.com/reference-guide/aws-paas-wechat-reference-guide/index.html>