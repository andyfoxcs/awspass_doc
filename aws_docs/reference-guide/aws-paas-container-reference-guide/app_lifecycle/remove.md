# 彻底卸载 | AWS PaaS应用容器与资源控制参考指南

# 彻底卸载

如果执行彻底卸载操作，与之相关的业务数据和物理表结构也将被删除。

> 警告：这是不可反悔的物理操作

在`AWS控制台》应用管理》应用卸载`列表，点击`彻底删除`按钮

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/uninstall-2.png)

也可在AWS命令行控制台中执行如下命令：
    
    
    in aws //进入shell环境
    remove app %AppId% //还原卸载的应用
    

### 相关数据将全部删除

这是一种不留痕迹的清除操作，且不可逆。与该应用相关的业务数据至少包括：

  * 该应用BO模型对应的物理表及数据
  * 该应用扩展的表结构及数据
  * 该应用上传到DC的文件
  * 该应用Process模型创建的实例化数据和控制数据（活动的、历史的）
  * 该应用Job调度实例控制数据