# 前言 | AWS 定时器开发参考指南

# AWS 定时器开发参考指南

欢迎阅读这个文档！

AWS PaaS的定时器（Job Scheduler）功能可用来定期执行一系列简单或复杂的程序任务，比如定时同步数据、对账、库存预警等。

开发者可以开发自己的任务逻辑，然后交给调度器，这些Job可在指定的周期重复执行，也可仅执行一次。

AWS PaaS的定时器基于[Quartz](<http://quartz-scheduler.org/>)并支持企业级集群。如果开发者熟悉Quartz编程，这里的概念和技术框架是相同的，您也可以通过互联网掌握更多Quartz开发技术。

> 现在，AWS PaaS使用[Quartz 2.2.1](<http://quartz-scheduler.org/documentation>)

### AWS PaaS支持的定时器类型

  * Job，常规定时任务
  * SOAP Job，定时访问SOAP Web服务
  * HTTP Job，定时访问HTTP(s) Web服务
  * SQL Job，定时执行数据库SQL

本文档适用于AWS PaaS应用开发者阅读。

## 声明

  * `炎黄盈动`、`Actionsoft`、`AWS`、`AWS CC`、`CoE`是北京炎黄盈动科技发展有限责任公司在中国的注册商标或产品字号
  * 本文档出现的一些商业产品名称、公司商号版权归相关拥有人，除非另行说明，本文档范例中涉及的公司、组织、产品、人物或事件均属虚构，并无意联系或暗示任何真实的公司、组织、产品、人物或事件