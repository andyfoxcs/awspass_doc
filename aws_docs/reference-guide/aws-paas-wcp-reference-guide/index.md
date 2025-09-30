# 前言 | AWS 流程引擎对WCP的支持评估

# AWS 流程引擎对WCP的支持评估

欢迎阅读这个文档！

工作流是AWS PaaS对应用提供的核心服务。在国际上，工作流引擎的能力可以通过对工作流控制模式(Workflow Control Flow Patterns,简称WCP)覆盖度进行评估，一个好的工作流引擎对模式的覆盖度也会越多。

工作流模式就像我们中国太极拳的拳术套路、招式。通过对模式的组合运用，就可以完美贯穿业务流程的典型处理场景。

![](https://docs.awspaas.com/reference-guide/aws-paas-wcp-reference-guide/taiji.png)

## WCP

![](https://docs.awspaas.com/reference-guide/aws-paas-wcp-reference-guide/WCP.png)

<http://www.workflowpatterns.com/patterns/control/>

WCP可以被理解成一组高度抽象的工作流业务场景。在2003年率先由Arthur教授等人提出了20个控制模式，随着研究的深入开展和实践，到了2006年在原有的基础上总结出43个控制模式。

## 适用范围

本文档适合AWS PaaS应用开发者、流程管理人员、BA业务架构师阅读。

我们发布了一个与本文档配套的App应用 `工作流控制模式(WCP)概念验证`，可登录AWS企业应用商店免费获取。

> ![](https://docs.awspaas.com/reference-guide/aws-paas-wcp-reference-guide/wcp-app.png)

## 声明

  * 炎黄盈动、Actionsoft、AWS、AWS CC、CoE是北京炎黄盈动科技发展有限责任公司在中国的注册商标或产品字号
  * 本文档出现的一些商业产品名称、公司商号版权归相关拥有人，除非另行说明，本文档范例中涉及的公司、组织、产品、人物或事件均属虚构，并无意联系或暗示任何真实的公司、组织、产品、人物或事件