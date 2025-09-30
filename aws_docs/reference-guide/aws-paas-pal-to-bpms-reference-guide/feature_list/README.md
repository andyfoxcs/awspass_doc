# 连接业务与IT | AWS PAL流程梳理到执行参考指南

# 连接业务与IT

  * 团队组合
  * 分工协作
  * 工作场景

## 团队组合

在企业中，业务和IT是两类专业的人群，AWS PaaS的PAL和BPMS服务把这两类人员连接到一起。

这两类专业人员对企业实施流程管理同等重要，并在系统中需要具备如下技能经验：

#### 业务专家

业务专家团队可能会包括公司高管、流程专员、BA业务架构师、业务骨干、内外部的业务顾问。

  * 对本企业、部门业务和同行业运作有实际经验
  * 使用AWS PAL（经过自学摸索或专门培训，可以具备）
  * 流程梳理的方式方法（对需要系统执行的流程，重点掌握BPMN）

#### IT专家

IT专家团队可能包括BPM工程师、系统架构师、系统管理员、系统运维人员等。

  * 使用AWS BPM PaaS进行建模配置和开发（经过自学摸索或专门培训，可以具备）
  * 将BPM PaaS融入到企业IT环境的基础架构对接，建立开发和运维监控规范
  * 了解AWS企业应用商店的标准流程应用，为业务提供落地建议

## 分工协作

业务 | IT  
---|---  
建立和梳理流程 | 分配待执行的流程到BPMS  
**业务视角** ：梳理流程结构和描述，包括属性、绩效、风险等流程管理要素 | **技术视角** ：配置流程执行规则，包括与流程相关的存储、表单、事件、系统集成的实施/开发  
**发布流程** ：发布到PAL流程站点，用户可以学习流程制度规范 | **部署流程** ：部署到员工PC和移动门户，用户可以在系统执行流程  
**输出报告** ：流程手册、风控手册、RACI分析等文件 | **运行维护** ：功能优化、流程监控运维  
**分析流程** ：使用BPA/BAM分析和监控流程执行效率 | **分析流程** ：使用SLA分析流程服务的可靠性和性能  
  
## 工作场景

**共享一个BPMN流程文件**

  * **业务** 流程团队在PAL中，非技术属性的设置和操作
  * **IT** 技术团队在BPMS中进阶做流程配置和开发

业务 - 梳理流程 | IT - 配置流程  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/feature_list/1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/feature_list/2.png)  
业务 - 流程管理要素 | IT - 流程执行规则  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/feature_list/3.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/feature_list/4.png)  
业务 - 修改流程 | IT - 流程被修改  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/feature_list/5.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-pal-to-bpms-reference-guide/feature_list/6.png)