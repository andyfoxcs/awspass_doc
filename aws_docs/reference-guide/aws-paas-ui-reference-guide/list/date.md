# 日期 | AWS UI组件参考指南

## 日期

创建一个含有日期控件的文本选择框，对标准INPUT type=TEXT元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端 | 移动端(不同移动设备可能略有不同)  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/dateR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/dateR1_m.png)  
  
**预置校验**

  1. 参见单行[预置校验](<text.html#check>)

  2. 格式YYYY-MM-dd

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/dated1.png)

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

  * **_日期范围_**

可配置日期范围的最小、最大值。支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)，如@monthBegin(@date)；支持`$字段名`表示获取当前表单其他日期字段值，用于实现该字段的最小(最大)日期不能小于(大于)`$字段名`字段值

  * **_显示月份_**

日期控件一次显示的月份数，支持单月显示、双月显示

  * **_显示星期_**

只读时是否显示星期

  * **_显示格式_**

`EE`表示星期，`(EE)`表示运行时格式如 `(星期一)`

  * **_高级配置_**

供高级开发人员使用，可对日期控件进行相关设置。例如：`{maxDate:'$字段名'}{minDate:'$字段名'}` 设置最大 最小时间。 注意：当通过高级配置设置显示格式后，如 `{dateFmt:'yyyy年MM月dd日'}`，显示日期属性将不再升效。

> 部分扩展属性不支持移动端