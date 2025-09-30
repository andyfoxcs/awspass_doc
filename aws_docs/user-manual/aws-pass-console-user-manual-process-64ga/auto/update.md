# 修改数据 · AWS PaaS文档中心

## 修改数据

修改数据就是当触发类型和触发条件满足时，按配置规则，修改目标表信息。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/update1.png)](<update1.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/update6.png)](<update6.png>)

  * `固定值`支持直接选择目标表 、源表字段
  * #[XXX] 表示目标表字段
  * $[XXX] 表示源表字段
  * 可通过@calc公式组合实现目标表、源表字段的 + - * / 运算。例如：商品库存量=原库存量 - 出库数量， 则可写为： `@calc(#[KCQUANTITY] - $[CKQUANTITY])`

### 应用举例

商品出库申请批准通过后后，在出库节点选择`确认出库`审核动作后，扣减对应该类商品的库存数量。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/update2.png)](<update2.png>)

### 效果预览

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/update3.png)](<update3.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/update4.png)](<update4.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/update5.png)](<update5.png>)