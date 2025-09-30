# 普通表格 | 表单模型

# 普通表格

为用户操作子表提供一组由普通HTML网页技术封装的网格操作界面，其主要特性：

  * 新增、修改记录可弹出明细窗口或侧边栏，适用于子表列众多的场景

## 运行

对话框  
---  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/pt.gif)  
侧边栏  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/pt1.gif)  
  
**运行时操作按钮**

AWS表单默认根据子表BO元数据结构动态生成一个网格。

![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/pt2.png)  
---  
项 | 属性  
---|---  
列标题 | 表单字段【标题】属性  
列宽度 | BO字段UI组件【查询列宽】属性  
新增按钮 | 弹出新增对话框或侧边栏，表单在该流程节点[表单应用>字段操作权限](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/authority.html>)中为该子表勾选[允许新增](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/authority.html>)属性  
删除按钮 | 表单在流程节点[表单应用>字段操作权限](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/authority.html>)中为该子表勾选[允许删除](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/authority.html>)属性  
编辑按钮 | 点击记录弹出修改窗口或侧边栏，表单在该流程节点[表单应用>字段操作权限](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/authority.html>)中勾选[允许修改](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/authority.html>)属性  
自定义按钮（关联录入） | 在配置自定义按钮（工具条左侧)关联录入  
导出按钮 | 表单在流程节点[表单应用>数据导入导出](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/data_import.html>)中为该子表设置了导出Excel文件策略  
导入按钮 | 表单在流程节点[表单应用>数据导入导出](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/data_import.html>)中为该子表设置了导入Excel文件策略  
下载模板按钮 | 表单在流程节点[表单应用>数据导入导出](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/data_import.html>)中为该子表设置了导入Excel文件策略  
  
> `新增` `删除` `导出` `导入`这四个通用按钮在表单设计器中是开启的，且在流程节点表单应用中也开启

## 普通表格配置

![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/pt3.png)  
---  
  
### 基本属性配置

**标题**

默认关闭，开启后，在单行框中输入标题

**添加/删除/拖动**

  * 点击`添加字段`按钮，选择字段对应的组件，默认为组件名称
  * 点击组件名称，切换到组件配置页进行相关配置
  * 鼠标放在字段名称上，显示`删除` `拖动`图标，点击删除图标，删除该字段；按住拖动图标，上下拖动调整位置

**隐藏字段**

设置子表字段在表格列中是否显示，仅控制主表单上的子表列的显示隐藏，不影响普通表格打开表单中的字段展示。

  * 点击`小眼睛图标`,隐藏字段在表单列表表格中的显示
  * 设置不显示后，子表Excle导出和导入将不显示被隐藏的字段
  * 被隐藏字段如果设置了不允许为空，编辑子表保存时不做必填校验

**高度**

子表显示高度，仅支持PX像素设置，当不设置时高度会随内容自适应

**样式**

简洁表格和边框表格两种，默认边框

**打开方式**

对话框和侧边栏两种

### 按钮配置

#### 通用按钮

  * `新增` `删除` `导出` `导入`,这四个通用按钮默认开启，这是一个全局的总开关  

  * 如果这不开启，流程节点上对应的[表单应用>字段操作](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/authority.html>)中为该子表开启对应的属性，在运行时也是不显示的  

  * 必须两处都开启，运行时该才显示对应的表单操作按钮
  * 子表导出模板是否包含隐藏字段有参数控制，详情见【AWS PaaS基础门户-表单运行】中的【子表导出模板是否包含隐藏字段(exportTemplateShowHidden)】参数，默认为true包含。仅适用于BO存储不可见和子表小眼睛控制是否显示的场景。包含时，隐藏的字段会存放在最后面

