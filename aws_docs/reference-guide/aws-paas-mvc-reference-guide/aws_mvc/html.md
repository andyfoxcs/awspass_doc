# HTML页面 · AWS PaaS文档中心

## HTML Document

AWS MVC框架为开发者提供了页面模版处理框架，通过定义模版变量和程序对变量的处理生成最终页面内容。

提交请求的响应结果通常是一个完整的HTML Document。在一些前端动态拼装场景，局部DOM结构也可以被独立的定义成模版文件。但有时局部DOM无需使用模版，直接由程序动态组装。

模版被存放在该应用安装目录的`template/page`下，通常以html或htm后缀结尾（命名区分大小写）。除内容符合标准HTML、CSS、JavaScript规范外，模版标签变量定义的规则是，将需要程序生成的部分以`<#变量名>`替换，最终由`HtmlPageTemplate.merge()`混合成用户浏览器中的html内容。

如果该模版中出现的文字需要进行多语言处理，可以<**I18N**`#变量名`>定义，其中变量名是为该应用抽取的多语言配置项的Item的Key。

**在View层程序中完成模版处理的示例**
    
    
    public class ABCWeb extends ActionWeb {
        public ABCWeb (UserContext uc) {
            super(uc);
        }
        public String getMainPage(String p2) {
            Map<String, Object> macroLibraries = new HashMap<String, Object>();
            macroLibraries.put("page_title", "hello");
            macroLibraries.put("p2", p2);
            macroLibraries.put("sid", getContext().getSessionId());
            return HtmlPageTemplate.merge("%AppId%", "模版文件名", macroLibraries);
        }
    }
    

**HTML模板示例**
    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title><#page_title></title>
        <!-- 在JS中使用变量，如果需要 -->
        <script>
            var sid = '<#sid>';
        </script>
    </head>
    <body>
        <form action="./w" method=post name=frmMain >
            <!-- 在HTML中使用变量，如果需要 -->
            p2的值是<b><#p2></b>
         </form>
    </body>
    </html>
    

### 模版文件默认编码字符集

utf-8

### HTML模版资源引用范围

  * AWS平台Web目录commons/下的js、css、图片等公共资源
  * AWS平台Web目录apps/**%appId%** /下自定义的资源（appId为本应用的id）
  * 建议使用相对路径，如../apps/xxx、../commons/xxx