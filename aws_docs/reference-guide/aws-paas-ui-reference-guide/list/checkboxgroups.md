# 复选组 | AWS UI组件参考指南

## 复选组

一组复选按钮控件，对标准INPUT type=checkbox元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端 | 移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/checkboxgroupsR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/checkboxgroupsR_m.png)  
  
**预置校验**

  * 若为文本类型，参见单行[预置校验](<text.html#check>)

  * 若为数值类型，参见数值[预置校验](<number.html#check>)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/checkboxgroupsD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_** 仅支持如下事件且不支持Ajax子表
        
        ///以下扩展代码不支持ajax子表
        /**
        * 点击事件
        *
        * @param {String} boItemName 字段名
        * @param {Object} $checkbox checkbox组件的jQuery对象
        * @param {String} val 被点击的checkbox的值
        */
        function onCheckboxClickEvent(boItemName, $checkbox, val) {
        //事件处理代码
        }
        /**
        * 选中事件
        *
        * @param {String} boItemName 字段名
        * @param {Object} $checkbox checkbox组件的jQuery对象
        * @param {String} val 被点击的checkbox的值
        * @param {Boolean} checked checkbox是否被选中
        */
        function onCheckboxCheckedEvent(boItemName, $checkbox, val, checked) {
        //事件处理代码
        }
        

**扩展属性**

  * **_数据源模式_**

参见列表[数据源模式](<combobox.html#data_source>)

  * **_每行显示个数_** 为数字，例如：每行显示3个，只支持正整数  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/checkboxgroupsD2.png)
  * **只读时显示全部选项** 表单只读状态时将全部选项显示出来  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/checkboxgroupsD3.png)

  * **分隔符号** 多个值之间的分隔符号。若选中多个值保存到数据库后，该值被组合成一个由分隔符隔开的串  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/checkboxgroupsD4.png)

> 可以配合该字段"默认值"给一个单选组提供一个默认选项，默认值应为数据库中存储值，如当数据源模式为键值字典时，默认值应为该键值字典对应`ITEMNO`字段值;当数据源模式为SQL语句时，默认值应为取值字段名对应值