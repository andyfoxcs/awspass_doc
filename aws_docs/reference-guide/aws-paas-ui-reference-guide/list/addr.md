# 省市县 | AWS UI组件参考指南

## 省市县

创建一个省市县控件，这是一个私有封装。通过点击INPUT框弹出选择框，选取省市县回填到表单，选择框中的省市县，是从[基础字典](<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/index.html>)应用中`省市县国标字典`中获取的，要求该应用版本不能低于1.1.63。同时使用省市县组件还要求平台不能低6.3.GA。

> 目前该UI组件不支持Ajax子表

### 运行

PC端  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addr1_PC.png)  
PC端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addr1.png)  
移动端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addr1_m.png)  
  
### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addrD1.png)

**预置校验**

参见单行[预置校验](<text.html#check>)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addr2.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

**扩展属性**

  * **_空值提示_**

参见单行[空值提示](<text.html#nulltip>)

  * **_选择模式_**

选择模式提供`省` `省/市` `省/市/县`、三个选项，默认`省/市/县`

    * **省代码回填字段** 非必填，支持模式是`省/市` `省/市/县`的，选择的省代码将自动回填到指定字段，该回填字段自动在表单隐藏，回填字段仅支持为文本的单行组件
    * **市代码回填字段** 非必填，支持模式是 `省/市/县`的，选择的市省代码将自动回填到指定字段，该回填字段自动在表单隐藏，回填字段仅支持为文本的单行组

    * **详细地址** 默认`关闭`，选择`开启`后，显示`详细地址回填字段` 属性

> **详细地址回填字段** 必填，输入的地址将回填到指定字段，该回填字段自动在表单隐藏，回填字段仅支持为文本的单行组件

    * **地图选点** 默认`关闭`，选择`开启`后，显示`高德key` `经纬度回填字段` `默认位置`属性

> 1.**高德key** 必填， 需调用第三方高德，要用户自己申请相关的key,配置到`AWS PaaS基础门户-AWSUI组件控制-定位组件的高德Key`参数或`该组件高德key`属性中才能使用，这两处填写的key会相互同步，填一处即可![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addr3.png)  
>  2.**经纬度回填字段** 必填，地图选点的经纬度回填到指定字段，该回填字段自动在表单隐藏，回填字段仅支持为文本的单行组件  
>  3.**默认位置** 默认`无`;选择`填单人位置`时，PC端默认显示城市中心，移动端支持详细地址定位  
>  4.不支持IE系统浏览器，ie8不显示地图选点图标，ie11、ie10 可通过地图回填，但在编辑时打开地图不能定位到具体地址