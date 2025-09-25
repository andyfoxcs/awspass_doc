# 开始事件（None Start Event）

常规的开始事件，不指定事件的起因，由API触发。

### 图形符号

| 单开始                                                       | 多开始                                                       |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/11.png) | ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/12.png) |

> 子流程通常是None Start Event的普通开始事件

### 选项开关

无

### API使用场景

开始事件（NoneStartEvent）不需要指定触发条件，由API触发。

```java
//启动流程实例并查询实例化的任务实例
List<TaskInstance> taskInsts=SDK.getProcessAPI().start(processInst).fetchActiveTasks();

//从指定的开始事件启动流程实例并查询实例化的任务实例
List<TaskInstance> taskInsts=SDK.getProcessAPI().start(processInst,startEventDefId).fetchActiveTasks();

//processBusinessKey,外部业务系统数据主键标识值或一个组合值，在工作流引擎实例表中全局不能重复
ProcessExecuteQuery query=SDK.getProcessAPI().startByBusinessKey(processBusinessKey);
```

### 客户端使用场景

通常一个流程只包含一个开始，在流程启动时会忽略选择开始事件的画面。AWS提供的标准流程客户端也是基于SDK API的封装。

| 多开始启动                                                   |
| :----------------------------------------------------------- |
| ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/13.png) |

| 从开始事件1启动                                              | 从开始事件2启动                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/14.png) | ![img](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/startevents/15.png) |

### 延伸阅读

- [启动流程对版本的选择](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/appendix/process_model_version.html)