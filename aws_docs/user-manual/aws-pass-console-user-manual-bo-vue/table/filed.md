# 结构 · AWS PaaS文档中心

# 结构

为表配置字段信息。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/filed1.png)](<filed1.png>)

项 | 说明  
---|---  
名称 | 必填，数据库字段名，不可重复   
标题 | 必填，在表单上默认显示的标题。对于某些敏感数据域提供采用AES加密存储，实施方法在标题前缀增加`**`，例如`**基本工资`，因此该类字段的类型必须是文本型。注意，加密后的文本长度大概是原值的20倍  
类型  | 对应数据库的字段类型分别为：  
．文本（Nvarchar2、Text、Varchar）  
．数值（Double、Long、Intger）  
．日期（Date、Timestamp）  
．大文本（File）  
长度 | 当类型为数值时，支持`12,2`格式，表示总长度是12位，小数是2位  
组件  | 表单运行时页面展示方式，参见[表单模型>组件](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue/_book/zj/>)  
默认值  | 表单运行时自动显示该字段默认值，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)  
必填  | 表单运行时自动校验该字段是否允许为空，不符合时自动给出`必填`的提示。仅在当前字段为编辑状态时校验。   
可见 | 当不勾选可见时，在表单运行时将自动隐藏，支持子表列表和子表表单页面。字段权限在AWS各种策略中的优先次序参见 https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/form_before_load.html   
只读 | 当勾选后，在表单运行时为只读状态，不可编辑。字段权限在AWS各种策略中的优先次序参见 https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/form_before_load.html   
可复制 | 仅对子表有效，勾选后该字段允许批量复制，需要配合[`流程>表单应用>数据导入导出>允许用户复制该记录`](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/data_import.html>)功能使用   
类型 | ．`实体字段` 对应数据库中物理字段  
．`虚拟字段`该字段在数据库中并不真实存在，因此运行时刻的值一般需要用户通过默认值方式配置   
操作  | 相关操作按钮，支持在下方添加、上移、下移、删除  
  
## 从模板组合

这是一个快速建模辅助支持操作，帮助实施人员从已存在的BO表结构元数据中组合追加到当前BO模型中。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/filed2.png)](<filed2.png>)

> 对于二级管理员使用该功能时默认仅允许从自己权限范围内选择，admin用户也可在AWS BPMS平台参数中通过`存储模型-从模板组合-设置模板应用(templateApp)`参数增加允许选择的范围

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/filed3.png)](<filed3.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/filed8.png)](<filed8.png>)

## 系统字段

为配合流程引擎驱动业务数据AWS平台为创建的BO表模型自动创建了9个系统字段，这些字段值由AWS平台引擎自动维护。

系统字段 | 字段标题 | 说明  
---|---|---  
ID | 主键唯一索引 | 记录唯一标识（主键），一个平台全BO表ID不重复的序列值  
ORGNO | 单位ID | 数据创建人所在单位ID  
BINDID | 绑定关系ID | 该业务数据的流程（或仅存储）的实例ID  
CREATEUSER | 创建人 | 数据创建人账户名  
CREATEDATE | 创建日期 | 数据创建日期  
UPDATEUSER | 修改人 | 数据最后一次修改人账户名  
UPDATEDATE | 修改日期 | 数据最后一次修改日期  
PROCESSDEFID | 流程定义ID | 该业务数据的流程（或仅存储）的模型定义  
ISEND | 是否结束 | 如果是流程驱动，流程是否已结束  
  
## 属性扩展

自定义扩展业务字段列，例如增加一列身份证号标识列，设置后对当前BO模型有效。可通过API和@公式获取。 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/filed5.png)](<filed5.png>)

项 | 说明  
---|---  
名称 | API和@公式获取时需要该参数，建意为纯字母  
标题 | 列属性显示标题  
默认值 | 默认值。控件为列表时，应为取值；控件为复选框时，应为true或false  
组件 | 支持复选框、列表、输入框。为输入框时，展示形式为一个文本输入框，用户可输入任意值；为复选框时，展示形式为一个check框，用户可勾选或不勾选，勾选后值为true，不勾选值为false；为列表时，展示形式为一个列表，此处需进阶配置列表值  
列表值 | 显示控件为列表时有效，高级格式`[["取值1","显示值1"],["取值2","显示值2"],.....]`  
列宽 | 列宽度，px  
  
### 获取扩展列值

API获取
    
    
    //根据表名、字段名、扩展属性名获得属性值
    SDK.getRepositoryAPI().getBOItemPropValue("表名", "字段名", "属性名称");
    
    //根据表名、扩展属性名、扩展属性值获得满足条件的字段定义模型列表
    SDK.getRepositoryAPI().getBOItemsOfProp( "表名",  "属性名称",  "属性值");
    

@公式获取
    
    
    //根据表名、字段名、扩展属性名获得属性值
    @boItemPropVal(*boName,*fieldName,*prop)
    

### 全局属性扩展定义

属性扩展支持在`AWS BPMS平台`参数`BO模型字段扩展属性`中设置。设置后所有BO模型有效。详细设置格式参见参数说明

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/filed6.png)](<filed6.png>)