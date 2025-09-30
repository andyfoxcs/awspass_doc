# 多语言 · AWS PaaS文档中心

## 多语言

AWS MVC框架对HTML/JavaScript多语言和Java程序多语言提供了一整套完善的开发方案，以下为AWS MVC的多语言处理架构。

[![多语言框架](https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/localization/i18n.png)](<i18n.png>)

AWS MVC每次接收到用户请求时，在会话对象（`UserContext.getLanguage()`）提供了该用户的界面语言信息，AWS MVC为应用提供了两种常见解决方案：

### Java程序

通过`SDK.getAppAPI().i18nValue()`获得指定用户界面的多语言资源配置
    
    
    SDK.getAppAPI().i18NValue("com.actionsoft.apps.poc.api", me, "info1")
    

### HTML模版

在HTML页面或JavaScript中出现的多语言标签，使用<**I18N**`#变量名`>替代，其中变量名为多语言资源配置`Item`的`Key`。
    
    
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
    

### 多语言资源文件

遵循AWS PaaS对App的资源定义规范，每个AWS应用的多语言资源配置文件被存放在应用安装目录`/i18n/`下。

该目录允许存在1个或多个符合Schema规范的xml文件，建议为自己的应用创建一个名为`resource.xml`的资源配置文件。

项 | 说明  
---|---  
item/key | 多语言资源名，同个App下不允许重复  
item/cn | 中文简体  
item/en | 英文  
item/big5 | 中文繁体  
item/**%lang%** | 其他扩展的语言名  
  
**resource.xml示例**
    
    
    <locale-config>
        <lang>
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
        </lang>
    </locale-config>
    

### 多语言资源文件管理

建议访问AWS企业应用商店，安装“[`多语言编辑器`](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.translate/index.html>)”。

该工具提供了可视化的多语言配置工具，能够极大提高翻译人员的工作效率。

### 如何扩展更多种语言

默认AWS PaaS只提供了中文简体、英文和中文繁体三种界面语言，扩展更多种语言，请参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-language-reference-guide/extend/README.html>)。

以下代码打印出当前AWS PaaS支持的语言集
    
    
    List<LanguageModel> langs = SDK.getPlatformAPI().getlanguages();
    for (LanguageModel lang : langs) {
      System.out.println(lang.getName());
    }