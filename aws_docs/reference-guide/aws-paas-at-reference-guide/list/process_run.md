# 流程 | AWS @公式参考指南

# 流程

  * processId
  * processVar
  * processTitle
  * processBusinessKey
  * processParentId
  * processParentTaskId
  * processCreateUser
  * processCreateTime
  * processStartTime
  * processEndTime
  * processStatus
  * isProcessEnd
  * isSubProcess
  * processCostTime
  * processExpireTime
  * processExt1
  * processExt2
  * processExt3
  * processExt4
  * processExt5
  * processExt6
  * processExt7
  * processExt8
  * taskId
  * taskPreTaskId
  * taskPreHumanTaskId
  * TaskSameHuman
  * taskTitle
  * taskOwner
  * taskTarget
  * taskPriority
  * taskStatus
  * taskHumanType
  * taskDueTime
  * taskBeginTime
  * taskReadTime
  * taskEndTime
  * taskCostTime
  * taskExpireTime
  * taskExt1
  * taskExt2
  * taskExt3
  * taskExt4
  * taskExt5
  * taskExt6
  * taskExt7
  * taskExt8
  * isTaskEnd
  * processComment

## processId

**_语法_**

@processId(_businessKey_)

  * 流程实例Id
  * businessKey用来表示一个外部业务系统对象的全局不重复标识，通常由外部业务维护或一组关键业务标识组合。如订单系统的订单编号。该参数作为一个可选项，在由API创建流程时被初始化，默认不启用的

**_参数_**

  * _businessKey_ （可选）从对应该业务主键的流程实例获取Id

**_例子_**
    
    
    当前流程实例Id是@processId,CRM系统A订单的流程实例Id是
    @processId(ORDER-2014070888)
    

**_结果_**
    
    
    当前流程实例Id是a6314e95-5973-4876-90c8-89586ba539c5,CRM系统A订单的流程实例Id是
    8911e732-b42a-4556-853f-ad32761bcbee
    

## processVar

**_语法_**

@processVar(_*varName,contextType,contextId_)

  * 流程实例变量
  * businessKey用来表示一个外部业务系统对象的全局不重复标识，通常由外部业务维护或一组关键业务标识组合。如订单系统的订单编号。该参数作为一个可选项，在由API创建流程时被初始化，默认不启用的

**_参数_**

  * _varName_ （必选）流程变量名，注意区分大小写

  * _contextType_ （可选）常量：id、businessKey

    * 如果值为id时，从一个流程实例Id查询流程实例
    * 如果值为businessKey时，从一个业务主键查询流程实例
  * _contextId_ （可选)当contextType给定时，必填）对应contextType的值

    * 如果contextType为id，该值必须给定一个的流程实例Id
    * 如果contextType为businessKey，该值必须给定一个业务主键

**_例子_**
    
    
    当前流程变量p1的值是@processVar(p1)
    
    流程实例Id为999的流程变量p1的值是@processVar(p1,id,999)
    
    业务主键为ORDER-888的流程变量p1的值是@processVar(p1,businessKey,ORDER-888)
    
    当前流程父流程实例的变量p1值是@processVar(p1,id,@processParentId)
    

## processTitle

**_语法_**

@processTitle(_contextType,contextId_)

  * 流程实例标题

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程的标题是@processTitle
    
    流程实例Id为999的标题是@processTitle(id,999)
    
    业务主键为ORDER-888的标题是@processTitle(businessKey,ORDER-888)
    
    当前流程父流程标题是@processTitle(id,@processParentId)
    

## processBusinessKey

**_语法_**

@processBusinessKey(_contextType,contextId_)

  * 绑定流程实例的外部业务系统主键值
  * 如果未设置BusinessKey，在创建流程实例时会默认初始化一个36位长度的字符串

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程的业务主键是@processBusinessKey
    
    流程实例Id为999的业务主键是@processBusinessKey(id,999)
    
    业务主键为ORDER-888的业务主键是@processBusinessKey(businessKey,ORDER-888)
    
    当前流程父流程业务主键是@processBusinessKey(id,@processParentId)
    

## processParentId

**_语法_**

@processParentId(_contextType,contextId_)

  * 父流程实例Id

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程父流程Id是@processParentId
    
    流程实例Id为999的父流程Id是@processParentId(id,999)
    
    业务主键为ORDER-888的父流程Id是@processParentId(businessKey,ORDER-888)
    
    当前流程父流程Id是@processParentId(id,@processId)
    
    当前流程父流程的父流程Id是@processParentId(id,@processParentId(id,@processId))
    

## processParentTaskId

**_语法_**

@processParentTaskId(_contextType,contextId_)

  * 父流程任务实例Id

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程由父流程在任务Id为@processParentTaskId的任务中启动
    

## processCreateUser

**_语法_**

@processCreateUser(_contextType,contextId_)

  * 流程实例创建人

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程由@processCreateUser创建
    

## processCreateTime

**_语法_**

@processCreateTime(_contextType,contextId_)

  * 流程实例创建时间

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程在@processCreateTime时被创建
    

## processStartTime

**_语法_**

