# PC端 · AWS PaaS文档中心

# PC端

## 标准表格

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/15.png)](<15.png>)

属性项 | 说明  
---|---  
表格模式 | 三种模式：标准、分组、树形，默认的表格模式是标准  
序号 | ● **默认开启** 显示序号；关闭不显示序号，序号每页重置、累加隐藏   
● **序号每页重置** 客户端数据列表显示【序号】列，每页【序号】从1开始   
● **序号每页累加** 客户端数据列表超出一页后，下一页【序号】值自动与上一页连续  
行高 | 默认`标准` 客户端数据列表行高的展示情况：`紧凑`、`标准`、`中等`、`高`、`超高`  
内容自动换行 | 开启后，客户端数据列表的内容超过列宽后自动换行显示，默认不开启  
行选择 | **默认开启** 显示行选择框，及相关选择属性；关闭不显示行选框，相关选择属性也隐藏  
●`多选`、`单选`, 默认多选   
●**一直显示** 选择后，客户端列表显示全选check框，且列表数据支持多选   
●**仅允许删除可显示** 当行记录不允许删除时，在该行记录左侧不显示check框  
行点击规则 | 默认未配置，点击配置，弹出点击规则配置，该配置同列属性/字段属性[点击规则](<culum.html#onclickrule>),配置后在序号列显示可点击的图标[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/dg1.png)](<dg1.png>)  
统计值显示 | 使用统计功能时的显示方式：表格底部或右下方。在分组和树形表格模式时，没显示统计值显示该属性  
  
> 分页在表格下方设置，每页显示多少条，默认每页15条

## 分组

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/grouptable.png)](<grouptable.png>)

分组是一种常用的视图配置，可以在表格里按照某一列的值进行分组。配置分组后，所有记录会按照分组条件归到不同组内，你可以查看不同组下的记录。比如，你可以在表格中按“完成状态”进行分组，所有记录都会归到“未开始”、“进行中”、“已完成”这几个组内。

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/grouptable1.png)](<grouptable1.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/grouptable2.png)](<grouptable2.png>)  
  
### 添加分组条件

可以在`交互模式`是`表格`，点击`高级选项`中的表格模式选择`分组`，然后添加一条分组条件。

一条分组条件包含两个信息：

  * 分组的列：即指定从哪一列分组数据。我们这里选择 “完成状态”。

  * 组间的排序：即拖动组间位置来进行组间的排序。

目前最多允许设置三级分组。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/grouptable3.png)](<grouptable3.png>)  
---  
  
### 设置分组的排序

设置分组条件后，针对不同的字段列类型，可以设置两种排序规则。

  * 文本类型排序：“A→Z” 、“Z→A” 。表示文本会按照ASCII码正序或者倒序排序（中文会按照中文拼音排序）

  * 日期、数值类型排序：“1→9”、“9→1”。表示数值会按照从大到小或者从小到大排序

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/grouptable4.png)](<grouptable4.png>)  
---  
  
### 展开折叠分组

我们可以点击组头的 “展开折叠图标” 对每组进行展开折叠操作。

也可以点击组头，展开组头对字段进行数据计算

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/grouptable5.png)](<grouptable5.png>)  
---  
  
**数据计算方式种类：**

项 | 说明  
---|---  
常规组件 | 不展示、记录总数 未填写、已填写、唯一值、未填写占比、已填写占比、唯一值占比  
日期、日期时间 | 不展示、记录总数 未填写、已填写、唯一值、未填写占比、已填写占比、唯一值占比、最早时间、最晚时间、时间范围（日）、时间范围（月）  
数字、货币 | 不展示、记录总数、求和、平均值、最大值、最小值、未填写、已填写、唯一值、未填写占比、已填写占比、唯一值占比  
  
**计算方式说明：**

