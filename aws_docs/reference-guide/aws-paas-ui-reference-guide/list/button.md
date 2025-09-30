# 按钮 | AWS UI组件参考指南

## 按钮

创建一个按钮控件，对标准INPUT= BUTTON元素的封装。可以通过自定义的按钮弹出数据选取对话框，显示和修改被表单数据源绑定后的数据，并自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端 | 移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/buttonR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/buttonR1_m.png)  
  
### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/buttonD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

不支持

**扩展属性**

  * **_按钮名称_**

按钮的名称，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)

  * **_配置及配置信息_**

    * **URL** 一个标准URL地址，例如：<http://www.awspaas.com/> , 请参见[URL规格说明，](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-nav/appendix/url_instruct.html>) 支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

    * **JavaScript** 一个表单中可访问的JavaScript方法名，若方法含有字符串参数，请使用半角双引号括起，例如：alert("ABC");并且支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **_只读有效_** 该字段处于只读状态时是否可用。