# 手写签批 · AWS PaaS文档中心

# 手写签批

用户可以在表单页面上直接手写意见，也可以自动签署个人的人名章

**主要特点**

  * 支持在该UI区手写签批和键盘输入
  * 支持保存签批意见时自动带出预设的人名章作为签名
  * 支持是否开启扫码填写和常用意见设置
  * 支持签批意见是否互相可见的设置
  * 支持签批意见显示顺序按部门和领导身份自动排序
  * 支持预设签批字体颜色及粗细等样式

**特别说明**

  * 如果使用人名章，需要安装并启用 表单电子印章 应用，并在表单电子印章中维护人名章
  * 如果使用常用意见设置，需要安装并启用审批意见库应用

## 运行

PC端  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/hw1.png)](<hw1.png>)  
扫码填写  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/hw2.png)](<hw2.png>)  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/hw3.png)](<hw3.png>)  
移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/hw4.png)](<hw4.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/hw5.png)](<hw5.png>)

**标题**

参见单行[标题](<text.html#title>)

**输入方式**

`手写` `键盘` `自选手写或键盘`，三种输入方式，默认手写

**笔颜色**

手写签批时笔颜色,默认黑色，点击颜色块，弹出颜色选项卡，选择其它颜色

**笔粗细**

手写签批时笔粗细度，提供了`细` `普通` `粗` `更粗`四种选项，默认是`细`

> `笔颜色` `笔粗细` 这两个属性，只在手写输入方式中显示

**输入区域大小**

操作区域大小，提供了`800px*高368px` `416px*高416px`两种选项，默认`宽800px*高368px`

**显示签名日期**

默认不开启，开启后，表单运行时点击已签批的签名，可以看到签名日期

  * **签名日期格式**

开启`显示签名日期`，才显示`签名日期格式`,提供了`年月日`、`年月日时`、`年月日时分`三种格式，默认`年月日`格式

**显示签名人信息**

默认不开启，开启后，表单 运行时点击已签批的 签名，可以看到签名人信息

  * **信息格式**

开启`显示签名人信息`，才显示信息格式，提供了`姓名`、`姓名+部门`两种格式，默认`姓名`格式

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/hw6.png)](<hw6.png>)

>   * 当AWS为相应账户维护了人名章时，在进行签批时，将自动显示相应人名章，有关人名章的维护请参见[表单电子印章](<https://docs.awspaas.com/apps/com.actionsoft.apps.formui.cachet/index.html>)  
> 
>   * 手写签批只读时，点击签批查询签名人信息及日期
> 

**常用意见**

默认不开启，键盘输入方式时显示`常用意见`属性，是否可从常用意见里选择，使用该功能需正常安装并启用[审批意见库](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.comments/index.html>) 应用

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/hw7.png)](<hw7.png>)

**允许使用空签名**

默认不开启，运行时添加签名，还没开始签名时，使用签名置灰；开启后，运行时添加签名，还没开始签名时，使用签名可点击保存

PC端 | 移动端  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/hw8.png)](<hw8.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/hw9.gif)](<hw9.gif>)  
  
**多人签批时互相可见**

默认开启，在可编辑时，是否可以查看他人签批意见,该属性适用流程

**多人签批时排序方式**

提供了`按组织机构`，`按签名时间`这两个排序方式，默认按`组织机构`

**按组织机构**

按组织机构树顺序排列

**按签名时间**

按签名时间正序排列

**控制属性**

参见单行[控制属性](<text.html#control>),只支持`必填`

**宽度**

参见单行[宽度](<text.html#wigth>)

**帮助说明**

参见单行[帮助说明](<text.html#help>)

手写签批在运行时刻适用性一览

项 | 说明  
---|---  
主表 | 支持  
普通表格 | 支持  
编辑表格 | 支持  
手机表单 | 支持  
表单外链 | 不支持  
手机表单 | 不支持子表移动端布局展示，其他场景是支持的  
DW表格 | 支持  
DW看板、相册 | 支持  
DW时间轴 | 支持  
DW移动端 | 支持  
手机表单 | 支持