项 | 说明  
---|---  
不展示 | 数值栏不显示任何字样  
记录总数 | 当前列数据总数，例如：显示：5条记录  
未填写币 | 当前列空数据数，例如：显示：未填写3  
已填写 | 当前列有数据数，例如：显示：已填写2  
唯一值 | 除相同数据和空数据以外的数据总数，例如：显示：唯一值 1  
未填写占比 | 未填写数和总数的比值，例如：显示：未填写占比0%  
已填写占比 | 已填写数和总数的比值，例如：显示：已填写占比0%  
唯一值占比 | 唯一值和总数的比值，例如：显示：唯一值占比0%  
最早时间 | 日期、日期时间组件，一组数据中的最早日期，例如：显示：最早时间2022-05-11  
最晚时间 | 日期、日期时间组件，一组数据中的最晚日期，例如：显示：最早时间2022-05-31  
时间范围（日） | 一组数据中，最早时间-最晚时间，（只有一条数据时，不构成范围，显示0），例如：显示：时间范围3天  
时间范围（月） | 一组数据中，最早时间-最晚时间，（只有一条数据时，不构成范围，显示0），例如：显示：时间范围3月  
求和 | 显示：求和5.3  
平均值 | 显示：平均值5.3  
最大值 | 显示：最大值7  
最小值 | 显示：最小值5  
  
**查看更多**

分组中默认加载数据15条，这15条是根据标准表格分页默认每页15条来的。超过15条，点`查看更多`继续加载，每次加载数据条数是默认的15条。如果想一次加载大于15条，可以切换到标准表格，设置每页条数大于15条，保存再切换到分组中，这时加载数据根据表格中设置的每页条数来加载

> 流程视图、表格导航树、日历不支持分组，数据来源是数据服务、数据流的也不支持分组

## 树形

序号结构  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/treetable1.png)](<treetable1.png>)  
父子结构  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/treetable2.png)](<treetable2.png>)  
  
通过配置父子关系或者序号结构，显示分层的数据表格的一种交互模式。

序号结构配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/treetable1.1.png)](<treetable1.1.png>)  
序号结构运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/treetable1.png)](<treetable1.png>)  
父子结构配置  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/treetable2.1.png)](<treetable2.1.png>)  
父子结构运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/treetable2.png)](<treetable2.png>)  
  
**插入** 插入当前级的子级；插入权限跟随新增权限  
**序号字段** 只支持文本组件的字段，设置的字段会提到第一列, 做序号列，原本的序号列不在显示

>   * 不能构成树形结构的数据在表格中不显示
>   * 不支持分页
>   * 流程视图不支持树形
> 

## 看板

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban.png)](<kanban.png>)

**设置样式**

管理看板信息，可以显示/隐藏列，也可以只显示内容不显示列名称

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban1.png)](<kanban1.png>)

属性项 | 说明  
---|---  
看板分组 | 下拉字段是根据配置表单数据源可见字段进行过滤，只显示是单行、列表、单选组、地址簿、网格数据字典等组件的字段，其他的过滤；sql数据源显示的是所有可见的字段  
标题字段 | 标题字段显示在第一个，且不能拖动排序，标题字段内容值在选择框后，区别于其他字段样式加黑加粗显示  
主线字段 | 按主线字段过滤数据。如存在多项目情况下选择主线字段，默认不选择  
过滤字段 | 过滤数据，与主线字段不能重复  
序号字段 | 只能显示组件为数值类型的字段来作为序号字段，设置了序号字段，分组内的记录才能拖动排序，否则不能。不设置序号字段，前端运行可以进行自定义排序，设置了就是手动拖动排序  
完成进度 | 同序号字段，只能是数值字段，数值不符合0-1情况默认显示0  
点击规则 | 详见`数据视图-列属性/字段属性`中的[点击规则](<culum.html#onclickrule>),看板中不支持`内嵌下方`的打开方式  
封面 | 下拉展示的是附件字段，勾选拉伸，图片等比适配，不勾选，图片默认原比例 选择附件，运行时显示附件的所有图片，在PC端连播点图片预览多张图片，移动端用手左右划动即可预览多张图片  
显示列名称 | 默认开启，关闭后，卡片中只显示字段内容  
全显示/隐藏 | 批量设置卡片字段显示/隐藏  
单个字段排序/隐藏 | 设置为标题字段的显示在第一个，字段前是一把锁图标，不能拖动排序，其他字段可以拖动排序，字段后面的开关设置显示/隐藏  
  
> 设置分组字段分组数不能超过20个，超过20需要重新设置分组

**折叠分组**

当分组较多时，点击分组右侧按钮选择折叠/展开，让信息更加聚焦

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban2.gif)](<kanban2.gif>)

