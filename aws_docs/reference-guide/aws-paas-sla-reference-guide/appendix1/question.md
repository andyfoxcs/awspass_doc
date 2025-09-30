# 常见的分析场景 | AWS SLA参考指南

# 常见的分析场景

**_通过示例，列举场景分析的方法_**

  * AWS服务器硬件资源负荷情况?
  * 在线用户数与并发数的预估比例?
  * 数据库并发连接数和性能情况?

## AWS服务器硬件资源负荷情况?

SLA只能监控分析AWS实例节点（App应用服务器）的硬件资源指标，不能监控Web和DB的资源负荷。

_15天监控指标数据，回放平均值（示例）_

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/22.png)

**分析结果**

  * CPU使用情况属于健康状态（每小时平均不高于30%）
  * JVM内存分配合理（4G），系统剩余可用内存充足（30G以上）
  * 可能发生过2次服务中断。其中一次机房断电故障导致从凌晨直至早上7点恢复正常（见上图箭头区域）
  * 虽然CPU平均使用率不高，我们在继续回放该指标峰值（最大值）数据时（下图），发现偶尔存在CPU达到90%的情况

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/23.png)

## 在线用户数与并发数的预估比例?

`并发数`是服务器在瞬间同时执行的任务数。`在线用户`与`并发数`的比例，与以下因素有关

  * 与用户实际部署AWS的硬件资源、数据库性能有直接关系。配置越高，产生的瞬间并发量越小
  * 与用户高峰期操作有关。相同用户规模下同一时间操作（如登录、处理任务）越频繁，产生的瞬间并发量越大
  * 与操作逻辑处理的复杂度有关。处理逻辑越复杂（如复杂的数据库处理、大量运算），产生的瞬间并发量越大

`并发数`高峰时，也是服务器压力最大的时段。通常可以从SLA的指标趋势图中，可以找到每家企业的`高峰期`规律。

_15天监控指标数据，回放最大值（示例）_

  * 并发请求数
  * 活跃用户数

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/21.png)

**分析结果**

  * 该客户每天有两个操作高峰期，上午10点和下午3点
  * 在线用户峰值在60-70人，并发数峰值在6-7个
  * 该客户的在线用户数与并发数的预估比例为10:1

## 数据库并发连接数情况?

如果一段时间突然出现不规律的高峰，请重点分析该时段是否存在慢SQL。

_15天监控指标数据，回放最大值（示例）_

  * 数据库连接池活动连接数
  * SQL执行耗时

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/24.png)

**分析结果**

  * 高峰期不超过10个连接并发，不存在对数据库造成高负荷压力
  * 虽然数据库并发不高，我们在继续回放`SQL执行耗时`指标峰值（最大值）数据时（下图），发现两次在凌晨3点执行SQL超过10秒的情况

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/25.png)

  * 我们通过查询该时段的`慢SQL`告警信息，定位到具体SQL（下图）

![](https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/26.png)