# 卸载 | AWS PaaS应用容器与资源控制参考指南

# 卸载

卸载操作将停止该应用的服务，并将该应用的资源从安装仓库转移到卸载仓库。

> 如果该应用存在子应用，应首先卸载子应用

在`AWS控制台》应用管理》应用管理`列表，点击`卸载`按钮

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/uninstall-1.png)

也可在AWS命令行控制台中执行如下命令：
    
    
    in aws //进入shell环境
    uninstall app %AppId% //卸载应用
    

### 卸载移动应用

如果卸载的应用属于安卓或iOS应用，AWS BYOD会监控到这一动作，同时向所有已安装该应用的手机设备发出卸载指令，从手机中删除该应用。