![](https://helpcdn.awspaas.com/picture/picture/202307/62d8fb1b87f140f2871e378bebb710ef.png)

  * 自定义子表导入模板字段，子表数据导入时，下载模板按需显示配置的字段

![](https://helpcdn.awspaas.com/picture/picture/202311/0b4a0b76345c4731920a8ee0f96d86ee.png)

#### 自定义按钮（工具条左侧）

自定义按钮（工具条左侧）可以添加`按钮` `按钮菜单` `按钮组` `间隔`这四种

  * `按钮` `按钮组`中有`关联录入`操作，参见关联录入
  * `按钮菜单`中没有`关联录入`操作
  * `按钮` `按钮菜单` `按钮组`有`触发自动化`操作
  * `按钮` `按钮菜单` `按钮组`其余的操作和配置属性与[数据窗口-自定义按钮](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/event.html>)一样，详见[数据窗口-自定义按钮](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/event.html>)
  * `间隔` 多个按钮间的分隔符，用的是竖线

**关联录入**

允许用户从关联的数据集选择，并将数据选择性插入到当前表格中。这是一个实施业务系统常用的数据间关联操作，例如在填写‘生产计划单’时，实施一个参考录入窗口，将‘生产需求表’数据关联到生产计划单。

![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/ck1.png)  
---  
  
**按钮样式**

与[数据窗口-自定义按钮](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/event.html>)一样，详见[数据窗口-自定义按钮](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/event.html>)

**关联录入操作**

选择按钮操作关联录入后，会显示与该操作相关的配置属性

![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/ck2.png)  
---  
  
**字典**

选择关联录入文件，列表展示的是当前应用及当前应用相关联的应用中的文件

**新增**

  * 没选择文件时，点新增配置关联录入文件，详细配置参见[附件-关联选择](<../pdf/dict.html>)
  * 在新增设计界面中关联录入还有 `关闭过滤回填字段` `插入前提示保存表单` `插入前校验字段必填` `插入后提示非空信息`等属性配置
  * 列数据必须添加ID字段(唯一标识)

  * **关闭过滤回填字段**

当数据来源是`关联表单` `关联存储`时，在列数据中`关闭过滤回填字段`属性,开启后，当子表表格中某个字段中的值与列数据开启该属性的值相同时，这时在`关联录入`中不显示这条数据

配置  
---  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/ck3.png)  
运行效果  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/ck3.1.gif)  
  
  * **插入前提示保存表单**

默认关闭,开启后在点击`关联录入`按钮时，提示保存表单

  * **插入前校验字段必填**

默认开启,当表格中有字段是必填，但关联录入回填的数据没有值，这时在回填时点`确定`,提示字段必填，当前数据不会插入到表格

配置  
---  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/ck4.png)  
运行效果  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/ck4.1.png)  
  
  * **插入后提示非空信息**

默认开启，当表格中有字段是必填，但关联录入回填的数据没有值，这时在回填时点`确定`,数据插入到表格，且会提示有必填字段是空值

配置  
---  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/ck5.png)  
运行效果  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/ck5.1.png)  
  
**预置数据-预置固定数据**

  * 默认【手动选择】，当切换到【预置数据】时，关联录入按钮在运行端不显示
    * 当在表格中没有数据且是第一次打开表单，自动插入数据
    * 仅获取第一页的数据，最多1000
    * 多个关联录入按钮，按按钮顺序依次获取每个按钮的数据，达到1000条为止
    * 流程节点不允许新增：开启允许参考录入,就会预置数据；不开启允许参考录入，是不会预置数据的；如果流程节点允许新增，这时允许参考录入属性禁用，不受允许参考录入配置的影响，能正常预置数据

