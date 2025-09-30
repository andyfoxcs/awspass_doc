# 日志编程接口 | AWS LOG日志参考指南

# 日志编程接口

## LogAPI

使用LogAPI可以持久记录开发者的日志信息到文件或数据库。

  * info()
  * debug()
  * warn()
  * err()
  * audit()
  * unauthorizedAccess()

##### info()

输出info级别日志信息，同时该信息输出至CONSOLE启动窗口
    
    
    //应用`com.abc.apps.xyz`输出一个`hi`日志
    LogAPI.getLogger(this.getClass()).info("hi");
    

##### debug()

输出debug级别日志信息，同时该信息输出至CONSOLE启动窗口

> 如果该应用`manifest.xml`的`debug`选项关闭，不输出该记录。
    
    
    //应用`com.abc.apps.xyz`输出一个`hi`日志
    LogAPI.getLogger(this.getClass()).debug("hi");
    

##### warn()

输出warn级别信息到日志文件
    
    
    //应用`com.abc.apps.xyz`输出一个`hi`日志
    LogAPI.getLogger(this.getClass()).warn("hi");
    

##### err()

输出err级别信息到日志文件
    
    
    //应用`com.abc.apps.xyz`输出一个`hi`日志
    SDK.getLogAPI().getLogger(this.getClass()).warn("hi");
    
    //应用`com.abc.apps.xyz`输出一个`hi`日志和异常堆栈
    LogAPI.getLogger(this.getClass()).error("hi",e);
    

##### audit()

记录一条客户端审计日志
    
    
    SDK.getLogAPI().audit("admin", "update", "订单1010101", "交易成功", "127.0.0.1", Level.INFO);
    

##### unauthorizedAccess()

检查到越权访问时记录，如非法访问未授权的功能
    
    
    SDK.getLogAPI().unauthorizedAccess(me, "越权执行订单。orderId=10101010");
    

## AppAPI

AppAPI也提供了运维日志接口，主要记录与该应用运行环境相关的临时日志，当应用重启后，非err级别的信息被丢弃。

<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/AppAPI.html>

  * info()
  * warn()
  * err()

> 注意，这类日志信息主要提供给系统开发者或应用方案安装调试人员，如运行环境依赖致导致部分功能关闭

## 延伸阅读

  * [LogAPI（平台的日志入口接口，包括审计日志和运行日志）](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/LogAPI.html>)
  * [Logger（文件日志输出接口）](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/Logger.html>)