**删除分组**

  * 鼠标移动在分组卡片，点击右上角的删除图标
  * 分组可删除，删除后原分组记录移动至`未分组`中，设置为分组字段的值被清空
  * 未分组不能删除

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban3.png)](<kanban3.png>)

**修改分组名称**

  * 修改分组名称长度不能超过字段存储长度  

  * 支持解析HTML标签
  * 只有字段是单行组件的可以修改分组名称，其他组件不支持修改分组名称

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban4.png)](<kanban4.png>)

**分组拖动排序**

除未分组外，其他分组支持拖动排序

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban5.png)](<kanban5.png>)

**分组内数据拖动排序**

选中分组中的记录数据，鼠标放在拖动图标上，按住后拖动至其他分组中，修改分组字段的内容；也可以组内拖动，分组内数据要能拖动排序必须先设置`序号字段`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban6.png)](<kanban6.png>)

**未分组**

  * 始终显示，未满足分组条件的记录，将统一`未分组`中，并且固定在最左边的位置。
  * 未分组中的记录可拖动，未分组这个分组不可拖动。
  * 未分组名称不能修改

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban7.png)](<kanban7.png>)

**添加/删除分组数据**

有新建数据权限才能进行添加或删除操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban8.png)](<kanban8.png>)

### 展示效果图

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/kanban9.png)](<kanban9.png>)

## 相册

相册视图是将记录以卡片的形式展示，以记录附件中的图片作为封面，适用于名片、物料和菜单等场景

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc1.png)](<xc1.png>)

**新增记录**

在相册视图中，点击视图末端的`添加`，可以新增卡片。显示添加的前提是需要有新建数据的权限，新建数据权限同表格视图

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc2.png)](<xc2.png>)

**标题字段**

选择字段作为卡片的标题，在卡片中显示在字段的最上面，加粗加黑显示，也不能参与排序

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc3.png)](<xc3.png>)

>   * 标题字段设置隐藏后，在卡片中隐藏，作为标题不被隐藏  
> 
>   * 支持的组件：单行、多行、数值、货币、列表、单选组、复选组、日期、时间、日期时间、手机号、邮箱、链接、身份证号、地址簿、网格字典、分类字典、树形字典、流程字典、省市县、流程号，其他的组件不支持
> 

**设置筛选**

使用主线字段、过滤字段来过滤记录，页面中只显示符合条件的记录卡片，主线字段、过滤字段支持同时设置两者是AND关系进行筛选，让数据更聚焦。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc4.png)](<xc4.png>)

>   * 主线字段、过滤字段不能选择重复的字段  
> 
>   * 主线字段、过滤字段支持的组件：单行、多行、数值、货币、列表、单选组、复选组、日期、时间、日期时间、手机号、邮箱、链接、身份证号、地址簿、网格字典、分类字典、树形字典、流程字典、省市县、流程号，其他的组件不支持
> 

**卡片布局**

决定卡片，每行展示几个，默认5个，最小2个，最大6个

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc5.png)](<xc5.png>)

> 不支持移动端，移动端始终显示2个

**点击规则**

