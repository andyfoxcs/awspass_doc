# 前端框架 | AWS 移动开发参考指南

# 前端框架

AWS对前端框架的选择并无限制，您可以选择使用任何您熟悉的框架。对于初学者，如果您并不了解移动前端框架，我们推荐使用MUI前端框架来打造您的页面。

## MUI

MUI是一个高性能前端框架，体验接近原生APP。 MUI有以下特点：

  * 轻量：MUI不依赖任何第三方JS库，压缩后的JS和CSS文件仅有100+K和60+K。
  * 原生UI：MUI以iOS平台UI为基础，补充部分Android平台特有的UI控件，风格样式接近原生样式。
  * 高性能：MUI直接使用class编写，性能远高于data-方式，在手机上使用可以拥有流畅体验。

**_AWS PaaS内置了MUI前端框架， 所有文件保存在`%AWS-HOME%\webserver\webapps\portal\commons\plug-in\mui`目录下_**

  * MUI在页面中的引用路径示例：*

    
    
    <script type="text/javascript" src="../commons/plug-in/mui/js/mui.xxx.js"></script>
    <link rel="stylesheet" type="text/css" href="../commons/plug-in/mui/css/mui.min.css">
    

如何使用MUI，请参考以下官方文档：

  * [新手指南](<http://dev.dcloud.net.cn/mui/getting-started/>)
  * [在线文档](<http://dev.dcloud.net.cn/mui/ui/>)

## 使用自己熟悉的前端移动框架

可将资源放入自己App Web资源，在HTML页面内正确引用即可
    
    
    %AWS-HOME%/webserver/webapps/portal/apps/%your appId%/...