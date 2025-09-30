# 滑杆 | AWS UI组件参考指南

## 滑杆

创建一个数值范围选择器，这是一个私有封装。该组件是一种特殊的输入控件，与滚动条类似，但滑块控件可设置最大最小值等特性，可以形象用于某些特殊场合，例如：优先级。显示和修改被表单数据源绑定后的数据，并自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端(横) | PC端(竖) | 移动端  
---|---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/sliderR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/sliderR2.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/sliderR1_m.png)  
  
### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/sliderD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

不支持

**扩展属性**

  * **_方向_**

水平和垂直两种

  * **_最小值_**

滑块最小值，必须为数字类型

  * **_最大值_**

滑块最大值，必须为数字类型

  * **_最小移动量_**

移动滑块时，最小增量值，必须为数字类型

  * **_单位_**

滑杆中值对应的单位，例如：单位为：个，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)

  * **_单位字体大小_**

设置单位的字体大小，必须为数字类型

  * **_单位字体颜色_**

设置单位的字体颜色

  * **_滑块消息_**

若勾选"提供消息事件"，需要在滑杆所在表单HTML中定义
        
        // 在表单HTML模板中实现如下JavaScript函数：
        /**
        * @param {Object} boItemName 字段名
        * @param {Object} sliderVal 滑杆值
        */
        function onSliderChangeEvent(boItemName, sliderVal) {
        //事件处理代码(不能有alert)
        }
        

> 部分扩展属性不支持移动端