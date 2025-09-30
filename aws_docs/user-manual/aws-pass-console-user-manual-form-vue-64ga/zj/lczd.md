# 流程清单 · AWS PaaS文档中心

# 流程清单

将与当前操作者选择的流程或流程节点及所在应用相关的属性值回填到当前表单，为领导决策提供与表单信息相关的数据，这是一个私有封装。该组件在运行时为用户提供一个可选择流程或流程节点的界面，实施该组件的字段类型应为文本类型，长度属性建议1000，将在数据库中存储选择的流程或节点的ID值。

> 流程范围UI组件不支持编辑子表

## 运行

PC端  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textprocess2_pc.png)](<textprocess2_pc.png>)   
  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textprocess1_pc.png)](<textprocess1_pc.png>)  
移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textprocess_mobile.png)](<textprocess_mobile.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textprocess1.png)](<textprocess1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**个数**

运行时，表单上最多能显示几个，默认5个

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textprocess2.1.png)](<textprocess2.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textprocess2.png)](<textprocess2.png>)  
  
**列表**

根据提供的列表，包含`设计` `停用` `运行` `DW数据方案` `展示流程节点` 等五种选项，可多选，默认始终勾选一个。在运行时，让用户在指定范围选择

>   * 默认展示流程版本号信息  
> 
>   * 包含设计版包含数据视图的数据
> 

**高级模式**

默认不开启高级模式，即普通模式，是单选；开启高级模式后，可以设置多选

  * **允许多选**

开启多选后，可以设置`取值字段` `回填字段`

    * **取值字段**

固定的四个取值字段流程组ID 流程组名称 流程ID 流程名称,可多选

    * **回填字段**

回填当前表单的字段为文本类型的组件，支持的组件有单行、多行

**控制属性**

参见单行[控制属性](<text.html#control>)

**宽度**

参见单行[宽度](<text.html#wigth>)

**字段规则**

参见单行[字段规则](<text.html#zdgz>)