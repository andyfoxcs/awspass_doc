# 附件 · AWS PaaS文档中心

# 附件

创建一个支持从本地附件上传、下载阅读的附件控件，这是一个私有封装，文件内容以附件形式存储到AWS PaaS平台doccenter目录

## 运行

PC端 | 移动端  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf_PC.png)](<textf_PC.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf_mobile.png)](<textf_mobile.png>)  
  
> 运行时上传附件支持手动上传及拖动附件上传

## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf1.png)](<textf1.png>)

**标题**

参见单行[标题](<text.html#title>)

**附件显示信息**

上传人、上传时间、文件大小，默认这三个信息都勾选

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf2.png)](<textf2.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf2.1.png)](<textf2.1.png>)  
  
**排序方式**

按上传时间、文件名升序、降序排序

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf3.png)](<textf3.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf3.1.png)](<textf3.1.png>)  
  
**限制文件数量**

默认为0不限制，控制指定个数的附件，只支持数字类型

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf4.png)](<textf4.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf4.1.png)](<textf4.1.png>)  
  
**限制单个文件大小**

  * 组件中默认为0，不限制文件大小
  * 还可在 %AWS_HOME%/bin/conf/server.xml文件filesize.max来配置附件大小,默认为50MB,设置单个文件的最大限制1024MB,组件与server.xml文件大小限制，限制取最小的
  * 如需上传超过1024MB的附件,可在%AWS_HOME%/webserver/webapps/portal/WEB-INF/web.xml中放开init-param属性，且配置!form-ui-file-设置单个文件的最大限制，同时server.xml文件中filesize.max也需要配置成与!form-ui-file-设置的最大限制一致

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf5.png)](<textf5.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf5.1.png)](<textf5.1.png>)  
  
> 数据库存储为附件文件名，因此字段超长限制仅限制附件文件名长度

**文件类型**

支持`不限` `文档` `图片`三种文档类型

  * **不限**
  * **文档**

    * 不选、不填表示不限制
    * `允许的文件格式`默认全选
    * `允许更多文件格式` 除`允许的文件格式`外，还可以填写其他的文件格式
  * **图片**

    * 不选、不填表示不限制
    * `允许的文件格式`默认全选
    * `允许更多文件格式` 除`允许的文件格式`外，还可以填写其他的文件格式
    * `显示方式` 图片列表，幻灯片这两种显示方式，默认图片列表
      * **图片列表**
        * 缩略图大小，提供了`大` `中` `小`三个选项，默认缩略图大小为`中`
        * 隐藏文件名等显示信息
      * **单行轮播**
        * 隐藏文件名等显示信息
        * 自动播放

> 隐藏文件名等显示信息，隐藏的是缩略图中的，预览的不隐藏  
> ; 显示信息即上面附件显示信息，如上传人、文件大小、上传时间  
> 单行轮播不支持编辑表格

PC图片列表 | PC单行轮播  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf6.png)](<textf6.png>)[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf6.1.png)](<textf6.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf6.2.png)](<textf6.2.png>)  
移动端图片列表 | 移动端单行轮播  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf7.png)](<textf7.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textf7.1.png)](<textf7.1.png>)  
  
  * `限制为手机拍照`默认不开启，可以从手机文件中选择图片上传；开启后，不能从手机文件中选择图片上传，直接拍照或录视频
  * `图片水印`默认不开启,开启后显示`水印位置` `水印模板`
  * `水印位置` 水印显示的位置，提供了`左上角`、`左下角`两个选项
  * `水印模板`提供了三类模板：打卡上报、现场巡检、自定义模板

    * **编辑模板**

**LOGO** 可上传/删除，最大1M，base64保存到后台表单模型文件

**标题** 最多128字符，可支持@公式，还可根据提供的四种颜色，设置标题背景

**数据** 前面的颜色块用来设置数据项的背景可以是透明的，也可是黑或者白

      * **日期** 选项有：日期、日期+时间、日期+星期、日期+星期+时间
      * **天气** 选项有：天气+温度、天气+温度+风速、湿度
      * **位置** 选项有：省+地点、市+地点、县镇+地点、市+县镇+地点、省市县镇+地点【支持web浏览器和Pad的定位】
      * **经纬** 选项有：北纬000°00’ , 东经000°00’
      * **拍摄人** 选项有：姓名、姓名+手机号后四位、姓名+部门、姓名+部门+手机号后四位
      * 如果勾选`限制手机拍照`，天气、位置、经纬三项显示可用（其他模板等同），否则这三项不显示

        * **添加水印数据** ，最多可以添加10个自定义数据
          * **表单值** 直接选择当前表单的其他字段，支持的组件单行、多行、数值、货币、单选、多选、日期类、手机、身份证、链接、邮箱、字典类、字段二维码、表单二维码
          * **自定义** 标题+内容支持@公式

> 日期、天气、位置、经纬、拍摄人等固定数据项有开关控制是否显示，手动添加的水印数据可进行删除操作

**禁止下载**

  * 默认关闭，开启后，运行端上传的附件不允许下载
  * 附件只读状态下，支持批量下载

**允许预览**

默认不开启，开启后，还需要安装了`文档预览服务`或`WPS文档在线预览`应用，支持预览的文件才能在线预览，如这两个应用都安装了，WPS文档在线预览优先调用。企业微信、钉钉、飞书上附件预览不调用这两个应用，是调用它们应用本身的预览

> `允许预览`，只支持文件类型是`不限` `图片`,文档类型`文档`的是`Office文档预览`

**Office文档预览**

  * 默认关闭，开启后，同上面的`允许预览`
  * 添加水印内容支持@公式
  * 设置样式，加粗、斜体
  * 设置字体大小
  * 设置字体颜色
  * 选择字体
  * 由WPS提供的在线预览，配置WPS预览服务应用id和应用Key,这两参数的配置与`WPS文档在线预览`应用中的参数同步,获取参数详见[WPS文档在线预览](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.wpsonline/index.html>)

**加密存储**

默认开启，对存储在doccenter目录下的附件文件名和内容进行加密

> 上传的附件文件名不支持的特殊符号`/[\^\&*\|\\'\/<>\?:"]/`

**控制属性**

参见单行[控制属性](<text.html#control>)

> 附件只支持必填、只读这两个控制属性

**宽度**

参见单行[宽度](<text.html#wigth>)

**帮助说明**

参见单行[帮助说明](<text.html#help>)

**字段规则**

参见单行[字段规则](<text.html#zdgz>)