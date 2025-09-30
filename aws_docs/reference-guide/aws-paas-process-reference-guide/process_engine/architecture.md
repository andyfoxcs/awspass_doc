# 引擎架构 | AWS BPMN2 Process参考指南

# 引擎架构

  * 总体架构
  * 引擎架构
  * 运行数据

## 总体架构

从引擎的使用场景，可分为三层：

  1. API层
  2. 引擎层
  3. 定义层

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_engine/21.png)

#### 1\. API层

**引擎为外部接口开发者提供两种编程模型：**

  * [SDK API](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/api-basic/process_api.html>)（如查询任务、创建和启动流程）
  * [事件编程](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/index.html>)（如流程事件、任务事件）

**API访问和安全**

安全是指调用方在和AWS PaaS服务间网络传输的通讯安全，要求是AWS PaaS的Web层只允许接受SSL(Secure Sockets Layer 安全套接层)的处理请求。（AWS PaaS云实例已开启SSL）

API类型 | 网络层采取的安全控制  
---|---  
[ HTTP(s)](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/http/README.html>) | \- 每次对参数用私钥签名，防止中途篡改、恶意拼凑  
\- 对请求的timestamp进行检查，控制url存活有效期  
[SOAP](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/README.html>) | \- 对入站参数进行解密、签名验证  
\- 对出站结果进行加密、签名计算  
\- 控制服务请求的有效期  
[Java SDK](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/README.html>) | 本地处理，无需处理网络层安全隐患  
  
#### 2\. 引擎层

引擎层在架构上也被设计成插板式轻量级架构，所有BPMN2的行为实现和接口机制也基于该扩展实现。

引擎产生的运行数据（Runtime Data，又称为控制数据）不缓存。

**引擎对内部实现开发者提供可插拔的编程接口：**

  * [扩展人工任务路由方案](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/performer.html>)
  * [处理未知的外部任务](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/eai_task.html>)
  * 重新实现/扩展BPMN2行为
  * 重新实现SDK API

> 引擎层开发属于AWS内部编程。如果您对BPMN2规范和引擎内部处理机制的经验不足，不要扩展内部编程接口

#### 3\. 定义层

为了适应未来BPMN2新规范甚至替代规范的升级，AWS PaaS对流程定义设计了解耦层。无论是AWS自带的流程设计器还是采用第三方BPMN2规范，都必须通过一个名为`BPMNI/O`的转换层进行处理，并转换成引擎能正常执行的元结构。

为程序读写流程结构开放的仓库API示例
    
    
    //读取一个符合BPMN2.0的流程定义文件
    String schema=SDK.getRepositoryAPI().getBPMN(processDefId);
    
    //读取一个BPMN图
    byte[] diagram=SDK.getRepositoryAPI().getBPMNDiagram(processDefId, diagramType);
    

> 这是被缓存的一层，禁止绕过API对外部物理文件进行操作

## 引擎架构

AWS BPM PaaS的流程引擎内核是一个基于令牌消费的自动机，对API开发者和商业用户是一个黑盒子，无需熟知其原理。

不过，我们还是为希望进一步了解其工作原理的技术人员提供概念参考。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_engine/aws-bpm-engine.png)

当多个AWS节点集群时，可以组成更强大的并行流程引擎。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_engine/engine-cluster.png)

## 运行数据

流程运行数据又称为过程日志数据，记录引擎各种行为的处理过程。主要包括：

  1. 流程控制数据(Workflow Control Data,WFC_*)
  2. 流程历史数据(Workflow History Data,WFH_*)
  3. 流程归档数据(Workflow Archive Data,WFA_*)

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_engine/db.png)

## 延伸阅读

  * [流程建模规范](<../appendix/definition_spec.html>)
  * [流程引擎规范](<../appendix/engine_spec.html>)
  * [流程引擎表结构](<../appendix/tables.html>)
  * [开发者高级配置](<../appendix/advance_cfg.html>)
  * [AWS PaaS的API架构](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/architecture/README.html>)
  * [AWS PaaS私有安装集群架构](<https://docs.awspaas.com/reference-guide/aws-paas-cluster-reference-guide/architecture/overview.html>)