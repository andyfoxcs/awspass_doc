# 监控安全风险 | AWS SLA参考指南

# 监控安全风险

分析某个AWS PaaS实例采集的`安全风险`类监控数据，包括

  * 告警事件
  * 账户冻结
  * 越权访问

对于风险类监控，当AWS处于集群部署时，每个AWS实例节点的监控数据是一样的。

## 告警事件

**说明：该AWS实例有关`安全风险`类指标发生的告警信息，列出最新5条。**

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/71.png)

告警规则Id | 告警标题 | 触发规则  
---|---|---  
Unauthorized Access | 发生越权访问 | 发生即触发  
  
告警规则是内置的，高级运维人员也可以修改和添加规则。

  * [平台内置的告警规则](<../appendix1/alarm_rules.html>)
  * [管理和修改告警规则](<setting.html>)

## 账户冻结

**说明：回放冻结账户的情况，用于辅助分析潜在的攻击风险。**

  * 最近24小时（5分钟合计数据）
  * 最近15天（1小时合计数据）
  * 最近1年（1天合计数据）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/92.png)

_诊断思路_

  * 正常情况下，存在一定比例的用户名、密码连续输错情况。如果某个期间该指标有较大波动，存在黑客攻击的风险
  * 连续登录失败超出`conf/aws-portal.xml`的`failLockedTimes`设定大小时被自动冻结，持续`unlockTime`时间后自动解冻

## 越权访问

**说明：回放拦截越权访问的情况，用于辅助分析潜在的攻击风险。**

  * 最近24小时（5分钟合计数据）
  * 最近15天（1小时合计数据）
  * 最近1年（1天合计数据）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/93.png)

_诊断思路_

  * 当用户通过URL地址伪造参数进行提权时，被记录为越权事件
  * 当开发者调用`LogAPI.unauthorizedAccess()`时，将该审计信息记录越权事件