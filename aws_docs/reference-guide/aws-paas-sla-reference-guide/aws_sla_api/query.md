# 查询接口 | AWS SLA参考指南

## 查询接口

AWS SLA开放了对指标监控数据和告警日志记录的查询，高级开发者可以通过这些API开发特定的或更有效的分析工具。

方法 | 说明  
---|---  
queryDayDataByMetricId | 查询一个SLA指标全部天维度的历史数据（只存储最近365天），可能多于365条  
queryHourDataByMetricId | 查询一个SLA指标全部小时维度的历史数据（只存储最近15天），可能多于360条  
queryMinuteDataByMetricId | 查询一个SLA指标全部分钟维度的历史数据（只存储最近24小时），可能多于288条  
countAlarmDataOfNoRead | 查询未读的告警日志数量  
queryAlarmData | 查询前N条告警记录  
queryAlarmDataByMetricId | 查询一个指标的前N条告警记录  
  
> 对query类接口说明，参见**aws-api-doc** 的SLAAPI。如果你的算法和创意足够棒，也欢迎将它封装成AWS扩展工具（`ADD-ONS`），提交到`AWS企业应用商店`，让更多AWS PaaS用户受益于你的成果。