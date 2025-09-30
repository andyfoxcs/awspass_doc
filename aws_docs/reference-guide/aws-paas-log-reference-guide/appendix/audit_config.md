# 自定义审计场景 | AWS LOG日志参考指南

# 自定义审计场景

通过扩展AWS平台的审计配置参数，开发者可以基于企业安全审计要求，对全平台的`dao`操作和MVC框架的`cmd`访问进行审计。

  * cmd
  * dao

审计配置文件路径
    
    
    %AWS-HOME%/bin/conf/aws-audit.xml
    

> 配置文件修改后不需要重启平台，自动更新

## cmd

假如您需要拦截用户执行`com.actionsoft.apps.poc.api_Home`的操作，配置示例如下：
    
    
    <audit type="cmd" catalog="client" id="com.actionsoft.apps.poc.api_Home"
    obj="测试cmd访问" op="access"/>
    

参数 | 说明  
---|---  
type | cmd表示拦截MVC的cmd  
catalog | 这里统一指定为client（即客户端操作）  
id | 要拦截的cmd名称  
obj | 客体对象名称，如模块名称、功能名  
op | 操作类型，见[审计日志](<../audit_log/README.html>)相关参数的描述  
info | 日志详细描述信息  
when | 对结果值进行处理，返回true表示拦截  
  
上述obj、op、info、when参数支持@公式和$参数处理，例如
    
    
    //如果functionId有值，操作为update，否则操作为create
    op="@if(@equals(@len(${functionId}),0),create,update)"
    
    //如果结果包含result变量且值为ok，拦截操作被触发
    when ="@equals($matr(&quot;result&quot;:&quot;,&quot;),ok)"
    

  * ${xxx}取cmd请求上下文中参数值
  * $matr匹配处理
  * $refCache读缓存对象做值翻译

## dao

假如您需要拦截TestDao执行`insert`/`update`的操作，配置示例如下：
    
    
    <audit type="dao" catalog="client" info="id是$arg(0)"
    id="com.actionsoft.apps.poc.api.local.app.dao.TestDao"
    obj="测试DAO" op="create" method="insert" />
    
    <audit type="dao" catalog="client" info="id是$arg(0)"
    id="com.actionsoft.apps.poc.api.local.app.dao.TestDao"
    obj="测试DAO" op="update" method="update" />
    

参数 | 说明  
---|---  
type | dao表示拦截MVC的dao  
catalog | 这里统一指定为client（即客户端操作）  
id | 要拦截的dao类全路径  
obj | 客体对象名称，如DAO对象名  
op | 操作类型，见[审计日志](<../audit_log/README.html>)相关参数的描述  
info | 日志详细描述信息  
method | 要拦截的dao方法名  
  
上述obj、op、info、when参数支持@公式和$参数处理

  * $arg(0) 表示取dao方法参数的值，从０开始为第一个参数