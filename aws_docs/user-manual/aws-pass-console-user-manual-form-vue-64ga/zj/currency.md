# 货币 · AWS PaaS文档中心

# 货币

创建一个含有货币符号前缀和货币格式的文本输入框，对标准INPUT type=TEXT元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。字段类型可设为数值，数据库只存储货币值，货币符号不存储

## 运行

PC端 | 移动端  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textC_pc.png)](<textC_pc.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textC_mobile.png)](<textC_mobile.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textC1.png)](<textC1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**长度**

默认长度10，小数位默认0，录入长度超过字段长度时，不允许保存

参见单行[长度](<text.html#length>)

**零值显示**

参见数值[零值显示](<number.html#zero>)

**货币种类**

一个货币符号，默认为人民币，该符号不在数据库进行存储，是一个iconfont图标

  * **不显示**

  * **人民币**

  * **美元**

  * **港元**

  * **欧元**

  * **自定义** 填写图片路径，例如：../commons/img/add1_16.png

**后缀**

参见单行[前后缀](<text.html#qhz>)

> 货币只支持后缀，设置标签文字

**限定金额范围**

参见数值[限定数值范围](<number.html#xd>)

**格式**

参见数值[格式](<number.html#gs>)

> 货币只支持`千分位分隔符` `保留小数位数` `负值标红`

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