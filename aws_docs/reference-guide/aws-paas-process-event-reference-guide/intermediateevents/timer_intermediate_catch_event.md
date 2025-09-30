# 捕获时间事件 | AWS BPMN2 Event参考指南

# 捕获时间事件（Timer Intermediate Catch Event）

当执行到达`捕获时间事件`时中断在这里，引擎会创建一个定时器，当定时器触发后事件结束，流程沿后继路线继续执行。

该事件到达后会在WFC_TASK表创建一个类型为`catchEvent`的记录，定时器被正常触发后，状态标记为`complete`归档到历史表。如果在定时器未触发器执行了特例处理（如流程终止、流程取消），状态标记为`terminate`（或对应的标记值）归档到历史表

> 当包含`捕获时间事件`的流程新版本被发布后，处于活动的旧版本的定时器会继续执行，直至旧版本不再有新的实例产生

### 图形符号

![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/11.png)

### 选项开关

一个可以折算成秒的定值或[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。在到达该事件时，该值被确定。

### API使用场景

捕获时间事件（TimerIntermediateCatchEvent）由定时器自动触发，不需要API。

### 客户端使用场景

等待时 | 执行完毕  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/12.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/intermediateevents/13.png)  
  
> 可以在后台的`实例运行管理`管理事件的任务实例