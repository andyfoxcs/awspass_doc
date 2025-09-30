# PC表单 · AWS PaaS文档中心

# PC表单

本章节将从以下几章节介绍PC表单的设计与运行时展示。

  * [新建表单](<../create>)
  * 表单基本信息
  * 组件
  * 数据源
  * 表单设计
  * 字段/布局属性
  * 表单属性
  * [主题设置](<../zt>)
  * PDF打印
  * 预览
  * [发布](<../fb>)

## 新建表单

详情参见[新建表单](<../create>)章节

## 表单基本信息

配置表单模型的基本信息，打开表单模型，点击左上角表单模型图标，打开基本信息窗口。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pc/baseinfo.png)](<baseinfo.png>)  
---  
项 | 说明  
---|---  
表单名称 | 同一个应用内不允许重复。支持%分类名%_表单名 格式，当流程节点绑定多个表单时，可按照分类名分组显示  
模型分类 | 这是所有业务模型的通用属性，用于标识该模型属于哪类业务区域  
是否受管 | 参见[受管应用](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>)，该类模型建意设为受管  
  
## 组件

提供19种常规组件、6种字典组件、8种布局、5种表格、9种高级组件 详情参见[组件](<../zj>)章节

## 数据源

详情参见[数据源](<../sjy>)章节

## 表单设计

  * 在`表单设计器`中，直接从左侧拖动组件到添加设计区
  * 设置`字段属性`及`表单属性`，设计完成点击保存
  * 在设计区的字段，还能进行`拖动` `复制` `删除`等操作,`删除`只是在表单设计区删除，在BO存储中还是存在的,在数据源中还能看到，删除字段标记为`未添加`，如果想再添加可以，在拖到设计区

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pc/design.png)](<design.png>)  
---  
  
## 字段/布局属性

字段属性为单个字段独有的属性设置，根据字段的不同，属性的设置也不尽相同。字段还可以由当前组件切换成其他组件，如单行切换成多行

字段属性   
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/quickstart/pzzdsx.png)](<../quickstart/pzzdsx.png>)  
布局属性   
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/quickstart/pzbjsx.png)](<../quickstart/pzbjsx.png>)  
  
## 表单属性

表单属性是对表单整体进行的一系列设置，区别于字段属性对于单个字段的设置

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/quickstart/pzbdsx.png)](<../quickstart/pzbdsx.png>)  
---  
  
详情使用参见[表单属性](<../sx>)

## 主题设置

详情参见[主题设置](<../zt>)章节

## PDF打印

详情参见[数据源](<../pdf>)章节

## 预览

设计的时候直接点击预览查看效果

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/quickstart/yl.gif)](<../quickstart/yl.gif>)  
---  
  
## 发布

详见[发布到应用商店](<../fb>)