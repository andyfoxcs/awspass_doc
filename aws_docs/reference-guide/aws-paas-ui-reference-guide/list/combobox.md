# 列表 | AWS UI组件参考指南

## 列表

创建一个列表选择控件，普通模式对标准SELECT元素封装，高级模式由AWSUI框架combobox实现。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

普通模式 |  高级模式 |  移动端(勾选手机UI展示后效果)  
---|---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxR1.png) |  ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxR2.png) |  ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxR_m.png)  
勾选里程碑展示后效果  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxR3.png)  
  
**预置校验**

  * 若为文本类型，参见单行[预置校验](<text.html#check>)

  * 若为数值类型，参见数值[预置校验](<number.html#check>)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_显示规则_**

参见单行[显示规则](<text.html#displayrule>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

参见单行[扩展代码](<text.html#componentExtendCode>)

> 列表为高级模式时，change事件如下
        
        /**
            * change事件
            *
            * @param {String} boItemName 字段名
            * @param {Object} $combobox combobox组件的jQuery对象
            * @param {String} val checkbox的值
            */
          function onComboboxChangeEvent(boItemName, $combobox, val) {
            //事件处理代码
          }
        

**扩展属性**

  * **_空值提示_**

参见单行[空值提示](<text.html#nulltip>)

  * **_数据源模式_**

    * **常量** 一个简单的常量串，语法格式=值1:显示1|值2:显示2...，例如： ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxD2.png)

    * **SQL语句** 一个完整的SQL。支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)、$字段名，例如【… where orderType=’$ORDERTYPE’】,该字段名为当前字段所在BO表中字段名

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxD3.png)

>       1. **数据源** `当前BPM数据源`数据来自当前AWS连接的本地数据库   
>  `CC 数据源`，数据来自【连接服务】 Database组件连接的外部数据库
> 
>       2. **显示字段名** 在SQL记录集存在的字段名，可不填写，如不填写，将默认为取值字段值，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)
> 
>       3. **取值字段名** 在SQL记录集存在的字段名，必须填写，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)
> 
>       4. **SQL语句** 一个完整的select SQL语句，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)
> 
>       5. **值转换** 当配置显示字段名与取值字段名不同时，用于后台字段名与取值字段名的快速转换。一个标准的SELECT查询，查询结果为应为显示字段名和取值字段名

    * **JSON数据** 数据源来源于JSON数据配置文件

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxD9.png)

> 1.**数据源** 必填，显示连接服务中对应的Http(s) Web服务名称

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxD10.png)

> 2.**显示键名** 必填，填写JSON数据文件中的名称

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxD11.png)

> 3.**取值键名** 必填，填写JSON数据文件中的值
> 
> 4.**列表根位置** 必填，如果从根路径获取，需要将JSON结构返回一个JSON数组，以便列表有序；如果存在路径，可以为一个JSON对象指定的路径下面的格式，还需要是JSON数组

    * **键值字典** 数据源来源于[基础字典](<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/index.html>)

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxD4.png)

>       1. **配置** 必填，显示基础字典中当前应用及关联应用的所有字典名称
> 
>       2. **数据过滤** 当前键值字典支持的属性过滤，有关各字段名介绍参见<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/appendix/table.html>   
> 

  * **高级模式** 适用于以上三种数据源模式

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxD6.png)

>     1. **列表宽度和高度** combobox展开的宽度和高度，单位：px 像素。当宽度为空时，默认与Input框宽度一致  
> 
> 
>     2. **分隔符号** 多个值之间的分隔符号，默认为逗号。建议：当任一列表值包含空格时，可选择用逗号或竖线分隔。例如：使用分隔符为逗号：  
>  ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/comboboxD8.png)
> 
>     3. **是否多选** 设置为多选时，下拉列表的选项值允许多选
> 
>     4. **是否只读** 设置为只读时，不允许用户从键盘输入，默认为否，当设为否时，用户可以从键盘输入值，该值不与列表中值做校验
> 
>     5. **模糊搜索** 只有单选只读时，才显示模糊搜索设置。设置为是，显示搜索框，设置为否，不显示搜索框

  * **有效性** 勾选`下载Excel模板时，使用Excel的数据有效性`后，仅当列表为单选时，在子表支持Excel导入时，下载的Excel模板和DW导入下载的Excel模板该字段值有列表值可选择，且列表值总和长度不超时255字符时。 如果不勾选，则下载的模板该字段值为空，可由用户自由输入

  * **移动界面展示** 移动端展示效果设置

    * **宽（每个元素）**
    * **高（每个元素）**
    * **翻页按钮字体大小**
    * **数据字体大小**

  * **里程碑展示** 仅当列表为单选时可用，在运行时以里程碑的方式展示，展示顺序为列表值的显示顺序。 _该功能在6.2.11.0828版本后可用_

    * **最大显示个数** 超出多余里程碑数后，前后会增加引导图标查看更多里程碑
    * **背景颜色** 可分别设置已完成、进行中、未进行的背景色
    * **字体颜色** 可分别设置已完成、进行中、未进行的字体色

> 运行时点击里程碑支持 `function onComboboxChangeEvent(boItemName, $combobox, val) {}`事件

  * **链接选项**

参见单行[链接选项](<text.html#link>)

> 部分扩展属性不支持移动端