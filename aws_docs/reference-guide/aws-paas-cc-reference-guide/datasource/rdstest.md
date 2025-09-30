# 测试一下 · AWS PaaS文档中心

# 测试一下

模拟测试DS服务。配置好后保存点击左下角测试一下按钮。

  * 勾选设置为null，则该参数向服务器传递的就是null
  * 如果删除参数，如果参数有默认值则向服务器端传递默认值，如果参数没有默认值则向服务器传递的就是null
  * 当参数设置为系统给定时，测试一下页面相应参数不允许编辑
  * 当参数勾选必填时，测试一下页面相应参数不允许勾选设置null和删除
  * 测试一下，当参数不填值时，执行，该参数就会当作空进行处理，如where字段时，就会当成空串进行查询；update 字段时就会把字段更新为空串

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds49.png)](<rds49.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds50.png)](<rds50.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds54.png)](<rds54.png>)

## API示例

只读显示通过CC DS API调用时示例，供开发者查看。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds51.png)](<rds51.png>)

## 输入输出结构

只读显示输入输出结构，供开发者查看。 [![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds52.png)](<rds52.png>)