# 流程版本 | AWS BPMN2 Process参考指南

# 流程版本

为保护已产生实例的流程正常运转，处于不同版本状态的流程给予建模人员的操作权限是不同的，AWS的流程版本分为三个互斥状态：

  * 设计状态版本（DESIGN）
  * 发布状态版本（RUN/RELEASE）
  * 关闭状态版本（CLOSED）

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/41.png)

  * 设计时刻差异
  * 运行时刻差异
  * 升级时刻差异

## 设计时刻差异

在建模设计时，不同版本开放的设计权限不同。

设计状态版本（DESIGN） | 发布状态版本（RUN/RELEASE） | 关闭状态版本（CLOSED）  
---|---|---  
\- 全设计功能  
\- 全属性配置  
\- 删除校验 | \- 部分设计功能  
-全属性配置  
\- 结构保护 | \- 全只读  
  
## 运行时刻差异

设计状态版本（DESIGN） | 发布状态版本（RUN/RELEASE） | 关闭状态版本（CLOSED）  
---|---|---  
\- 全功能 | \- 全功能 | \- 未运行完的实例继续运行  
  
当用户拥有该流程启动权限，在新建流程实例时，以下版本均可视：

  * 设计版
  * 运行版

> 流程级别为`子流程`的流程不可直接使用。

#### 流程定义ID和流程版本ID的区别

对于API开发者，这是一个重要概念。每个流程（包括不同的版本）模型都会分配一个不重复的`流程定义ID`，当流程模型被创建多个版本时，设计器会取第1个版本作为`流程版本ID`。

我们假设一个A流程的版本结构如下：

流程定义ID | 流程版本ID | 版本号  
---|---|---  
aaa | aaa | 1.0  
bbb | aaa | 2.0  
ccc | aaa | 3.0  
  
要为A流程创建实例，API代码可能如下:
    
    
    SDK.getProcessAPI().createProcessInstance("aaa", uid, title);
    

如上场景是我们推荐的，即送入`流程版本ID`作为启动流程API的`processDefId`参数值。当用户停用了1.0版本，部署2.0版本时，createProcessInstance方法仍然能够智能的对应到`bbb`模型。也就是说，`流程版本ID`的出现，避免了开发者硬代码对特定流程模型的锁定。

如果将`bbb`或者`ccc`作为API参数值，createProcessInstance方法会强行执行该版本的模型定义，无论该流程是否有了新的版本。

**在设计器查看流程版本ID:**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/42.png)

**使用API查询流程的版本ID：**
    
    
    //送入一个流程模型ID，获得该模型的版本ID
    SDK.getRepositoryAPI().getProcessVerId(processDefId);
    

## 升级时刻差异

完整的AWS PaaS系统包括`DEV`、`QAS`和`PRD`三类部署环境，分别用于应用开发、质量保证和生产运行。与其他AWS PaaS的元数据模型一样，在DEV或QAS`dist`打包的版本升级到`PRD`环境时，含有`受管(Managed)`的流程模型将直接覆盖到生产环境。

## 延伸阅读

  * [设计器语法校验](<semantics_validate.html>)
  * [AWS PaaS的平台版本环境](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/version/README.html>)
  * [受管应用](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>)
  * [SDK的ProcessAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/ProcessAPI.html>)