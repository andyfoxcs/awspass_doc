# 微应用 | AWS @公式参考指南

# 应用

  * getProperty
  * getAppName
  * isActive

## getProperty

**_语法_**

@getProperty(_*name,appId_)

  * 获得App参数值

**_参数_**

  * _name_ （必选）参数名称
  * _appId_ （可选）应用ID，从指定的应用中获取，默认为当前所在应用

**_例子_**
    
    
    获得应用"单位通讯录"的参数职务名称的参数值是@getProperty(positionName,com.actionsoft.apps.entaddress)
    

**_结果_**
    
    
    职务
    

## getAppName

**_语法_**

@getAppName(*appId)

  * 获得App名称

**_参数_**

  * _appId_ （必选）应用ID，从指定的应用中获取

**_例子_**
    
    
    获得应用"com.actionsoft.apps.entaddress"的名称是@getAppName(com.actionsoft.apps.entaddress)
    

**_结果_**
    
    
    单位通讯录
    

## isActive

**_语法_**

@isActive(*appId)

  * 如果未安装或停用返回false

**_参数_**

  * _appId_ （必选）应用ID，从指定的应用中获取

**_例子_**
    
    
    获得应用"单位通讯录"未安装或停用返回结果是@isActive(com.actionsoft.apps.entaddress)
    

**_结果_**
    
    
    true