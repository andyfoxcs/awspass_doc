# 系统 | AWS @公式参考指南

# 系统

  * sid
  * lang
  * i18n
  * deviceType
  * clientIp
  * portalUrl
  * serverInstance
  * serverProperty
  * sysProperty
  * env
  * secretIdentityToken

## sid

**_语法_**

@sid

  * 操作者会话

**_参数_**

无

**_例子_**
    
    
    Tom登录的会话是@sid
    

**_结果_**
    
    
    Tom登录的会话是a5140bac-34a1-49fc-b752-1289e6219e77
    

## lang

**_语法_**

@lang

  * 操作者使用的界面语言

**_参数_**

无

**_例子_**
    
    
    Tom使用的界面语言是@lang
    

**_结果_**
    
    
    Tom使用的界面语言是cn
    

## i18n

**_语法_**

@i18n(*key,*appId,lang)

  * 获取指定键值的多语言配置

**_参数_**

  * _key_ （必选）多语言Key，注意区分大小写

  * _appId_ （必选）该配置在指定的appId应用资源包中

  * _lang_ （可选）语言名，如未指定默认取当前操作者所处的语言环境

**_例子_**
    
    
    无
    

## deviceType

**_语法_**

@deviceType

  * 操作者使用的设备类型

**_参数_**

无

**_例子_**
    
    
    Tom使用的设备类型是@deviceType
    

**_结果_**
    
    
    Tom使用的设备类型是pc
    

## clientIp

**_语法_**

@clientIp

  * 操作者的IP地址

**_参数_**

无

**_例子_**
    
    
    Tom的IP是@clientIp
    

**_结果_**
    
    
    Tom的IP是10.10.0.1
    

## portalUrl

**_语法_**

@portalUrl

  * 用户访问AWS门户的根URL
  * 该项出厂时未配置，用于指定外部用户访问BPM请求的根URL，例如在一封互联网邮件中打开一个待办任务。如果内外网同时访问，该配置项应该是一个域名地址
  * 后缀无/

**_参数_**

无

**_例子_**
    
    
    外部用户访问AWS BPM客户端的URL根地址是@portalUrl
    

**_结果_**
    
    
    外部用户访问AWS BPM客户端的URL根地址是http://www.domain.com/portal
    

## serverInstance

**_语法_**

@serverInstance

  * 当前AWS服务的实例Id
  * 集群部署时，实例名不同

**_参数_**

无

**_例子_**
    
    
    当前的AWS实例Id是@serverInstance
    

**_结果_**
    
    
    当前的AWS实例Id是aws1
    

## serverProperty

**_语法_**

@serverProperty(_*name_)

  * AWS服务器扩展参数配置
  * 读取server.xml中有关properties内的扩展参数值
  * 名称区分大小写

**_参数_**

  * _name_ (必选)由管理员在server.xml中配置的扩展参数名

**_例子_**
    
    
    自定义参数ABC的值是@serverProperty(ABC)
    

## @sysProperty

**_语法_**

@sysProperty(name)

  * 支持aws.home、系统环境变量

**_参数_**

  * _name_ (可选)供开发人员参考使用，详见<https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#getProperties-->

**_例子_**
    
    
    key的值是@sysProperty(java.version)
    

## @env

**_语法_**

@env(*varName,valueOf)

  * 取CC环境变量值，如果参数不存在将抛出异常

**_参数_**

  * _varName_ (必选) CC环境参数名称
  * _valueOf_ (可选) 可设置常量ext1、ext2、ext3取扩展值

**_例子_**
    
    
    @env(crmServerUrl)/api/abc
    

## @secretIdentityToken

**_语法_**

@secretIdentityToken(_secretIdentityTokenId,_ fieldName)

  * 根据策略与字段名称，获取缓存内容

**_参数_**

  * _varName_ (必选) CCToken身策略Id
  * _valueOf_ (必选) 字段名称

**_例子_**
    
    
    @secretIdentityToken(secretIdentityTokenId,access_token)