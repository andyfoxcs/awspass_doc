# 关系映射 | AWS UI组件参考指南

## 关系映射

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/dictGxys1.png)

**目标类型**

目标类型有BO数据表和DW查询条件两种

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/dictrelate1.png)

>   1. 目标类型为BO数据表，应用于表单中的网格数据字典组件
>   2. 目标类型为[DW查询条件](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw/new_dw/query.html#griddictionary>)，目标字段为对应数据窗口模型中查询字段的UI组件为字典模型的列名称，参与数据回填 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/dictrelate2.png)
> 

项 | 说明  
---|---  
目标数据表 | 映射到表单数据源BO表名  
源字段名称 | 在源数据结构中合法的字段名  
目标字段名称 | 映射到表单数据源BO表中，合法的字段名（大写）  
若未设置该项，此列值仅显示给用户，不参与数据回写  
源字段类型 | 在源数据结构中字段类型  
UI类型 | 运行时，查询条件输入框展示形式  
● `文本` 一个Input输入框  
● `日期` 弹出日期选择组件  
● `日期时间` 弹出日期时间选择组件  
● `时间`弹出时间选择组件  
● `列表`一个下拉列表框  
● `地址簿`弹出地址簿选择框  
●  `树形字典`弹出下拉树框  
  
参考值配置 | 不同UI组件该属性配置不同  
列标题 | 网格中显示的该列的标题名称  
列宽度 | 网格中显示的该列的宽度，单位px（像素）  
是否隐藏 | 当值需要回填到表单，但不希望显示给用户看到时  
是否模糊过滤 | 当该字段值希望参与到[模糊查询](<../list/griddictionary.html#like>)时，只允许‘文本’类型字段参与模糊检索  
精确查询 | 当该字段值希望参与到[精确查询](<../list/griddictionary.html#dy>)时，‘文本、日期、数值’类型都可以参与精确查询  
DW查询列标识(仅在DW查询有效) | 当目标类型是DW查询条件时，配置映射后，该值会自动生成  
  
> 网格数据字典仅支持回填的字段UI类型为单行、多行、数值、货币、列表、单选组、复选组、日期、时间、日期时间、滑杆、开关、网格数据字典、地址簿、附件

### 精确查询

### 文本

**_参考值配置_**

  * 无

**_运行示例_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/input.png)

### 日期

**_参考值配置_**

  * 无

**_运行示例_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/data.png)

### 日期时间

**_参考值配置_**

  * 无

**_运行示例_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/datatime.png)

### 时间

**_参考值配置_**

  * 无

**_运行示例_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/time.png)

### 列表

**_参考值配置_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/selectD.png)

  * **常量** 列表值来源于固定值，语法格式：值1:显示1|值2:显示2...，支持@公式
  * **SQL数据源** 列表值来源于SELECT查询语句结果，支持@公式
  * **JSON数据** 详细参见<https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/combobox.html#json>
  * **键值字典** 列表值来源于基础字典，详细参见<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/reference/dw.html>

**_运行示例_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/selectR.png)

### 地址簿

**_参考值配置_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/dzb.png)

地址簿分为人员地址簿和部门地址簿两种,详细参见<https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/address.html#dzb>

**_运行示例_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/dzb_1.png)

### 树形数据字典

**_参考值配置_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/tree.png)

配置详细参见<https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/treedictionary.html>

**_运行示例_**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/tree_1.png)