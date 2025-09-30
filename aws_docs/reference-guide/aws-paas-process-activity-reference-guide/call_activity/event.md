# 事件触发器 | AWS BPMN2 Activity参考指南

# 事件触发器

事件遍布在流程实例的全生命周期范围之内。调用子流程（Call Activity）在创建和执行过程中，可以触发开发者的Java代码，通常是空跑事件。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/code.png)

> 注意：程序员开发的事件Java类，编译后的jar包资源必须与该流程模型处于同一个AWS PaaS应用

### 延伸阅读

  * [了解CALLACTIVITY_BEFORE_SUBPROCESS_START事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/callactivity_event/callactivity_before_subprocess_start.html>)
  * [了解CALLACTIVITY_AFTER_SUBPROCESS_COMPLETE事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/callactivity_event/callactivity_after_subprocess_complete.html>)
  * [节点通用事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/activity_event/README.html>)
  * [节点的异常处理](<exception.html>)