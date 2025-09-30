# 注册监听器 | AWS SLA参考指南

## 注册监听器

当告警事件被触发时，SLA告警器会同步触发一个钩子接口。开发者可通过实现自己的监听器对告警做处理（如向客户的IT基础设施发送告警日志， 或者根据告警级别发送短信）

### 注册一个外部告警监听器

  1. 编写AlarmListener监听器接口实现类
  2. 当自己的App启动时，调用如下API完成注册

    
    
    SDK.getSLAAPI().registerAlarmListener(listener);
    

### 卸载一个外部的告警监听器

当自己的App暂停时，调用如下API完成卸载
    
    
    SDK.getSLAAPI().unRegisterAlarmListener(listener);
    

> 对于AlarmListener接口说明，参见**aws-api-doc**

### 注意事项

监听器将被SLA告警器同步触发，如果你的代码存在超时或网络延时，将会同步影响到AWS相关操作。建议：

  1. 避免你的代码成为性能瓶颈
  2. 使用线程处理你的代码