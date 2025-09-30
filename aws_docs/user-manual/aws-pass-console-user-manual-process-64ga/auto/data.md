# 数据服务 · AWS PaaS文档中心

# 数据服务

获取外部系统数据，支持数据服务和数据流两种外部系统数据来源。

[![](https://helpcdn.awspaas.com/picture/picture/202308/82cc2fe330d64de6a1b3dd879be84dcd.png)](<https://helpcdn.awspaas.com/picture/picture/202308/82cc2fe330d64de6a1b3dd879be84dcd.png>)

## 数据服务

**数据服务** 来自【连接服务-数据】列表中的数据，只显示当前应用及关联应用的【连接服务-数据】，详情请参见[数据服务](<https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/>)。

**数据集位置**

根据选择的数据服务，选择对应的数据集，数据集只支持数组类型的。

**参数** 选择的数据服务参数，如果是系统给定的参数不允许删除，非系统给定的可以删除。

  * 当前CC数据源如果支持分页查询，组件数据源只取第一页数据

**新增输出映射**

先选择执行动作的目标，可以是流程，也可以是视图，然后再新增字段映射，映射的目标字段包含表单的主、子表存储及流程变量。

[![](https://helpcdn.awspaas.com/picture/picture/202308/b3949c4e35c14f60be58d3c9e78a3789.png)](<https://helpcdn.awspaas.com/picture/picture/202308/b3949c4e35c14f60be58d3c9e78a3789.png>)

## 数据流

需要安装[服务编排](<https://docs.awspaas.com/apps/com.actionsoft.apps.dataflow/>)应用及对应的服务，详情请参见[服务编排](<https://docs.awspaas.com/apps/com.actionsoft.apps.dataflow/>)在上层中使用与数据服务一致。

## 应用举例

员工信息修改流程，在填写节点选择【提交】审核动作后，通过数据服务从外部获取的用户名及用户ID映射到员工档案表中的账号、姓名。

[![](https://helpcdn.awspaas.com/picture/picture/202308/2e88caddf0e348c9950c33e67408093d.png)](<https://helpcdn.awspaas.com/picture/picture/202308/2e88caddf0e348c9950c33e67408093d.png>)

[![](https://helpcdn.awspaas.com/picture/picture/202308/cdf64170b97d48f884df2d8cecbc941a.png)](<https://helpcdn.awspaas.com/picture/picture/202308/cdf64170b97d48f884df2d8cecbc941a.png>)

## 效果预览

当选择提交并办理成功后，数据服务从外部获取的用户名及用户ID映射到员工档案表中的账号、姓名。

[![](https://helpcdn.awspaas.com/picture/picture/202308/bfbfa690b94148c688d9a4ccc4961d43.png)](<https://helpcdn.awspaas.com/picture/picture/202308/bfbfa690b94148c688d9a4ccc4961d43.png>)

员工档案表中映射了相应的账号、姓名的数据。

[![](https://helpcdn.awspaas.com/picture/picture/202308/134069c4465240f59d4a86e3034abc9a.png)](<https://helpcdn.awspaas.com/picture/picture/202308/134069c4465240f59d4a86e3034abc9a.png>)

## SQL数据

  * 支持本地数据源或者是CC数据源
  * SQL语句仅支持select

  * 映射字段规则：

    * 所有映射字段只能同时是一个主表的字段，或者同时是一个子表的字段，不能既有主表又有子表的字段
    * 如果映射的是主表：根据SQL结果生成对应数量的实例，按照字段配置映射
    * 如果映射的是子表：会把sql的结果都给到子表，这些数据的bindid是一样

## 应用举例

员工信息修改流程，在填写节点选择【提交】审核动作后，通过SQL数据用SQL语句查出用户名及用户ID映射到员工档案表中的账号、姓名。

[![](https://helpcdn.awspaas.com/picture/picture/202312/a5f220fb99154f22993281feb4048402.png)](<https://helpcdn.awspaas.com/picture/picture/202312/a5f220fb99154f22993281feb4048402.png>)

[![](https://helpcdn.awspaas.com/picture/picture/202312/9c874147f18e43caba30b67710b2da65.png)](<https://helpcdn.awspaas.com/picture/picture/202312/9c874147f18e43caba30b67710b2da65.png>)

## 效果预览

当选择提交并办理成功后，SQL数据用SQL语句查出用户名及用户ID映射到员工档案表中的账号、姓名

[![](https://helpcdn.awspaas.com/picture/picture/202308/bfbfa690b94148c688d9a4ccc4961d43.png)](<https://helpcdn.awspaas.com/picture/picture/202308/bfbfa690b94148c688d9a4ccc4961d43.png>)

员工档案表中映射了相应的账号、姓名的数据。

[![](https://helpcdn.awspaas.com/picture/picture/202312/574e9900c0e14af7862aaa8f8cd83e36.png)](<https://helpcdn.awspaas.com/picture/picture/202312/574e9900c0e14af7862aaa8f8cd83e36.png>)