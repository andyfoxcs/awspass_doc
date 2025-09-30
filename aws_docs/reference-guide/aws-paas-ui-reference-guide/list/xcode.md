# 条形/二维码 | AWS UI组件参考指南

## 条形/二维码

动态显示一个条形码/二维码图片，这是一个私有封装。该组件可以将指定值转换成条形码/二维码图片。

### 运行

PC端 | 移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/xcodeR1.png)   
  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/xcodeR2.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/xcodeR1.png)   
  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/xcodeR2.png)  
  
### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/xcodeD1.png)

**基本属性**

  * **_查询列宽_**

不支持

  * **_帮助说明_**

不支持

  * **_扩展代码_**

不支持

**扩展属性**

  * **_类型_**

条形码和二维码

  * **_表格中显示为_**

在子表列表和DW列表中展示方式：`图片`,条形码和二维码的缩略图;`原值`,条形码和二维码的值,即配置信息中字符串解析@公式后的值

  * **_显示类型_**

三种显示类型`码和文字` `码` `文字`，默认选中`码和文字`

  * **_文字显示位置_**

当显示类型是`码和文字`时，显示文字位置选项`码上方` `码下方` 默认选中`码上方`

  * **_文字复制_**

当显示类型是`码和文字`时，文字是否允许复制，默认`允许`

  * **_图片配置_**

  * 当`类型`为`条形码`时，可设置条形码宽度，用来决定图片的清晰度，不设置使用图片的原始宽度
  * 当`类型`为`二维码`时可用于设置二维码的高度和宽度

  * **_配置信息_**

一个字符串，通常该值由@公式提取表单动态值

> 部分扩展属性不支持移动端  
>  表单运行时保存后才显示条形/二维码信息