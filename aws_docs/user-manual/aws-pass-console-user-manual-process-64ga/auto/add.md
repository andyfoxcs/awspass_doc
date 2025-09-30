# 新增数据 · AWS PaaS文档中心

## 新增数据

新增数据就是当触发类型和触发条件满足时，按配置规则，为目标表单主表、子表添加数据。支持同步创建新实例或在已有实例添加。

### 同步创建新实例

会同步为目标表单关联的流程创建一个新实例。 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/add1.png)](<add1.png>)

  * `目标表`会自动罗列出当前所选目标表单中所有的主表和子表
  * `源表` 可在当前流程模型引用的所有主表、子表中选择，如果为子表，子表多条数据，新增到目标表后流程实例数据只有一条，BO业务数据会对应创建多条
  * `表单值` 可以在选择的源表字段列表中选择
  * `固定值` 支持@公式
  * 目标字段如果不进行源映射，则在执行时，如果该字段配置了默认值，会自动为该字段插入字段默认值
  * 字段映射仅支持以下UI组件类型：单行、多行、数值、货币、列表、单选组、复选组、附件、日期、时间、日期时间、HTML排版、网格数据字典、平板数据字典、树形数据字典、地址簿

### 在已有实例新增

根据过滤条件（一般为业务唯一标识字段），为查询到的流程实例，添加BO数据。该选项主要用于为目标表单的子表数据进行记录的增加。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/add5.png)](<add5.png>)

### 应用举例

日常费用申请流程，在填写节点选择`提交`审核动作后，将日常费用申请数据插入到日常费用报销记录流程表中。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/add3.png)](<add3.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/add4.png)](<add4.png>)

### 效果预览

当选择提交并办理成功后，日常费用申请数据插入到日常费用报销记录流程表中

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/add6.png)](<add6.png>)

日常费用报销记录流程中添加了相应的日常费用申请数据

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/add7.png)](<add7.png>)