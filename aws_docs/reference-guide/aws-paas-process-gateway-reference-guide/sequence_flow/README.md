# 连线（Sequence Flow） | AWS BPMN2 Gateway参考指南

## 连线（Sequence Flow）

Sequence Flow是BPMN2规范中的流程定义元素，中文可称为“连线”、“顺序流”、“路径条件”、“连接弧”。连线可以在编排流程时，控制流程的执行顺序。

当连线作为排他网关、包容网关和复杂网关的拆分路径时，可以设定条件规则。

### 使用

从形状边缘拉出连线 | 改变连线样式  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/sequence_flow/1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/sequence_flow/2.png)  
  
注释可以让流程路线更直观和易于识别，注释不参与到引擎规则判断中，如某条连线代表`同意`，某条连线代表`不同意`。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/sequence_flow/3.png)

**如何为连线添加注释？**

  * 鼠标选中连线
  * 按空格键，输入或编辑注释

### 条件连线（Conditional Sequence Flow）

当连线位于网关（Gateway）、活动（Activity）、事件（Event）的右侧时，允许在连线上设定规则条件。引擎在执行网关、活动的后继拆分路线时，将通过评估条件的连线作为选择路径。

**如何为连线设置条件？**

  * 鼠标双击连线
  * 在弹出的`连线条件属性`对话框，完成条件设置

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/sequence_flow/4.png)

> 注意，不同BPMN对象，对连线条件的评估要求不同，建模人员应根据具体的网关（Gateway）、活动（Activity）、事件（Event）场景来决定是否要设定条件。例如，一个并行网关，不会评估任何后继的连线条件。

#### 条件和条件组

  * 一个或多个条件项，以AND关系组合，被称为一个`条件组`
  * 多个`条件组`以OR关系组合，按顺序进行评估

#### 表达式类型

  * 流程变量
  * 业务参数（BO数据源）
  * 流程实例参数
  * 任务实例参数
  * 审核菜单
  * 自定义条件

#### 判断类型

  * 等于
  * 大于
  * 小于
  * 大于等于
  * 小于等于
  * 不等于
  * 包含（*适用于文本类）
  * 全部等于（*适用于记录集）
  * 全部大于（*适用于记录集）
  * 全部小于（*适用于记录集）
  * 全部大于等于（*适用于记录集）
  * 全部小于等于（*适用于记录集）
  * 全部不等于（*适用于记录集）
  * 全部包含（*适用于记录集的文本类）
  * 全部不包含（*适用于记录集的文本类）

#### 值类型

  * 固定值，如`100`、`VIP`
  * 含有@公式的规则脚本，如`@uid`

### 默认连线（Default Sequence Flow）

在BPMN2规范中，一些进行条件评估的对象（如排他网关）允许有一个默认的连线。当所有后继路线的条件都不通过时，引擎会选择这条默认路线。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/sequence_flow/5.png)

**如何设置默认连线？**

  * 鼠标双击网关
  * 在弹出的对话框，选中一个`默认分支`