![](https://helpcdn.awspaas.com/picture/picture/202312/4c6c794a73f4410fbe1efbfd84cc631f.png)

> 在普通表格中预置数据，预置的是固定数据，不随主表字段动态获取

**预置数据-主子表数据动态联动**

![](https://helpcdn.awspaas.com/picture/picture/202401/6d2a2968454c4a4cb837555074a7b7a2.png)

预置数据【主子表动态联动】支持编辑表格，移动端不支持

【主子表动态联动】功能应用场景：仅在第一次打开表单时，根据用户选择主表中的某个选项或输入内容时，子表中会对应展示过滤后与输入项关联的内容，没点击表单保存之前都是动态更新数据，点保存之后是动态追加数据

效果展示：当用户选择某个供应商时，子表中会展示该供应商能够提供的产品清单。

![](https://helpcdn.awspaas.com/picture/picture/202401/3a91d94e7e174228babf39be6c4bdb8f.gif)

**编辑**

关联录入选择文件后，`新增按钮`变成`编辑` `删除`

配置后将在子表工具条出现相关按钮

配置   
---  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/pt7.png)  
运行   
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/pt6.png)  
  
禁用规则、显示规则、样式规则、校验规则中的规则条件与[数据窗口-自定义按钮](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/event.html>)不同，这的规则条件根据下面四种条件来判断：

  * 根据`主表单` `可编辑` `只读`这两种状态作为条件
  * 根据`表格列表` `可编辑` `只读` `可新增` `可删除`这四种情况作为条件
  * 根据`流程状态`等于`流程结束后`作为条件
  * 根据`任务状态`等于`普通待办`、`抄送`、`沟通`、`通知`、`已办`、`全部状态`、`共享状态`等状态作为条件

![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/ck6.png)  
---  
  
> 任务状态是`通知`的场景比较特殊，只有在未读状态打开表单时生效，已读打开表单规则失效

**触发自动化**

自动化配置，详见[流程模型-自动化](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/auto.html>)

**自动化**

显示当前表单绑定流程中的自动化，选中自动化保存后，按钮的自动化动作会同步到对应流程的自动化动作触发中，如果在流程 自动化这删除表单按钮的自动化动作，也会同步清空对应表单按钮中选择的自动化

配置   
---  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/auto1.png)  
同步到流程   
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/auto2.png)  
运行   
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/auto3.png)  
  
#### 自定义按钮（工具条右侧）

  * 自定义按钮（工具条右侧）只支持添加按钮
  * 按钮中的操作不支持关联录入，其他的操作都与自定义按钮（工具条左侧）一致，相关配置和使用参见自定义按钮（工具条左侧）

#### 自定义按钮（悬浮记录右侧）

  * 自定义按钮（悬浮记录右侧）支持添加`按钮` `按钮菜单` `按钮组`
  * 按钮中的操作不支持关联录入，但有新增`复制记录`按钮,其他的操作都与自定义按钮（工具条左侧）一致，相关配置和使用参见自定义按钮（工具条左侧）

**复制记录**

允许复制的字段需要在BO模型字段属性中勾选允许复制属性，表格操作列显示复制按钮

配置  
---  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/auto4.png)  
运行效果  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/auto5.png)  
  
> 移动端不支持`自定义按钮（悬浮记录右侧）`

**子表自定义按钮运行效果**

自定义按钮  
---  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/auto6.png)  
移动端  
![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/auto7.png) | ![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/auto8.png)  
  
### 高级配置

默认关闭，开启后显示`每页数` `排序字段` `合计字段`等高级属性

  * **每页数**

设置子表记录分页参数，默认为0，即不分页

> 为了不影响表单的性能，当表格如果未设置分页， 数ridMaxPageSize值将作为每页最大的展示数据，其余分页显示。默认显示300条记录。建议不要设置过大，否则会影响表单加载速度。详见`AWS PaaS基础门户-表单运行-子表未设置分页时每页显示的最大记录数(gridMaxPageSize)`
> 
> ![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/pt4.png)  
> ---  
  
  * **排序字段**

设置该子表输出时的排序方案，此处是下拉单选存在的字段，可以添加多个。如果未设置排序字段值，系统默认按追加记录的顺序排序。

> 该设置比[FORM_GRID_FILTER](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/form_grid_filter.html>)事件优先级低

  * **合计字段**

数值类型字段合计功能

![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/pt5.png)  
---  
  
>   * 移动端不支持`合计字段`功能
>   * 小计统计的是当前页，合计统计的是所有数据的
> 

  * **过滤数据**

过滤子表数据,设置后在表单运行时为子表工具栏提供过滤按钮

![](https://helpcdn.awspaas.com/picture/picture/202309/a028cf533652491cb73dba2290e8562f.png)

右上角切换查询条件是满足所有还是任一

  * **所有** ：多个条件之间是and关系
  * **任一** ：多个条件之间是or关系
  * 查询条件被应用后只有在当前流程实例和当前人可以使用，办理给下一人或者是新建的流程实例，查询条件会被清空

### 表格规则

参见[表单规则](<../gz>)