@processStartTime(_contextType,contextId_)

  * 流程实例启动时间

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程在@processStartTime时被启动
    

## processEndTime

**_语法_**

@processEndTime(_contextType,contextId_)

  * 流程实例结束时间

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程在@processEndTime时被结束，状态是@processStatus
    

## processStatus

**_语法_**

@processStatus(_contextType,contextId_)

  * 流程实例状态
  * 常见状态参考
    * Active：活动(运行中)
    * Suspend：挂起(暂停)
    * End：结束(正常)
    * Terminate：终止+结束

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程的状态是@processStatus
    

## processComment

**_语法_**

@processComment(*activityId,*policy,contextType,contextId)

  * 用户审批留言
  * 获得指定节点的审批留言。activityId为指定的节点Id；policy是要提取的属性，支持：time、menuName、comment、file常量，多个属性用竖线隔开
  * policy常见状态参考，多个属性用竖线隔开
    * time：审批留言的时间
    * menuName：审批留言的菜单名称
    * comment：留言内容
    * file：审批留言的附件
  * 审批留言中存放的是节点名称，根据activityId参数查到该节点和审批记录中的节点名称比对，找到第一个名称匹配的则不在继续寻找

**_参数_**

  * _activityId_ （必选）为指定的节点Id

  * _policy_ （必选）policy是要提取的属性，支持：time、menuName、comment、file常量，多个属性用竖线隔开

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前用户的审批留言是@processComment
    

## isProcessEnd

**_语法_**

@isProcessEnd(_contextType,contextId_)

  * 流程实例是否已结束，结束返回TRUE

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程结束了吗?@isProcessEnd
    

## isSubProcess

**_语法_**

@isSubProcess(_contextType,contextId_)

  * 流程实例是否是子流程，是返回TRUE

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程是子流程实例吗?@isSubProcess
    

## processCostTime

**_语法_**

@processCostTime(_contextType,contextId_)

  * 流程实例执行总耗时(毫秒)，该值在流程结束时自动统计

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程总共耗费了@processCostTime毫秒，折合@calc(@processCostTime/1000/60)分钟
    

## processExpireTime

**_语法_**

@processExpireTime(_contextType,contextId_)

  * 流程实例执行超时时间(毫秒)，该值在流程结束时自动统计
  * 默认建模的流程并未设置流程合理完成时限和警告时限，在这种情况下，超时时间不被统计

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    当前流程总共超时了@processExpireTime毫秒，折合@calc(@processExpireTime/1000/60)分钟
    

## processExt1

**_语法_**

@processExt1(_contextType,contextId_)

  * 流程实例扩展字段1的值
  * 该值可由SDK API设置或在流程扩展属性配置

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    无
    

## processExt2

**_语法_**

@processExt2(_contextType,contextId_)

  * 流程实例扩展字段2的值
  * 该值可由SDK API设置或在流程扩展属性配置

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    无
    

## processExt3

**_语法_**

@processExt3(_contextType,contextId_)

  * 流程实例扩展字段3的值
  * 该值可由SDK API设置或在流程扩展属性配置

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    无
    

## processExt4

**_语法_**

@processExt4(_contextType,contextId_)

  * 流程实例扩展字段4的值
  * 该值可由SDK API设置或在流程扩展属性配置

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    无
    

## processExt5

**_语法_**

@processExt5(_contextType,contextId_)

  * 流程实例扩展字段5的值
  * 该值可由SDK API设置或在流程扩展属性配置

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    无
    

## processExt6

**_语法_**

@processExt6(_contextType,contextId_)

  * 流程实例扩展字段6的值
  * 该值可由SDK API设置或在流程扩展属性配置

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    无
    

## processExt7

**_语法_**

@processExt7(_contextType,contextId_)

  * 流程实例扩展字段7的值
  * 该值可由SDK API设置或在流程扩展属性配置

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    无
    

## processExt8

**_语法_**

@processExt8(_contextType,contextId_)

  * 流程实例扩展字段8的值
  * 该值可由SDK API设置或在流程扩展属性配置

**_参数_**

  * _contextType_ （可选）参见@processVar参数说明

  * _contextId_ （可选）参见@processVar参数说明

**_例子_**
    
    
    无
    

## taskId

**_语法_**

@taskId

  * 任务实例Id

**_参数_**

无

**_例子_**
    
    
    当前任务实例Id是@taskId
    

## taskPreTaskId

**_语法_**

@taskPreTaskId(_taskInstId_)

  * 前一个任务实例Id
  * 如果已经是第1个任务，返回-1

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务是由@taskPreTaskId创建的
    

## taskPreHumanTaskId

**_语法_**

@taskPreHumanTaskId(_taskInstId_)

  * 前一个人工任务实例Id
  * 该操作向前寻找父任务（按实际运行的轨迹），直至寻找到最近的一个人工任务。如果没有返回-1

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务最近一个人工任务是@taskPreHumanTaskId
    

## taskTitle

**_语法_**

@taskTitle(_taskInstId_)

  * 当前任务标题

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务标题是@taskTitle
    
    前一个任务标题是@taskTitle(@taskPreTaskId)
    
    前一个人工任务标题是@taskTitle(@taskPreHumanTaskId)
    

