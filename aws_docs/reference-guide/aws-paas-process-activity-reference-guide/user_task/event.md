# 事件触发器 | AWS BPMN2 Activity参考指南

# 事件触发器

事件遍布在流程实例的全生命周期范围之内。人工任务（User Task）在创建和执行过程中，可以触发开发者的Java代码，通常是空跑事件。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/code.png)

> 注意：程序员开发的事件Java类，编译后的jar包资源必须与该流程模型处于同一个AWS PaaS应用

## 延伸阅读

  * [节点通用事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/activity_event/README.html>)
  * [人工任务专有事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/usertask_event/README.html>)
  * [流程表单事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/README.html>)
  * [在事件Java代码中如何输出业务对话](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/appendix/message.html>)