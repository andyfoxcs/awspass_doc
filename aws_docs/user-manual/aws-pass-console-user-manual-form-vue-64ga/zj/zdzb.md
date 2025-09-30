# 字段子表 · AWS PaaS文档中心

# 字段子表

创建一个带有增、删、改功能的子表控件，这是一个私有封装。在AWS PaaS表单模型中支持主子关系的数据源，但是并不能显示的设计主、子、孙子级关系的数据关系，字段子表的设计目标是解决这一实施障碍，将一个子表嵌套到另一个子表内。用于显示和修改被表单数据源绑定的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。使用该UI的字段类型可以是实体字段，也可以是虚拟字段。

> 目前该UI组件不支持移动端

## 运行

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/zdzb.png)](<zdzb.png>)  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/zdzb1.png)](<zdzb1.png>)  
  
## 配置字段子表属性

  * 添加`表格`后，在`表格属性`-`添加字段`选择`字段子表`添加
  * 然后点击`字段子表`,打开对应的属性，属性配置与表格中的五种表格配置相同，详见[表格](<bg.html>)配置

> 在AWS PaaS系统中主表与子表的关联关系由BO模型BINDID字段值自动关联，即主表和子表BINDID字段值相等，均为当前流程实例ID，而子表与字段子表的关联关系是由子表ID字段值与字段子表BINDID字段值自动维护，即字段子表中BINDID字段值为当前子表行记录值中ID字段值。