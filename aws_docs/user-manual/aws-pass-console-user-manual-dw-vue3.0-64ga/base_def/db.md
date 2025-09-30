# 多表数据源 · AWS PaaS文档中心

# 多表数据源

为了满足用户在同一张视图中查看和分析多张表单业务数据的需求，提升了标准表格视图数据的呈现能力，在选择视图的数据来源时，支持同时选择多个业务表单/存储的数据源，将多张表的数据呈现在同一个表格视图中，方便用户更清晰地管理和分析数据。

[![](https://helpcdn.awspaas.com/picture/picture/202308/750dcbdc9382449394a9a5dcada2dfca.png)](<https://helpcdn.awspaas.com/picture/picture/202308/750dcbdc9382449394a9a5dcada2dfca.png>)

  * _数据来源中仅关联表单、关联存储支持多表数据源_
  * _支持选择多表数据源的视图类型：标准表格、看板、相册、日历、地图_

## 关联表单

[![](https://helpcdn.awspaas.com/picture/picture/202308/d4decb730a8d4584b07be0bc26753f1f.png)](<https://helpcdn.awspaas.com/picture/picture/202308/d4decb730a8d4584b07be0bc26753f1f.png>)

## 关联存储

[![](https://helpcdn.awspaas.com/picture/picture/202308/3bdf7f8976dc495ebc6b76402b1c8963.png)](<https://helpcdn.awspaas.com/picture/picture/202308/3bdf7f8976dc495ebc6b76402b1c8963.png>)

## 关联

选择多表数据源后，必须配置关联，且关联关系不能少于选择的多表-1，如选择了三个存储，关联关系不能少于2，如下图

[![](https://helpcdn.awspaas.com/picture/picture/202308/9c4c2023c7ea4d93a894e481f400b504.png)](<https://helpcdn.awspaas.com/picture/picture/202308/9c4c2023c7ea4d93a894e481f400b504.png>)

  * _有一种情况不需要配置关联，即关联表单勾选一个主子表，虽然有多个存储，但不需要再手动配置关联_

## 字段

多表数据源，字段是分表展示的，第一个为主表有且仅有一个主表，其他的是子表，子表也可以设置为主表，这时关联关系也需要与主子表对应上，否则无法生成正常的SQL

[![](https://helpcdn.awspaas.com/picture/picture/202308/6d05cfef9c124f95b49028f396c5001e.png)](<https://helpcdn.awspaas.com/picture/picture/202308/6d05cfef9c124f95b49028f396c5001e.png>)

如图中勾选的三个存储，采购主表是主表，其余两个是子表，第一条关联关系配置的是主表与第一个子表的关联

[![](https://helpcdn.awspaas.com/picture/picture/202308/354bbb7d4f4949c2b93b3a652dc47325.png)](<https://helpcdn.awspaas.com/picture/picture/202308/354bbb7d4f4949c2b93b3a652dc47325.png>)

这时把天津区采购子表B设置为主表，采购主表是第一个子表了，这时第一条关联与下面的数据源不匹配了，生成不了SQL,这时需要修改关联，设置成修改后的主表与第一个子表的关联

[![](https://helpcdn.awspaas.com/picture/picture/202308/4c68709b307c44c5adab47f972a0ea1a.png)](<https://helpcdn.awspaas.com/picture/picture/202308/4c68709b307c44c5adab47f972a0ea1a.png>)

多表数据源选择注意事项：

● 当选择的数据源为表单时，且选择的表单数量为2个及以上，且其中两组表单分别为主子表关系时，第二组表单的子表的字段不展示。  
示例：当选择表单1（A表单主表）+表单2（A表单子表）+表单3（B表单主表）+表单4（B表单子表）时，则表单4（B表单子表）字段数据信息无法展示。

## 应用场景

在一张表格视图中，展示采购信息和采购清单

[![](https://helpcdn.awspaas.com/picture/picture/202308/862bb3f42f49493db20c7f5c47809a3a.png)](<https://helpcdn.awspaas.com/picture/picture/202308/862bb3f42f49493db20c7f5c47809a3a.png>)

  * _根据后台配置的关联关系生成的数据展示中主表与子表是一对多的关系时，主表字段自动进行行合并_
  * _数据导出也是行合并的效果_