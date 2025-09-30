# 复杂合并 | AWS BPMN2 Gateway参考指南

## 复杂合并

### 1.基于条件的复杂合并

允许通过设置一个条件确定是否达成合并，例如您可以指定一个令牌（活动的前置输入连线）数量或要求完成数量的占比，一旦条件达成就取消其他分支继续向下执行（或忽略，当这些被忽略的活动分支到达网关时，mergeIncoming()方法会被再次触发）。

下图给出一个使用复杂网关进行合并路径的例子。当网关B执行合并时，如果flow1、flow2、flow3和flow4分支中的3个已到达网关B，就继续向下执行。同时设置通过后策略为：取消其他未完成的分支，避免剩余的活动分支执行完后再次激活网关B的合并行为。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/complex_gateway/4.png)

#### 设置汇聚令牌数

在上个示例中我们为复杂网关设置了汇聚令牌数量为3，这样，当达到这个数量时便不再等待其他活动的分支。如下图：

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/complex_gateway/5.png)

“汇聚令牌”可以设置一个完成数量（整值），也可以设置一个完成百分比（后缀为%的串，如25%）。如果此处提供了无效值，引擎将抛出异常。当开发者实现了“自定义算法”，该配置将不起作用。

### 2.基于代码的复杂合并

作为一个高级功能，编程人员可以通过实现ComplexGatewayInterface接口，编写mergeIncoming()方法来决定合并条件是否达成。mergeIncoming()方法会将引擎上下文对象和所有前置分支及已完成的前置分支作为参数提供给开发者，由开发者决定条件是否达成。

下图给出一个使用复杂网关进行合并路径的例子。当网关B执行合并时，如果flow1、flow2和flow3分支中的2条已到达网关B，就继续向下执行。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/complex_gateway/6.png)

#### 复杂网关（网关B）代码实现

这是重点要介绍的部分。在上述示例中，该网关开发了一个名为“ComplexGateway2Test”的Java类，针对这一特殊场景对mergeIncoming()方法进行了实现，代码如下：
    
    
    /**
     * 复杂网关-Merge Sample
     */
    public class ComplexGateway2Test implements ComplexGatewayInterface {
    
        /**
         * 汇聚前置分支
         *
         * @param ctx 引擎上下文
         * @param incomingSequenceFlows 前置分支定义
         * @param finishedSequenceFlows 已完成的前置分支
         * @return 符合聚合条件返回true
         */
        public boolean mergeIncoming(final BehaviorContext ctx, final List<SequenceFlowModel> incomingSequenceFlows, final List<SequenceFlowModel> finishedSequenceFlows) {
            if (finishedSequenceFlows.size() == 2) {
                return true;
            } else {
                return false;
            }
        }
    
        /**
         * 评估，返回后继分支路径
         *
         * @param outgoingSequenceFlows 后继分支定义
         * @return 要激活的后继分支连线，如果返回了null或一个空的List集合且该网关定义了一个默认的连线，那么该默认分支将被执行
         */
        public List<SequenceFlowModel> branchOutgoing(final BehaviorContext ctx, final List<SequenceFlowModel> outgoingSequenceFlows) {
            return outgoingSequenceFlows;
        }
    }
    

> 关于该代码的ComplexGatewayInterface 接口说明，可参见AWS SDK API的JavaDoc文档 <https://docs.awspaas.com/api/aws-api-javadoc/index.html>