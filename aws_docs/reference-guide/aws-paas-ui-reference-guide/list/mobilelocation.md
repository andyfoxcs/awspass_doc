# 定位 | AWS UI组件参考指南

## 定位

该组件运行时只支持移动端，在PC上只读显示定位的地址，不支持定位。在设计界面不支持IE系列浏览器

### 运行

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/MobileLocationR1.png)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/MobileLocationD1.png)

**基本属性**

  * **_查询列宽_**

不支持

**扩展属性**

下面的扩展属性默认都没有勾选，运行时在移动表单上点击`定位我的位置`定位显示当前所在位置的具体地址

  * **_高德key_** 必填，需调用第三方高德，要用户自己申请定位组件相关的key,配置到AWS PaaS基础门户-AWSUI组件控制-定位组件的高德Key参数中才能使用，配置的这个参数会同步到该属性，也可以直接在这填写 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addr3.png)

  * **_显示经纬度_**

勾选`显示经纬度`，定位获取当前位置所在的经纬度，运行时移动表单上显示经纬度及当前地址

  * **_显示地图_**

勾选`显示地图`，运行时，在移动表单上，点击`定位我的位置` 定位显示当前所在位置的具体地址及定位当前位置的地图

    * **允许微调** 勾选`允许微调`后，才可设置微调范围，移动单上点击`地图`,跳转到新的页面，新页面地图上把设置的微调范围圈出来了

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/MobileLocationR2.png)

  * **_限制定位范围_**

勾选`限制定位范围`后，可以新增/删除/编辑限制定位范围,移动端表单上在限制范围进行定位

> 扩展属性中允许微调、限制定位范围功能要求平台不低于6.3.GA

需要在移动表单自定义如下事件，对定位值进行处理
    
    
    /**
      * 定位后事件
      *
      * @param {String} boItemName 字段名
      * @param {String} longitude 经度
      * @param {String} latitude 纬度
      */
    function onLocationEvent(boItemName, longitude, latitude) {
      //事件处理代码
    }