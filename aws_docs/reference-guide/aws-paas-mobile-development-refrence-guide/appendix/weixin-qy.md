# 接入微信企业号 | AWS 移动开发参考指南

# 接入微信企业号

AWS PaaS开发的H5页面可以被直接配置到微信企业号之中，下面是配置微信企业号应用的简要过程。

> 前提条件： AWS PaaS服务具有公网访问地址。

  1. 新建企业号
  2. 从微信同步应用
  3. 设置企业号应用可信域名
  4. 设置企业号应用回调地址
  5. 配置菜单
  6. 发布本地修改

#### 1.新建企业号

_步骤_

1.在AWS PaaS控制台`工具附加`中找到 `微信企业号管理开发平台`。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/addon.png)

2.点击`新建企业号`, 输入企业号信息后保存。如何获取CorpID和Secret，见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-wechat-reference-guide/register_wechat/README.html>)

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/qy_add.png)

#### 2.从微信同步应用

进入企业号后， 点击`从微信同步应用`，可将微信企业号的应用同步过来。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/qy_sync.png)

#### 3.设置企业号应用可信域名

在微信企业号后台设置企业号应用可信域名。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/trust_domain.png)

如果AWS PaaS的Web URL服务有端口号，那可信域名也必须加上端口号。如果为正式环境，可信域名必须是一个通过ICP备案验证的互联网域名，如果为临时开发环境，可信域名可以是一个公网IP地址，访问时可能会出现风险安全提示框。 

#### 4.设置企业号应用回调地址。

_步骤_

  1. 进入微信企业号后台开启回调模式， 随机获取Token和EncodingAESkey。 ![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/qy_callback2.png)

  2. 在微信企业号管理开发平台中编辑该应用，将在上面生成的Token和EncodingAESkey粘贴到对应的输入框，点击`确定`。 ![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/qy_edit.png)

  3. 复制回调地址。 ![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/qy_callback_url.png)

  4. 将复制的回调地址粘贴到微信企业号应用中，点击`保存`，会提示成功配置企业服务器。 ![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/qy_callback.png)

#### 5.配置菜单

可添加、编辑、删除菜单。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/qy_menu_edit.png) ![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/qy_menu_edit2.png)

#### 6.发布本地修改。

发布本地修改后，需要最多**24小时** 在微信客户端生效。测试时先取消关注企业号再重新关注，可以达到微信客户端快速生效的效果。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/qy_publish.png)