# 人工任务专有事件 | AWS 流程事件开发参考指南

## 人工任务专有事件

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/usertask_event/1.png)

UserTask（人工任务节点）的处理过程更加复杂，如上图所示。当节点推进过程可以分为二个阶段：任务执行和节点离开。

  * （1）首先，当该人工节点即将产生任务时ACTIVITY_CONFIRM_PARTICIPANTS事件被触发；
  * （2）任务即将完成时，TASK_BEFORE_COMPLETE事件被触发，如果没有被中断将在任务实例完成后TASK_AFTER_COMPLETE事件被触发；
  * （3）如果处于多例并签或串签，依次处理和触发COMPLETE事件；
  * （4）节点进入离开处理阶段。首先ACTIVITY_BEFORE_LEAVE事件被触发，如果没有被中断ACTIVITY_ADHOC_BRANCH事件被触发，如果未定义那么PROCESS_ACTIVITY_ADHOC_BRANCH流程全局事件被触发，确定后继分支后ACTIVITY_AFTER_LEAVE事件被触发，完成离开并向下推进。