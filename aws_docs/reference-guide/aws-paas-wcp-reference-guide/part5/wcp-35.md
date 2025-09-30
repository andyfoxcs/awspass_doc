# WCP35-Cancelling Partial Join for Multiple Instances(取消部分多例合并，M选N) | AWS 流程引擎对WCP的支持评估

## WCP35-Cancelling Partial Join for Multiple Instances(取消部分多例合并，M选N)

在某一个流程实例中，某个任务可以创建多个并发实例（设为M）。实例的数目在第一个任务实例开始的时候就已经知道。一旦N个任务实例已经完成（其中N小于M），流程中的下一个任务被触发，同时剩余的M-N个实例会被取消。

  * 在同一流程中，同步完成在设计期定义好的创建实例个数和执行实例个数，并取消未执行实例。即当N个实例执行完，触发后面的任务执行后，没有执行完的M-N个实例会被取消。
  * 对500份蛋白质样品检查，前400份全部合格，则取消剩余样品的检查。

## 解决方案

### 场景设计

  * “节点1”任务办理时无须指定“节点2”任务的办理者
  * 多个办理者会同时收到任务，当所有办理者办理任务后，“节点2”任务才完成

### 流程建模

![](https://docs.awspaas.com/reference-guide/aws-paas-wcp-reference-guide/part5/wcp35-process-model.png)

> 可以在`工作流控制模式概念验证`应用的`流程模型>5.Multiple Instance Patterns(多实例模式)>WCP35-Cancelling Partial Join for Multiple Instances(取消部分多例合并，M选N)`中访问该流程模型

### 引擎执行

  * 确认已安装`工作流控制模式概念验证`应用，访问前端`WCP概念验证`菜单入口
  * 在左侧树中点击`WCP35-Cancelling Partial Join for Multiple Instances(取消部分多例合并，M选N)`项
  * 在列表中点击`新建`按钮，流程实例被创建
  * 此时，“节点1”已经创建一个任务实例，点击`办理`按钮，完成任务，此时“节点2”的参与者已经被确定
  * 多个办理者会同时收到任务，只要半数参与者完成办理任务，“节点2”任务完成，未办理的任务实例被取消，流程实例结束

> 如果列表中未出现`新建`按钮，请首先为此用户设置可启动该流程的权限