# 数据源 · AWS PaaS文档中心

# 数据源

数据源是表单绑定的数据结构，表单引擎在执行时会根据数据结构动态与表单模板、UI组件、权限等进行关联，生成用户访问页面，并自动完成数据库持久化操作。支持单表、主子关系、一主多子关系、主子子关系, 实现主子子关系，需要借助字段子表组件，实施人员可以随时调整BO表间关系，对各层模型进行优化和调整。

数据源的元数据载体必须是AWS建模的[BO存储模型>BO表或BO视图。](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo/index.html>)

**展示数据源**

  * 新建打开表单模型，默认在组件页签，从左侧组件页签中拖动组件到设计区，会创建新的数据源BO存储，在数据源页签中展示

  * 如果不拖动组件创建数据源，也可以在数据源页签中点击`绑定已有数据源`

  * 弹出选择数据源框，选择存储
  * 配置每行列数，点确定，绑定好数据源，字段在表单设计区中显示

**切换数据源**

  * 在数据源页签主表名后点击箭头图标，打开选择数据源窗口，可快速更改当前表单模型BO数据源

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/sjy/sjy1.png)](<sjy1.png>)  
---  
>`选择数据源-存储`下拉选项列出的是与当前应用相关联的应用 **打开数据源链接**  [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/sjy/sjy2.png)](<sjy2.png>)  
---  
  
  * 点击主表或主表字段标题前的图标，链接打开对应的主表存储
  * 点击子表标题名称前的图标，链接打开对应的子表存储

**隐藏字段**

  * 主表字段隐藏，点击主表字段后面的小眼睛，隐藏字段在表单上不显示，取消隐藏再次点击小眼睛。默认是显示的
  * 子表字段隐藏，详见`表格-普通表格`[隐藏字段](<../zj/pt.html#yczd>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/sjy/sjy3.png)](<sjy3.png>)  
---