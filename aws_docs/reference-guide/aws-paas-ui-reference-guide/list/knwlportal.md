# 知识门户 | AWS UI组件参考指南

## 知识门户

使用该UI组件需要正常安装并启用[KMS知识管理](<https://docs.awspaas.com/apps/com.actionsoft.apps.kms/>)应用。

> 目前该UI组件不支持移动端

### 运行

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/knwlportalR1.png)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/knwlportalD1.png)

**基本属性**

  * **_查询列宽_**

不支持

  * **_扩展代码_**

不支持

**扩展属性**

无

> 该UI组件运行时数据库存储为知识卡片ID，需由开发者调用 `aslp://com.actionsoft.apps.kms/GetKnwl`进行后续操作