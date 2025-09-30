# 流程全局事件 | AWS 流程事件开发参考指南

## 流程全局事件

在AWS PaaS中，提供全局事件目的在于捕获对人工任务的处理动作，为AWS人工任务的推送（到达提醒、对企业已有统一工作台服务的集成）提供完整支持。全局事件的开发以AWS应用插件形式完成，允许多个App处理自己的全局事件监听器，详细说明参见《AWS 插件扩展开发参考指南》。

> 【流程全局事件监听器】<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/process_public_event_scenes.html>

在处理全局事件监听逻辑时，应尽量避免复杂的业务处理或I/O、JDBC操作，降低流程引擎的整体处理性能。如果性能影响明显存在，一种优化方案是可以将程序逻辑处理通过线程完成。