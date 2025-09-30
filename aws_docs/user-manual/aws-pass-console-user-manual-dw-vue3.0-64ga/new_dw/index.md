# 创建视图 · AWS PaaS文档中心

# 创建视图

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/operation/createDW.gif)](<../operation/createDW.gif>)

在创建视图前，要求当前应用下已完成BO存储、表单、流程的创建，步骤：

  1. 登录AWS PaaS控制台
  2. 点击左侧菜单“应用服务 > 业务建模”，点击左上角的新建图标
  3. 设置应用名称和业务模型分类，选择统计分析`DW 视图模型`  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/8.png)](<8.png>)
  4. 点击"确定"按钮，弹出"新建视图模型"窗口
  5. 设置相关信息，点击"确定"按钮完成 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/9.png)](<9.png>)

属性项 | 说明  
---|---  
视图类型 | `流程应用视图` 针对工作流引擎流程  
`数据应用视图` 没有流程控制，仅用于数据维护  
  
绑定流程组 | 仅在`流程应用视图`时可见，一个流程组只允许创建一个DW模型  
应用主标题 | 标题名称，在设计时可修改，`数据应用视图`时，该值不允许重复  
模型分类 | 仅在`数据应用视图`时可见，用于标识该模型属于哪类业务区域  
数据方案 | 仅在`数据应用视图`时可见，快速初始化数据方案，多个使用英文逗号隔开  
也可在[数据方案管理器](<../manager_data>)维护  
表单应用 | 仅在`数据应用视图`时可见，实施人员给定一默认表单。  
如果是外部系统的URL，此处可暂时留空，在设计时给定  
  
> 自动生成的配置文件存放在%AWS_HOME%/apps/install/%appid%/repository/dw目录下， 通常该文件由平台自动维护

## 发布

点击左上角的`发布`按钮，将视图发布到AWS PaaS客户端，供用户访问。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/9-2.png)](<9-2.png>)

该视图及视图所在的子系统从没有发布到导航菜单时，出现选择部署方式的选项

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/9-3.png)](<9-3.png>)

**一键完成**

子系统、目录、菜单名称全是默认的方便、简单一键完成部署操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/9-4.png)](<9-4.png>)

> 数据视图中点一键完成时会把工具条上的新建按钮的增删权限同步过来

**自定义**

  1. 点击“发布”按钮（右上角按钮），出现选择部署方式的选项
  2. 选择“自定义”，弹出快速部署框，设置子系统和目录，添加访问者权限组
  3. 点击“部署”按钮，完成操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/9-5.png)](<9-5.png>)

项 | 说明  
---|---  
子系统 | 1\. 如果该应用已在导航菜单绑定了一个子系统，默认是该子系统  
2\. 如果没有，默认以该模型所在应用名为子系统  
3.自定义部署时还可以新建子系统，不默认创建目录   
  
目录 | 1\. 如果该子系统下已存在目录名为该模型“分类”名，默认是该目录  
2.如果没有，且该模型分类下其他模型已部署过菜单，默认该目录  
3.如果都没有，默认为该模型分类创建目录  
4.自定义部署时还可以新建目录,不默认创建目录   
  
菜单名称 | 默认以当前模型名称为名，可修改  
  
> 有关DW的创建与部署更多详细信息请参见：<https://docs.awspaas.com/getting-started-guide/aws-dw-app-quick-start-guide/create-dw/deploy-dw.html>