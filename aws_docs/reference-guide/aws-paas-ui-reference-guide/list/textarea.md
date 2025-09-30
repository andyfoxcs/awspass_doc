# 多行 | AWS UI组件参考指南

## 多行

创建一个多行文本输入框，对标准TEXTAREA元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

| PC端 | 移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textareaR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textareaR_m.png)  
  
**预置校验**

参见单行[预置校验](<text.html#check>)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/textareaD1.png)

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

  * **_高度_**

仅在字段可编辑时刻有效。控制textarea元素style样式height值

  * **_自动高度_**

勾选后【高度】属性将不可用，在可编辑状态时多行文本框高度将自动根据录入信息自动调整

> 如果多行文本值是通过JS自动赋值，要想支持该属性需JS赋值后调用 `$("#字段名").trigger("input");`触发自动调整高度事件

  * **_空值提示_**

参见单行[空值提示](<text.html#nulltip>)

  * **_多文本换行_**

仅支持Ajax子表列表，当勾选了多文本换行，则换行显示所 有的内容；不勾选时，不换行显示；默认不勾选

  * **_快捷键设置_**

鼠标快速定位到多行控件。支持ctrl、alt、shift与一个A~Z字母的组合快捷键，当设置的快捷键组合与浏览器自身快捷键冲突时失效

> 该属性仅支持部分浏览器且不支持Ajax子表、移动端设备

  * **_键盘参考_**

参见单行[键盘参考](<text.html#keyboard>)