详见`数据视图-列属性/字段属性`中的[点击规则](<culum.html#onclickrule>)

> 不支持内嵌下方

**设置样式**

在相册视图中对记录卡片的样式进行调整，让信息更加聚焦，版面更加简洁。

  * 是否展示封面，封面效果是否拉伸
  * 显示/隐藏字段列，是否展示列名
  * 对字段列进行排序

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc6.png)](<xc6.png>)

创建相册视图时，`附件`字段中的图片将作为封面图，如有多个附件，默认展示第一个附件字段的图片。附件列中如有多张图片，点击封面图弹出放大通过箭头切换浏览。

封面图可选择拉伸或自适应模式，拉伸时填充整个封面区域，自适应则是将图片按比例缩放后完整显示。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc7.gif)](<xc7.gif>)

卡片信息可选择显示/隐藏所有字段列，也可以通过字段列名后的开关来控制。另外，还可以设置是否显示字段列名称，简化卡片信息。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc8.png)](<xc8.png>)

拖动字段列名称前的按钮，快速调整卡片上的字段顺序。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc9.gif)](<xc9.gif>)

### 展示效果图

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/xc10.png)](<xc10.png>)

## 日历视图

日历视图以天为单位，以日历形式展示表格数据。除了日期呈现更直观、团队协作更高效之外，还能在日历上通过拖拽，快速调整日程安排、起止日期，常用于一些需要关注日程的工作场景，如：会议室预约、服务档期预约、排课表、客户拜访计划、项目与活动策划、候选人面试安排等。

### 使用日历视图

**快速调整任务起止日期** 当日历视图设置了开始日期和结束日期，可通过拖拽日历上的任务条来改变日期安排的起止日期或者通过拉长或缩短任务条两侧来调整起止日期

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar1.gif)](<calendar1.gif>)

**快速调整日期安排** 当日历视图仅设置了开始日期或结束日期，可通过拖拽日历上的任务条来调整日期安排 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar2.gif)](<calendar2.gif>)

### 创建日历视图

点击视图页签栏的【创建视图】，选择日历视图，输入视图名称 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar3.png)](<calendar3.png>)

### 设置日历视图

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar4.png)](<calendar4.png>)

配置项 | 说明  
---|---  
开始/结束日期 | 只显示数据来源中的日期或日期时间组件的字段，系统字段及设置了隐藏的字段不显示  
点击规则 | 配置同列属性/字段属性[点击规则](<culum.html#onclickrule>)，配置后，卡片中出现`详细`按钮  
日历高度 | 默认和偏高，两种  
主题风格 | 任务条的主题风格，提供了7种风格供选择  
标签设置 | 设置展示在任务条上的字段值及显示的背景色，也可以调整字段值的显示顺序  
封面 | 选择数据源中是图片的附件字段，图片可以是多张，点击预览，采用手动轮播形式  
拉伸 | 图片原比例和统一比例的切换  
显示列 | 卡片内容的字段名称的显示、隐藏  
详情卡片 | 鼠标放在任务条上展示卡片，支持图片，支持对卡片内字段显示隐藏及排序  
  
**显示时分**

当只设置了开始或结束日期时，且配置的是日期时间组件，日历视图任务条及卡片中显示日期时间组件的

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar4.png)](<calendar4.png>)

**日历高度**

默认占满屏幕；偏高给出适当高度

默认  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar5.png)](<calendar5.png>)  
偏高  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar6.png)](<calendar6.png>)  
  
**还有X项**

根据日历各自高度自适应 ，多余的数据通过点击`还有X项`查看

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar7.gif)](<calendar7.gif>)

**日历视图的其他配置**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar8.png)](<calendar8.png>)

### 展示效果图

单日期  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar9.png)](<calendar9.png>)  
日期范围  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/calendar10.png)](<calendar10.png>)  
  
> 不支持分组，小眼睛即字段的显示隐藏功能，也不支持打印

## 地图

