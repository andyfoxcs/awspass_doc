# 前言 | AWS BPMN2 Gateway参考指南

# AWS BPMN2 Gateway参考指南

欢迎阅读这个文档！

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/events.png)

BPMN2.0对流程执行语义定义了三类基本要素，本文档将重点介绍[Gateway（网关）](<./gateways/README.html>)。

  * [Events（事件）](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/index.html>)
  * [Gateways（网关）](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/index.html>)
  * [Activities（活动）](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/index.html>)

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/bpmn2.png)

### BPMN2.0

BPMN2.0（Business Process Model & Notation <http://www.omg.org/bpmn/index.htm> ）是商业流程建模和执行的最新标准规范，已被ISO在2013年列入信息领域的模型标准。

BPMN2.0相对于旧的1.0规范以及XPDL、BPML、BPEL等最大的区别是定义了规范的执行语义和描述格式，利用标准的图元去建模真实的业务发生过程，保证相同的流程在不同的流程引擎得到的执行结果一致。

> 流程是AWS PaaS的核心服务，AWS PaaS 的流程建模和流程引擎完全基于最新的BPMN2规范。为了满足企业级客户对流程控制的灵活要求和高性能处理，我们会遵循BPMN扩展语法使用一些被称为 `AWS BPMN扩展`的功能, 它们并不属于BPMN 2.0规范。

## 适用于

本文档适合AWS PaaS应用开发者阅读。

## 声明

  * `炎黄盈动`、`Actionsoft`、`AWS`、`AWS CC`、`CoE`是北京炎黄盈动科技发展有限责任公司在中国的注册商标或产品字号
  * 本文档出现的一些商业产品名称、公司商号版权归相关拥有人，除非另行说明，本文档范例中涉及的公司、组织、产品、人物或事件均属虚构，并无意联系或暗示任何真实的公司、组织、产品、人物或事件