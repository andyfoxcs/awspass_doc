# 权限 · AWS PaaS文档中心

# 权限

在数据窗口中可以灵活的配置单个视图、数据列表字段、按钮、查询条 件等用户的访问范围。但不同视图，新建、删除按钮对应的授权方式不同， 可分为如下两种授权方式：

  * **AC授权** AWS PaaS平台一种细粒度授权机制，如果未授权则所有AWS用户均可访问，如已授权，则仅在权限范围内的用户可访问。

  * **增、删权限** 新建、删除数据列表权限

功能 | AC授权 | 增、删权限  
---|---|---  
视图授权 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<no.png>)  
列表字段授权 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<no.png>)  
新建、删除按钮 | 流程应用视图 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<no.png>)  
数据应用视图 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<yes.png>)  
其它按钮 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<no.png>)  
范围查询策略 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<no.png>)  
条件查询策略 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<no.png>)  
  
  * [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<yes.png>) 表示支持
  * [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<no.png>) 表示不支持

> 上方工具条上的按钮授权会在应用户所拥有的访问权限中显示，也可以在[权限服务-访问权限](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-security-vue/authority/menu_power.html>)`中对按钮授权 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/ac.png)](<ac.png>)