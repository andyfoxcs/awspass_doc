# 条件查询 · AWS PaaS文档中心

# 条件查询

**步骤**

  1. 打开用户视图配置界面
  2. 鼠标划动到"配置查询条件"区域并点击"配置查询条件"，显示成可编辑状态
  3. 点击"添加"按钮，默认是按条件查询，可在弹出的"查询字段配置选项卡"修改查询方式
  4. "查询字段配置选项卡"的相关操作配置完成后，点"保存"，完成操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/29.png)](<29.png>)

属性项 | 说明  
---|---  
显示名称 | 客户端显示名称，可修改，修改后按回车或点对勾提交修改  
数据项 | 查询条件名称  
比较方式 | 支持`等于`、`不等于`、`大于`、`小于`、`包含`等多种方式，根据字段在BO存储类型不同过滤比较方式  
● 类型为`文本`支持`等于`、`不等于`、`包含`、`不包含`、`左包含`、`右包含`、`等于`、`不等于`、`大于`、`小于`、`大于等于`、`小于等于`  
● 类型为`日期` `数值`支持`等于`、`不等于`、`大于`、`小于`、`大于等于`、`小于等于`  
● 选择范围 根据具体的组件实施配置选择范围，支持@公式  
UI组件 | 运行时，查询条件输入框展示形式  
● `文本` 一个Input输入框  
● `日期` 弹出日期选择组件  
● `日期时间` 弹出日期时间选择组件  
● `时间`弹出时间选择组件  
● `列表`一个下拉列表框  
● `复选组`  
● `范围`  
●  `级联`  
● `地址簿`  
  
默认值 | 查询条件默认值，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)  
配置 | 不同UI组件该属性配置不同  
必填 | 客户端查询条件必填  
关系 | 多个条件时组合关系  
查询方式 | ● 条件  
● 范围  
访问权限 | 设置允许访问的用户范围  
唯一标识 | 由系统自动维护  
删除 | 删除配置的查询字段  
拖动 | 查询条件项支持拖动位置，运行时与拖动后位置一致  
  
> UI组件文本输入框展示形式的设置模糊匹配，支持输入多个条件以英文逗号隔开，如查询条件：NAME字段，允许用户输入：张三,李四,王五

## 文本

**参考值配置**

  * 无

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/input.png)](<input.png>)

## 日期

**参考值配置**

  * 无

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/data.png)](<data.png>)

## 日期时间

**参考值配置**

  * 无

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/datatime.png)](<datatime.png>)

## 时间

**参考值配置**

  * 无

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/time.png)](<time.png>)

## 列表

**参考值配置** [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/selectD.png)](<selectD.png>)

  * **常量** `值`可手动输入常量值，也可选择 已有的列表数据;`显示`输入要显示的名称,支持@公式；`高级`在高级框中输入一个简单的常量串，语法格式：值1:显示1|值2:显示2...。高级与上面添加的值，显示相互同步

  * **SQL数据源** 列表值来源于SELECT查询语句结果，支持@公式

  * **键值字典** 列表值来源于基础字典，详细参见<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/reference/dw.html>

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/selectR.png)](<selectR.png>)

> 支持多个列表字段数据来源是sql的级联查询，级联字段sql支持的格式：$[字段名+查询字段ID]

## 复选组

**参考值配置**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/CheckboxD.png)](<CheckboxD.png>)

  * **参见列表**

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/CheckboxR.png)](<CheckboxR.png>)

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/fanwei.png)](<fanwei.png>)

## 级联

**参考值配置**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/jilianD.png)](<jilianD.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/jilianD2.png)](<jilianD2.png>)

  * **连接符** 连接符
  * **查询字段** 对应查询字段
  * **类型** 查询字段类型
  * **比较方式** 比较方式
  * **数据配置**
    * **显示字段** 查询列表显示的值，在SQL结果集存在的字段名
    * **取值字段** 查询列表取值，在SQL结果集存在的字段名，该值将与`查询字段`值进行比较
    * **SQL语句** SELECT查询语句，支持`$`变量，该变量将在运行时，自动获取上一条列表取值字段值
  * **默认值** 支持@公式
  * **宽度** 运行时，查询条件输入框宽度

**_运行示例_**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/jilianR.png)](<jilianR.png>)

## 地址簿

**参考值配置**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/dzb.png)](<dzb.png>)  
---  
  
配置中的属性详见[UI组件参考指南-地址簿](<https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/address.html>)

**_运行示例_**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/dzb1.png)](<dzb1.png>)