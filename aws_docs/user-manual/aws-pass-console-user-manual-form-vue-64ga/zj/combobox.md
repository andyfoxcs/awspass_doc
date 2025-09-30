# 列表 · AWS PaaS文档中心

# 列表

创建一个列表选择控件，普通模式对标准SELECT元素封装，高级模式由AWSUI框架combobox实现。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

## 运行

PC端单选 | PC端多选  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS_pc1.png)](<textS_pc1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS_pc2.png)](<textS_pc2.png>)  
移动端轮播选项卡 | 移动端里程碑  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS2.1.png)](<textS2.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS3.1.png)](<textS3.1.png>)  
  
**新增数据**

当列表的数据源来自`关联表单`，且当前登录用户有对应视图菜单和新建按钮权限，列表中没有数据时显示【无数据，点击`添加`】、有数据但不是想选择的数据时显示【无匹配，点击`添加`】，打开对应的表单添加数据

无数据 | 有数据，但无匹配数据  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS3.gif)](<textS3.gif>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS31.1.png)](<textS31.1.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS1.png)](<textS1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**长度**

参见单行[长度](<text.html#length>)

**数据源**

参见单行[辅助录入](<text.html#source>)

> 单选支持[颜色开关](<radiogroups.html#color>)的控制，多选不支持

**多选**

默认多选开启，下拉列表的选项值允许多选

  * **分隔符号**

提供了空格、逗号、竖线三个分隔符号。多个值之间的分隔符号，默认为逗号。建议：当任一列表值包含空格时，可选择用逗号或竖线分隔。运行时表单上看不到分隔符效果，值存入数据库中可以看到多值分隔符的效果

**模糊搜索**

默认开启，运行时在选择框中可输入关键字对选项进行模糊搜索

**界面展示**

  * 轮播选项卡

    * **数据字体大小** 设置选项项字体大小

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS2.png)](<textS2.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textS2.1.png)](<textS2.1.png>)  

  * 里程碑

    * **背景颜色** 可分别设置已完成、进行中、未进行的背景色
    * **字体颜色** 可分别设置已完成、进行中、未进行的字体色

[![配置](https://helpcdn.awspaas.com/picture/picture/202308/8efbfe67cec042dbbd48b9b3cbbe717a.png)](<https://helpcdn.awspaas.com/picture/picture/202308/8efbfe67cec042dbbd48b9b3cbbe717a.png>)

PC端运行效果

[![PC端运行](https://helpcdn.awspaas.com/picture/picture/202308/e888415021bb4964a7a23c9d83a7480f.png)](<https://helpcdn.awspaas.com/picture/picture/202308/e888415021bb4964a7a23c9d83a7480f.png>)

移动端运行效果

[![移动端运行](https://helpcdn.awspaas.com/picture/picture/202307/59279770bdb54009aa287a55fe1088b6.png)](<https://helpcdn.awspaas.com/picture/picture/202307/59279770bdb54009aa287a55fe1088b6.png>)

>   * 仅当列表为单选时可用，在运行时以里程碑的方式展示，展示顺序为列表值的显示顺序
>   * 轮播选项卡与里程碑这两种界面展示，不能同时勾选
> 

**链接选项**

参见单行[链接选项](<text.html#link>)

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