依据数据源中定位或省市县组件经纬度，在地图中标记地理位置，并查看对应数据详情。适用于门店管理，监控位置维护，地图标点定位等。用定位或省市县组件需环境中安装了[高德开放平台](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.gaode/index.html>)且配置了对应的key及密钥参数，详见[高德开放平台](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.gaode/index.html>)文档

配置项 | 说明  
---|---  
地图中显示 | 勾选该配置，在地图中定位旁边显示标题  
标题字段 | 选择数据中某一字段作为标题  
定位字段 | 数据源中有省市县或定位这两个组件中的一个，必填  
点击规则 | 配置同列属性/字段属性[点击规则](<culum.html#onclickrule>)，配置后，卡片中出现`详细`按钮  
详情卡片 | 点击定位图标，展示卡片，支持图片，支持对卡片内字段显示隐藏  
封面 | 选择数据源中是图片的附件字段，图片可以是多张，采用手动轮播形式  
拉伸 | 图片原比例和统一比例的切换  
显示列 | 卡片内容的字段名称的显示、隐藏  
左侧数据列表 | 仅展示标题名称和定位地址，可展收收起，显示数据数量，点击，快速定位至对应地址，并打开详情卡片  
配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/map1.png)](<map1.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/map1.1.png)](<map1.1.png>)  
  
>   * 标题字段不支持系统字段,计算字段、附件、高级排版、滑杆、打分、开关、关联查询及高级组件除流水号
>   * 地图满足滚轮缩放和鼠标拖动
>   * 平面、3D、卫星三种不同的地图展现方式可进行切换查看，但默认始终是平面，切换在3D或卫星，不会保存，下次打开还是平面
> 

## 层级

层级视图，可以将具有1对多关系的记录按层级树的方式展示出来，关联关系可以是具有父-子 、上下级关系的数据

配置项 | 说明  
---|---  
标题字段 | 选择数据中某一字段作为标题  
画布方向 | 纵向结构、横向结构两种  
线条样式 | 支持实线、虚线、曲线三种  
点击规则 | 配置同列属性/字段属性【点击规则】，配置后，卡片中出现【详细】按钮  
封面 | 选择数据源中是图片的附件字段，图片可以是多张，采用手动轮播形式  
拉伸 | 图片原比例和统一比例的切换  
显示列名称 | 卡片内容的字段名称的显示、隐藏  
卡片显示的字段与排序 | 卡片内容的字段名称的显示、隐藏，可选择显示/隐藏所有字段列，也可以通过字段列名后的开关来控制。另外，还可以设置是否显示字段列名称，简化卡片信息，排序字段的显示位置  
  
**纵向结构**

