# 平板数据字典 | AWS UI组件参考指南

## 平板数据字典

创建一个带有文本录入和按钮的常规数据参考字典控件，对标准INPUT type=TEXT和 BUTTON元素的组合封装。可以通过按钮弹出的数据字典对话框，选取值回填到表单。用于显示和修改被表单数据源绑定的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。平板分类组件用于实施数据记录量不大，要求返回值单一，且需要友好分类显示的场景。

### 运行

PC端  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/flatdictionaryR1.png)  
移动端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/flatdictionaryR1_m.png)  
  
**预置校验**

  * 若为文本类型，参见单行[预置校验](<text.html#check>)

  * 若为数值类型，参见数值[预置校验](<number.html#check>)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/flatdictionaryD1.png)

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

  * **_模式_**

    * 对话框模式：以对话框的模式显示平板数据字典数据

    * 下拉模式：以下拉模式显示平板数据字典数据，该模式不支持Ajax子表

  * **_数据源_**

`当前BPM数据源`，数据来自当前AWS连接的本地数据库  
  
`CC 数据源`，数据来自【连接服务】 Database组件连接的外部数据库

  * **_显示字段名_**

显示字段名，也是回填给表单字段的显示值，支[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **_取值字段名_**

末级取值字段名，也是回填给表单字段的值，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **_主分类字段名_**

一级分类字段名，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **_次分类字段名_**

显示在页面区域的二级分类字段名，可不设置，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **_SQL语句_**

一个标准的SELECT查询语句，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

  * **链接选项**

参见单行[链接选项](<text.html#link>)

> 部分扩展属性不支持移动端