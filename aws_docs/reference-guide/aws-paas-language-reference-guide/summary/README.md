# 约束 | AWS PaaS多语言开发参考指南

# 约束

多语言资源文件是指存放在平台`%AWS_HOME%/apps/install/%APPID%/i18n`目录中的所有符合Schema规范的xml文件。文件内容格式如下：
    
    
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
    

项 | 说明  
---|---  
item/key | 多语言资源名  
item/cn | 中文简体  
item/en | 英文  
item/big5 | 中文繁体  
item/%lang% | 其他扩展的语言名