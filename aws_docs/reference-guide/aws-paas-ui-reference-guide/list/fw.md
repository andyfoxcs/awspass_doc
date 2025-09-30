# 流程范围 | AWS UI组件参考指南

## 流程范围

将与当前操作者选择的流程或流程节点及所在应用相关的属性值回填到当前表单，为领导决策提供与表单信息相关的数据，这是一个私有封装。该组件在运行时为用户提供一个可选择流程或流程节点的界面，实施该组件的字段类型应为文本类型，长度属性建议1000，将在数据库中存储选择的流程或节点的ID值。

> 流程范围UI组件不支持Ajax子表

### 运行

PC端  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/processfwR1.png)   
  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/processfwR3.png)  
移动端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/processfwR1_m.png)  
  
### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/processfwD1.png)

**基本属性**

  * **_查询列宽_**

不支持

**扩展属性**

  * **_流程定义范围_**

根据提供的`展示设计` `停用` `运行流程` `流程版本号` `DW流程`等五种选项，可多选。在运行时，让用户在指定范围选择

> `展示设计流程`包含数据视图的数据

  * **_流程模式_**

流程模式包含`完整流程` `流程节点`两种,默认选中`完整流程`

  * **_模式_**

模式`普通模式` `高级模式`,默认选中`普通模式`,在运行时，是多选。下面的`选择模式` `分隔符` `取值字段` `回填字段`这四个属性在`普通模式`时不显示，只有选择`高级模式`才显示

  * **_选择模式_**

选择模式分`单选` `多选`两种，默认`多选`

  * **_分隔符_**

`空格` `逗号`两种分隔符，默认`空格`

  * **_取值字段_**

固定的四个取值字段`流程组ID` `流程组名称` `流程ID` `流程名称`,可多选

  * **_回填字段_**

回填当前表单的字段为文本类型的组件，支持的组件有单行、多行