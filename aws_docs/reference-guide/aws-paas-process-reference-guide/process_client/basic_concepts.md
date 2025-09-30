# 基本概念 | AWS BPMN2 Process参考指南

# 基本概念

流程客户端是最终用户处理工作流任务的交互入口。AWS默认的标准流程客户端经过十余年BPM用户需求沉淀，能够满足95%以上的企业用户需求。

  * 工作项
  * 工作台
  * 流程跟踪

流程客户端也是基[于AWS MVC编程框架](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/index.html>)和标准[SDK API](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/api-basic/process_api.html>)开发完成。

## 工作项

Worklist。工作项（又称为工作箱）是为流程提供的一组标准任务处理界面，参见标[准流程客户端](<../process_client/README.html>)。

  * 适用于单项业务集中处理
  * 流程设计人员功能测试

> 更高级的单项业务流程处理页面（如自定义数据项、查询），可使用AWS的[DW模型进行建模配置](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw/>)

**引擎API示例**
    
    
    //查询任务实例
    List<TaskInstance> list1=SDK.getTaskQueryAPI().target(uid).listPage(firstRow, rowCount);
    
    //查询流程实例
    List<ProcessInstance> list2=SDK.getProcessQueryAPI().listPage(firstRow, rowCount);
    

## 工作台

Workbench或者Workbox。工作项台汇聚了所有流程的任务处理，比工作项提供的功能更加强大，流程参与者可以在工作台中完成任务的全部工作。

  * 集中处理全部流程
  * 休假设置代理人

## 流程跟踪

跟踪流程的处理过程。流程跟踪将流程图和运行数据进行叠加，为用户提供直观的处理过程。

**引擎API示例**
    
    
    //获得一个流程跟踪页面的URL
    String url=SDK.getFormAPI().getFormTrackURL(bpmPortalHost, sid, processInstId);