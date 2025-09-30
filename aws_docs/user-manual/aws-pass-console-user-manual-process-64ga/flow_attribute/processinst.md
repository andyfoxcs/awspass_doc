# 流程操作 · AWS PaaS文档中心

## 流程操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/common_set4.png)](<common_set4.png>)

项 | 说明  
---|---  
作废 | 开启后任务在第一个节点时工具条提供`作废`按钮，如果任务是退回至流程第一个节点时，  
作废后流程实例被强制终止，并且从已办任务中可查看  
撤销 | 是否允许该流程发起者在流程未结束时主动撤销流程，该功能提供在`流程中心 > 发起跟踪`  
的撤销列和流程组发出列表撤销列[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/common_set6.png)](<common_set6.png>)  
不允许撤销节点 | 该属性在`撤销`被开启时可用  
1.到达：可指定某些节点未执行完毕（若任务已发送至该节点但尚未办理），则不提供撤销操作  
2.经过：可指定某些节点已执行完毕（若任务已发送至该节点但已办理），则不提供撤销操作  
撤销时清空历史审批记录 | 若勾选，撤销流程时，将会把该流程实例的所有已办任务删除，也会删除历史的审批记录  
收回 | 是否允许该流程任务的上个执行者收回下个任务，指下个任务是人工任务且尚未办理并且是  
单例时可收回，即反悔操作(串签不允许收回)。该功能提供在`流程中心 > 已办查询`的  
收回列和流程组已办列表收回列并行多实例允许收回的场景：  
1.并行多实例时，如果处于抢先接收的状态，还没有被抢先接收的情况，可以收回  
2.并行多实例时，未处于抢先接收的状态，如果没有人办理的情况，可以收回  
**其余的非单例情况均不允许收回**  
跟踪 | 跟踪流程执行过程  
跟踪图查看表单数据 | 该选项用于控制用户在流程跟踪图中，是否为每个任务提供`查看数据`按钮，表单打开为只读形式[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/common_set7.png)](<common_set7.png>)  
跟踪方式 | ． BPMN流程图  
． 不提供流程跟踪  
． 任务轨迹跟踪图  
催办 | 向当前流程执行人发送催办通知，支持邮件、短信、企业微信、阿里钉钉、飞书、系统通知  
(需要安装并启动通知中心应用，且系统通知即在6.4.2及以后版本提供)；安装并启用[邮件通知](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/index.html>)应用，短信、企业微信、阿里钉钉、飞书的相关配置详见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/notice.html>  
传递 | 开启后，启动流程时可设置优先级并自动向下传递。  
新页签打开 | ． 默认不开启（使用工作台/工作箱/DW的配置)   
． 开启后，新窗口打开（浏览器标签页）  
分布式受管 | 详见[Matrix分布式网格服务>配置策略>分布式应用](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.matrix/config/tab5.html>)  
  
催办通知展示

短信 | 邮件  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/sms-cuiban.png)](<sms-cuiban.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/email-cuiban.png)](<email-cuiban.png>)  
企业微信 | 阿里钉钉信  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/weixin-cuiban.png)](<weixin-cuiban.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/dingding-cuiban.png)](<dingding-cuiban.png>)  
飞书  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/feishu-cuiban.png)](<feishu-cuiban.png>)