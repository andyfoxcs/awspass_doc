# 扩展属性 · AWS PaaS文档中心

## 扩展属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/extended1.png)](<extended1.png>)

### 网关模式

仅当当前节点有多条出线时可用。这是一种隐性网关，需由流程设计者定义多条出现的运行模式。当选择包容分支或排他分支时，进而会执行多条出现的连线条件。有关网关的更多介绍参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/index.html>) 。

### 实例高级分类

需要安装并启用[实例高级分类管理](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.iox/index.html>)应用。

### 自定义属性

自定义属性是一种扩展。通过Key 、Value形式定义，开发者通过SDK.getRepositoryAPI().getActivityExtendAttribute(...)获取属性值。

  1. 系统内置了8个特殊Key`(EXT1,EXT2,EXT3...EXT8)`，会在实例创建时，将对应的值存入该实例的对应系统表字段中。
  2. 内置特殊键值`TASK_COMPLETE_CUSTOM_INFO`配置流程结束时提示信息