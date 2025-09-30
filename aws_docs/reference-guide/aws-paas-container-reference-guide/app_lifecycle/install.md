# 安装 | AWS PaaS应用容器与资源控制参考指南

# 安装

符合[应用资源结构](<../app_resource/README.html>)的.app文件（一个zip压缩格式），都可以安装到AWS PaaS中。

### 安装一个.app介质文件

.app文件是由[分发](<dist.html>)生成的安装包。

**步骤一：**

可以手工将文件拷贝至apps/upload文件夹，也可以在`AWS控制台》应用管理》应用安装`点击`本地上传App文件`，完成上传

**步骤二：**

在`AWS控制台》应用管理》应用安装`列表会出现全部待安装的应用，点击`安装`按钮

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/install-1.png)

也可在AWS命令行控制台中执行如下命令：
    
    
    in aws //进入shell环境
    install app %AppId%,%AppId%.. //安装应用，多个用半角逗号隔开
    

### 从AWS企业应用商店安装

在`AWS控制台`右上角点击`访问AWS企业应用商店`，打开向导窗口，从列表中选择待安装的应用，一键完成安装。

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/install-2.png)

> 如果安装失败，可将鼠标移动到`重试`按钮，查看原因。如下图： ![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/install-3.png)

### 授权访问

这是一个容易被PaaS初级用户忽略的操作。如果安装的应用提供了客户端访问入口，需要授权才可以正常访问。建议在安装新应用后，按此步骤完成授权：

**步骤一：**

在`AWS控制台》应用管理》应用管理`列表，打开刚刚安装的应用，检查`部署`页

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/install-4.png)

  * 如果此处无记录，表示该App无需授权，后继步骤可忽略
  * 如果有菜单定义并显示`已部署`，表示该App的导航菜单已自动创建，待授权
  * 如果有菜单定义并显示`未部署`，点击可为该App创建导航菜单

**步骤二：**

完成授权，让相关用户可以访问。此处与日常运维习惯有关，不再细节描述。

  * 直接在该应用的`部署`页完成
  * 在`AWS控制台》公共设施》权限服务`列表，为特定权限组授权
  * 在`AWS控制台》公共设施》导航菜单`列表，为特定菜单授权

### 安装移动应用

如果安装的应用属于安卓或iOS应用，会自动出现在`AWS控制台》移动应用管理》移动应用列表`中。首次安装，应点击`安装授权`，授权哪些用户可以安装到个人移动设备上。

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/install-5.png)