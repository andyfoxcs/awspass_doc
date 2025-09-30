# 表单规则 · AWS PaaS文档中心

# 表单规则

在用户编辑、保存表单时，对表单字段、数据进行校验。支持以下规则：

  * 提交规则
  * 显示规则
  * 必填规则
  * 修改规则
  * 计算规则

## 配置入口

  * 主表单，点击右侧`表单属性`页签中的`表单规则`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/bdgz.png)](<bdgz.png>)  
---  
  
  * 子表，在表单设计区选中子表，点击右侧`表单属性`页签中的`表单规则`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/subbdgz.png)](<subbdgz.png>)  
---  
  
### 提交规则

当用户保存表单数据时，对数据合法性进行校验。等同于编写服务器端java程序进行数据提交校验。该提交规则仅在表单对应字段状态处于可编辑状态时执行，会逐条校验`编辑表格`记录。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/subbdgz3.png)](<subbdgz3.png>)  
---  
  
  * 主表中点提交/办理时给校验提示
  * 表格中的点保存校验，但点主表中的提交/办理时也给出校验
  * DW数据视图，点保存校验，当有警告中断又有仅提示的时只提示警告中断，没有警告中断后，仅提示与保存成功提示一起显示

  * 判断符号，常用判断符号包括

类型 | 支持的判断符号  
---|---  
文本 | `等于` `包含` `不包含` `开头是` `结尾是`  
数值 | `大于` `小于` `等于` `不等于` `大于等于` `小于等于`  
日期 | `大于` `小于` `等于` `不等于` `大于等于` `小于等于`  
  
  * 支持@公式用法详情参见：[AWS @公式参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)

  * `警告并中断` 当校验不通过时，弹出输出信息并阻止提交

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/subbdgz1.png)](<subbdgz1.png>)  
---  
  * `仅提示` 当校验不通过时，仅弹出输出信息

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/subbdgz2.png)](<subbdgz2.png>)  
---  
  * `提示内容` 当校验不通过时，返回给用户的提示信息

### 显示规则

配置字段、子表或指定DIV区域的显示隐藏或更新字段标题。此配置优先级最低，即如果字段被在BO存储、流程节点配置等场景设为隐藏后，通过此处配置是无法显示相应字段的。

1.同一个字段被多次设为显示或隐藏后，仅最下面的配置有效  
2.如果项，不支持同一个字段配置多次  
3.该规则不支持编辑表格  
4.提供扩展事件displayRuleExtEvent(displayRules, expressionResult) ，详细参见配置页说明  
5.显示仅适用于DIV区域在表单初始化时通过style="display: none;"设置为隐藏状态场景，可通过该规则设为显示  
6.条件字段列表中仅显示支持的UI组件类型字段  
7.结果字段支持的UI组件类型参见 AWS UI组件运行设计一览表  
8.配置的条件最好相反成对出现，如条件一当字段A等于admin，字段B显示，同时也需要配置条件二，字段A不等于admin，字段B隐藏。如果只配置条件一，当字段A不等于admin,字段B还是必填

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/displayrule1.png)](<displayrule1.png>)  
---  
  
> 条件匹配关系为包含时，支持逗号分隔的多个值，在运行时多值间为或的关系。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/displayrule2.png)](<displayrule2.png>)  
---  
  
### 必填规则

灵活配置字段是否必填及必填提示语。

1.同一个字段被多次设为必填或不必填后，仅最下面的配置有效  
2.`如果`项，不支持同一个字段配置多次  
3.该规则不支持编辑子表  
4.运行时表单是只读或隐藏状态时，忽略必填校验  
5.条件字段列表中仅显示支持的UI组件类型字段  
6.结果字段支持的UI组件类型参见 AWS UI组件运行设计一览表  
7.配置的条件最好相反成对出现，如条件一当字段A等于admin，字段B必填，同时也需要配置条件二，字段A不等于admin，字段B不必填。如果只配置条件一，当字段A不等于admin,字段B还是必填

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/requiredrule.png)](<requiredrule.png>)  
---  
  
> 条件匹配关系为包含时，支持逗号分隔的多个值，在运行时多值间为或的关系。

### 修改规则

通过规则配置可编辑的字段只读。

1.条件字段列表中仅显示支持地的UI组件类型字段  
2.结果字段支持的UI组件类型参见 AWS UI组件运行设计一览表

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/modifyrule.png)](<modifyrule.png>)  
---  
  
> 条件匹配关系为包含时，支持逗号分隔的多个值，在运行时多值间为或的关系。

### 计算规则

表单字段及子表字段自动计算规则。

1.支持+、 -、 * 、/、()运算符号  
2.支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)  
3.支持子表特定函数，详细参见配置界面子表函数  
4.值初始化时自动计算用于字段有默认值时，新增数据自动计算 如果出现负数的字段需要对于运算符表达式在字段外添加小括号，例：(BO_EU_JSGZZIBIAO.W2)-(BO_EU_JSGZZIBIAO.W1)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/calcrule.png)](<calcrule.png>)  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/gz/calcrule1.png)](<calcrule1.png>)