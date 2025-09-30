# WCP14-Multiple Instances with a Priori Run-Time Knowledge(运行期确定多例) | AWS 流程引擎对WCP的支持评估

## WCP14-Multiple Instances with a Priori Run-Time Knowledge(运行期确定多例)

在某一个流程实例中，某个任务可以创建多个实例。产生的实例的个数取决于一些运行时因素，包括状态数据、资源可用性和进程间通信，但在任务实例必须创建之前就知道了。一旦启动，这些实例是相互独立，并同时运行的。这些任务实例在完成时需要同步，任务实例都完成后，会触发后续任务。

  * 在同意流程中，一个任务的实例个数是动态的，即在设计时未知，而在运行期间所有实例需被执行前的某点才能知道其数目。
  * 在论文提交给期刊的审查过程中，评审论文的任务的执行次数根据论文的内容，裁判和作者的凭证来决定。评审过程只能当所有评论都完成了再继续。

## 解决方案

### 场景设计

  * “节点2”任务的参与者在“节点1”任务办理时指定，当所有参与者办理任务后，“节点2”任务才完成

### 流程建模

![](https://docs.awspaas.com/reference-guide/aws-paas-wcp-reference-guide/part5/wcp14-process-model.png)

> 可以在`工作流控制模式概念验证`应用的`流程模型>5.Multiple Instance Patterns(多实例模式)>WCP14-Multiple Instances with a Priori Run-Time Knowledge(运行期确定多例)`中访问该流程模型

### 引擎执行

  * 确认已安装`工作流控制模式概念验证`应用，访问前端`WCP概念验证`菜单入口
  * 在左侧树中点击`WCP14-Multiple Instances with a Priori Run-Time Knowledge(运行期确定多例)`项
  * 在列表中点击`新建`按钮，流程实例被创建
  * 此时，“节点1”已经创建一个任务实例，点击`办理`按钮，完成任务，此时指定“节点2”的办理者
  * 多个办理者会同时收到任务，只有所有办理者都办理任务过后，“节点2”任务才完成，流程实例结束

> 如果列表中未出现`新建`按钮，请首先为此用户设置可启动该流程的权限