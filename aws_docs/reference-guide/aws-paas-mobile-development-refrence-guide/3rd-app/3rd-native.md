# 集成原生应用 | AWS 移动开发参考指南

# 集成第三方原生应用

  1. 在AWS平台为第三方应用注册SSO服务
  2. 第三方原生应用进行SSO集成开发
  3. 将第三方原生应用添加到AWS平台

## 1\. 在AWS平台为第三方应用注册SSO服务

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/nativesso.png)

> 进行此步骤前需先安装AWS应用`SSO单点登录管理`， 如不需要与第三方应用进行SSO集成， 可跳过此步骤

1.登录AWS控制台， 找到并打开「工具附加>SSO单点登录管理」。

![addons](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/addons.png)

2.点击「新建」按钮进行SSO服务注册。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/register.png)

主要项 | 说明  
---|---  
可用状态 | 当处于`暂停`时，SSO API对该系统的服务暂不可用  
限定人群 | 如果设置了用户范围，那么只允许范围内用户可访问，其他用户的令牌校验返回权限被拒绝  
SSO URL | 对于原生应用而言，此处可为任意值， 因这里注册SSO服务的**主要目的在于获取access_key**  
  
3.点击「保存」按钮后，可获得调用该SSO验证的access_key。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/accesskey.png)

#### Android集成开发

第三方应用在manifest.xml中注册隐式Intent，该Intent的action name需要与第三方应用的package name保持一致。 假设package name是`com.actionsoft.entaddress`, 则Intent应为：
    
    
        <activity
            android:name="com.actionsoft.entaddress.MainActivity"
            android:configChanges="orientation|keyboard|keyboardHidden|screenSize">
            <intent-filter>
                <action android:name="com.actionsoft.entaddress" />
                <category android:name="android.intent.category.DEFAULT" />
            </intent-filter>
        </activity>
    

AWS移动门户调用该Intent打开三方应用， 并传递tokenId参数。
    
    
        Intent intent = new Intent("[三方应用 package name]");
        intent.putExtra("tokenId", "xxxxx");
        startActivity(intent);
    

第三方应用需要在Activity中获取tokenId， 并上传到服务器做验证。
    
    
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            String tokenId = getIntent().getStringExtra("tokenId");
            //TODO 将tokenId传递给第三方服务器进行验证
        }
    

#### iOS集成开发

在App中注册URL Schemes， 值与Bundle ID保持一致，假设Bundle ID是`com.actionsoft.entaddress`

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/urlschema.jpg)

AWS移动门户通过以下代码打开第三方应用， 并传递tokenId参数。
    
    
        NSString *url=[NSString stringWithFormat:@"[三方App Bundle ID]://sso?tokenId=%@", xxxx];
      [[UIApplication sharedApplication] openURL:[NSURL URLWithString:url]]
    

第三方应用可通过下面的代理方法获取tokenId， 并上传到服务器做验证。
    
    
    - (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
      sourceApplication:(NSString *)sourceApplication
             annotation:(id)annotation
    {
        NSLog(@"URL scheme:%@", [url scheme]);
        NSLog(@"URL query: %@", [url query]);
        //TODO  获取tokenId并上传到三方服务器做验证
    
    }
    

## 2\. 第三方原生应用进行SSO集成开发

第三方服务器获取到第三方应用传递来的tokenId后，需向AWS服务器发送请求进行验证。

**服务请求地址**

向AWS发送请求的URL地址，该服务在安装本应用后自动提供。

_假设AWS服务的访问地址是：<https://abc.awspaas.com> ，地址示例如下_
    
    
    https://abc.awspaas.com/r/jd?cmd=com.actionsoft.apps.addons.sso_validate&tokenId=xxxx&access_key=xxxx
    

_如果是开发者自己的本地开发环境，地址可能如下_
    
    
    http://localhost:8088/portal/r/jd?cmd=com.actionsoft.apps.addons.sso_validate&tokenId=xxxx&access_key=xxxx
    

**服务请求参数**

参数名 | 说明  
---|---  
cmd | 此处为固定值`com.actionsoft.apps.addons.sso_validate`  
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

>   * 当令牌验证通过后，会在json结果中提供`uid`，即该令牌对应的AWS登录账户，开发者可根据该账户在该系统的权限，返回对应在该系统的业务数据
>   * 如果Token提供的账户与第三方系统账户不一致，需要额外的实施和维护账户匹配规则（不在本应用标准功能之内）
> 

> 
> 更多SSO API规范请参考[这里](<https://docs.awspaas.com/reference-guide/aws-paas-sso-reference-guide/dev/sso_api.html>)

## 3\. 将第三方原生应用添加到AWS平台

1.登录AWS实例控制台， 在「移动应用管理>移动应用列表」 页面中，点击左上角 「添加」 按钮， 选择 `iOS应用程序文件`或者`Android应用程序文件`。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/addnative.png)

2.上传apk或者ipa文件

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/upload.png)

3.填写应用基本信息

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/native_basic.png)

项 | 说明  
---|---  
应用图标 | 3张png图标， 大小分别为16x16, 64x64, 96x96, 此时应已从应用程序文件中自动提取出图片  
应用生成文件 | 上传的原生应用程序文件的名称， 此处为只读，不可修改。  
应用名称 | 该应用显示给用户的名称，默认显示从应用中提取的应用名称，可修改。  
PaaS应用ID | AWS平台内部唯一的应用标识，默认随机生成，可修改。  
实际应用ID | 原生应用本身的标识，从应用程序中提取，不可修改。  
版本号 | 应用版本号，从应用程序中提取，不可修改。  
支持的设备类型 | 应用支持的设备类型，包含手机，平板和通用（手机、平板都支持）。iOS应用不可修改， Android可修改。  
支持SSO | 是否支持移动门户单点登录。如果进行了SSO集成， 则勾选此项。  
  
4.填写应用扩展信息

![基本信息](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/ext.jpg)

5.对应用进行授权

![基本信息](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/3rd-app/auth.jpg)

至此，在移动应用列表中会出现该应用，被授权用户从移动门户中也可查看到该应用。