# 附录2-程序文件 · AWS PaaS文档中心

# 附录2-程序文件

应用的安装、部署和运行由AWS PaaS自动化完成，但在开发阶段需要开发者了解这些资源结构。

## Web层资源

Web层是指部署在`Web Server`（如Tomcat）的资源。AWS PaaS为每个App分配了独立的目录，被称为Web层根资源根目录。

你可以在这个目录中规划自己的js、css等资源结构。
    
    
    //存放Web参数解析配置
    %AWS-HOME%/webserver/webapps/portal/apps/%appId%/action.xml
    //存放css
    %AWS-HOME%/webserver/webapps/portal/apps/%appId%/css/
    //存放js
    %AWS-HOME%/webserver/webapps/portal/apps/%appId%/js/
    //存放图片
    %AWS-HOME%/webserver/webapps/portal/apps/%appId%/img/
    //存放jsp程序(*不允许jsp直连数据库的开发模式，使用MVC cmd开发)
    %AWS-HOME%/webserver/webapps/portal/apps/%appId%/jsp/
    //自定义
    %AWS-HOME%/webserver/webapps/portal/apps/%appId%/.../
    

  * `%AWS-HOME%`是AWS PaaS的安装根目录
  * `%appId%`是应用的Id名

## App层资源

App层是指部署在`AWS Server`的资源。AWS PaaS为每个App分配了独立的目录，并通过安装、卸载库进行管理。

在开发的应用在容器仓库里处于`install`状态，与MVC编程相关的目录资源如下
    
    
    //存放App的配置描述
    %AWS-HOME%/apps/install/%appId%/manifest.xml
    //存放App的LOGO
    %AWS-HOME%/apps/install/%appId%/icon16.png
    %AWS-HOME%/apps/install/%appId%/icon64.png
    %AWS-HOME%/apps/install/%appId%/icon96.png
    //存放程序编译的jar文件和第三方类库
    %AWS-HOME%/apps/install/%appId%/lib/
    //存放HTML模版
    %AWS-HOME%/apps/install/%appId%/template/page/
    //存放多语言资源
    %AWS-HOME%/apps/install/%appId%/i18n/resource.xml