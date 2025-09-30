# WCP12-Multiple Instances without Synchronization(异步多例) | AWS 流程引擎对WCP的支持评估

## WCP12-Multiple Instances without Synchronization(异步多例)

在某一流程实例中，某个任务会创建多个实例。这个任务实例相互依赖并且同时执行，但是不需要同时完成。多实例任务创建的实例要在同一流程实例的环境中执行（即它们使用相同的标识符，访问相同的数据元素），这些任务实例独立执行，与触发它们的任务无关。

  * 在同一流程中，创建多个独立实例，这些实例的完成不需要同步。
  * 例如警署收到报案，每收到一次报案创建一次任务列表。这些任务并行运行完成，不触发任何后续任务。他们不需要同步完成。

## 解决方案

### 场景设计

  * “节点1”任务允许进行传阅

### 流程建模

![](https://docs.awspaas.com/reference-guide/aws-paas-wcp-reference-guide/part5/wcp12-process-model.png)

> 可以在`工作流控制模式概念验证`应用的`流程模型>5.Multiple Instance Patterns(多实例模式)>WCP12-Multiple Instances without Synchronization(异步多例)`中访问该流程模型

### 引擎执行

  * 确认已安装`工作流控制模式概念验证`应用，访问前端`WCP概念验证`菜单入口
  * 在左侧树中点击`WCP12-Multiple Instances without Synchronization(异步多例)`项
  * 在列表中点击`新建`按钮，流程实例被创建
  * 此时，“节点1”已经创建一个任务实例，点击`传阅`按钮，可以生成任务实例，点击`办理`按钮，完成任务

> 如果列表中未出现`新建`按钮，请首先为此用户设置可启动该流程的权限