# 排他网关（Exclusive Gateway） | AWS BPMN2 Gateway参考指南

## 排他网关（Exclusive Gateway）

排他网关定义了一组分支的唯一决策，所有流出的分支被按顺序评估，第一个条件被评估为true（当多个条件为true时，第一个决策被执行）的分支被执行，并且不再继续评估下面的分支。如果所有分支条件决策都为false且该网关定义了一个默认的连线，那么该默认分支将被执行。如果没有可到达的分支，抛出异常，该网关所处的分支被中断，在流程建模设计上应避免这种情况发生。排他网关有分支和合并两种行为，允许一进一出。

下图给出一个排他网关的示例。网关A评估后继三个分支，如果变量var1等于1执行Service1路径，如果变量var1等于2执行Service3路径，如果都不通过执行Service2路径；如果Service1或Service2被执行，网关B做路径合并，后继Service4路径被执行，流程结束；如果Service3被执行，流程结束。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/exclusive_gateway/1.png)

### 排他拆分

顺序判断排他网关定义的每个分支连线的条件，但最多只有一个分支被执行。使用排他网关的分支连线必须设置条件规则，未设置规则的连线被评估为false。当分支被选择后，一个令牌被创建。如上图例子中，网关A只会选择三条路径的其中之一。

由于排他网关所有流出的分支按顺序评估，确定判断的顺序是非常重要的。打开网关属性对话框可查看执行顺序，通过拖动列表即可完成先后次序的设置。

如果后继多个分支存在都不通过的情况，应该合理的选择一个默认路径，否则引擎执行到该网关的分支将被中断于此。

### 排他合并

只要前置分支有一个到达，该网关的后继路径被激活。这意味着使用排他网关做合并时，应使用在一进一出的场景。如果前置可能会有多个正在执行的分支（如使用了并行网关或包容网关做路径拆分），排他网关之后的路径将在每个分支到达时被重复实例化（除非这是你希望达成的预期结果，否则应避免这种情况的发生）。如在上图例子中，网关B只会等待Service1或Service2路径的其中一条到达，Service4路径即被执行。

### 常见用法

示例 | 说明  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/exclusive_gateway/2.png) | N选一，同意执行一条路径，不同意执行另一条路径  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/exclusive_gateway/3.png) | A、B、C三个分支只要一条被执行，D分支即被执行