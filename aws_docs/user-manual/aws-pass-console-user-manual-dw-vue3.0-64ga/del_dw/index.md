# 视图模型基本操作 · AWS PaaS文档中心

# 视图模型基本操作

**删除DW**

  1. 登录AWS PaaS控制台
  2. 点击左侧菜单“应用服务 > 业务建模 > 某应用 > 数据窗口”
  3. 右侧将显示该分类下所有DW模型
  4. 勾选相应记录，点击工具条"删除"按钮
  5. 按照提示信息，完成删除操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/del_dw/deleteDW.png)](<deleteDW.png>)

**流程/数据应用视图**

删除视图时，将删除%AWS_HOME%/apps/install/%Appid%/repository/dw/下相应配置文件，该操作不可逆，请谨慎操作。

**模型另存为**

基于选择视图模型另存为一个新的视图模型。步骤：

1.在视图模型列表中选中某一个视图模型，下方工具条将显示另存为...按钮  
2.点击另存为...按钮，弹出对话框中设置相关属性，点击确定按钮，完成

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/del_dw/save.png)](<save.png>)

> 流程视图不支持另存为操作

**修改模型名称**

在列表中选个视图，右侧显示相关的信息，上面显示的名称可进行修改，其他信息只读

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/del_dw/modify.png)](<modify.png>)

**设置增删权限**

只有数据视图、sql数据源视图提供设置增删权限，流程视图不支持

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/del_dw/ac.png)](<ac.png>)

> 设置的增删权限，与[配置按钮-新建/删除权限一致](<new_dw/group.html>)