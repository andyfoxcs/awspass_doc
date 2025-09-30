# 什么是流程事件? | AWS 流程事件开发参考指南

## 什么是流程事件?

事件遍布在流程实例的全生命周期范围之内，当流程在执行过程中，AWS流程引擎会触发相关的[监听事件](<../appendix/listener_handler.html>)，通常是空跑事件。

如果开发者为这些事件编写了Java程序，[监听器](<../appendix/listener_handler.html>)会将AWS流程引擎的处理暂时接管给这些程序，例如在流程启动时检查业务数据并阻止启动操作。

当一个事件到达时，由[监听器](<../appendix/listener_handler.html>)捕获，此时如果该事件存在开发者的代码，就会被动的触发一次。

  * 继承父类（通常不同类型的事件提供不同的父类），基于[接口编程](<../introduction/interface.html>)
  * 注册到指定的流程中，等待触发

> AWS应用容器为每个App分配了独立的classloader，开发者的所有Jar包应提供在该流程模型所在的应用资源目录下（install/%AppId%/lib/）。了解AWS应用容器，点击此处<https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/index.html>