# 流程设计器 | AWS BPMN2 Process参考指南

# 流程设计器

AWS PaaS的流程设计器核心基于最先进的HTML5 Canvas和SVG（可缩放矢量图形）技术实现，拥有较高的用户体验和低学习成本。

无需安装和配置客户端，无需插件下载，流程设计和实施人员只需打开浏览器即可安全完成所有工作。

  * 简单
  * 专业
  * 智能

## 简单

还原企业办公用户的做图习惯，全程提供所见即所得的图形化操作。在无需培训情况下，经过3-5分钟摸索即可上手使用。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/11.png)

**设计器被简化成三个区域**

  1. 工具条
  2. 画板
  3. 画布

#### 1\. 工具条

**常用操作**

项 | 说明  
---|---  
保存 | 保存用户的修改。保存即生效设置  
撤销/恢复 | 可以反悔用户做出的操作  
格式刷 | 和Office格式刷一样，批量格式化流程对象的外观效果  
字体 | 批量设置选中流程对象的字体类型/大小/颜色/粗细/对齐等  
填充 | 批量设置选中流程对象的背景颜色和渐变效果  
边框 | 批量设置选中流程对象的边框颜色  
线宽 | 批量设置选中流程对象边框、连线的粗细  
线条样式 | 批量设置选中流程对象边框、连线的线条样式  
连线样式 | 批量设置选中连线的类型，如直线、折线、曲线  
排列 | 批量设置选中流程对象的位置排列，简单强大  
视图 | 放大、缩小做图画布  
形状属性 | 打开选中流程对象的属性对话框  
流程属性 | 打开流程属性对话框  
流程文档 | 打开流程文档的编辑对话框，写流程帮助文档  
查看BPMN文件 | 查看当前流程图背后的BPMN2文件描述  
导出图片 | 导出当前流程图的PNG文件  
引用模板 | 基于`流程模板管控`创建一个合规流程  
运行 | 测试、执行流程  
版本 | 显示当前流程版本信息，管理、创建和发布流程版本  
  
#### 2\. 画板

画板是用户最常用的选择区。将画板的`形状`拖到`做图画布`，完成流程设计。

画板 | 介绍  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/12.png) | `BPMN Shape`提供了当前流程设计器支持的建模符号（形状）。这些符号按类型组织，点击符号右下角选择更多符号  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/13.png)  
  
`Lane`提供了横向和纵向泳池、泳道。一个合法的流程模型，只允许一个泳池，但可以拖拽多个泳道。就像一个游泳池里多个泳道那样理解  
  
`导航`提供了缩略图鹰眼，对于大图可以移动视觉方格定位流程图的局部位置。另外这里还提供了`演示视图`和`全屏视图`，适合流程团队在会议投影中全屏操作  
  
#### 3\. 画布

画布是用户设计流程的主要工作区域。按照用户习惯，画布支持两种交互模式：

  * 鼠标交互
  * 键盘交互（对于专业人员）

**常用键盘操作**

操作 | 快捷键  
---|---  
移动画布 | 按Alt移动鼠标  
多选 | 长按Ctrl点击形状  
打开形状属性 | 点击形状，按Shift+P  
打开流程属性 | 点击空白画布，按Shift+P  
全选 | 点击空白画布，按Ctrl+A  
复制 | 点击形状，按Ctrl+C  
复用 | 点击形状，按Ctrl+D  
剪切 | 点击形状，按Ctrl+X  
粘贴 | 点击空白画布，按Ctrl+V  
删除 | 点击形状，按Delete  
编辑文本 | 点击形状，按空格  
锁定 | 点击形状，按Ctrl+L  
解锁 | 点击形状，按Ctrl+Shift+L  
置于顶层 | 点击形状，按Ctrl+]  
置于底层 | 点击形状，按Ctrl+[  
  
##### 批量操作示例

操作 | 示例  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/14.png) | `批量锁定` \- 鼠标长按左键拖动的区域可批量选中对象，右键菜单选中`锁定`操作![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/15.png)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/14.png) | `批量移动` \- 鼠标长按左键拖动的区域可批量选中对象，鼠标移动到选中对象进行拖动（或键盘移动）![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/16.png)  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/14.png) | `批量设置` \- 鼠标长按左键拖动的区域可批量选中对象，在菜单批量设置外观![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/17.png)  
  
## 专业

  * 全球超过200万做图用户的体验
  * 设计符合ISO信息领域的模型标准

#### 全球超过200万做图用户的体验

AWS PaaS的商业版流程设计器与享誉全球的[ProcessOn](<http://www.processon.com>)在线做图工具同属一个技术架构。ProcessOn在全球拥有超过200万注册会员，平均每秒钟就会设计出一个张全新的流程图。

与其他BPM Process Designer不同，我们时刻关注数百万做图用户真实体验和反馈，使我们有机会提供最易用和最智能的流程建模工具。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/ProcessOn.png)

炎黄盈动在流程建模领域积累了十多年技术和专业经验，从第一代的网页配置到第三代HTML5智能设计器，始终给用户以最高效率的体验和工具价值。

第一代：网页配置 | 第二代：客户端Studio | 第三段：HTML5智能设计器  
---|---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/m1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/m2.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/m3.png)  
  
#### 设计符合ISO信息领域的模型标准

BPMN2.0（Business Process Model & Notation <http://www.omg.org/bpmn/index.htm> ）是商业流程建模和执行的最新标准规范，已被ISO在2013年列入信息领域的模型标准。

[ISO/IEC 19510:2013](<http://www.iso.org/iso/catalogue_detail.htm?csnumber=62652>)

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/iso.png)

**符合ISO标准的流程模型，对企业的好处**

  * 建模符号和方法全球通用，易于人才和知识的积累
  * 避免BPM供应商绑定，业务流程是企业的通用资产
  * 降低不同软件流程建模和执行的复杂度和集成难度

## 智能

  * 热点感知
  * 引导建模
  * 位置对齐
  * 语法检查
  * 历史回放

#### 热点感知

当鼠标移动到流程图形状边缘时，能够根据当前流程版本、活动类型提供进阶提示。例如

快速更换类型 | 边缘拖出连线  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/18.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/19.png)  
  
#### 引导建模

当用户画出一根连线时，提供进阶操作提示，做图过程流畅自然。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/20.png)

#### 位置对齐

当拖动单个或多个形状时，提供横向、纵向位置对齐锚线，让初级用户也可以画出结构清晰的流程图。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/21.png)

#### 语法检查

对于初次接触BPMN的用户，可能无法一次设计出符合引擎规范的流程结构，AWS流程设计器提供一键检查，并提供解决方案说明。 ![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/22.png)

#### 历史回放

设计器会智能记录用户的每次操作差异，随时以动画方式再现调整过程。系统还能够提供基于自动保存的历史还原。

  * 操作一次等待0.5秒（快速播放）
  * 操作一次等待3秒（慢速播放）

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/23.png)

## 延伸阅读

  * [流程建模规范](<../appendix/definition_spec.html>)