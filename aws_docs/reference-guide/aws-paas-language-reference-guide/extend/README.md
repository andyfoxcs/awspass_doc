# 扩展其它语言 | AWS PaaS多语言开发参考指南

# 扩展其它语言

  1. 配置`%AWS_HOME%/bin/conf/aws-portal.xm`文件修改默认登录语言和扩展其它语言。
         
         <!--name,语言名称关键字，与i18n文件的item语言项对应
          title,语言标题
          default,是否默认，只允许其中一个lang为true
         -->
         <language>
          <lang name="cn" title="简体中文" default="true"/>
          <lang name="en" title="English" />
          <lang name="big5" title="繁體中文"/>
          <lang name="jp" title="日文"/>
         </language>
         

  2. 修改`%AWS_HOME%/webserver/webapps/portal/index.jps`登录页，增加相应语言选项
         
         <select class="aws-login-font" name=lang id=lang onchange="setLangCookie(this.value);loadLang();">
          <option value=cn>中文</option>
          <option value=en>English</option>
          <option value=big5>繁體</option>
          <option value=jp>日文</option>
         </select>
         

  3. 配置`%AWS_HOME%/apps/install/%APPID%/i18n/`多语言资源文件
         
         <item key="PageTitle">
              <cn><![CDATA[这是标题]]></cn>
              <en><![CDATA[This is Title]]></en>
              <big5><![CDATA[這是標題]]></big5>
              <jp><![CDATA[これはタイトルです。]]></jp>
         </item>