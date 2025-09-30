# 分发 | AWS PaaS应用容器与资源控制参考指南

# 分发

所有处于安装状态的应用，都可以一键制作成.app安装包，分发到其他PaaS实例进行安装或升级。

> 每执行一次分发操作，该应用的build号自动加1

在`AWS控制台》应用管理》应用开发`页面，点击`分发应用`按钮

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/dist-1.png)

也可在AWS命令行控制台中执行如下命令：
    
    
    in aws //进入shell环境
    dist app %AppId% //打包成分发的介质文件
    

### 将应用发布到AWS企业应用商店

<https://www.awsappstore.com/>

如果开发者对该应用拥有版权，是应用的法定收益方，可以通过发布到AWS企业应用商店，让更多企业用户受益。了解如何成为AWS企业应用商店的认证开发者和应用上架审核规范，请与炎黄盈动客户经理联系。