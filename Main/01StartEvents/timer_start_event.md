# 时间开始事件（Timer Start Event）

时间（定时）开始事件用来在指定的时间启动一个流程，也可以在指定周期内循环启动多次流程，例如每月1号凌晨2点开始启动账务结算处理流程。

当满足设定的时间条件时，`时间开始事件`被触发，流程被创建。

> 当包含`时间开始事件`的流程新版本被保存（或发布到生产环境）后自动创建定时器，旧版本的定时器将被暂停

### 图形符号

| 单开始                                                       | 多开始                                                       |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/21.png) | ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/22.png) |

### 选项开关

**简单时间**

- 间隔启动无限次
- 间隔启动N次
- 指定的有效期时段

> 间隔是一个可以折算成秒的定值或[@公式](https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html)。在到达该事件时，该值被确定。

**周期时间**

- 每天
- 每周
- 每月
- Cron表达式
- 指定的有效期时段

### API使用场景

时间开始事件（TimerStartEvent）由定时器自动触发，不需要API。