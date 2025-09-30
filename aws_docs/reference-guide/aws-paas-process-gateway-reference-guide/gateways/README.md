# 网关（Gateway） | AWS BPMN2 Gateway参考指南

## 网关（Gateway）

Gateway是BPMN2规范中的流程定义元素，中文可称为“网关”、“决策”、“判断”。网关用来控制流程的执行流向，当在拆分路径时产生令牌，在合并路径时消费令牌。常用网关可分为排他网关（XOR）、并行网关（AND）和包容网关（OR）。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/1.png)

### 使用

从面板拖放一个网关 | 创建连线时选择一个网关  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/11.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/12.png)  
改变网关类型 | 复制网关  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/13.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/14.png)  
  
### 清单

BPMN2 | 名称 | 说明  
---|---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/2.png) | [Exclusive Gateway  
排他网关](<../exclusive_gateway/README.html>) | 排他网关定义了一组分支的唯一决策，  
所有流出的分支被顺序评估，  
第一个条件被评估为true的分支被执行，  
并不再继续评估下面的分支  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/3.png) | [Parallel Gateway  
并行网关](<../parallel_gateway/README.html>) | 并行网关根据前置连线或后继连线，  
无条件创建分支或回收分支  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/4.png) | [Inclusive Gateway  
包容网关](<../inclusive_gateway/README.html>) | 包容网关是排他网关和并行网关的综合体。  
当决策时，与排他网关所不同的是，  
所有条件为true的后继分支都会被执行  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/5.png) | [Complex Gateway  
复杂网关](<../complex_gateway/README.html>) | 复杂网关允许根据特定业务场景的需要，  
自定义路径拆分和收回算法  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/6.png) | [Event-Based Gateway  
事件网关](<../event-based_gateway/README.html>) | 仅适用于对后继路线拆分，该网关选择事件最先到达  
的路径（如时间事件、消息事件），取消其他分支  
  
### 各种网关结构组合

Gateway的基本结构约定：

  * 网关必须有一个或多个输入连线（Incoming）
  * 网关必须有一个或多个输出连线（Outgoing）

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/7.png)

### 拆分（Fork）

从网关流出（Outgoing）的连线（Sequence Flow）被称为路径拆分，每个连线在流程结构上表达了一个执行路径，拆分对应了流程引擎的Splitting(Branch)行为。根据BPMN2规范要求，不同类型的网关，对路径拆分的决策评估模式是不同的。连线支持条件规则的设定，但是当使用并行网关时，设置的条件规则被忽略。

### 合并（Join）

所有指向（Incoming）该网关的连线被称为路径合并，合并在流程结构上表达了对一个执行路径的等待，对应流程引擎的Merging行为。根据BPMN2规范要求，不同类型的网关，对执行路径的等待处理模式是不同的。被合并的连线不需要进行规则设定。

### 拆分与合并的组合

通常网关是成对出现的，通过网关的拆分和合并组合出各种流程编排模式。但这种组合是受BPMN2规范和语法约束的，不支持的错误搭配会由流程设计器给出警告，而对于那些由运行时刻动态决策的模式，则需要有经验的流程顾问和技术人员的综合判断。AWS流程设计器和引擎支持的组合模式如下表所示。网关下方有流出箭头的代表拆分行为，下方有流入箭头的代表合并行为。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/8.png)

  * YES 表示稳定的结构，没问题
  * MAYBE 表示运行时动态决策，不确定
  * / 表示不支持该类组合

### 一个网关，即执行拆分又执行合并

以下场景是等效的

A合并通过后，执行B的拆分 | A合并通过后，执行A的拆分  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/9.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/gateways/10.png)