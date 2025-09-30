# 升级 | AWS PaaS应用容器与资源控制参考指南

# 升级

待升级的.app文件也是标准的应用安装文件。当要安装的应用已在当前PaaS中安装，且其版本号高于正在运行的应用版本号（或版本号相同，编译号高于正在运行的应用）时，可执行升级操作。

### 从一个.app介质文件升级

.app文件是由[分发](<dist.html>)生成的安装包。

**步骤一：**

可以手工将文件拷贝至apps/upload文件夹，也可以在`AWS控制台》应用管理》应用升级`点击`本地上传App文件`，完成上传

**步骤二：**

在`AWS控制台》应用管理》应用升级`列表会出现全部待安装/升级的应用，点击`升级`按钮

也可在AWS命令行控制台中执行如下命令：
    
    
    in aws //进入shell环境
    upgrade app %AppId%,%AppId%.. //升级应用，多个用半角逗号隔开
    

### 从AWS企业应用商店升级

在`AWS控制台`右上角点击`访问AWS企业应用商店`，打开向导窗口，从列表中选择待升级的应用，一键完成升级。

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/upgrade-1.png)

### 升级注意事项

  * 应用升级时不一定是全资源覆盖，请阅读[受管应用](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>)说明