# 程序开发多语言 | AWS PaaS多语言开发参考指南

# 程序开发多语言

程序开发国际化的标签格式为`<I18N#XXX>`。 所有I18N资源请存放在所属应用`%AWS_HOME%/apps/install/%APPID%/i18n`目录下。

### 常规代码开发示例

常规的代码开发中如果需要使用国际化，请使用：
    
    
    I18nRes.findValue(String appId, String key);//系统会根据用户上下文对象获取语言
    I18nRes.findValue(String appId, String lang, String key);//指定语言的情况
    
    //其中appId为当前AWS应用的唯一标识，lang是语言代码，可使用UserContext的对象调用getLanguage()方法获取，使用的时候请注意UserContext对象进行非空校验，需将lang设置一个默认值"cn"。
    

### 带变量场景开发示例
    
    
        <item key="displayMsg">
            <cn><![CDATA[显示第 {0} 条到第 {1} 条，一共 {2} 条]]></cn>
            <en><![CDATA[Showing {0} to {1}, a total of {2}]]></en>
            <big5><![CDATA[顯示第 {0} 條到第 {1} 條，一共{2} 條]]></big5>
        </item>
    

可使用下面的方法实现：
    
    
    I18nRes.findValue(String appId, String lang, String key, Object... repleaseValue)
    
    //1.appId：指定使用的应用资源文件
    //2.lang：语言代码，可使用UserContext的对象调用getLanguage()方法获取，使用的时候请注意UserContext对象进行非空校验，需将lang设置一个默认值”cn”。
    //3.key：关键字，即国际化资源中的displayMsg
    //4.repleaseValue：要替换的内容。如果国际化资源中有变量值，需要替换的变量的具体的值，可使用new Object[]{...}直接构建，如 new Object[]{"用户名","密码"}，会按照国际化内容中的{0}{1}…顺序替换
    

### 构造平台标准`警告、错误`提示信息界面开发示例

AWS PaaS平台底层对`AlertWindow`类中一系列方法和`ResponseObject`类中`msg(String)，err(String)，warn(String)`三个方法处理了国际化内容，不需要使用者处理。即使用者在调用时直接传中文参数即可。例如：
    
    
    return AlertWindow.getWarningWindow("指定的栏目已不存在");
    <!--只需要将【指定的栏目已不存在】作为key放到国际化资源文件中即可。-->
    
    <!-- 以下为I18n资源-->
    <item key="指定的栏目已不存在">
        <cn><![CDATA[指定的栏目已不存在]]></cn>
        <en><![CDATA[The specified column no longer exists]]></en>
        <big5><![CDATA[指定的欄目已不存在 ]]></big5>
    </item>
    

### JavaScript开发示例

当某些字符串信息被静态存储在.js文件时，请遵循如下规范

  1. 将JS内引用到的常量抽取成变量，并定义在JS引用的html模板区域内，保证在页面body加载前加载完成
  2. 定义的var变量名请使用全部英文或全部中文，且除下划线外，不能出现任何形式的标点符号
  3. 在`%AWS_HOME%/apps/install/%APPID%/template/form/`目录下配置多语言资源

示例：
    
    
    <!--HTML代码-->
    <head>
        <script type="text/javascript">
         var 确定删除这个文件夹吗="<I18N#确定删除这个文件夹吗>";
        </script>
    </head>
    
    <!--js代码-->
    alert(确定删除这个文件夹吗);
    
    <!-- I18n资源-->
    <item key="确定删除这个文件夹吗">
        <cn><![CDATA[确定删除这个文件夹吗?]]></cn>
        <en><![CDATA[Are you sure to delete this folder?]]></en>
        <big5><![CDATA[確定删除這個資料夾嗎? ]]></big5>
    </item>
    

### AWS MVC框架多语言开发示例

AWS MVC框架开发多语言配置可分为Java程序、系统HTML模板、I18N资源

#### Java程序
    
    
    listHtml.append("<tr><td><br>&nbsp;</td><td align=center><br><br><br><div align=center><I18N#您输入的条件格式不正确_请重新输入></div></td></tr>");
    
    SDK.getAppAPI().i18NValue("com.actionsoft.apps.poc.api", me, "info1");
    

#### 系统HTML模板

系统HTML模板存放在`%AWS_HOME%/apps/install/%APPID%/template/page`目录下。
    
    
    <!doctype html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title><I18n#PageTitle></title>
    
        <script>
        var var1 = "<I18n#Var1>";
        var var2 = "<I18N#Var2>";
        alert(var1);
        alert(var2);
        </script>
    </head>
    <body>
    Hi,<I18n#PageTitle>
    </body>
    </html>
    

#### I18N资源
    
    
        <item key="您输入的条件格式不正确_请重新输入">
            <cn><![CDATA[您输入的条件格式不正确,请重新输入]]></cn>
            <en><![CDATA[Conditional formatting you entered is incorrect, please try again]]></en>
            <big5><![CDATA[您輸入的條件格式不正確,請重新輸入]]></big5>
        </item>
         <item key="info1">
                <cn><![CDATA[这是中文简体语言]]></cn>
                <en><![CDATA[This is the English language]]></en>
                <big5><![CDATA[這是中文繁體語言]]></big5>
            </item>
            <item key="PageTitle">
                <cn><![CDATA[这是标题]]></cn>
                <en><![CDATA[This is Title]]></en>
                <big5><![CDATA[這是標題]]></big5>
            </item>
            <item key="Var1">
                <cn><![CDATA[这是变量1]]></cn>
                <en><![CDATA[This is Var1]]></en>
                <big5><![CDATA[這是變量1]]></big5>
            </item>
            <item key="Var2">
                <cn><![CDATA[这是变量2]]></cn>
                <en><![CDATA[This is Var2]]></en>
                <big5><![CDATA[這是變量2]]></big5>
            </item>
    

> AWS MVC框架开发国际化更多信息参见<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/localization/locale.html>