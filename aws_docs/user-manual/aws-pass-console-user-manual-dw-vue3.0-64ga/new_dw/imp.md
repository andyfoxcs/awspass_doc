# 数据导入 · AWS PaaS文档中心

# 数据导入

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/24-3.png)](<24-3.png>)

属性项 | 说明  
---|---  
表单名称 | 列出当前视图绑定的表单  
  
## 数据导入配置说明

添加表单名称后，显示数据导入的配置项

属性项 | 说明  
---|---  
模板配置 | 运行时,显示的名称及下载的模板文件名称，必填  
最大行数 | 运行时，一次导入最大的数据量，默认最大行数20000  
新增导入 | 默认显示`无`，显示新增导入的配置项，是增加导入的数据，始终显示  
更新导入 | 勾选`显示更新`，显示更新导入的配置项，导入更新的字段，不是所有的数据都进行导入更新，而是被设置关键字段的才进行导入更新操作  
多表单同步上传 | 当配置多个表单，选择不控制：表示可以上传也可以上传；选择多表单同时上传，当前表单模板必须上传  
仅导入数据 | 运行时，导入数据只往BO表中存数据，不会产生流程实例的数据，该属性在数据应用视图中显示  
可维护管理 | 运行时，导入数据除了往对应BO表中存数据，还会产生流程实例的数据，该属性在数据应用视图中显示  
初始流程状态 | 选首结点待办，运行时，导入的是待办视图数据；选归档结束，运行时，导入的是已办视图数据。该属性在流程应用视图中显示  
导入选项 | 更新导入时，更新的是结束流程数据还是不更新结束流程数据，该属性在流程应用视图中显示  
新增 | 添加运行时DW列表允许导入的字段  
删除 | 删除运行时DW列表允许导入的字段  
增加BO表 | 增加表单数据源中的BO表，运行时，可同时导入主子表及字段子表的数据  
关键字段 | 多选，运行时，被设置为关键字段的值在上传的Excel中不能重复且值要与列表中的一致，根据这个对应关系去更新列表中一致的其他字段值，必填  
列名 | 默认显示数据源BO存储的列名  
列名称 | 可修改，运行时，Excel模板列名称  
  
**多表单同步上传**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/24-3.1.png)](<24-3.1.png>)

主子表及字段子表在excel模板中维护示例：

主表  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/zhu.png)](<zhu.png>)  
子表  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/zi.png)](<zi.png>)  
字段子表  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/zizi.png)](<zizi.png>)  
  
1.在excel模板中子表及字段子表模板中有个主序列字段且是必填的  
2.子表中主序列填写的是在excel中维护主表数据对应的excel的序列号  
3.同理，字段子表中主序列填写的是子表数据对应的excel的序列号  
4.主子表是一对多的关系，所以主表数据对应的excel的序列号可以对应多条在excel中维护子表的数据

## Java事件

Java事件是执行后端Java代码逻辑的容器，在客户端页面加载时被触发，由开发者通过Java程序影响视图页面显示内容。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/24-5.png)](<24-5.png>)

项 | 说明  
---|---  
Java类名 | 一个遵循AWS事件接口实现的Java程序，格式：类路径+类名  
事件类型 | 各种事件名称，不同的事件要求开发人员实现的接口不同，每个事件只允许注册一个类  
注册 | 将指定的Java类注册到事件  
说明示例 | 选事件类型后，在注册后面会显示一个可点击的问号图标，可查看所选事件的示例  
删除 | 将Java类从一个事件中移走  
  
### 导入前事件

  * **接口** com.actionsoft.bpms.dw.exec.event.ideimport.DataWindowValidateImportInterface
  * **示例说明见下图**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/24-6.png)](<24-6.png>)

**_运行效果_** [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/24-7.gif)](<24-7.gif>)