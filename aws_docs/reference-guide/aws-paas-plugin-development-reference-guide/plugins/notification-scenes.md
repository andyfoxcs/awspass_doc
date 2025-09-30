# 应用场景 · AWS PaaS文档中心

# 应用场景

`通知中心`是AWS PaaS默认提供的一个消息提醒机制，可以接收来自各个应用推出的消息，并统一推送给用户的PC门户或移动门户。

功能介绍可参考这里：<https://docs.awspaas.com/solution-package/aws-paas-app-solution-package-oa/communication/notification.html>

平台默认为开发者提供了通用消息API
    
    
    SDK.getNotificationAPI().sendSystemMessage(String to, String content, String level)
    

如果开发者希望自定义消息交互内容（例如用户接收到消息时提供`按钮`操作），就可以通过扩展开发，自定义消息频道和处理方式。

**下图列出各应用扩展的消息提醒示例**

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/notification-1.png)](<notification-1.png>)

### 了解PC端消息通知结构

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/notification-3.png)](<notification-3.png>)

### 了解移动端消息通知结构

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/notification-5.png)](<notification-5.png>)