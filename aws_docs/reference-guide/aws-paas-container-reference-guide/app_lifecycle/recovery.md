# 还原 | AWS PaaS应用容器与资源控制参考指南

# 还原

AWS PaaS为卸载应用提供反悔操作。

> 被还原的应用默认处于`暂停`状态，可以手工启动

在`AWS控制台》应用管理》应用卸载`列表，点击`还原`按钮

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/uninstall-2.png)

也可在AWS命令行控制台中执行如下命令：
    
    
    in aws //进入shell环境
    recovery app %AppId% //还原卸载的应用