[![配置](https://helpcdn.awspaas.com/picture/picture/202309/dfb89d013c0841f7a952fa38b9ddfab7.png)](<https://helpcdn.awspaas.com/picture/picture/202309/dfb89d013c0841f7a952fa38b9ddfab7.png>)

[![运行效果](https://helpcdn.awspaas.com/picture/picture/202309/ca5b38cb20224318a4aa2ca869c6b20c.png)](<https://helpcdn.awspaas.com/picture/picture/202309/ca5b38cb20224318a4aa2ca869c6b20c.png>)

_纵向结构，能根据层级自定义层级名称_

**横向结构**

[![配置](https://helpcdn.awspaas.com/picture/picture/202309/e3aa65a04dd4471791b7945367499739.png)](<https://helpcdn.awspaas.com/picture/picture/202309/e3aa65a04dd4471791b7945367499739.png>)

[![运行效果](https://helpcdn.awspaas.com/picture/picture/202309/33fe7712a69948dfa68560eb688813f9.png)](<https://helpcdn.awspaas.com/picture/picture/202309/33fe7712a69948dfa68560eb688813f9.png>)

  * 标题字段不支持系统字段,计算字段、附件、高级排版、滑杆、打分、开关、关联查询及高级组件除流水号

**使用场景**

  * 项目管理：用层级视图将项目任务分解成树形结构，方便项目查看和管理

[![](https://helpcdn.awspaas.com/picture/picture/202309/fdfb908d94494018927787c7556e3572.png)](<https://helpcdn.awspaas.com/picture/picture/202309/fdfb908d94494018927787c7556e3572.png>)

  * 组织架构管理：用层级视图展示公司组织架构，能够清晰地查看公司部门之间的层级关系

[![](https://helpcdn.awspaas.com/picture/picture/202309/59572122604446dfbcbd9c2eadd9880c.png)](<https://helpcdn.awspaas.com/picture/picture/202309/59572122604446dfbcbd9c2eadd9880c.png>)

## 时间轴

  * 高级开发人员可通过修改JSON结构自定义展示内容、样式

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/15-4.png)](<15-4.png>)

> 建议在配置数据源字段列表中设置日期字段的排序规则

### 展示效果图

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/operation/timer_pc.png)](<../operation/timer_pc.png>)

## 甘特图

甘特图视图基于表格中的日期列生成，支持日期、开始日期、结束日期等列类型以及其他输出值为日期的列。如果表格内没有日期类型，需要创建后才可以生成甘特视图。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/wbs1.png)](<wbs1.png>)

1视图配置区 | 2任务列表区  
---|---  
**3任务图形区** | **4图形配置区**  
  
**视图配置区**

同表格视图，[配置查询条件](<select.html>)、[配置按钮](<tool.html>)、[配置分组标签](<group.html>)等操作

**任务列表区**

任务列表区的操作与表格视图保持一致，用于设置样式、显示规则、点击规则、修改规则等任务字段名称

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/wbs2.png)](<wbs2.png>)

**图形配置区**

**普通模式**

属性项 | 说明  
---|---  
主线字段 | 按主线字段过滤数据。如存在多项目情况下选择主线字段，默认不选择  
过滤字段 | 过滤数据，与主线字段不能重复  
开始日期字段 | 选择开始日期字段，字段的值作为甘特图开始日期  
结束日期字段 | 选择结束日期字段，字段的值作为甘特图结束日期  
序号字段 | 可以进行自定义排序，设置了就能手动拖动排序  
完成进度 | 只能是数值字段，数值不符合0-1情况完成进度显示0或100%  
移动端显示字段 | 选择移动端显示的字段  
主题风格 | 甘特图进度条展示的主题风格，默认提供7种  
标签设置 | 设置展示在甘特图进度条上的字段值及显示的背景色，还支持拖动调整位置及删除等操作  
  
  * 需要配置开始日期、结束日期，甘特图上才显示任务条，如果日期中没有值，则需要填充后才能显示任务条。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/wbs3.png)](<wbs3.png>)

  * 配置`序号字段`,`排序方案`隐藏
  * 配置`序号字段`，鼠标悬停在对应的字段上纵向拖动任务改变其排序

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/wbs4.gif)](<wbs4.gif>)

  * 配置`序号字段`后，通过指定序号插入数据

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/wbs5.gif)](<wbs5.gif>)

**WBS模式**

属性项 | 说明  
---|---  
序号间隔符样式 | 支持`1.1.1` `1_1_1` 这两种，维护数据时需要先选择一种间隔符，当有数据后该选项不能在修改  
  
>   * 其他配置属性同`普通模式`  
> 
>   * WBS模式下支持对下级序号列缩起展开操作
> 

**任务图形区**

  * 清晰呈现任务的开始日期、结束日期和进度,以任务条形式展式  

  * 任务条颜色浅的是任务周期，拖动任务条的两端可调整任务周期，改变任务条对应的开始和结束日期,同步任务列表区中的开始、结束日期字段值  

  * 任务条颜色深的是任务的完成进度情况，鼠标放在颜色深进度条最右边可以左右拖动任务进度  

  * `开始日期`、`结束日期`和`进度`都需要在图形配置区配置

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/wbs3.gif)](<wbs3.gif>)

  * 在图形区右上角，点击选择日期的聚焦格式，支持日、周、月、季、年 4 种精度查看任务进度，还可以指定当天的，在图中用一根蓝线标记当天

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/wbs6.png)](<wbs6.png>)

