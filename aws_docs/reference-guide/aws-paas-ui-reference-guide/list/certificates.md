# 证件识别 | AWS UI组件参考指南

# 证件识别

在移动端实现证件识别。

使用该UI组件需要正常安装并启用[聚合数据平台](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.juhe/index.html>)应用

### 配置key

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/key.png)

key需要到聚合数据平台官网进行获取

### 运行

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/Certificates1.png)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/Certificates2.png)

**基本属性**

  * **_查询列宽_**

不支持

  * **_扩展代码_**

不支持

**扩展属性**

需要在移动表单自定义如下事件，对证件识别值进行处理
    
    
    /**
      * 回填前事件
      *
      * @param {JSONObject} data 识别后的值
      * @param {String} photoName 照片的名称
      */
    function onBeforefillEvent(data,photoName) {
      //事件处理代码
    }
    

> 照片映射的业务字段需要附件组件
> 
> 营业执照只支持竖版,不支持横板
> 
> 支持普通子表和ajax子表