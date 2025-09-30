# 扩展属性 | AWS BPMN2 Activity参考指南

# 扩展属性

  * 对任务实例设置高级分类
  * 扩展流程节点结构属性

### 实例高级分类

实例高级分类能够按业务域、组织区域等维度分类流程和任务实例。系统提供最多四个大维度的分类，每个维度都可以单独开启或关闭：

  * 业务域-IOBD（Instance Of Business Domain）
  * 组织区域-IOR（Instance Of Regional）
  * 系统区域-IOS（Instance Of System）
  * 自定义-IOC（Instance Of Customize）

#### 用API动态指定实例高级分类
    
    
    //设置业务域类型
    SDK.getProcessAPI().setIoX(processInstId, InstanceAdvanceExtendConst.TYPE_IOBD, valueId);
    
    //设置区域类型
    SDK.getProcessAPI().setIoX(processInstId, InstanceAdvanceExtendConst.TYPE_IOR, valueId);
    
    //设置系统类型
    SDK.getProcessAPI().setIoX(processInstId, InstanceAdvanceExtendConst.TYPE_IOS, valueId);
    
    //设置扩展类型
    SDK.getProcessAPI().setIoX(processInstId, InstanceAdvanceExtendConst.TYPE_IOC, valueId);
    

> 这是一个AWS流程引擎高级特性的增强，对于统一流程平台服务的客户，建议安装和规划该应用的使用。 详细介绍请访问 <https://docs.awspaas.com/apps/com.actionsoft.apps.addons.iox/>

### 属性扩展

可以在设计阶段，为任务的定义扩展自定义的配置项，这些扩展属性能够在开发者事件编程中引用。

扩展属性以Key/Value键值对表达。键名提供了3个特殊的关键字，如果给定为`EXT1`,`EXT2`,`EXT3`，在任务创建时，会将对应的值存入该实例对应字段。

#### 用API获取扩展属性
    
    
     //获取该流程“键”对应的值
    SDK.getRepositoryAPI().getProcessExtendAttribute("流程定义ID", "属性键名");
    
    //获取该流程全部扩展属性定义，一个JSON串
    SDK.getRepositoryAPI().getProcessExtendAttribute("流程定义ID");
    
    //获取该节点“键”对应的值
    SDK.getRepositoryAPI().getActivityExtendAttribute("流程定义ID", "节点定义ID", "属性键名");
    
    //获取该节点全部扩展属性定义，一个JSON串
    SDK.getRepositoryAPI().getActivityExtendAttribute("流程定义ID", "节点定义ID");
    
    //获取该流程各个节点全部扩展属性定义，一个JSON串
    SDK.getRepositoryAPI().getActivityExtendAttribute("流程定义ID");
    

### 延伸阅读

  * [实例高级分类管理产品发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.iox/>)