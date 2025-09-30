# 添加H5应用 | AWS 移动开发参考指南

## 添加H5应用

1.登录AWS控制台， 在`移动应用管理` -> `移动应用列表` 页面中，点击左上角 `添加` 按钮， 选择 `H5应用`。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/addh5.png)

2.填写应用基本信息。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/basic.png)

项 | 说明  
---|---  
应用图标 | 需要3张png图标， 大小分别为16x16, 64x64, 96x96  
URL | H5应用的入口页面地址，既可以是属于该H5应用内部的页面地址， 页可以是其它AWS web 应用的页面地址， 还可以是三方系统的页面地址。AWS平台内部的地址支持简写， 如 `cmd=com.actionsoft.apps.helloh5_test_home`， `/apps/com.actionsoft.apps.poc.h5/index.html` 如无需进行SSO集成， 可直接写三方页面地址， 如 `https://www.abc.com`  
应用名称 | 该应用显示给用户的名称  
PaaS应用ID | AWS平台内部唯一的应用标识  
版本号 | 应用版本号，目前由平台自动生成  
支持的设备类型 | 应用支持的设备类型，包含手机，平板和通用（手机、平板都支持）  
支持SSO | 是否支持移动门户单点登录。需要通过AWS用户认证才能访问的页面需勾选此项，勾选后从移动门户打开该应用时，会自动向页面地址传入sid参数  
  
3.填写应用扩展信息。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/ext.png)

4.对应用进行授权。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/auth.png)

添加完成后，在移动应用列表中会出现该应用，被授权用户从移动门户中也可查看到该应用。