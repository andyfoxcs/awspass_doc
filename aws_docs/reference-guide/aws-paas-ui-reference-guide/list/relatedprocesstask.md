# 关联任务 | AWS UI组件参考指南

## 关联任务
    
    
    将与当前操作者相关的已办任务关联到当前表单，为领导决策提供与表单信息相关联的其他流程数据，这是一个私有封装。该组件在运行时为用户提供一个任务关联界面，实施该组件的字段类型应为文本型，将在数据库中存储关联任务的ID值。
    

>   1. 关联任务UI组件仅支持主表单，不支持子表
>   2. 当一个流程实例当前用户有多个已办任务时，只显示最后一个已办任务
> 

### 运行

PC端  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/relatedprocesstaskR1.png)   
  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/relatedprocesstaskR3.png)  
移动端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/relatedprocesstaskR1_m.png)  
      
    
        ###设计###
    
        ![](./relatedprocesstaskD1.png)
    
    
        **基本属性**
    

  * **_查询列宽_**

不支持

  * **_扩展代码_**

不支持

**扩展属性**

  * **_配置参数_**

    * 填写流程版本ID，多个时以逗号隔开
    * 不填写时，默认显示当前用户有权限查看的所有关联任务

> 流程版本ID可在流程模型列表中查看
> 
> ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/relatedprocesstaskD2.png)

  * **_包含任务_**

配置是否显示传阅任务

  * **_关联字典_**

选择一个[网格数据字典](<../appendix/dgriddictionary.html>)模型，该网格数据字典有如下要求：

    1. 查询数据源必须为BO模型数据源，且结果集必须有BINDID字段
    2. 必须要配置BINDID关系映射到当前表单某个字段(可为隐藏字段，注意不是当前关联流程任务字段)，，且必须支持模糊过滤

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/relatedprocesstaskD3.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/relatedprocesstaskD4.png)

  * **_回调事件_**

选择任务之后回调事件，开发人员可以在表单里实现如下JS函数

    
    
        /**
          * 选中事件
          *
          * @param {String} boName BO表名
          * @param {String} boItemName 字段名
          * @param {JSONArray} jsonArrayVal 选择任务的JSON数组结构数据
          */
        function onTaskSelectedEvent(boName, boItemName, jsonArrayVal) {
          //事件处理代码
        }
    

> 关联字典、回调事件仅支持AWS 6.2.14及后续版本