## taskOwner

**_语法_**

@taskOwner(_taskInstId_)

  * 任务创建人账户

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务发起人是@taskOwner
    
    前一个人工任务发起人是@taskOwner(@taskPreHumanTaskId)
    

## taskTarget

**_语法_**

@taskTarget(_taskInstId_)

  * 任务执行人账户

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务办理人是@taskTarget
    
    前一个人工任务办理人是@taskTarget(@taskPreHumanTaskId)
    

## taskPriority

**_语法_**

@taskPriority(_taskInstId_)

  * 任务优先级
  * 值参考：
        
        - 0：低
          - 1：无
          - 2：中
          - 3：高
        

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务优先级是@taskPriority
    

## taskStatus

**_语法_**

@taskStatus(_taskInstId_)

  * 任务状态
  * 值参考：
        
        - active：活动（运行中）
          - suspend：挂起（暂停）
          - error：系统异常（非人工任务）
          - complete：完成
          - compensate：补偿
          - delete：删除
          - cancel：取消
          - terminate：终止结束
        

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务状态是@taskStatus
    

## taskHumanType

**_语法_**

@taskHumanType(_taskInstId_)

  * 人工任务的类型
  * 值参考：
        
        - 1：常规待办任务
          - 2：只读传阅任务【不影响流程推进】
          - 3：待办任务，从哪来回哪去
          - 4：只读等待任务，如等待作者修改
          - 9：系统通知任务【不影响流程推进】
          - 11：加签任务
        

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务类型是@taskHumanType
    

## taskDueTime

**_语法_**

@taskDueTime(_taskInstId_)

  * 任务实例的执行期限
  * 该值可由SDK API设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务的逾期时间是@taskDueTime
    

## taskBeginTime

**_语法_**

@taskBeginTime(_taskInstId_)

  * 任务实例的开始执行时间

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务开始执行时间是@taskBeginTime
    

## taskReadTime

**_语法_**

@taskReadTime(_taskInstId_)

  * 任务实例的第一次阅读时间

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务由执行人第一次阅读的时间是@taskReadTime
    

## taskEndTime

**_语法_**

@taskEndTime(_taskInstId_)

  * 任务实例结束时间

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务执行完毕的时间是@taskEndTime
    

## taskCostTime

**_语法_**

@taskCostTime(_taskInstId_)

  * 任务实例执行耗时(毫秒)，该值在任务结束时自动统计
  * 如果是人工任务，应用该账户的工作时间设置，忽略非工作时间

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务执行总耗时是@taskCostTime毫秒，折合@calc(@taskCostTime/1000/60)分钟
    

## taskExpireTime

**_语法_**

@taskExpireTime(_taskInstId_)

  * 任务实例执行超时(毫秒)，该值在任务结束时自动统计
  * 应用该账户的工作时间设置，忽略非工作时间
  * 默认建模的人工节点并未设置流程合理完成时限和警告时限，在这种情况下，超时时间不被统计

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    当前任务执行总超时了@taskCostTime毫秒，折合@calc(@taskCostTime/1000/60)分钟
    

## taskExt1

**_语法_**

@taskExt1(_taskInstId_)

  * 任务实例扩展字段1
  * 该值可由SDK API设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    无
    

## taskExt2

**_语法_**

@taskExt2(_taskInstId_)

  * 任务实例扩展字段2
  * 该值可由SDK API设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    无
    

## taskExt3

**_语法_**

@taskExt3(_taskInstId_)

  * 任务实例扩展字段3
  * 该值可由SDK API设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    无
    

## taskExt4

**_语法_**

@taskExt4(_taskInstId_)

  * 任务实例扩展字段4
  * 该值可由SDK API设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    无
    

## taskExt5

**_语法_**

@taskExt5(_taskInstId_)

  * 任务实例扩展字段5
  * 该值可由SDK API设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    无
    

## taskExt6

**_语法_**

@taskExt6(_taskInstId_)

  * 任务实例扩展字段6
  * 该值可由SDK API设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    无
    

## taskExt7

**_语法_**

@taskExt7(_taskInstId_)

  * 任务实例扩展字段7
  * 该值可由SDK API设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    无
    

## taskExt8

**_语法_**

@taskExt8(_taskInstId_)

  * 任务实例扩展字段8
  * 该值可由SDK API设置

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    无
    

## isTaskEnd

**_语法_**

@isTaskEnd(_taskInstId_)

  * 任务实例是否结束，如果已结束返回TRUE

**_参数_**

  * _taskInstId_ （可选） 从指定的任务实例中获取

**_例子_**
    
    
    无
    

## TaskSameHuman

**_语法_**

@TaskSameHuman(_*nextUserTaskDefId,isPerformer,taskInstId_)

  * 判断指定节点的办理人，如果相同返回TRUE

**_参数_**

  * _nextUserTaskDefId_ （必须） 节点定义ID
  * _isPerformer_ （可选） 是否只匹配执行人忽略可选人，默认false
  * _taskInstId_ （可选） 从指定的任务实例中获取，默认当前实例

**_例子_**
    
    
    无