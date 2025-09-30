# 前言 | AWS BPMN2 Process参考指南

# AWS BPMN2 Process参考指南

欢迎阅读这个文档！

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/BPMPaaS.png)

> “不积跬步，无以至千里；不积小流，无以成江海。” ----《荀子》

在全球产业链结构重塑和新兴经济对传统商业模式冲击下，用户以最直接方式体验和反馈企业的运营过程，企业是一个透明的大鱼缸。用户获得更高体验，企业获得更高的回报。对于高成长和大中型企业，企业的运作流程让其在所处行业竞争变得独一无二。

很少会有软件公司能够做到将一个产品持续15年，尤其是在日新月异的移动互联网时代。在继承中创新，作为AWS的下一代产品，AWS BPM PaaS采用全新引擎技术和流程规范，将我们十余年经验沉淀成创新、简单、可靠的产品和服务。

**流程设计即执行** 。AWS BPM PaaS为您的流程管理落地带来飙风的速度，让商业流程的执行和变化跟上用户的眼球和手指。

### 文档章节

  * [流程结构](<process_structure/README.html>)
  * [流程设计](<process_designer/README.html>)
  * [流程部署](<process_deployment/README.html>)
  * [流程引擎](<process_engine/README.html>)
  * [流程客户端](<process_client/README.html>)
  * [流程监控运维](<process_administrator/README.html>)
  * [流程API接口](<process_api/README.html>)
  * [附录](<appendix/README.html>)

### BPMN2.0

BPMN2.0（Business Process Model & Notation <http://www.omg.org/bpmn/index.htm> ）是商业流程建模和执行的最新标准规范，已被ISO在2013年列入信息领域的模型标准。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/bpmn2.png)

BPMN2.0相对于旧的1.0规范以及XPDL、BPML、BPEL等最大的区别是定义了规范的执行语义和描述格式，利用标准的图元去建模真实的业务发生过程，保证相同的流程在不同的流程引擎得到的执行结果一致。

> 流程是AWS PaaS的核心服务，AWS PaaS 的流程建模和流程引擎完全基于最新的BPMN2规范。为了满足企业级客户对流程控制的灵活要求和高性能处理，我们会遵循BPMN扩展语法使用一些被称为 `AWS BPMN扩展`的功能, 它们并不属于BPMN 2.0规范。

## 适用于

本文档适合AWS PaaS应用开发者、流程管理人员、BA业务架构师阅读。

## 声明

  * `炎黄盈动`、`Actionsoft`、`AWS`、`AWS CC`、`CoE`是北京炎黄盈动科技发展有限责任公司在中国的注册商标或产品字号
  * 本文档出现的一些商业产品名称、公司商号版权归相关拥有人，除非另行说明，本文档范例中涉及的公司、组织、产品、人物或事件均属虚构，并无意联系或暗示任何真实的公司、组织、产品、人物或事件