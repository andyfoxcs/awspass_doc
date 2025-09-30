# 单行 | AWS UI组件参考指南

## 单行

创建一个文本输入框，对标准INPUT type=TEXT元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端 | 移动端 | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textR_m.png) **预置校验**

  * 录入长度超过字段长度时，不允许保存 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/overlengthtip.png)
  * 若字段设置非空且填写表单时值未输入，不允许保存 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/notnulltip.png)
  * 若字段从数据源读取值为NULL或空串且该字段设置了【默认值】，则显示该值 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/defaultvalue.png)
  * 若在表单模型为该字段设置了[`有效性`](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form/pc/list.html>)校验,保存时自动校验

> 当人工审核菜单未勾选[`是否校验表单`](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/check_menu.html>)项或表单应用未勾选[`保存时校验数据`](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/authority.html>)项时，办理流程或保存表单时，不执行以上预置校验

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textD1.png) **基本属性**

  * **_查询列宽_** 控制各种子表表格列宽度、报表查询结果列宽度，单位：像素(px)

  * **_显示规则 > 组织映射_** 仅在字段只读时刻有效。若字段从数据源读取值为某组织`(人员、角色、团队、部门、部门全路径、单位)`名称ID时，在表单运行时如果该字段为只读状态，则自动显示为相应组织名称。支持多值，多值间请用空格或逗号隔开。如`设置为部门全路径时` ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/see.png)

  * **_帮助说明_** 仅在字段可编辑时刻有效。鼠标经过编辑区时，系统自动显示该提示说明注释框，鼠标移走，提示内容消失。可帮助用户在填写数据时识别字段项含义，提高表单数据的正确性和工作效率  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/tip.png)

###### 输入要求

    * 普通常量文字字符说明, 最大长度支持225个字符
    * 支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)，例如`@if(@equals(@activityDefName,提报节点),请输入本月预算值,请确定该预算值的合理性)`

  * **_扩展代码_**
    * **事件** 支持HTML表单元素和鼠标onXXX事件，例如`onchange="alert('Hello!')"`
    * **样式** style语法，参见INPUT样式标签属性，例如`style="border-color:red"`。  

> 如需控制单行组件宽度，需增加和style平级的`nofit="true"`，例如 `style="width:200px" nofit="true"`

    * **属性** 支持`readonly 、 disabled`。

> 字典类组件，`readonly`仅控制文本框不可编辑，选择按钮仍然可用；`disabled`可控制文本框和选择按钮均不可用。

**扩展属性**

  * **_组件类型_** 提供`文本` `手机号` `邮箱` `网址`这四种类型，默认是文本
    * **手机号** 只读时在`移动端`可给该字段上的手机号直接拨打电话
    * **邮箱** 只读时可点击弹出操作系统配置邮箱服务链接
    * **网址** 只读时可用`新窗口`或`侧边栏`方式打开对应的网址链接
    * **默认前缀** 选择`网址`，显示该属性，提供`无` `http://` `https`三个选项，默认选中`无`
    * **打开目标** 选择`网址`，显示该属性,提供`新窗口` `侧边栏`,默认选中`新窗口` ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textread.png)

> 组件类型功能使用要求平台版本不低于6.3.GA

  * **_空值提示_** 仅在字段可编辑时刻有效。若字段从数据源读取值为NULL或空串时，在编辑区将自动显示该提示说明。输入要求参见`帮助说明`，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/nulltip.png)

> IE系列浏览器仅支持IE10及以上  
>  `组件类型`是`手机号` `邮箱` `网址`有固定的空值提示，不支持该属性![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/nulltip1.png)

  * **_键盘参考_** 当用户输入字符时即时提供命中率参考列表，默认为‘否’ ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textR2.png)
    * **显示记录数** 当键盘命中SQL记录过多时最多显示的记录数
    * **数据源** `当前BPM数据源`，数据来自当前AWS连接的本地数据库  
`CC 数据源`，数据来自【连接服务】 Database组件连接的外部数据库
    * **字段名** 在SQL记录集存在的字段名，必须填写
    * **SQL语句** 一个完整的select SQL语句，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)

  * **_允许清空（移动端）_** 该属性仅对移动端有效。是否显示清空图标
  * **_扫码录入（移动端）_** 该属性仅对移动端有效。是否提供扫码操作图标

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/MobileGetBarCodeR1.png) 需要在移动表单自定义如下事件，对扫码值进行处理
    
    
        /**
          * 扫码后事件
          *
          * @param {String} boItemName 字段名
          * @param {String} val 扫码之后的值
          */
        function onGetBarCodeEvent(boItemName, val) {
          //事件处理代码
        }
    

> 扫码录入仅支持AWS 6.2.14及后续版本  
>  `组件类型`是`手机号` `邮箱` `网址`时，扫码录入禁选，不支持该属性

  * **_链接选项_** 链接选项提供无、主表单、子表记录、自定义URL四个链接选项，默认无。在表单运行中，只有字段只读时有效，字段值变蓝色，支持链接打开对应表单页面，可以是流程表单，也可以是DW表单。如果链接的有多个相同的字段值，取最近的 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/link1.gif)
    * **表单模型** 列表显示当前应用、当前应用的父应用及当前应用关联应用的表单模型
    * **取值字段** 默认当前$[字段名]，支持@公式
    * **关联字段** 链接选项选主表单，默认该表单主表相同字段名，单选  
选子表记录，默认该表单子表首个相同字段名， 单选  
也可以下拉单选不同的字段名
    * **表单状态** 链接表单的三种状态：常规、只读、可编辑
    * **窗口位置** 链接表单打开表单的两种方式：新窗口、侧边栏
    * **侧边栏标题** 窗口位置选择侧边栏显示`侧边栏标题`项 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/link2.gif)

### 常见实施场景

当字段配置组合显示时，需要为组合字段配置扩展代码`style="width:98%" nofit="true"` ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textF1.png) ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textF2.png)