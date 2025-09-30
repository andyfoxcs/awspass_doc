# 基本信息 · AWS PaaS文档中心

## 基本信息

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/info1.png)](<info1.png>)

### 名称

节点名称，例如`财务初审`

### 审批记录

默认开启，显示审批记录，就是显示当前任务节点及当前任务节点之前的任务审批记录

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/base4.png)](<base4.png>)  
---  
  
### 表单应用

配置任务执行窗口表单页面。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/form1.png)](<form1.png>)| [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/form1.1.png)](<form1.1.png>)  
---|---  
  
  * [配置表单](<basic_info.html#config>)
  * [访问权限](<basic_info.html#ac>)
  * [操作权限](<basic_info.html#ac1>)
  * [表单复制](<basic_info.html#copy>)
  * [表单留痕](<basic_info.html#ll>)
  * [删除](<basic_info.html#del>)

**配置表单**

在表单库列表选择表单名点击可添加到表单应用列表。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/form2.gif)](<form2.gif>)

>   1. 支持绑定多个表单，拖动调整表单顺序  
> 
>   2. 当表单名称为`%分组名&_表单名`格式时,运行时自动分组 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/form1.2.png)](<form1.2.png>)
> 

**复用当前表单配置到...**

当前节点的绑定的表单复用到其他任务节点

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/5.gif)](<5.gif>)

**访问权限**

点击表单名后的编辑按钮，进入对应表单，设置该表单被允许访问的范围，若未设置，默认该任务的参与者都可以访问该表单

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/form20.png)](<form20.png>)

> 当办理人无任何表单的访问权限时，将给出当前流程处于模拟测试状态的页面。 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/form21.png)](<form21.png>)

**操作权限**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/form5.png)](<form5.png>)

项 | 说明  
---|---  
修改表单 | 控制主表、子表的编辑权限。开启时，显示`保存时校验`、`保存时不校验`选项， 不开启，不显示`保存校验数据`、`保存时不校验`选项且运行时无表单保存按钮  
保存时校验 | 点击表单保存按钮时，是否校验表单信息。选择`保存时不校验数据`，则在进行主表单保存时，不会校验主表单和表格数据，仅在办理任务前校验表单数据有效性。  
子表 > 允许新增 | 在运行时子表是否允许新增记录  
子表 > 提示保存主表 | 新建流程实例当主表数据未保存时，新增子表记录是否给出提示  
子表 >允许关联录入 | 表单可编辑时，允许关联录入开关禁用，子表表单只读时开关可操作  
子表 > 允许删除 | 在运行时子表是否允许删除记录  
子表 > 允许导入 | 在运行时子表是否允许导入数据  
子表 > 允许导出 | 在运行时子表是否允许导出数据  
隐藏 | 勾选后字段值在表单运行时作为隐藏域被隐藏  
只读 | 勾选后字段值在表单运行时只读不可修改  
留痕 | 在表单设计器中添加修改记录组件后，运行时勾选 的字段在表单上填写保存表单数据，再次修改保存才会留下痕迹  
身份权限 | 更细粒度权限，设置某用户对该字段的只读隐藏权限  
  
>   * 参见[字段权限在AWS各种策略中的优先次序](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/form_before_load.html>)
>   * 对于只读字段，导入时不会读取Excle中的值，如果该字段有默认值，会被使用
>   * 导入时不支持子表的[有效性检查](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-64ga/pc/list.html>)
> 

**表单留痕**

在表单设计器中添加[修改记录](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-64ga/pc/designer.html>)后，运行时在表单上填写保存表单数据，再次修改保存才会留下痕迹。

表单留痕提示：

  1. 不支持表单留痕的UI组件，在表单留痕配置框中禁选
  2. 字段为数值类型的，数值变大或变小，在留痕记录中有向上向下的箭头标记
  3. 附件UI组件在留痕记录中下载或在线预览查看
  4. HTML组件在留痕记录中以大文本形式显示
  5. 表单留痕，仅支持在表单执行保存动作时，数据有差异时记录留痕动作，因此如果通过API 、SQL、参考录入、Excle导入等不调用表单保存动作的场景进行数据的增删改处理，不会有留痕记录，此时需要开发者自行调用 BOAPI.createValueHistory(XXX)处理，API详情参见[这里](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/BOAPI.html#createValueHistory-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.String-int->)

人工任务基本信息字段配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/formmark.png)](<formmark.png>)  
表单设计器中配置  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/formmark1.1.png)](<formmark1.1.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/formmark1.png)](<formmark1.png>)  
  
**优先办理**

仅当该节点设置为并签且表单可编辑时有效，并行多人收到任务后，首个办理人优先办理后其他人员方可办理

**表单快照**

  * **保存表单快照**

