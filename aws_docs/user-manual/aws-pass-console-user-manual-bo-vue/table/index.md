# 索引 · AWS PaaS文档中心

# 索引

为数据库表字段建立索引。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/index2.png)](<index2.png>)

  * `普通索引` 即数据库普通Index索引
  * `不重复索引` 即数据库Unique Index索引，参与索引字段的已有组合值不能重复
  * `索引备注` 用于表单保存时，当数据违反不重复索引时，展现给用户的提示信息

>   1. 如果确定该BO表为主表，建议为BINDID字段创建不重复索引
>   2. 如果确定该BO表为子表，建议为BINDID字段创建普通索引
> 

示例：

**在BO索引配置索引备注**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/index4.png)](<index4.png>)

**表单保存时，当有重复数据时，提示备注信息**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/index3.png)](<index3.png>)