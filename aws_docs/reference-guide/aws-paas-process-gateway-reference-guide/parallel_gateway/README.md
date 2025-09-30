# 并行网关（Parallel Gateway） | AWS BPMN2 Gateway参考指南

## 并行网关（Parallel Gateway）

并行网关用于无条件的拆分或合并分支，该类网关对连线条件是忽略的。并行网关有分支和合并两种行为，允许多进多出。

下图给出一个并行网关的示例。网关A拆分了三个分支，Service1和Service2执行完毕后被网关B合并继续执行Service4；网关C等待Service4和Service3执行完毕后，流程结束。(注：引擎执行并行分支时，同一时刻只执行一个路径直至该路径被中断或结束，然后再依次执行完剩余的路径，而不是在同一时刻同时执行Service1、Service2和Service3路径)

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/parallel_gateway/1.png)

### 并行拆分

并行网关的每个后继分支路径都被无条件执行。当一个路径被执行时，一个令牌被创建。如上图例子中，网关A会按建模的自然顺序一次执行完后继的三个分支。

### 并行合并

所有到达并行网关的分支路径都汇聚于此等待，直到每个输入流的分支都执行完毕，然后执行该网关的输出流，如果其中有分支未被执行或中断，那么该并行网关将处于永久等待状态。如在上图例子中，网关B会等待Service1和Service2路径的完成，网关C会等待Service4和Service3路径的完成。