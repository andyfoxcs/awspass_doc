# 结构检查 · AWS PaaS文档中心

# 结构检查

由于某种原因导致BO模型文件与数据库物理表存在差异时，可使用该功能将两种统一，原则上是以BO模型文件为准，同步修改数据库物理表。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/checkbo/checkbo1.png)](<checkbo1.png>)

>   1. BO视图仅支持物理视图是否存在与模型文件的差异，不支持视图字段列的差异检查
>   2. BO表原则上仅支持物理表字段的新增、修改操作，不处理删除操作
>