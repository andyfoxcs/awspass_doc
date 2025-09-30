# 网关（Gateways） | AWS BPMN2 Process参考指南

# 网关（Gateways）

Gateway是BPMN2规范中的流程定义元素，中文可称为“网关”、“决策”、“判断”。网关用来控制流程的执行流向，当在拆分路径时产生令牌，在合并路径时消费令牌。常用网关可分为排他网关（XOR）、并行网关（AND）和包容网关（OR）。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/events.png)

### 清单

BPMN2 | 名称 | 说明  
---|---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/2.png) | [Exclusive Gateway  
排他网关](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/exclusive_gateway/README.html>) | 排他网关定义了一组分支的唯一决策，  
所有流出的分支被顺序评估，  
第一个条件被评估为true的分支被执行，  
并不再继续评估下面的分支  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/3.png) | [Parallel Gateway  
并行网关](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/parallel_gateway/README.html>) | 并行网关根据前置连线或后继连线，  
无条件创建分支或回收分支  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/4.png) | [Inclusive Gateway  
包容网关](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/inclusive_gateway/README.html>) | 包容网关是排他网关和并行网关的综合体。  
当决策时，与排他网关所不同的是，  
所有条件为true的后继分支都会被执行  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/5.png) | [Complex Gateway  
复杂网关](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/complex_gateway/README.html>) | 复杂网关允许根据特定业务场景的需要，  
自定义路径拆分和收回算法  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/6.png) | [Event-Based Gateway  
事件网关](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/event-based_gateway/README.html>) | 仅适用于对后继路线拆分，该网关选择事件最先到达  
的路径（如时间事件、消息事件），取消其他分支