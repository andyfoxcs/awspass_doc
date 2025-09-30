# 节点通用事件 | AWS 流程事件开发参考指南

## 节点通用事件

根据不同类型的节点，AWS引擎定义了通用节点事件和专有节点事件。

通用节点事件能够被BPMN2的各种节点捕获，专有事件仅提供给特定类型的节点。特定节点包括：UserTask(人工任务)、CallActivity(调用子流程)等。

节点事件的处理过程如下图所示：

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/activity_event/1.png)

当节点推进过程可以分为二个阶段：任务执行和节点离开。

  * （1）任务即将完成时，TASK_BEFORE_COMPLETE事件被触发，如果没有被中断将在任务实例完成后TASK_AFTER_COMPLETE事件被触发；
  * （2）节点进入离开处理阶段。首先ACTIVITY_BEFORE_LEAVE事件被触发，如果没有被中断将检查后继分支后ACTIVITY_AFTER_LEAVE事件被触发，完成离开并向下推进。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/activity_event/2.png)

当任务实例尚未完成处理，任务实例发生挂起操作后TASK_SUSPEND事件被触发，任务实例进入挂起状态；直至恢复后TASK_SUSPEND事件被触发。