# 省市县 · AWS PaaS文档中心

# 省市县

创建一个省市县组件，这是一个私有封装。通过点击INPUT框弹出选择框，选取省市县回填到表单，选择框中的省市县，是从基础字典应用中省市县国标字典中获取的，要求该应用版本不能低于1.1.63。同时使用省市县组件还要求平台不能低6.3.GA。

> 目前该U组件不支持编辑子表

## 运行

PC端  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textssx1_pc.png)](<textssx1_pc.png>)  
PC端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textssx2_pc.png)](<textssx2_pc.png>)  
移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textssx_mobile.png)](<textssx_mobile.png>)  
  
## 配置字段属性

[![](https://helpcdn.awspaas.com/picture/picture/202310/bfcdc71691a540fe8bef104f71c5dc0e.png)](<https://helpcdn.awspaas.com/picture/picture/202310/bfcdc71691a540fe8bef104f71c5dc0e.png>)

**标题**

参见单行[标题](<text.html#title>)

**选择范围**

提供`省` `省/市` `省/市/县`三个选项，默认`省/市/县`

  * **省代码回填字段** 非必填，支持范围是`省/市` `省/市/县`的，选择的省代码将自动回填到指定字段，该回填字段自动在表单隐藏，回填字段仅支持为文本的单行组件

  * **市代码回填字段** 非必填，支持范围是 `省/市/县`的，选择的市省代码将自动回填到指定字段，该回填字段自动在表单隐藏，回填字段仅支持为文本的单行组

  * **详细地址** 默认`关闭`，选择`开启`后，显示`详细地址回填字段`属性

> `详细地址回填字段` 必填，输入的地址将回填到指定字段，该回填字段自动在表单隐藏，回填字段仅支持为文本的单行组件

  * **地图选点** 安装[高德开放平台](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.gaode/index.html>)才显示该属性，默认`关闭`，选择`开启`后，显示`自定义高德key` `高德安全密钥` `经纬度回填字段` `默认位置`属性

1.`自定义高德key`必填， 需调用第三方高德，要用户自己申请相关的key,配置到[高德开放平台](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.gaode/index.html>)参数名mapKey和securityKeyJsCode这两个中才能使用，这两处填写的key和安全密钥会同步到组件中 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textssx2.png)](<textssx2.png>)  

2.`高德安全密钥`2021年12月02以后申请的Key,需要配合安全密钥使用  
3.`经纬度回填字段` 必填，地图选点的经纬度回填到指定字段，该回填字段自动在表单隐藏，回填字段仅支持为文本的单行组件  
4.`默认位置` 默认`无`;选择`填单人位置`时，PC端默认显示城市中心，移动端支持详细地址定位

  1. `地图导航`可打开地图导航至定位地点，默认关闭，开启`地图选点`后，运行时选好地址后会显示去导航的按钮。
     * 仅支持移动端
     * 字段只读也支持
     * 点`去导航`，跳转的是设备上已安装的导航，如果安装多个导航相关的应用，弹出来供选择；如果没有安装，会提示请安装第三方地图应用

[![](https://helpcdn.awspaas.com/picture/picture/202310/57961170f7604a84a8778848c2379a55.png)](<https://helpcdn.awspaas.com/picture/picture/202310/57961170f7604a84a8778848c2379a55.png>) | [![](https://helpcdn.awspaas.com/picture/picture/202310/c50afc5ce1c147149078400c44d1c1bf.png)](<https://helpcdn.awspaas.com/picture/picture/202310/c50afc5ce1c147149078400c44d1c1bf.png>)  
---|---  
  
**控制属性**

参见单行[控制属性](<text.html#control>)

**不允许重复录入**

参见单行[不允许重复录入](<text.html#nocopy>)

**宽度**

参见单行[宽度](<text.html#wigth>)

**提示文字**

参见单行[提示文字](<text.html#tip>)

**帮助说明**

参见单行[帮助说明](<text.html#help>)

**字段规则**

参见单行[字段规则](<text.html#zdgz>)