# 单选组 · AWS PaaS文档中心

# 单选组

创建一组单选按钮控件，对标准INPUT type=radio元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

## 运行

PC端  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/radiogroups.png)](<radiogroups.png>)  
移动端普通交互列表 | 移动端普通交互选项  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/radiogroupsD1.png)](<radiogroupsD1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/radiogroupsD1.1.png)](<radiogroupsD1.1.png>)  
移动端轮播选项卡 | 移动端里程碑  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS2.1.png)](<textS2.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS3.1.png)](<textS3.1.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRA1.png)](<textRA1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**数据源**

  * **添加“其他”选项**

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRA2.png)](<textRA2.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRA3.png)](<textRA3.png>)  
  
用户在表单中选择`其他`，显示出一个输入框，输入用户想输入的内容

**颜色开关**

对业务人员设计表单，提供更友好的自定义选项设置，列表、复选组等类似场景在DW、仪表盘中的操作一致；对重要状态类字段，在表单、表格上能一目了然的直观区分

  * `自定义`颜色开关在数据源组件自定义页签中，支持拖动选项的顺序、设置默认选择中、删除选项等操作

自定义颜色配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRA4.png)](<textRA4.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRA4.1.png)](<textRA4.1.png>)  
  
  * `关联表单`、`关联存储`、`关联字典`、`SQL数据源`、 `CC数据服务`的颜色开关在数据源组件外字段属性中

非自定义颜色配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRA5.png)](<textRA5.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRA4.1.png)](<textRA4.1.png>)  
  
**添加规则**

  * 未匹配到时，默认颜色，可以设置颜色
  * 点添加规则，把配置数据源对应SQL中的值，手动填在输入框并可以修改对应的颜色
  * 如果配置的数据源与自定义有关联，会把自定义中的key同步到颜色开关规则中，省去了再手动配置的麻烦

> 颜色开关配置后，运行效果不支持子表及移动端

数据源的其他配置项，参见单行[辅助录入](<text.html#source>)

**每行显示个数**

填写数字，例如：每行显示3个  

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/radiogroupsD2.png)](<radiogroupsD2.png>)

**移动界面展示**

  * **普通交互**

普通交互又有两种形式：列表、选项

  * 轮播选项卡

参见列表[轮播选项卡](<combobox.html#lb>)

  * 里程碑

参见列表[里程碑](<combobox.html#lcb>)

**控制属性**

参见单行[控制属性](<text.html#control>)

> 单选组只支持必填、只读这两个控制属性

**不允许重复录入**

参见单行[不允许重复录入](<text.html#nocopy>)

**宽度**

参见单行[宽度](<text.html#wigth>)

**帮助说明**

参见单行[帮助说明](<text.html#help>)

**字段规则**

参见单行[字段规则](<text.html#zdgz>)