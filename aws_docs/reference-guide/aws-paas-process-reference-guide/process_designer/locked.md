# 多人编辑 | AWS BPMN2 Process参考指南

# 多人编辑

  * PRD生产环境下的多人编辑
  * 团队开发下的多人编辑

## PRD生产环境下的多人编辑

使用AWS的流程设计器，无需考虑传统的版本同步问题（例如`Check In`、`Check Out`操作），在生产环境上真正实现`设计即执行`的便捷。

假设A用户正在打开X流程进行设计，此时B用户也打开X流程，B用户的设计器将**自动** 进入锁定模式：

  * 保持A用户对X流程的工作权限
  * 只读锁定B用户对X流程的操作

锁定B用户对X流程的操作  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/201.png)  
B用户如果强行获得编辑，A用户的画面**自动锁定**  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/202.png)  
  
## 团队开发下的多人编辑

多人开发模式下，流程模型以xml文件存储。建议将`%AWS-HOME%/apps/install`目录纳入版本管理系统（如SVN、Git、VSS）。

**位置**
    
    
    %AWS-HOME%/apps/install/%appId%/repository/process/