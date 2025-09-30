# 数值 | AWS UI组件参考指南

## 数值

创建一个含有数值校验的文本输入框，对标准INPUT type=TEXT元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端 | 移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/numberR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/numberR_m.png)  
  
**预置校验**

  * 保存时若字段值为非数字，不允许保存

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/numberR2.png)

  * 若字段从数据源读取值为NULL或0且该字段设置了【默认值】，则显示该值

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/numberR3.png)

  * 其它参见单行[预置校验](<text.html#check>)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/numberD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

参见单行[扩展代码](<text.html#componentExtendCode>)

**扩展属性**

  * **_零值处理_**

若字段从数据源读取值为NULL或0，编辑区是否自动显示0

    * **显示为"0"** 自动显示0

    * **什么都不显示** 什么都不显示

  * **_空值提示_**

参见单行[空值提示](<text.html#nulltip>)

  * **_允许清空(移动端)_**

参见单行[允许清空(移动端)](<text.html#delete>)

  * **_自动补零_**

若字段设置了小数位，但从数据源读取值比设置的小数位少，会自动补零，满足设置的小数位

  * **_科学计数法显示_**

若字段值较大位数多，这时用科学计数法显示方便查看，运行时点击INPUT框可查看原值，失去焦点后，还原成科学计数法显示

    * 保留小数位 用科学计数法显示要保留的小数位