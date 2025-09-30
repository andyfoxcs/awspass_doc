# 数值 · AWS PaaS文档中心

# 数值

创建一个含有数值校验的文本输入框，对标准INPUT type=TEXT元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

## 运行

PC端 | 移动端  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN_PC.png)](<textN_PC.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN_mobile.png)](<textN_mobile.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN1.png)](<textN1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**长度**

默认长度10，小数位默认0，录入长度超过字段长度时，不允许保存

参见单行[长度](<text.html#length>)

**前后缀**

参见单行[前后缀](<text.html#qhz>)

**零值显示**

  * 不显示
  * 显示为'0'
  * 显示为'--'

配置不显示 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN2.png)](<textN2.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN2.1.png)](<textN2.1.png>)  
配置显示为'0' | 运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN3.png)](<textN3.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN3.1.png)](<textN3.1.png>)  
配置显示为'--' | 运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN4.png)](<textN4.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN4.1.png)](<textN4.1.png>)  
  
> 没有填写时默认是空，只有输入为0时才存0，当存0时才按照`零值显示`配置显示

**限定数值范围**

设置最小、最大值，运行时输入框中只能输入限定范围内的数值，不在限定范围内的数值，输入后会自动变成最小或最大值

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN5.png)](<textN5.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN5.1.gif)](<textN5.1.gif>)  
  
> 如果默认值不在限定范围内，运行时默认显示最小值

**格式**

表单运行时，输入数值后，数值的展现形式

  * 千分位分隔符
  * 百分比
  * 保留小数位数
  * 负值标红
  * 提供数值调节按钮
  * 科学计数法

配置千分位分隔符 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN6.png)](<textN6.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN6.1.png)](<textN6.1.png>)  
配置百分比 | 运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN7.png)](<textN7.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN7.1.png)](<textN7.1.png>)  
配置保留小数位数 | 运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN8.png)](<textN8.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN8.1.png)](<textN8.1.png>)  
配置负值标红 | 运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN9.png)](<textN9.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN9.1.png)](<textN9.1.png>)  
配置提供数值调节按钮 | 运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN10.png)](<textN10.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN10.1.png)](<textN10.1.png>)  
配置科学计数法 | 运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN11.png)](<textN11.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textN11.1.png)](<textN11.1.png>)  
  
>   * `千分位分隔符`和`百分比`不能同时勾选  
> 
>   * 没设置`小数位`时，`保留小数位数`禁选,设置`小数位`时，`提供数值调节按钮`禁选
> 

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