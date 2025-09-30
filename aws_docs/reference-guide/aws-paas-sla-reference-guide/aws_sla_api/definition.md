# 指标定义 | AWS SLA参考指南

## 指标定义

AWS SLA为开发者开放了读取指标定义的API。
    
    
    //SLA监控资源对象的指标定义
    ResourceMetric metric=SDK.getSLAAPI().getMetric("Infrastructure.cpu");
    
    //全部SLA监控资源对象的指标定义
    List<ResourceMetric> list=SDK.getSLAAPI().getMetrics();
    
    //获得SLA指标的多语言名称
    String name=SDK.getSLAAPI().getMetricName("Infrastructure.cpu","en");
    

> 对于SLAAPI详细说明及用法，参见**aws-api-doc**