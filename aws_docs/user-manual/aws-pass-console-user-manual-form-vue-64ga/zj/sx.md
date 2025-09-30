# 树形表格 · AWS PaaS文档中心

# 树形表格

通过配置父子关系显示分层的数据表格的一种模式。其主要特性：

  * 树形结构显示
  * 操作特性与普通子表功能相似

## 运行

父子结构  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/treetable.png)](<treetable.png>)  
序号列  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/treetable1.png)](<treetable1.png>)  
  
## 树形表格配置

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/treetable2.png)](<treetable2.png>)

**树结构**

通过配置父子关系显示分层的数据表格,这种形成树结构的方式有两种：`父子结构` `序号列结构`

**父级字段**

选择父级字段

**子级字段**

选择子级字段

**树样式风格**

提供了5种风格，一种默认风格

**显示连线**

是否显示连线，默认不显示

> 显示连线开启后，`简洁表格`、`边框表格`样式失效

**显示图标**

默认不显示图标，`常态图标` `展开状态图标` `收起状态图标`都不显示，开启`显示图标`，这三种图标属性才显示

  * **常态图标**

即叶子节点图标，通过`设计图标选项卡`来配置`常态图标`

  * **展开状态图标**

父节点展开后显示的图标，通过`设计图标选项卡`来配置`展开状态图标`

  * **收起状态图标**

父节点收起后显示的图标，通过`设计图标选项卡`来配置`收起状态图标`

> 其他配置属性同[普通表格](<pt.html>)