# 业务模型使用场景 · AWS PaaS文档中心

# 业务模型使用场景

AWS PaaS平台目前已实现数据源可引用CC DS的场景如下：

  * 表单中列表组件
  * 表单中单选组组件
  * 表单中复选组组件
  * 表单中网格字典组件
  * 表单中分类字典组件
  * 表单中树形字典组件
  * 表单中表格参考录入

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/sy1.png)](<sy1.png>)

步骤：

  1. DS中创建模型
  2. 表单相组件配置`CC数据服务`数据源

### 1\. DS中创建模型

有关DS模型的创建与配置参见本文档相关章节。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/sy2.png)](<sy2.png>)

### 2\. 表单相组件配置`CC数据服务`数据源

创建表单模型，拖动列表组件，配置数据源为`CC数据服务`，有关表单的使用详细参见[这里](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form/>)。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/sy3.png)](<sy3.png>)

### 注意事项：

  1. 表单组件中数据集位置只支持array（object）类型的
  2. 列表、单选组、复选组、分类字典、树形字典不支持DS有分页的
  3. 网格字典，支持有分页，分页走网格字典的分页
  4. 组件不支持分页，DS支持分页时，组件运行结果为DS的第一页数据
  5. 组件不支持分页，DS不支持分页时，组件运行结果为DS全部返回数据的前500条
  6. 组件支持分页，DS支持分页时，按组件设置分页显示取DS的全部数据
  7. 组件支持分页，DS不支持分页时，按组件分页取DS的前500条数据
  8. DS支持分页时， 组件的分页配置属性显示
  9. DS不支持分页时，组件的分页配置属性不显示