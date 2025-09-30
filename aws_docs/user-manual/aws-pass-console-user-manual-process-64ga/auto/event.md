# 触发类型 · AWS PaaS文档中心

## 触发类型

设置AWS流程引擎触发类型，支持当前流程绑定的表单数据源和特定动作两类

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/a.png)](<a.png>)

### 当前表单数据源

可触发当前流程绑定表单的BO表的触发动作有新增、修改、删除数据这三种。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/event2.gif)](<event2.gif>)

项 | 说明  
---|---  
触发类型 | 新增数据、修改数据、删除数据  
触发对象 | 可在当前流程绑定表单的主表、子表中选择数据所在存储  
  
> 选择`修改数据`选择存储后，还需要添加监控字段

### 特定动作

可监控当前流程特定流程引擎的执行动作有流程状态变化、定时触发、点击按钮。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/event3.png)](<event3.png>)

**流程状态变化**

  * 支持各节点审核菜单动作   

  * 支持流程撤销、作废、终止、结束事件   

  * 支持节点任务收回   

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/event3.1.gif)](<event3.1.gif>)

**定时触发**

项 | 说明  
---|---  
触发类型 | 定时触  
触发对象 | 可在当前流程绑定表单的主表、子表中选择数据所在存储  
开始时间 | 通过组件选择时间或自定义开始时间，支持@公式  
重复类型 | 仅触发一次、每天/周/月/季/年一次、Cron公式  
结束时间 | 通过组件选择时间或自定义结束时间，支持@公式  
  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/event3.2.gif)](<event3.2.gif>)

**点击按钮**

选择流程或表单子表自定义按钮

自动化点击按钮  
---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/event3.3.png)](<event3.3.png>)  
子表自定义按钮  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto/event3.4.png)](<event3.4.png>)