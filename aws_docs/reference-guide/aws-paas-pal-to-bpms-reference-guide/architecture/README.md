# 技术架构演进 | AWS PAL流程梳理到执行参考指南

# 技术架构演进

  * 四层架构级别
  * 实现Leve3架构的方案
  * 关键技术 BPMN2.0

## 四层架构级别

在缺乏标准和工具方法下，集团企业的业务流程管理和执行系统是隔离的。而在信息化初期阶段，大部分的企业无需设立推动流程管理改进的专职岗位，流程被直接构建在BPM或专业系统中。

  * Leve0架构 - 业务流程独立在各系统
  * Leve1架构 - 业务流程集中在BPMS系统
  * Leve2架构 - 业务流程管理和BPMS执行相互独立
  * Leve3架构 - 业务流程管理和BPMS执行时时一致

> 并不是所有企业都需要达到Leve3架构，应当根据企业所处行业、规模来设定架构目标。例如对于大型集团企业和制造业，Leve3架构能够明显增强流程管理的灵活性，并大大降低流程管理的投入成本；而对于中小型和高成长阶段的企业，Leve1架构更加适合。

流程梳理到执行的一体化技术架构，彻底撕破了管理与IT两层皮的现状，是集团企业信息化架构演化的Top Level。这种演进与具体的支撑技术无关，如云、虚拟化、容器、移动、大数据等。

Leve0架构 - 业务流程独立在各系统 | 说明  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/architecture/1.png) | \- 业务流程独立在各系统，局部最优  
\- 每个系统有独立的流程设计和执行  
\- 数据和功能驱动，无法实现端到端的业务流执行和监控  
Leve1架构 - 业务流程集中在BPMS系统 | 说明  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/architecture/2.png) | \- 业务流程集中在BPMS系统，整体最优  
\- 为每个系统共享流程设计和执行服务  
\- 流程、数据和功能驱动的IT架构，全局执行和监控  
Leve2架构 - 业务流程管理和BPMS执行相互独立 | 说明  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/architecture/3.png) | -业务流程管理体系为BPMS执行提供依据  
\- 业务流程集中在BPMS系统，整体最优  
\- 为每个系统共享流程设计和执行服务  
\- 流程、数据和功能驱动的IT架构，全局执行、分析和监控  
Leve3架构 - 业务流程管理和BPMS执行时时一致 | 说明  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/architecture/4.png) | -流程体系文件直接与BPMS系统双向共享  
\- 业务流程集中在BPMS系统，整体最优  
\- 为每个系统共享流程设计和执行服务  
\- 流程、数据和功能驱动的IT架构，全局执行、分析和监控  
  
## 实现Leve3架构的方案

受限于技术、企业和厂商多种现实因素，对于一些企业，追求业务流程管理和IT执行系统的一致性，是困扰多年的路线障碍。

目前，在全球范围内的标杆企业也不多见，这是一个标准组织、厂商与企业都在积极探索的新领域。随着`BPMN2`规范的发布，Level3架构的实现已不再是空中楼阁。

厂商 | 实现方案 | 介绍  
---|---|---  
炎黄盈动 | AWS CoE 6 + AWS BPMS 6 | 轻量级一体化的下一代PaaS架构，  
支持公有云和私有安装部署  
IBM | IBM Blueworks Live + IBM BPM 8.5 | 混合云，两套独立产品的整合方案  
Oracle | Aris 9 + Oracle BPM 12c | 传统软件，两个厂商产品的整合方案  
  
## 关键技术 BPMN2.0

BPMN2.0（Business Process Model & Notation <http://www.omg.org/bpmn/index.htm> ）是商业流程建模和执行的最新标准规范，已被ISO在2013年列入信息领域的模型标准。

BPMN2.0相对于旧的1.0规范以及XPDL、BPML、BPEL等最大的区别是定义了规范的执行语义和描述格式，利用标准的图元去建模真实的业务发生过程，保证相同的流程在不同的流程引擎得到的执行结果一致。

> 流程是AWS PaaS的核心服务，AWS PaaS 的流程建模和流程引擎完全基于最新的BPMN2规范。为了满足企业级客户对流程控制的灵活要求和高性能处理，我们会遵循BPMN扩展语法使用一些被称为 `AWS BPMN扩展`的功能, 它们并不属于BPMN 2.0规范。