# 范围查询 · AWS PaaS文档中心

# 范围查询

配置快速查询条件或导航树交互风格时的分类导航树结构。

**步骤**

  1. 打开用户视图配置界面
  2. 鼠标划动到"配置查询条件"区域并点击"配置查询条件"，显示成可编辑状态
  3. 点击"添加"按钮，默认是按条件查询，可在弹出的"查询字段配置选项卡"修改查询方式为"范围"
  4. 弹出提示点"确定"切换到范围查询方式，弹出范围查询的配置框
  5. 相关配置操作后，点"保存"，完成操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/30.png)](<30.png>)

属性项 | 说明  
---|---  
标题 | 查询条件名称，可修改名称，在选项卡修改提交；也可在`配置-分组`中修改  
添加 | 点击`添加`,弹出查询条件配置框  
查询条件项 | 支持拖动位置，运行时与拖动后位置一致  
查询条件项删除 | 删除当前查询条件项  
访问权限 | 设置允许访问的范围  
删除 | 删除整个查询条件  
  
## 固定值

过滤条件是单一字段，值由特定常量来匹配。

**参考值配置**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/searchgudingD.png)](<searchgudingD.png>)

  * **类型** 根据选择的类型，下面的属性展示不一样，编辑时类型只读
  * **标题** 查询列表选择的名称
  * **分组** 查询条件分组的标题
  * **字段列表** 查询字段
  * **比较方式** 支持`等于`、`不等于`、`大于`、`小于`、`包含于`等多种方式
  * **条件值** 支持@公式，支持`｜`符号运行时组合成下拉列表多条件值，如`值1|值2|值3`

**_运行示例_**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/searchgudingR.png)](<searchgudingR.png>)

## 范围值

过滤条件可以是一组字段，值由特定常量来匹配。

**参考值配置**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/searchefanweiD.png)](<searchefanweiD.png>)

  * **类型** 根据选择的类型，下面的属性展示不一样，编辑时类型只读
  * **标题** 查询列表选择的名称
  * **分组** 查询条件分组的标题
  * **关系** 多个条件时组合关系(并且/或)
  * **字段列表** 查询字段
  * **比较方式** 支持`等于`、`不等于`、`大于`、`小于`、`包含于`等多种方式
  * **条件值** 支持@公式

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/searchefanweiR.png)](<searchefanweiR.png>)

## 常规SQL

过滤条件是单一字段，值由SQL结果集匹配。

**参考值配置**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/searcheSQLD.png)](<searcheSQLD.png>)

  * **类型** 根据选择的类型，下面的属性展示不一样，编辑时类型只读
  * **标题** 查询列表选择的名称
  * **分组** 查询条件分组的标题
  * **字段信息** 查询字段
  * **比较方式** 支持`等于`、`不等于`、`大于`、`小于`、`包含于`等多种方式
  * **值** 列表取值，在SQL结果集存在的字段名，该值将与`字段列表`值进行比较
  * **显示** 列表显示值，在SQL结果集存在的字段名
  * **SQL语句** SELECT查询语句，支持@公式

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/searcheSQLR.png)](<searcheSQLR.png>)