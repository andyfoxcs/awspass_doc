# 关联选择 · AWS PaaS文档中心

# 关联选择

创建一个带有文本录入和按钮的常规数据参考字典控件，对标准INPUT type=TEXT和 BUTTON元素的组合封装。可以通过按钮弹出的数据字典对话框，选取行并回填到表单。用于显示和修改被表单数据源绑定的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。

## 运行

PC端  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textwgzd_PC.png)](<textwgzd_PC.png>)  
移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textwgzd_mobile.png)](<textwgzd_mobile.png>)  
  
**新增数据**

当关联选择的数据源来自`关联表单`，且当前登录用户有对应视图菜单和新建按钮权限，关联选择中没有数据时显示【无数据，点击`添加`】、有数据但不是想选择的数据时显示【无匹配，点击`添加`】，打开对应的表单添加数据

无数据 | 有数据，但无匹配数据  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textwgzd4.png)](<textwgzd4.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textwgzd4.1.png)](<textwgzd4.1.png>)  
  
**模糊查询**

当关联选择文本类型字段勾选模糊过滤属性后，在运行时，用户可对相应字段进行模糊查询

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textwgzd2.png)](<textwgzd2.png>)  
运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textwgzd2.1.png)](<textwgzd2.1.png>)  
  
**条件查询**

当关联选择字段开启条件查询过滤属性后,在运行时，用户可对相应字段进行条件查询

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textwgzd3.png)](<textwgzd3.png>)  
运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textwgzd3.1.png)](<textwgzd3.1.png>)  
  
>   * 有关关联选择的设计详细参见[附录>关联选择模型](<pdf/dict.html>)章节  
> 
>   * 如果有模糊查询，条件查询最多可配置两个字段  
> 
>   * 只配置条件查询时，最多可配置三个字段  
> 
>   * 条件查询不支持移动端  
> 
>   * 配置了条件查询或模糊查询，运行端会显示`查询方案`
> 

**查询方案**

用户可自定义查询条件并保存起来。

  * **查询条件**

用户可自定义查询条件

  * **方案名称**

默认为条件字段名称的拼接串，为查询条件保存命名，方便下次直接查询

  * **共享**

当勾选共享后，所有AWS用户均可使用该查询方案，如未共享则查询方案仅创建人自己可见，其他用户不可见

### 手动输入查询

回填关联选择字段必须配置模糊查询或条件查询，在表单关联选择组件中输入配置了查询字段对应的值，按回车会查询对应的数据，如果查询结果只有一条，直接回填表单对应的字段值；如果是多条数据，弹出结果对话框供选择。移动端不支持该操作。

[![](https://helpcdn.awspaas.com/picture/picture/202305/c9c11e11f9af4db4ae3eb634d800ea43.gif)](<https://helpcdn.awspaas.com/picture/picture/202305/c9c11e11f9af4db4ae3eb634d800ea43.gif>)

  1. 当配置多个字段模糊查询时，输入的值对多个字段进行查询，查询结果是多个字段的合集
  2. 当配置多个字段是条件查询时，输入的值只对回填关联选择字段进行查询
  3. 当配置了键盘只读时，手动输入查询功能失效

[![](https://helpcdn.awspaas.com/picture/picture/202309/80006a4716624ec8ad633a4b7ca4f543.png)](<https://helpcdn.awspaas.com/picture/picture/202309/80006a4716624ec8ad633a4b7ca4f543.png>)

## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textwgzd1.png)](<textwgzd1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**长度**

参见单行[长度](<text.html#length>)

**前后缀**

参见单行[前后缀](<text.html#qhz>)

**配置方案** 选择关联选择模型文件，展示当前应用，或与当前应用关联的应用字典模型文件

**新增/修改** 新增/修改 `关联选择`模型文件，详见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue/pdf/dict.html>

**展示外观**

`对话框`以对话框的模式显示字典数据

**多选**

默认不开启，只允许选择一条记录回填到表单字段，若开启此开关，允许选择多值

### 是否保留输入内容

当没配置键盘只读时，开启该属性，输入框中输入的值可以作为查询条件值也可以作为值保留存入数据库

  * **分隔符**

开启多选时显示,多选，字典数据可以用`空格` `逗号` `竖线`分隔，回填字段为列表、复选组、地址簿，建议与字典使用一样的分隔符，没有时用逗号分隔

**链接选项**

参见单行[链接选项](<text.html#link>)

**控制属性**

参见单行[控制属性](<text.html#control>),与单行不同的是，这增加了键盘只读属性，默认不勾选，输入框中可以输入值，作为查询条件值也可以作为值保留存入数据库；勾选键盘只读，输入框不让输值

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