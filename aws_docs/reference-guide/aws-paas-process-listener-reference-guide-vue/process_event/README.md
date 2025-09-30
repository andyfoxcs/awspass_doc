# 流程事件 | AWS 流程事件开发参考指南

## 流程事件

可以从流程启动、中间处理和结束三个阶段了解AWS的流程事件处理过程。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/1.png)

### 1.完成流程启动

如上图所示，在流程启动时被分为二个阶段：实例创建和启动。

  * （1）当流程即将启动时，PROCESS_BEFORE_CREATE事件被触发，如果没有被中断将在完成流程实例创建后PROCESS_AFTER_CREATE事件被触发，完成实例创建操作；
  * （2）如果后继存在可达的StartEvent（开始事件），那么将流程推进到开始节点后PROCESS_START事件被触发，完成实例启动；
  * （3）如果启动后继路线成立，流程进入到中间处理阶段。

### 2.中间处理

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/2.png)

当处理过程中（或结束后），流程实例发生删除操作前PROCESS_BEFORE_DELETE事件被触发，如果没有被中断将在完成流程实例删除后PROCESS_AFTER_DELETE事件被触发，完成流程实例删除操作。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/3.png)

当处理过程中，流程实例发生挂起操作后PROCESS_SUSPEND事件被触发，流程实例进入挂起状态；直至恢复后PROCESS_SUSPEND事件被触发。

### 3.结束流程实例

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/process_event/4.png)

流程实例在结束时将捕获一系列事件，如上图所示。

  * （1）当流程实例即将结束时PROCESS_BEFORE_COMPLETE事件被触发，如果没有被中断继续执行；
  * （2）此时如果操作来自“终止”，那么PROCESS_BEFORE_TERMINATE事件被触发。如果操作来自“取消”，那么PROCESS_BEFORE_CANCEL事件被触发。如果没有被中断继续执行，引擎完成结束处理后；
  * （3）对应于“终止”时PROCESS_AFTER_TERMINATE事件被触发，“取消”时PROCESS_AFTER_CANCEL事件被触发；
  * （4）最后PROCESS_AFTER_COMPLETE事件被触发，完成流程结束操作。