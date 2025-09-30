# 表单应用 | AWS BPMN2 Activity参考指南

# 表单应用

表单是用户与任务交互的界面，界面由表单模板、BO数据和权限规则驱动。特殊情况下，外部的URL页面也可以作为一种表单类型绑定到人工任务上。

  * PC浏览器表单
  * 平板电脑表单（H5）
  * 手机表单（H5）

> 如果实际的应用只用到AWS流程引擎，此部分可忽略

### 主要配置项

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/10.png)

  * 绑定一个或多个AWS表单
  * 对字段的读、写、隐藏权限进行配置
  * 对子表记录的增、删、改权限进行配置
  * 对子表的导入、导出策略进行配置

绑定多表单 | 运行时刻效果  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/11.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/user_task/12.png)  
  
### 用API获得表单执行界面
    
    
    //返回完整的带有工具栏的表单
    String page1 = SDK.getFormAPI().getFormMainPage(userContext, processInst, taskInst);
    
    //返回表单页面，不包含工具栏
    String page2 = SDK.getFormAPI().getFormPage(userContext, processInstId,taskInstId,
    openState, currentPage, formDefId, boId);
    
    //返回带有工具栏的表单URL
    String url = SDK.getFormAPI().getFormMainURL(awsPortalHost, sid, processInstId,
    taskInstId,formDefId, openState);
    

### 用API实现表单数据的CURD操作
    
    
    //为指定的BO表新增记录
    SDK.getBOAPI().create(boName, recordData, processInst, userContext);
    
    //更新一条BO表记录
    SDK.getBOAPI().update(boName, recordData);
    
    //删除一条BO表记录
    SDK.getBOAPI().remove(boName, boId);
    
    //查询BO数据
    List<BO> list=SDK.getBOAPI().query("BO_ABX").listPage(firstRow, rowCount);
    

> 全部API文档，[参见这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)

### 延伸阅读

  * [流程表单事件](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/README.html>)