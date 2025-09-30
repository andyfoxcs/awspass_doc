# 单选组 | AWS UI组件参考指南

## 单选组

创建一组单选按钮控件，对标准INPUT type=radio元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端 |  移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/radiogroupsR1.png) |  ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/radiogroupsR_m.png)  
勾选里程碑展示后效果  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/radiogroupsR2.png)  
  
**预置校验**

  * 若为文本类型，参见单行[预置校验](<text.html#check>)

  * 若为数值类型，参见数值[预置校验](<number.html#check>)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/radiogroupsD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_** 仅支持如下事件且不支持Ajax子表
        
        //以下扩展代码不支持ajax子表
          /**
            * 点击事件
            *
            * @param {String} boItemName 字段名
            * @param {Object} $radio radio组件的jQuery对象
            * @param {String} val 被点击的radio的值
            */
          function onRadioClickEvent(boItemName, $radio, val) {
            //事件处理代码
          }
          /**
            * 选中事件
            *
            * @param {String} boItemName 字段名
            * @param {Object} $radio radio组件的jQuery对象
            * @param {String} val 被点击的radio的值
            * @param {Boolean} checked radio是否被选中
            */
          function onRadioCheckedEvent(boItemName, $radio, val, checked) {
            //事件处理代码
          }
        

**扩展属性**

  * **_数据源模式_**

参见列表[数据源模式](<combobox.html#data_source>)

  * **每行显示个数** 为数字，例如：每行显示3个  

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/radiogroupsD2.png)

  * **只读时显示全部选项** 表单只读状态时将全部选项显示出来  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/radiogroupsD3.png)

  * **有效性** 勾选`下载Excel模板时，使用Excel的数据有效性`后，在子表支持Excel导入时，下载的Excel模板和DW导入下载的Excel模板该字段值有列表值可选择，且列表值总和长度不超时255字符时。 如果不勾选，则下载的模板该字段值为空，可由用户自由输入

  * **移动界面展示**

参见列表[手机UI展示](<combobox.html#lbmobileui>)

  * **里程碑展示** 在运行时以里程碑的方式展示，展示顺序为单选值的显示顺序。 _该功能在6.2.11.0828版本后可用_

    * 最大显示个数引用每行显示个数，当超出多余里程碑数后，前后会增加引导图标查看更多里程碑
    * `背景颜色` 可分别设置已完成、进行中、未进行的背景色
    * `字体颜色` 可分别设置已完成、进行中、未进行的字体色

> 可以配合该字段"默认值"给一个单选组提供一个默认选项，默认值应为数据库中存储值，如当数据源模式为键值字典时，默认值应为该键值字典对应`ITEMNO`字段值;当数据源模式为SQL语句时，默认值应为取值字段名对应值