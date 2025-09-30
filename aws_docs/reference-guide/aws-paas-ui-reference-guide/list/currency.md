# 货币 | AWS UI组件参考指南

## 货币

创建一个含有货币符号前缀和货币格式的文本输入框，对标准INPUT type=TEXT元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。字段类型可设为数值，数据库只存储货币值，货币符号不存储。

### 运行

PC端 | 移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/currencyR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/currencyR_m.png)  
  
**预置校验**

参见单行[预置校验](<text.html#check>)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/currencyD1.png)

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

参见单行[扩展代码](<text.html#componentExtendCode>)

**扩展属性**

  * **_零值处理_**

参见数值[零值处理](<number.html#valueprocess>)

  * **_空值提示_**

参见单行[空值提示](<text.html#nulltip>)

  * **_货币种类_**

一个货币符号，默认为人民币，该符号不在数据库进行存储，是一张图片

    * **不显示**

    * **人民币**

    * **美元**

    * **港元**

    * **欧元**

    * **自定义** 填写图片路径，例如：../commons/img/jap.png

  * **_允许清空(移动端)_**

参见单行[允许清空(移动端)](<text.html#delete>)