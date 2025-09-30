# 分类选择 · AWS PaaS文档中心

# 分类选择

创建一个带有文本录入和按钮的常规数据参考字典控件，对标准INPUT type=TEXT和 BUTTON元素的组合封装。可以通过按钮弹出的数据字典对话框，选取值回填到表单。用于显示和修改被表单数据源绑定的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。分类字典组件用于实施数据记录量不大，要求返回值单一，且需要友好分类显示的场景。

## 运行

PC端  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textfl_pc.png)](<textfl_pc.png>)  
移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textfl_mobile.png)](<textfl_mobile.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textfl1.png)](<textfl1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**长度**

参见单行[长度](<text.html#length>)

**前后缀**

参见单行[前后缀](<text.html#qhz>)

> 后缀有默认图标

**数据源**

参见单行[辅助录入](<text.html#source>)

>   * 分类字典中的数据源只有`关联表单` `关联存储` `关联字典` `SQL数据` `CC数据服务`，没有`自定义`  
> 
>   * 数据源只有`关联表单` `关联存储` `SQL数据` `CC数据服务`显示且需要配置`主分类` `次分类`,数据源是`关联字典`不显示`主分类` `次分类`
> 

**主分类**

一级分类字段名

**次分类**

显示在页面区域的二级分类字段名，可不设置

**字典展示外观**

可以用`对话框`或`下拉框` 这两种外观形式展示

  * **对话框** ：以对话框的模式显示平板数据字典数据

  * **下拉框** ：以下拉模式显示平板数据字典数据，该模式不支持编辑子表

**多选**

默认不开启，只允许选择一个值;开启多选，允许选择多个值

  * **分隔符**

仅在开启`多选`时可用，多值之间可用`逗号`或`空格`或`竖线`分隔

**链接选项**

参见单行[链接选项](<text.html#link>)

**控制属性**

参见单行[控制属性](<text.html#control>)

**不允许重复录入**

参见单行[不允许重复录入](<text.html#nocopy>)

**宽度**

参见单行[宽度](<text.html#wigth>)

**提示文字**

参见单行[提示文字](<text.html#tip>)

**帮助说明**

参见单行[帮助说明](<text.html#help>)

**字段规则**

参见单行[字段规则](<text.html#zdgz>)