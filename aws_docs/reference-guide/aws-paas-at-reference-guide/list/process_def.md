# 模型 | AWS @公式参考指南

# 模型

  * processDefId
  * processDefName
  * processDefVersionId
  * processDefGroupId
  * processDefGroupName
  * processDefAppId
  * processDefDurationTime
  * processDefWarningTime
  * activityDefId
  * activityDefNo
  * activityDefName
  * activityDefDurationTime
  * activityDefWarningTime
  * activityDefExt
  * formDefId
  * formItemDefId
  * boItemPropVal

## processDefId

**_语法_**

@processDefId(_contextType,contextId_)

  * 流程定义Id
  * 当流程版本切换时，流程定义Id是不同的

**_参数_**

  * _contextType_ （可选）常量：id、businessKey
        
        - 如果值为id时，从一个流程实例Id查询流程实例
                   - 如果值为businessKey时，从一个业务主键查询流程实例
        

  * _contextId_ （可选)当contextType给定时，必填）对应contextType的值
        
        - 如果contextType为id，该值必须给定一个的流程实例Id
                  - 如果contextType为businessKey，该值必须给定一个业务主键
        

**_例子_**
    
    
    当前流程实例的流程模型Id是@processDefId
    

## processDefName

**_语法_**

@processDefName(_contextType,contextId_)

  * 流程定义名称
  * 当流程版本切换时，流程定义Id是不同的

**_参数_**

  * _contextType_ （可选）参见@processDefId参数说明

  * _contextId_ （可选）参见@processDefId参数说明

**_例子_**
    
    
    当前流程实例的流程模型名称是@processDefName
    
    当前流程父流程实例的流程模型名称是@processDefName(id,@processParentId)
    

## processDefVersionId

**_语法_**

@processDefVersionId(_contextType,contextId_)

  * 流程版本Id
  * 当流程版本切换时，流程定义Id是不同的

**_参数_**

  * _contextType_ （可选）参见@processDefId参数说明

  * _contextId_ （可选）参见@processDefId参数说明

**_例子_**
    
    
    当前流程实例的流程版本Id是@processDefVersionId
    

## processDefGroupId

**_语法_**

@processDefGroupId(_contextType,contextId_)

  * 流程组Id
  * 同一流程组的各个流程，流程组Id是相同的

**_参数_**

  * _contextType_ （可选）参见@processDefId参数说明

  * _contextId_ （可选）参见@processDefId参数说明

**_例子_**
    
    
    当前流程实例的流程组Id是@processDefGroupId
    

## processDefGroupName

**_语法_**

@processDefGroupName(_contextType,contextId_)

  * 流程组名称
  * 同一流程组的各个流程，流程组名称是相同的

**_参数_**

  * _contextType_ （可选）参见@processDefId参数说明

  * _contextId_ （可选）参见@processDefId参数说明

**_例子_**
    
    
    当前流程实例的流程组名称是@processDefGroupName
    

## processDefAppId

**_语法_**

@processDefAppId(_contextType,contextId_)

  * 应用Id

**_参数_**

  * _contextType_ （可选）参见@processDefId参数说明

  * _contextId_ （可选）参见@processDefId参数说明

**_例子_**
    
    
    当前流程实例的流程定义来自这个应用：@processDefAppId
    

## processDefDurationTime

**_语法_**

@processDefDurationTime(_contextType,contextId_)

  * 流程合理完成时限(毫秒)
  * 如果返回0表示未设置

**_参数_**

  * _contextType_ （可选）参见@processDefId参数说明

  * _contextId_ （可选）参见@processDefId参数说明

**_例子_**
    
    
    当前流程实例的合理完成时限要求是@processDefDurationTime毫秒以内
    

## processDefWarningTime

**_语法_**

@processDefWarningTime(_contextType,contextId_)

  * 流程宽延警告时限(毫秒)
  * 如果返回0表示未设置

**_参数_**

  * _contextType_ （可选）参见@processDefId参数说明

  * _contextId_ （可选）参见@processDefId参数说明

**_例子_**
    
    
    当前流程实例的宽延警告时限要求是@processDefWarningTime毫秒以内
    

## activityDefId

**_语法_**

@activityDefId(_taskInstId_)

  * 节点定义Id
  * 当流程版本切换时，节点定义Id是不同的

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务实例的节点模型Id是@activityDefId
    

## activityDefNo

**_语法_**

@activityDefNo(_taskInstId_)

  * 节点序号
  * 当流程被增加或删除节点后，序号可能被重新排列

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务实例的节点序号是@activityDefNo
    

## activityDefName

**_语法_**

@activityDefName(_taskInstId_)

  * 节点名称

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务实例的节点名称是@activityDefName
    
    前一个人工任务实例的节点名称是@activityDefName(@taskPreHumanTaskId)
    

## activityDefDurationTime

**_语法_**

@activityDefDurationTime(_taskInstId_)

  * 节点合理完成时限(毫秒)
  * 如果返回0表示未设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务实例的合理完成时限要求是@activityDefDurationTime毫秒以内
    

## activityDefWarningTime

**_语法_**

@activityDefWarningTime(_taskInstId_)

  * 节点宽延警告时限(毫秒)
  * 如果返回0表示未设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务实例的宽延警告时限要求是@activityDefWarningTime毫秒以内
    

## activityDefExt

**_语法_**

@activityDefExt(_taskInstId_)

  * 节点自定义扩展属性

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

## boItemPropVal

**_语法_**

@boItemPropVal(*boName,*fieldName,*prop)

  * 取BO模型字段扩展属性值

**_参数_**

  * _boName_ （必选）BO表名称

  * _fieldName_ （必选）字段名称

  * _prop_ （必选）属性扩展列名称

**_例子_**
    
    
    当前流程表单字段F1的值是@boItemPropVal(BO_ABC,F1,ZY)
    

## formDefId

**_语法_**

@formDefId

  * 当前表单模型定义Id
  * 从当前流程表单引擎的上下文中获得处于操作状态的表单模型Id

**_参数_**

无

**_例子_**
    
    
    无
    

## formItemDefId

**_语法_**

@formItemDefId

  * 当前表单子表模型定义Id
  * 从当前流程表单引擎的上下文中获得处于操作状态的表单子表模型Id

**_参数_**

无

**_例子_**
    
    
    无