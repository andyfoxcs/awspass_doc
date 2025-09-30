# 基本信息 · AWS PaaS文档中心

## 流程信息

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/common_set1.png)](<common_set1.png>)

项 | 说明  
---|---  
流程名称 | 流程的名称  
流程说明 | 说明文字不超过120个文字  
设置图标 | 可自由设计图标，图标由iconFontCode,iconFontColor两部分组成 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/tb.png)](<tb.png>)  
  
**设置图标**

在这设计的图标保存后会同步到`导航菜单`、 `配置应用-移动入口`、`流程中心-发起流程-设置`这三个能设计图标的地方

### 用API更改任务优先级
    
    
    //设置任务优先级，该操作只允许更新活动的待办任务
    SDK.getTaskAPI().setPriority(taskInstId, priority);