# 其他设置 · AWS PaaS文档中心

## 其他设置

**流程期限**

这是一项为实现流程绩效管理而提供的流程效率指标。当完成流程或节点任务时超过指定时限，可通过设置节点`时限`策略触发相应动作。参见[人工任务属性/基本属性/办理选项中的合理完成时限和宽延告警时限](<../manual_task/route.html>)。

**流程级别**

  * `不指定` 可以是顶级流程也可以是子流程  

  * `顶级流程`仅作为主流程，不会出现在[`调用子流程 > 子流程模型`](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/call_activity/README.html>)列表中  

  * `子流程`仅允许由主流程启动该流程实例，在流程工作箱无`新建`、`删除`按扭

**模型分类**

这是所有业务模型的通用属性，用于标识该模型属于哪类业务区域

**修改分类**

修改分类名称

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/xgfn1.png)](<xgfn1.png>)

**迁移分类**

把当前分类下的模型迁移到当前应用的指定分类下

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/qyfn1.png)](<qyfn1.png>)

**应用受管**

显示当前模型所在应用信息。是否受管参见[受管应用](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>)，该类模型建意设为不受管。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/common_set13.png)](<common_set13.png>)