# WCP13-Multiple Instances with a Priori Design-Time Knowledge(设计期确定多例) | AWS 流程引擎对WCP的支持评估

## WCP13-Multiple Instances with a Priori Design-Time Knowledge(设计期确定多例)

在某一个流程实例中，某个任务可以创建多个实例。而产生的实例的个数在流程设计时就事先知道了。这些实例都是相互独立并且同时运行的。这些实例在完成时需要同步，实例都完成后，会触发后续任务。

  * 在同一流程中，同步完成在设计期设定好的实例个数。这些实例在完成是需要同步，实例都完成后，会触发后续任务。
  * 年度评审必须签署的六个导演都同意，才能发布。

## 解决方案

### 场景设计

  * “节点2”任务固定参与者，当所有参与者办理任务后，“节点2”任务才完成

### 流程建模

![](https://docs.awspaas.com/reference-guide/aws-paas-wcp-reference-guide/part5/wcp13-process-model.png)

> 可以在`工作流控制模式概念验证`应用的`流程模型>5.Multiple Instance Patterns(多实例模式)>WCP13-Multiple Instances with a Priori Design-Time Knowledge(设计期确定多例)`中访问该流程模型

### 引擎执行

  * 确认已安装`工作流控制模式概念验证`应用，访问前端`WCP概念验证`菜单入口
  * 在左侧树中点击`WCP13-Multiple Instances with a Priori Design-Time Knowledge(设计期确定多例)`项
  * 在列表中点击`新建`按钮，流程实例被创建
  * 此时，“节点1”已经创建一个任务实例，点击`办理`按钮，完成任务，此时“节点2”的办理者已经被确定
  * 多个办理者会同时收到任务，只有所有办理者都办理任务过后，“节点2”任务完成，流程实例结束

> 如果列表中未出现`新建`按钮，请首先为此用户设置可启动该流程的权限