# 日期 · AWS PaaS文档中心

# 日期

创建一个含有日期控件的文本选择框，对标准INPUT type=TEXT元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

## 运行

PC端 | 移动端  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdate_pc.png)](<textdate_pc.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdate_mobile.png)](<textdate_mobile.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdate1.png)](<textdate1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**限定日期范围**

限定日期的最小最大范围，输入框中支持@公式、$[字段名]字段名是表单中的其他字段

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdate2.png)](<textdate2.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdate2.1.png)](<textdate2.1.png>)  
  
**限定星期范围**

按星期选择限定的范围

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdate3.png)](<textdate3.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdate3.1.png)](<textdate3.1.png>)  
  
> `限定日期范围``限定星期范围`同时都设置了，显示两者的交集

**显示星期**

默认未开启，开启后运行时会显示选择的日期对应的星期几

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdate4.png)](<textdate4.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdate4.1.png)](<textdate4.1.png>)  
  
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