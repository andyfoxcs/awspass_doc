# 字段子表 | AWS UI组件参考指南

## 字段子表

创建一个带有增、删、改功能的子表控件，这是一个私有封装。在AWS PaaS表单模型中支持主子关系的数据源，但是并不能显示的设计主、子、孙子级关系的数据关系，字段子表的设计目标是解决这一实施障碍，将一个子表嵌套到另一个子表内。用于显示和修改被表单数据源绑定的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。使用该UI的字段类型可以是实体字段，也可以是虚拟字段。

> 目前该UI组件不支持移动端

### 运行

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fieldtableR1.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fieldtableR2.png)

> 字段子表UI组件仅适用于普通子表、Ajax子表

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fieldtableD2.png)

**基本属性**

  * **_查询列宽_**

不支持

  * **_帮助说明_**

不支持

  * **_扩展代码_**

不支持

**扩展属性**

  * **_数据源_**

数据源只能选择该存储所在的表单数据源中的子表，列表已经过滤了当前存储

### 实施步骤

**步骤一：**

创建主表BO模型A及结构

**步骤二：**

创建子表BO模型B及结构（该表某字段设置使用【字段子表】UI组件），例如： ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fieldtableD1.png)

**步骤三：**

为嵌套子表创建BO模型C及结构

**步骤四：**

创建主表单Form模型，将A挂接为主表、B、C挂接为子表

**步骤五：**

在子表BO模型B【字段子表】UI组件字段中设置数据源属性值为BO模型C表，完成实施

> 在AWS PaaS系统中主表与子表的关联关系由BO模型BINDID字段值自动关联，即主表和子表BINDID字段值相等，均为当前流程实例ID，而子表与字段子表的关联关系是由子表ID字段值与字段子表BINDID字段值自动维护，即字段子表中BINDID字段值为当前子表行记录值中ID字段值。