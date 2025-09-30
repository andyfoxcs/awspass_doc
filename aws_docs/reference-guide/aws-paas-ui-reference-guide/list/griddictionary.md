# 网格数据字典 | AWS UI组件参考指南

## 网格数据字典

创建一个带有文本录入和按钮的常规数据参考字典控件，对标准INPUT type=TEXT和 BUTTON元素的组合封装。可以通过按钮弹出的数据字典对话框，选取行并回填到表单。用于显示和修改被表单数据源绑定的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。

### 运行

PC端  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryR1.png)  
移动端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryR1_m.png)  
  
**预置校验**

  * 若为文本类型，参见单行[预置校验](<text.html#check>)

  * 若为数值类型，参见数值[预置校验](<number.html#check>)

**模糊查询**

当网格数据字典文本类型字段勾选模糊过滤属性后，在运行时，用户可对相应字段进行模糊查询

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryD5.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryR4.png)

**精确查询**

当网格数据字典字段勾选精确查询过滤属性后,在运行时，用户可对相应字段进行精确查询

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryD5.1.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryR4.1.png)

>   * 有关网格数据字典的设计详细参见[附录>网格数据字典模型](<../appendix/dgriddictionary.html>)章节  
> 
>   * 如果有`模糊查询`，精确查询最多可配置两个字段
>   * 只配置`精确查询`时，最多可配置三个字段
>   * `精确查询`不支持移动端
> 

**查询方案**

用户可自定义查询条件并保存起来。

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryR2.gif)

> 有配置`模糊查询`，移动端才显示自定义查询

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryR2.1.png)

  * **_查询条件_**

用户可自定义查询条件

  * **_方案名称_**

默认为条件字段名称的拼接串，为查询条件保存命名，方便下次直接查询

  * **_共享_**

当勾选共享后，所有AWS用户均可使用该查询方案，如未共享则查询方案仅创建人自己可见，其他用户不可见

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryD1.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_显示规则_**

参见单行[显示规则](<text.html#displayrule>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

    * 参见单行[扩展代码](<text.html#componentExtendCode>)

    * readonly仅控制文本框不可输入，但按钮还是可以点击

    * disabled控制文本框和按钮均不可使用

**扩展属性**

  * **_空值提示_**

参见单行[空值提示](<text.html#nulltip>)

  * **_模式_**

    * 对话框模式：以对话框的模式显示字典数据
    * 下拉模式：以下拉模式显示字典数据，该模式不支持Ajax子表

  * **_文件名_**

从当前应用、父应用、依赖应用下选择一个字典文件

> 依赖应用是指该应用的manifest.xml声明依赖的应用
>         
>         <requires>
>           <require appId="依赖应用的AppId" notActiveHandler="error"/>
>          </requires>
>         
> 
>     * notActiveHandler=error，表示高度依赖。如果服务提供方被停用，该应用将收到错误
>     * notActiveHandler=warning，表示中度依赖。如果服务提供方被停用，该应用将收到警告
>     * notActiveHandler=none，表示智能依赖。如果服务提供方被停用，该应用不会收到任何信息

  * 允许行多选

默认只允许选择一条记录回填到表单字段，若勾选此开关，允许选择多值

  * 数据校验

针对回填字段的数据校验,仅支持单选状态和对话框模式，不支持Ajax子表、移动端

  * 允许清空

表单的网格数据字典字段增加按扭![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/griddictionaryD4.png)，清除由网格数据字典填写的字段信息。

  * 数据字典管理器

打开数据字典配置管理器，有关数据字典模型的配置详细参见[附录>网格数据字典模型](<../appendix/dgriddictionary.html>)章节

  * 行多选分隔符

仅当勾选`允许行多选`时有效,字典用竖线，回填字段为列表、复选组、地址簿等只能用逗号分隔；字典单选时，回填字段为列表、复选组、地址簿等也只能用逗号分隔

> 当源字段是附件类型时，仅支持单选

  * **链接选项**

参见单行[链接选项](<text.html#link>)

> 部分扩展属性不支持移动端