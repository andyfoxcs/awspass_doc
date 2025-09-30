# 规则设置 | AWS SLA参考指南

# 规则设置

SLA标准产品预制了[常用告警规则](<../appendix1/alarm_rules.html>)，系统管理员可以根据需要修改和增删新规则。

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/aws_sla_management/101.png)

> 有关告警规则的基本概念，请[参见这里](<../work/alarm_rule.html>)

## 规则表达式

任何指标都可以通过表达式描述成一个告警规则，当表达式成立时触发一次告警事件。
    
    
    例如：当CPU使用率连续2次大于90%时，发出一条警告类息息
    

项 | 说明  
---|---  
监控指标 | 取值对象。请[参见这里](<../appendix1/resource_metric.html>)  
时段 | 取值范围。支持即时、5分钟数据、1小时数据、1天数据  
连续 | 当连续发生N次时，默认为1  
比较 | 值比较  
值 | 阈值。具体视指标单位，如百分百单位时，0.9表示90%  
告警级别 | 支持三种级别，错误、警告、通知  
  
## 设置通知列表

SLA通知列表显示的是系统通知中配置的，支持短信通知、邮件通知、企业微信、钉钉、飞书通知，详见[系统通知](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/appendix/scenes.html#b>)

## 延伸阅读

  * [内置的监控指标](<../appendix1/resource_metric.html>)
  * [内置的告警规则](<../appendix1/alarm_rules.html>)