# 开关 | AWS UI组件参考指南

## 开关

创建一个带有文字和开关的控件，可以通过自定义的按钮进行开关操作，显示和修改被表单数据源绑定后的数据，并自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端 | 移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/switchbuttonR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/switchbuttonR1_m.png)  
  
### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/switchbuttonD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

不支持

  * **_扩展代码_**

不支持

**扩展属性**

  * **_显示文字_**

选择"是"，开关按钮上显示设置的文字

  * **_"开 "文字_**

"开"状态时显示的文字

  * **_"关 "文字_**

"关"状态时显示的文字

  * **_开字体颜色_**

"开"状态时文字显示的颜色

  * **_关字体颜色_**

"关"状态时文字显示的颜色

  * **_开关颜色_**

开关运行时显示的颜色

  * **_字体大小_**

开关按钮上文字的大小

  * **_宽度_**

开关按钮的宽度，单位为像素：px，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **_高度_**

开关按钮的高度，单位为像素：px，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>) 。

  * **_存储类型_**

    * 数值类型："开"状态取值为1，"关"状态取值为0

    * 布尔类型："开"状态取值为true，"关"状态取值为false

    * 自定义值：仅可设置两个值，如“A|B”，"开"状态取竖线前面的值，"关"状 态取后面的；设置自定义值，要注意字段类型，防止出错