# 日期时间 | AWS UI组件参考指南

## 日期时间

创建一个含有日期、时间控件的文本选择框，对标准INPUT type=TEXT元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端 | 移动端(不同移动设备可能略有不同)  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/datetimeR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/datetimeR1_m.png)  
  
**预置校验**

  1. 参见单行[预置校验](<text.html#check>)

  2. 格式YYYY-MM-dd hh:mm:ss

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/datetimeD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

参见单行[扩展代码](<text.html#componentExtendCode>)

**扩展属性**

  * **_空值提示_**

参见单行[空值提示](<text.html#nulltip>)

  * **_起始时间_**

可选范围开始时间，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)，如@monthBegin(@datetime)

  * **_结束时间_**

可选范围结束时间，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)，如@monthBegin(@datetime)

  * **_显示月份_**

日期时间控件一次显示的月份数，支持单月显示、双月显示

  * **_分秒显示_**

控制分秒是否显示，当设置不显示后，分、秒值将不存储到数据库，因此当系统上线后，建意不要再更改该配置

  * **_高级配置_**

供高级开发人员使用，可对日期时间控件进行相关设置

> 部分扩展属性不支持移动端