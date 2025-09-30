# 结束事件 | AWS BPMN2 Event参考指南

# 结束事件（End Event）

表示流程或分支的自然结束，什么都不做。当流程有多个分支路线被激活时，最后一个分支自然结束后，流程实例结束。

结束操作将流程实例的状态标记为`end`值，正常完成的任务状态标记为`complete`值。
    
    
    //流程结束后的状态常量
    ProcessRuntimeConst.INST_STATE_END
    
    //任务结束后的状态常量
    TaskRuntimeConst.INST_H_STATE_COMPLETE
    

### 图形符号

单结束 | 多结束  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/11.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/12.png)  
  
### 选项开关

  * 通知提醒人范围

### API使用场景

结束事件（EndEvent）由引擎自动触发，不需要API。

### 客户端使用场景

  * 当分支结束时，提示`分支结束`
  * 当流程结束时，提示`流程结束`

单结束 | 多结束  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/13.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/endevents/14.png)