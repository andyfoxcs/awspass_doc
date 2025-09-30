# 树形数据字典 | AWS UI组件参考指南

## 树形数据字典

创建一个树形下拉框控件，这是一个私有封装。树形组件也是一种字典类组件，可以根据树状SQL 数据源，构造成一棵异步展开的树。选择树节点后，树节点对应的表记录可以根据预设的字段对应关系回填到当前表单。用于显示和修改被表单数据源绑定的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。

### 运行

PC端  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/treedictionaryR1.png)  
移动端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/treedictionaryR1_m.png)  
  
> 检索的关键字是配置属性中节点文字配置后展示的内容

**预置校验**

  * 若为文本类型，参见单行[预置校验](<text.html#check>)

  * 若为数值类型，参见数值[预置校验](<number.html#check>)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/treedictionaryD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_显示规则_**

参见单行[显示规则](<text.html#displayrule>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

参见单行[扩展代码](<text.html#componentExtendCode>)

**扩展属性**

  * **_空值提示_**

参见单行[空值提示](<text.html#nulltip>)

  * **_窗口名称_**

弹出的窗口名称，仅对Ajax子表有效

  * **_数据源_**

    * **当前BPM数据源** ，数据来自当前AWS连接的本地数据库  

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/treedictionaryD2.png)

>       1. **SQL语句** 一个标准的SELECT查询语句，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)
> 
>       2. **查询SQL** 一个标准的SELECT查询语句，结果值为树形字典搜索框进行搜索时的范围
> 
>       3. **关系定义** 树形数据字典通过SQL数据源中设置的父子字段查询当前节点的子节点数据。原理：当组件通过select * from ORGDEPARTMENT where parentdepartmentid = 0 构建出一棵带根的树后，如果用户点击根节点，组件将parentdepartmentid = 0替换为parentdepartmentid = 根节点id，从而查询出根节点的子节点，其余节点依次类推
> 
>       4. **叶子节点标识** 设置叶子节点的显示条件

    * **键值字典** ，数据源来源于[基础字典](<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/design/tree-value-dict.html>)

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/treedictionaryD3.png)

>       1. **配置** 必填，显示基础字典中当前应用及关联应用的所有字典名称
> 
>       2. **数据过滤** 当前键值字典支持的属性过滤，有关各字段名介绍参见<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/appendix/table.html>   
> 

    * **CC 数据源** ，数据来自【连接服务】 Database组件连接的外部数据库

> 参见当前BPM数据源

  * **_数据过滤_**

配置树过滤范围，支持`$getform(字段名)`格式获取当前表单数据

  * **_回填策略_**

设置节点对应数据是否可以回填，默认节点都可使用，可选的输入值包括：

    * 非叶子节点：非叶子节点可以回填

    * 叶子节点：叶子节点可以回填

    * 条件约束：格式为："字段:值"，回填字段满足指定的值时可以回填，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **_多选_**

勾选后支持多选，并可设置多个之间的分隔符，`勾选继承`选择父节点，是否自动选择子节点

  * **_显示全路径_**

勾选后，在回填结果里将显示全路径

  * **_节点图标样式_**

改变树节点图标，例如 `parent:{../commons/img/add1_16.png};leaf:{../commons/img/airplane_16.png}`

  * **_节点文字样式_**

改变树节点文字样式，例如`parent:{color:red;font-size:12px;};leaf:{color:blue;font-size:15px;}`

  * **_节点文字_**

可自行定义节点文字内容，如果取字段的值使用$[XXX]，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **_取值字段_**

双击节点时，取值SQL数据源中存在的字段值，多个字段名用|隔开，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **_展示字段_**

配置源表一个字段名，用于双击节点源表字段值回填后到当前表单字段后显示的内容

  * **_回填字段_**

双击节点时，对应取到的源表字段值回填到当前表单字段，多个字段名用|隔开。【取值字段】和【回填字段】个数和次序必须匹配，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **链接选项**

参见单行[链接选项](<text.html#link>)

> 部分扩展属性不支持移动端