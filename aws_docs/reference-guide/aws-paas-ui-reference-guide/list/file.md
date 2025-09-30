# 附件 | AWS UI组件参考指南

## 附件

创建一个支持从本地附件上传、下载阅读的附件控件，这是一个私有封装，文件内容以附件形式存储到AWS PaaS平台doccenter目录下。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

### 运行

PC端  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileR1.png)  
移动端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileR_m.png)  
  
**预置校验**

  * 参见单行[预置校验](<text.html#check>)

  * 上传附件类型限制

  * 附件数量限制

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/file_filenumber.png)

  * 单附件大小限制

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/file_filezise.png)

> 数据库存储为附件文件名，因此字段超长限制仅限制附件文件名长度

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)，鼠标经过上传按扭时提示

  * **_扩展代码_**

不支持

**扩展属性**

  * **_文件方案_**

支持`相册`、`office文档`、`任意文件`、`手机拍照`四种方案

    * **相册**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileD2.png)

>     1. **图片类型** 允许上传图片类型
>     2. **开启压缩水印** 勾选后，在表单运行时，为附件上传人员提供`压缩、水印`check框，由上传人员决定是否需要压缩和添加水印
>     3. **水印图/文** 水印内容。不支持与用户组织、流程、表单等上下文相关的At公式
>     4. **水印位置** 水印位置
>     5. **水印文字大小** 水印文字大小
>     6. **水印文字颜色** 水印文字颜色
>     7. **默认压缩宽度** 图片压缩后宽度
>     8. **时长限制** 只支持移动端，上传指定时间内的照片
>     9. **添加时间水印** 只支持移动端，上传时添加时间水印

    * **office文档**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileD3.png)

>     1. **扩展名** 允许上传的附件类型
>     2. **支持预览** 该属性隐藏，只有安装了[文档预览服务](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.onlinedoc/>)或WPS文档在线预览应用，支持预览的文件才能在线预览，如这两个应用都安装了，WPS文档在线预览优先调用。企业微信、钉钉、飞书上附件预览不调用这两个应用，是调用它们应用本身的预览

    * **任意文件**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileD5.png)

>     1. **支持预览** 该属性隐藏，只有安装了[文档预览服务](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.onlinedoc/>)或WPS文档在线预览应用，支持预览的文件才能在线预览，如这两个应用都安装了，WPS文档在线预览优先调用

    * **手机拍照**

移动端仅支持拍照上传。在PC端无限制

  * **_加密存储_**

对存储在doccenter目录下的附件文件名和内容进行加密

  * **_最大上传个数_**

默认为0不限制，控制指定个数的附件，只支持数字类型

  * **_单个文件大小_**

默认为50MB，可在 `%AWS_HOME%/bin/conf/server.xml`文件中配置filesize.max,设置单个文件的最大限制1024MB；如需上传超过1024MB的附件，可在`%AWS_HOME%/webserver/webapps/portal/WEB-INF/web.xml`中放开`init-param`属性，且配置!form-ui-file-设置单个文件的最大限制，同时server.xml文件中filesize.max也需要配置成与!form-ui-file-设置的最大限制一致

  * **_手动排序_**

手动移动上下箭头进行排序，不支持移动端

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileD6.png)

  * **_排序字段_**

上传时间或文件名排序

  * **_排序方式_**

倒序或正序

  * **_文件分类_**

设置文件分类，多个以|分隔

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileD7.png)

  * **_上传详细信息_**

设置附件列表可显示的列

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileD4.png)

  * **_附件历史版本_**

运行时上传重复的附件，查看附件历史版本，不支持移动端

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/fileD8.png)

> 开发者可通过BOAPI完成附件的上传和读取等操作。<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/BOAPI.html>