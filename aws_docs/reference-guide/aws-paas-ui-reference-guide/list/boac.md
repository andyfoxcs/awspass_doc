# 自定义权限 | AWS UI组件参考指南

## 自定义权限

为当前流程实例数据提供自定义的授权机制，开发人员可调用AC API检查该流程实例数据是否有读、写访问权限，通常这是个抽象的权限机制，可根据需要进行利用。使用该UI的字段类型可以是实体字段，也可以是虚拟字段。

> 目前该UI组件不支持移动端

### 运行

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/ACR1.png)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/ACD1.png)

**基本属性**

  * **_查询列宽_**

不支持

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

不支持

**扩展属性**

开发者调用SDK.getPermAPI().havingACPermission(uid,resourceType,resourceId,accessMode)方法判断用户是否有访问权限
    
    
    //uid：待鉴权的用户UID
    //resourceType：固定值："platform.process"
    //resourceId：当前boId(记录ID)
    //accessMode：固定值：0
     SDK.getPermAPI().havingACPermission("admin", "platform.process", "f2ead2e0-07bb-423f-9eb5-fc8d97657bbd", 0);
    

> 有关权限接口的详细介绍请参见<https://docs.awspaas.com/api/aws-api-javadoc/index.html>
> 
> 用户可根据需要自开发AC权限，详细请参见<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/ac.html>