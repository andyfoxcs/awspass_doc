# 附录1-编程资源 · AWS PaaS文档中心

# 附录1-编程资源

AWS MVC是一个开放的编程架构，你可以方便的将自己需要的工具包加入到自己的App中使用：

  * **三方Jar类库** 存放到App安装目录的lib下
  * **三方JavaScript、CSS库** 存放到Web层的`apps/%appId%/`下

## AWS PaaS提供的开源Jar类库

可在你的程序中直接使用AWS PaaS自带的一些第三方开源类库，这些Jar文件存放在AWS安装目录的`bin/lib`和`bin/jdbc`下。

类库 | 说明  
---|---  
commons-* | Apache提供的若干工具类  
barcode4j | 条形码生成  
cajo | RMI工具类  
csv | CSV数据处理工具  
xalan/... | XML数据处理  
json-lib | JSON数据处理  
poi | Office文件处理  
httpclient | HTTP客户端  
itext | PDF处理  
sigar | 系统性能监控  
log4j | Java日志处理系统  
cxf | Web服务处理框架  
... | ...  
  
## AWS PaaS封装的Web UI

这些组件全部基于JQuery和JQueryMobile底层框架封装，使用这些UI有助于开发的应用界面与AWS其他应用保持一致的交互习惯。详细说明参见**[AWS UI](<aws_ui.html>)** 章节