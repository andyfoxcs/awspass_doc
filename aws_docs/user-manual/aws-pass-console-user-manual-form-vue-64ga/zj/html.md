# 高级排版 · AWS PaaS文档中心

# 高级排版

创建一个支持HTML编辑的排版控件，对ueditor的封装，内容以附件形式存储到AWS PaaS平台doccenter目录下。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

## 运行

PC端 | 移动端  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/texth_pc.png)](<texth_pc.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/texth_mobile.png)](<texth_mobile.png>)  
  
  * HTML排版控件编辑的内容被存储到文件系统，与绑定字段的长度无关
  * 可点击`图片-上传图片``图片-网络图片`将本地、网络图片上传至服务器，并参与排版
  * 可点击（）将本地文件上传至服务器，并提供下载链接

## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/texth1.png)](<texth1.png>)

**标题**

参见单行[标题](<text.html#title>)

**高度**

HTML组件运行时显示的高度，只支持数字类型，单位为像素，如果不设定将自适应

**控制属性**

参见单行[控制属性](<text.html#control>)

> `高级排版`只支持必填、只读

**字段规则**

参见单行[字段规则](<text.html#zdgz>)