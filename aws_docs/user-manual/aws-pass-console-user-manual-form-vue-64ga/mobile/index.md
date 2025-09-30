# 移动表单 · AWS PaaS文档中心

# 移动表单

本章节将从以下几章节介绍移动表单的设计与运行时展示。

  * 表单设计区
  * 主题设置
  * 表格展示方式

## 表单设计区

  * 建空白表单，从左侧拖动字段到设计区，在没保存之前PC和移动端同步添加，如果保存后，再拖动字段到设计区，PC和移动端不同步添加
  * 从数据源新建表单和从模板库创建，数据源中的字段PC和移动端都自动在设计区展示
  * 移动表单字段只能一列展示
  * 支持`拖动` `复制` `删除`字段等操作，同PC操作一样，删除字段只是在设计区删除，存储中还存在，在数据源中还能看到，删除字段标记为`未添加`，如果想再添加可以切换到数据源，在拖到设计区

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/design1.png)](<design1.png>)  
---  
  
## 主题设置

移动端有自己独特的`卡片风格`，主题设置的详细配置参见[移动端主题风格配置](<../zt/README.html#mobilestyle>)

## 表格展示方式

`普通表格`、`编辑表格`、`树形表格`展示方式一样，`字段内容` `摘要信息` `布局展示` `自定义布局` 这四种展示方式

**字段内容**

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile1.1.png)](<mobile1.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile1.png)](<mobile1.png>)  
  
**摘要信息**

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile2.1.png)](<mobile2.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile2.png)](<mobile2.png>)  
  
**布局展示**

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile3.1.png)](<mobile3.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile3.png)](<mobile3.png>)  
  
**自定义布局**

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile9.1.png)](<mobile9.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile9.png)](<mobile9.png>)  
  
  * 选择自定义配置，显示`布局配置`
  * 点`布局配置`中的`添加`按钮，可添加行，在行中设置取值字段，对取值字段进行样式设计
  * `拖动`、`删除`都是对行进行的操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile10.gif)](<mobile10.gif>)  
---  
  
`折列表格`展示方式只有 `摘要信息` 这一种展示方式

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile4.1.png)](<mobile4.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile4.png)](<mobile4.png>)  
  
> 展示所有字段内容

`WBS表格`按配置模式显示

**WBS普通模式**

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile5.1.png)](<mobile5.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile5.png)](<mobile5.png>)  
  
**WBS模式**

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile6.1.png)](<mobile6.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile6.png)](<mobile6.png>)  
  
> 不支持进度条的拖动

**分页**

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile7.1.png)](<mobile7.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile7.png)](<mobile7.png>)  
  
**参考录入**

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile8.1.png)](<mobile8.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/mobile/mobile8.gif)](<mobile8.gif>)  
  
> 合计在移动端不支持