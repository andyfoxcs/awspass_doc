# 存储SLA数据的表 | AWS SLA参考指南

# 存储SLA数据的表

表 | 说明  
---|---  
SYS_SLA_DIM_M | SLA 指标分钟维度数据。以 5 分钟为单位,存储每个 AWS 服务节点的 SLA 指标值。只滚动保留某一指标最近24小时的数据  
SYS_SLA_DIM_H | SLA 指标小时维度数据。以 1 小时为单位,存储每个 AWS 服务节点的 SLA 指标值。只滚动保留某一指标最近15天的数据  
SYS_SLA_DIM_D | SLA 指标天维度数据。以 1 天为单位,存储每个 AWS 服务节点的 SLA 指标值。只滚动保留某一指标最近365天的数据  
SYS_SLA_ALARM | SLA 告警记录。存储每个 AWS 服务节点的 SLA 告警记录