### 展示效果图

普通模式  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/wbs7.png)](<wbs7.png>)  
WBS模式  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/wbs8.png)](<wbs8.png>)  
  
## 导航日历(表格/时间轴)

导航日历模式不能单独使用，需配合表格、时间轴联合使用。

  * 必需配置一个日期字段与日历关联，展示时将自动按该日期字段在日历中切换过滤
  * 其它属性配置同表格、列表、卡片、时间轴的相关配置

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/15-5.png)](<15-5.png>)

### 展示效果图

导航日历表格  |  导航日历时间轴   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/operation/table2_pc.png)](<../operation/table2_pc.png>) |  [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/operation/timer2_pc.png)](<../operation/timer2_pc.png>)  
  
## 导航树

  * 鼠标划动到展示导航的区域中间，会显示"添加"的操作
  * 点击"添加"，弹出配置框

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/searcheTreeSQLD-1.png)](<searcheTreeSQLD-1.png>)

**导航树配置**

配置项 | 说明  
---|---  
支持多选 | 默认不开启，导航树是单选查询，开启后常规SQL类型和树形SQL类型内部多选以OR形式关联查询，外部不同类型间是AND查询  
远程搜索 | 默认不开启，导航树展开后在搜索框输入时时搜索结果，开启后，需输入条件按回车才显示搜索结果  
  
### 固定值

配置详见[配置查询条件-范围查询-固定值](<navigation.html#guding>)

### 范围值

配置详见[配置查询条件-范围查询-范围值](<navigation.html#fanwei>)

### 常规SQL

配置详见[配置查询条件-范围查询-常规SQL](<navigation.html#sql>)

### 树形SQL

过滤条件是单一字段，值由可构建层级关系SQL结果集匹配。

**参考值配置**

[![](https://helpcdn.awspaas.com/picture/picture/202309/c8b322dc221641b887d4aebf005c36dc.png)](<https://helpcdn.awspaas.com/picture/picture/202309/c8b322dc221641b887d4aebf005c36dc.png>)

  * **节点图标** 可自由设计图标，图标由iconFontCode,iconFontColor两部分组成 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/tb.png)](<tb.png>)
  * **子节点图标** 同上
  * **节点文字样式** CSS样式，如：color:blue;font-size:12px
  * **子节点文本样式** 同节点文字样式
  * **单击事件** 单击树节点触发的事件名称
  * **过滤事件** 实现`com.actionsoft.bpms.dw.design.event.DataWindowTreeFilterEventInterface`接口的类，示例：

    
    
    import java.sql.ResultSet;
    import java.sql.SQLException;
    
    import com.actionsoft.bpms.dw.design.event.DataWindowTreeFilterEventInterface;
    import com.actionsoft.bpms.server.UserContext;
    
    public class DataWindowTreeSqlFIlterEvent implements DataWindowTreeFilterEventInterface {
    
      /**
       * 树的节点过滤方法
       * @param me  用户上下文
       *  @param rs 数据集
       * @return 返回 true 过滤掉此数据
       * 说明：
       * 1.必须实现类 com.actionsoft.bpms.dw.design.event.DataWindowTreeFilterEventInterface
       * 2.此示例实现的是 : 过滤掉测试部门
       */
      public boolean treeSqlFilter(UserContext me, ResultSet rs) {
        String name = "";
        boolean f = false;
        try {
          name = rs.getString("departmentname");
          if (name.equals("测试部门")) {
            f = true;
          }
        } catch (SQLException e) {
          e.printStackTrace();
        }
        return f;
      }
    
    }
    

**展示效果图**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/operation/4.png)](<../operation/4.png>)