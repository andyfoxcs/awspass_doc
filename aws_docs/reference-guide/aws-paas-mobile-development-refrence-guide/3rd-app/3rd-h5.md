# 集成H5应用 | AWS 移动开发参考指南

# 集成第三方H5应用

  1. 在AWS平台为第三方应用注册SSO服务
  2. 第三方系统进行SSO集成开发
  3. 将第三方系统H5应用添加到AWS平台

## 1\. 在AWS平台为第三方应用注册SSO服务

> 进行此步骤前需先安装AWS应用`SSO单点登录管理`， 如不需要与第三方应用进行SSO集成， 可跳过此步骤

1.登录AWS实例控制台， 找到并打开「工具附加>SSO单点登录管理」。

![addons](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/addons.png)

2.点击「新建」按钮进行SSO服务注册。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/register.png)

主要项 | 说明  
---|---  
可用状态 | 当处于`暂停`时，SSO API对该系统的服务暂不可用  
限定人群 | 如果设置了用户范围，那么只允许范围内用户可访问，其他用户的令牌校验返回权限被拒绝  
SSO URL | 对方系统用于接收AWS门户发出的免登录请求地址，接收令牌并完成验证，返回登录后页面  
参数列表 | 附加该系统需要的额外参数，非必须  
  
3.点击「保存」按钮后，可获得访问该SSO服务的AWS URL入口及调用该SSO验证的access_key。 ![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/accesskey.png)

  * AWS平台单点登录访问第三方系统时需使用其注册SSO服务时生成的AWS URL
  * access_key会在第三方系统进行SSO集成开发时用到
  * 如需跳转到不同的页面,可利用单点登录服务的扩展参数，根据扩展参数的不同跳转到不同页面。
        
        ./w?sid=@sid&cmd=com.actionsoft.apps.addons.sso_access&ssoId=xxx-xxx&ext=xxx
        

有关扩展参数和参数列表的详细说明，参加[这里](<https://docs.awspaas.com/reference-guide/aws-paas-sso-reference-guide/manage/register.html>)

## 2\. 第三方系统进行SSO集成开发

> 如不需要与第三方应用进行SSO集成， 可跳过此步骤

AWS平台单点登录到第三方系统时，会向第三方系统提供的用于SSO验证的URL中传递tokenId参数, 假设第三方系统用于SSO验证的URL是：<https://www.abc.com/sso，> 那么AWS平台会产生类似下面的请求：
    
    
    https://www.abc.com/sso?tokenId=xxx&ext=xxx&xxx=xxx
    

  * 请求中一定会包含tokenId参数，第三方系统需要向AWS平台验证该tokenId是否合法。
  * 使用SSO服务的AWS URL时如果增加了扩展参数ext， 则向三方系统请求时会包含ext参数。
  * 如果注册SSO服务时定义了参数列表， 请求中会包含相应参数。

#### 验证Token

**服务请求地址**

向AWS发送请求的URL地址，该服务在安装本应用后自动提供。

_假设AWS服务的访问地址是：<https://abc.awspaas.com> ，地址示例如下_
    
    
    https://abc.awspaas.com/r/jd?cmd=com.actionsoft.apps.addons.sso_validate&tokenId=xxxx&access_key=xxxx
    

_如果是开发者自己的本地开发环境，地址可能如下_
    
    
    http://localhost:8088/portal/r/jd?cmd=com.actionsoft.apps.addons.sso_validate&tokenId=xxxx&access_key=xxxx
    

**服务请求参数**

参数名 | 说明  
---|---  
cmd | 此处为固定值com.actionsoft.apps.addons.sso_validate  
tokenId | 来自AWS提供给该URL的`tokenId`参数值  
access_key | [注册该SSO服务](<../manage/register.html>)时提供的`access_key`值  
  
**请求处理结果**

_结果以json数据结构返回。假设要验证的`tokenId`为`AAA`，`access_key`为`xxx-xxx`，返回的数据结构如下_
    
    
    {
    "data":{
    "uid":"对应的AWS登录账户名",
    "tokenId":"AAA",
    "access_key":"xxx-xxx",
    "validate":true
    },
    "msg":"",
    "result":"ok"
    }
    

  * 当`data/validate`值为true时，表示该令牌有效
  * 当`result`不为`ok`时，说明发生系统级错误，相关错误码请[参考这里](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/error-code.html>)

>   * 当令牌验证通过后，会在json结果中提供`uid`，即该令牌对应的AWS登录账户，开发者可根据该账户在该系统的权限，返回对应在该系统的页面内容
>   * 如果Token提供的账户与第三方系统账户不一致，需要额外的实施和维护账户匹配规则（不在本应用标准功能之内）
> 

> 
> 更多SSO API规范请参考[这里](<https://docs.awspaas.com/reference-guide/aws-paas-sso-reference-guide/dev/sso_api.html>)

## 3\. 将第三方系统H5应用添加到AWS平台

在AWS控制台「移动应用管理>移动应用列表」 页面，添加H5应用。

_此处H5应用URL的值应为该SSO服务的AWS URL入口，比如`./w?sid=@sid&cmd=com.actionsoft.apps.addons.sso_access&ssoId=abec3453-0b1d-4052-932b-f55886e6c412&ext=%7B%22dtype%22%3A1%7D`_

添加H5应用的详细步骤可参考[这里](<../appendix/add-h5.html>)。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/basic.png)