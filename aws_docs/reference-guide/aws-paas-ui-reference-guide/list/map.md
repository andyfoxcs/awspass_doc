# 地图选点 | AWS UI组件参考指南

# 地图选点

使用该UI组件需要正常安装并启用[高德开放平台](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.gaode/index.html>)应用且配置对应的应用参数：获取具体位置信息API配置及打开高德地图所使用的key。

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/2.1.png)

> 目前该UI组件不支持Ajax子表

### 运行

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/map.gif)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/map2.png)

**基本属性**

  * **_查询列宽_**

不支持

  * **_扩展代码_**

不支持

**扩展属性**

  * **_地图选点配置规则：_**

    * **地图风格** 必填，默认是标准风格，共11种风格
    * **3D地图** 默认关闭
    * **俯仰角度** 当开启3D时可用，角度有效范围0度到83度
  * **_地图展示配置规则：_**

    * **展示位置** 展示地图位置的标签id值，标签id需自行在表单页面配置。默认为空，表示不在表单页面显示地图；不为空地图则展现在对应标签内
    * **地图风格** 默认是标准风格，共11种风格
    * **标记文本** 配置展示位置可用。默认值：选中位置
    * **标记点动画** 三种，分别是：无动画、点标掉落、点标弹跳
    * **拖动** 默认否，选择是，可拖动标记文本框

> 移动端不支持地图展示配置规则

  * **_位置数据回填映射规则：_**
    * **将地址、省份、省份代码、市区、市区代码、县城、县城代码、经度、纬度等回填映射到表单字段中**
    * **映射字段建议不要填写当前字段，当前字段在存储中存了选择地址的经度、纬度，以便编辑打开地图展示之前选择的地址**
    * **映射字段必填**

> 内置根据经纬度查询地址信息[注：返回[基础字典](<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/index.html>)的省市县区域编码]

  * **_支持回填后事件_**
        
        /**
        * 回填后事件
        *
        * @param {JSONObject} data 当前位置的所有信息
        */
        function onBackfillEvent(data) {
        //事件处理代码
        }
        

> 运行时，默认获取移动设备所在的当前位置，只能在https协议中生效，否则获取不到