# HTML排版 | AWS UI组件参考指南

# HTML排版

创建一个支持HTML编辑的排版控件，对ueditor的封装，内容以附件形式存储到AWS PaaS平台doccenter目录下。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端 | 移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/htmleditorR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/htmleditorR1_m.png)  
  
  * HTML排版控件编辑的内容被存储到文件系统，与绑定字段的长度无关
  * 可点击（![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/htmleditorR3.png)）将本地图片上传至服务器，并参与排版
  * 可点击（![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/htmleditorR4.png)）将本地文件上传至服务器，并提供下载链接

**预置校验**

  * 参见单行[预置校验](<text.html#check>)

  * 不校验长度

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/htmleditorD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

不支持

  * **_扩展代码_**

不支持

**扩展属性**

  * **_排版模式_**

启用高级模式，与HTML排版设置及特性相同，仅提供了更多排版功能

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/htmleditorD2.png)

未启用高级模式，HTML排版显示为：

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/htmleditorD3.png)

  * **_粘贴格式_**

勾选`是否开启纯文本粘贴`后，不支持从Word中粘贴带有特定字体、样式的段落内容至HTML排版组件

  * **_选项_**

勾选后将支持对应选项内容

  * **_高度和宽度_**

HTML组件运行时显示的宽度和高度，只支持数字类型，单位为像素，如果不设定将自适应

  * **_水印图/文_**

仅对HTML排版组件中图片上传按钮(![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/htmleditorR3.png))有效，设置水印内容，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)

  * **_默认压缩宽度_**

仅对HTML排版组件中图片上传按钮(![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/htmleditorR3.png))有效，设置图片上传后压缩大小

> 部分扩展属性不支持移动端

  

**表单JS操作HTML**
    
    
      UE.getEditor("字段名").getContent();  // 获取HTML排版的值
      UE.getEditor("字段名").setContent("内容"); // 为HTML排版赋值
    

**BO API读取HTML内容**
    
    
      SDK.getBOAPI().get("表名", "BO记录ID","字段名");
    
      或者
    
      List<BO> list = SDK.getBOAPI().query("bo表名", true);
    

### 延伸阅读

  * [BOAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/BOAPI.html>)