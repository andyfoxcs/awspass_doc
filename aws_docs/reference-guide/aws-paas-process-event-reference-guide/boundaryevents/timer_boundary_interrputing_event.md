# 边界时间事件 | AWS BPMN2 Event参考指南

# 边界时间事件（Timer Boundary Interrputing Event）

当执行到达`边界时间事件`依附的任务时（如[人工任务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/README.html>)、[系统任务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/README.html>)、[子流程](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/README.html>)），引擎会创建一个定时器，当定时器触发后，流程沿`边界时间事件`的后继路线继续执行。如果该边界事件设置为`中断`，依附的任务将中断执行。

该事件到达后会在`WFC_TASK`表创建一个类型为`catchEvent`的记录，定时器被正常触发后，状态标记为`complete`归档到历史表。如果在定时器未触发器执行了特例处理（如流程终止、流程取消），状态标记为`terminate`（或对应的标记值）归档到历史表

> 当包含`边界时间事件`的流程新版本被发布后，处于活动的旧版本的定时器会继续执行，直至旧版本不再有新的实例产生

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/boundaryevents/11.png)

### 选项开关

**简单时间**

  * 间隔执行无限次
  * 间隔执行N次
  * 指定的有效期时段

> 间隔是一个可以折算成秒的定值或[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。在到达该事件时，该值被确定。

**周期时间**

  * 每天
  * 每周
  * 每月
  * Cron表达式
  * 指定的有效期时段

**是否中断**

如果中断，附加的活动（任务）实例被终止，执行该事件的后继路线

### API使用场景

边界时间事件（TimerBoundaryInterrputingEvent）由定时器自动触发，不需要API。

> 可以在后台的`实例运行管理`管理事件的任务实例