当用户执行人工任务完毕时，在服务器端为该主表单保留一份克隆的表单文件版本（私有格式文件），该操作不会额外增加存储或性能开销，值得注意的是：AWS对附件的删除是物理删除，因此快照版本在view时，无法查看已删除的附件; 表单快照仅支持系统内部表单，不支持Ajax子表及URL表单等会有动态数据请求的表单

  * **允许显示版本列表**

该选项用于显示当前流程已存储的表单快照版本，在表单中给出一个List清单

  * **快照列表**

选择表单打印模板，使用PDF表单打印模板机制，创建需要提供快照功能的表单打印模板。[PDF表单打印](<https://awsappstore.com/apps/detail/com.actionsoft.apps.addons.formprint>)应用已安装，且绑定表单是VUE表单，快照列表必填；非VUE表单不显示该列表选择框。选择快照使用PDF机制生成快照。[PDF表单打印](<https://awsappstore.com/apps/detail/com.actionsoft.apps.addons.formprint>)应用未安装时，且绑定表单是VUE表单，表单快照功能禁用

[![配置](https://helpcdn.awspaas.com/picture/picture/202311/d4f5aa289d794ac2acc8ad7e4c71ce9d.png)](<https://helpcdn.awspaas.com/picture/picture/202311/d4f5aa289d794ac2acc8ad7e4c71ce9d.png>)

[![运行](https://helpcdn.awspaas.com/picture/picture/202311/d3150b212a2341b587b094ed970addd9.png)](<https://helpcdn.awspaas.com/picture/picture/202311/d3150b212a2341b587b094ed970addd9.png>)

**复制表单**

设定历史表单作为模板，在用户填写表单时，快速从历史表单中复制数据，提高用户填单效率。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/formcopy3.3.png)](<formcopy3.3.png>)

项 | 说明  
---|---  
复制表单 | 点编辑打开复制表单的配置框  
个人模板 | 使用个人历史任务的数据作为模板填写表单  
固定模板 | 由管理员设定历史表单作为模板  
  
>   1. 多次对同一个模板进行复制，是覆盖的机制
>   2. 字段只读隐藏状态下也可复制成功
>   3. 支持所有AWS标准UI组件的值复制
>   4. 复制数据只显示最新的20条，没有分页显示，选择其他可通过搜索查找
>   5. 固定模板可以修改标题以及删除模板
>   6. 复制表单后，数据会自动保存到数据库 7.在这配置后，还需要在按钮操作-自定义按钮中添加复制表单操作，运行时才显示复制表单按钮
> 

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/formcopy3.1.png)](<formcopy3.1.png>)  
按钮操作中自定义按钮配置  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/formcopy3.2.png)](<formcopy3.2.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/formcopy3.png)](<formcopy3.png>)  
  
**删除**

删除绑定的表单。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/form22.png)](<form22.png>)

### 任务通知

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/info-task.gif)](<info-task.gif>)

当新任务到达该节点时，为当前节点办理者自动发送邮件、短信、企业微信、钉钉、飞书等任务到达通知，若成功发送，该办理者、任务接收人均必须在个人信息中设置了外部邮件地址、手机号且在组织中需创建与企业微信、钉钉、飞书相同的账号。邮件通知策略支持：

  1. 可以在邮件中点击链接直接办理（无需登录系统）
  2. 在邮件中点击链接进行口令验证，验证成功后可直接办理
  3. 默认免登录，关闭后需口令验证

[![](https://helpcdn.awspaas.com/picture/picture/202311/9211066345cb46b188620311c55d3a53.png)](<https://helpcdn.awspaas.com/picture/picture/202311/9211066345cb46b188620311c55d3a53.png>)

邮件通知  
---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/mail1.png)](<mail1.png>)  
口令验证  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/mail2.png)](<mail2.png>)  
  
>   * 邮件正常发送必须提前配置邮件服务器，详见[邮件通知](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/index.html>)文档  
> 
> 

任务到达短信、企业微信、钉钉、飞书通知展示

短信 | 飞书  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/sms-infotask7.png)](<sms-infotask7.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/feishu-infotask4.png)](<feishu-infotask4.png>)  
企业微信 | 阿里钉钉  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/weixin-infotask5.png)](<weixin-infotask5.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/dingding-infotask6.png)](<dingding-infotask6.png>)  
  
>   * 短信、企业微信、钉钉、飞书的相关配置详见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/notice.html>
> 

#### 延伸阅读

  * [邮件通知发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/index.html>)
  * [短信通知发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.sms/index.html>)
  * [企业微信集成](<https://docs.awspaas.com/reference-guide/aws-paas-wechat-reference-guide/index.html>)
  * [钉钉集成](<https://docs.awspaas.com/apps/com.actionsoft.apps.dingding/index.html>)
  * [飞书集成](<https://docs.awspaas.com/apps/com.actionsoft.apps.feishu.open/index.html>)