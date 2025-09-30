# 事件触发器 · AWS PaaS文档中心

## 事件触发器

事件触发器是执行后端Java代码逻辑的容器，是实施AWS平台必须掌握的核心功能之一。当节点、流程状态即将（已经）改变、动作即将（已经）执行时，会触发一系列的事件，开发者可以注册自己的Java代码来实现这些事件，例如 _【当用户点击‘办理’按钮时，在后端触发一个VALIDATE有效性校验事件】_ 。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/form24.png)](<form24.png>)

项 | 说明  
---|---  
Java类名 | 一个遵循AWS事件接口实现的Java程序，格式：类路径+类名  
事件类型 | 各种事件名称，不同的事件要求开发人员实现的接口不同，每个事件只允许注册一个类  
添加 | 将指定的Java类注册到事件  
删除 | 将Java类从一个事件中删除  
  
## 复用当前事件触发器到...

当前节点的事件触发器复用到其他任务节点

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/7.png)](<7.png>) [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/8.png)](<8.png>)

### 延伸阅读

  * [AWS 流程事件开发参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/index.html>)