# 关联查询 · AWS PaaS文档中心

# 关联查询

关联查询自动查询出其他表单或存储中的一条或多条数据，作为单独的查询展示功能，在存储中以虚拟字段存在，不做入库处理

## 运行

PC端 | 移动端  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx1.png)](<glcx1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx2.png)](<glcx2.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx3.png)](<glcx3.png>)

**标题**

参见单行[标题](<text.html#title>)

**数据源**

  * 数据来源有`关联表单` `关联存储` `SQl数据源` `CC数据服务`
  * 关联表单（表单单选、过滤仅主表字段、排序仅主表字段）
  * 关联存储（存储单选）
  * `关联表单` `关联存储` `SQl数据源` `CC数据服务`在这不需要有`值` `显示值` `值转换`等属性,其他属性的具体配置详细参见单行[辅助录入](<text.html#source>)

**显示字段**

选择需要显示在关联查询中的字段。显示字段仅作为展示使用，不提交入库，也不能参与公式等计算，可以在提交数据时查看这些数据。

点击 `显示字段`后的`添加`按钮即可添加显示字段，可以对已添加的显示字段进行修改名称、删除、显示/隐藏、拖动排序等操作

> 关联查询添加字段不支持添加虚拟字段,如关联查询组件  
> 

**数据条数**

  * 显示数据条数分为`一条`和`多条`
  * 通过数据源过滤条件过滤出来的数据可能会有多条，如果多条数据都需要显示则选择`多条`；如果选择了`一条`，则按照数据源查询结果显示第一条数据
  * 显示`多条`数据没有分页，通过懒加载来加载数据

**显示方式**

  * 显示数据分别为`字段` `卡片` `表格`三种
  * `数据条数`选择`一条`,只能按`字段` 来显示
  * `数据条数`选择`多条`,可以选择 `卡片` `表格`两种中的任一种方式来显示
  * `表格`显示方式，在设计器中可通过拖动调整字段列宽
  * 两种显示条数与显示方式的样式展示如下：

**PC端**

数据条数`一条` 显示方式`字段`  
---  
PC | 移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx4.png)](<glcx4.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx4_m.png)](<glcx4_m.png>)  
数据条数`多条` 显示方式`卡片`  
PC | 移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx5.png)](<glcx5.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx5_m.png)](<glcx5_m.png>)  
数据条数`多条` 显示方式`表格`  
PC | 移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx6.png)](<glcx6.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx6_m.png)](<glcx6_m.png>)  
PC子表 | 移动端子表  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx7.png)](<glcx7.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/glcx7_m.png)](<glcx7_m.png>)  
  
> `字段`应用表单主题设置中的布局效果，但不显示表格线 `卡片` `表格`不应用表单布局效果

**每行列数**

显示方式为字段、卡片时显示每行列数

> 记录小于列数时占满行

**链接选项**

参见单行[链接选项](<text.html#link>)

**宽度**

参见单行[宽度](<text.html#wigth>)

**帮助说明**

参见单行[帮助说明](<text.html#help>)

>   * 关联查询运行时展示的只读，不可编辑，数据来源数据库：  
>  1.有显示值、取值的都显示成显示值如列表、单选组、复选组、地址簿等组件  
>  2.需要查询详情的，能点击查看，如高级排版、附件、手写签批等组件  
>  3.关联查询不支持数据视图的场景
>