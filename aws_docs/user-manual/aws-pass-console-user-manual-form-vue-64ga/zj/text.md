# 单行 · AWS PaaS文档中心

# 单行

创建一个文本输入框，对标准INPUT type=TEXT元素封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态。

## 运行

PC端 | 移动端  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR_PC.png)](<textR_PC.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR_mobile.png)](<textR_mobile.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR1.png)](<textR1.png>)

**标题**

  * **标题** 在表单上默认显示的标题。对于某些敏感数据域提供采用AES加密存储，实施方法在标题前缀增加`**`，例如`**基本工资`，因此该类字段的类型必须是文本型。注意，加密后的文本长度大概是原值的20倍
  * **名称** 数据库字段名，不可重复
  * **开关** 控制标题隐藏/显示,默认显示

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR2.png)](<textR2.png>)

> 移动端不支持标题隐藏

**默认值**

  * **自定义**

若字段从数据源读取值为NULL或空串且该字段设置了【默认值】，则显示该值

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR3.1.png)](<textR3.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR3.png)](<textR3.png>)  
  
  * **数据联动**

能够一次从数据来源规则里关联多个字段，配置效率高、执行一次关联多个性能好。如果从第三方系统关联多个字段，只需一次API请求，不会对三方系统造成压力。

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRld3.1.gif)](<textRld3.1.gif>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRld3.png)](<textRld3.png>)  
  
**添加联动字段**

  * 点击`数据联动`按钮，弹出的对话框来实际联动配置的对话框规则

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRld3.2.png)](<textRld3.2.png>)  
---  
  * 如果联动设置了多个字段，其他字段`默认值`类型下拉框值变为`数据联动`且该下拉框只读，对应的字段在存储中默认值框标记`已经设置数据联动`且不能在编辑

联动字段 | 存储中联动字段  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRld4.1.gif)](<textRld4.1.gif>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRld4.png)](<textRld4.png>)  

  * 如果取消了该字段的联动，则`默认值`类型下拉框值变为`自定义`且该下拉框可编辑
  * 当类型设置为`数据联动`后，运行时该字段只读不可编辑
  * 数据联动，运行表单读取的是联动数据的第一条
  * 添加联动支持的组件：单行、多行、数值、货币、列表、单选组、复选组、日期、时间、日期时间、滑杆、开关、网格数据字典、地址簿、邮箱、手机号、身份证号
  * 数据来源用的是关联表单，添加联动字段时，联动显示的只显示主表单的字段，如果想配置显示子表单的字段改关联存储来实施

**打开表单时检查更新**

默认不勾选，在运行时当表单数据保存后，不在随联动数据改变 勾选后，在运行时当表单数据已保存，但联动数据有变动如新增，删除、排序、过滤等操作导致第一条数据发生改变，这时重新打开表单获取时时改变的第一条数据

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRld3.3.png)](<textRld3.3.png>)  
---  
  
**数据联动运行**

  * 设置全表单只读时，不触发联动请求和处理，字段只读或表单 所有字段只读还是会触发联动请求
  * 联动字段通过手填、字典、规则触发、脚本触发发生变化时，根据联动回填值，没检查到回填空串

  * **计算公式**

对该字段设置@公式，填写表单时自动显示@公式生成的字段值。

点击「编辑公式」进入@公式编辑器框，输入要设置的公式，使用方法参见：[AWS @公式参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

**相关值改变重新计算**

默认勾选且禁用

**新建记录时使用默认值计算**

默认不勾选，可以根据具体的业务需求来实施是否勾选

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textRld3.3.1.png)](<textRld3.3.1.png>)  
---  
  
**长度**

默认长度128，录入长度超过字段长度时，不允许保存

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR4.1.png)](<textR4.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR4.png)](<textR4.png>)  
  
**前后缀**

字段值说明的更清楚明白

  * **设计图标**
  * **标签文字**

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR5.1.png)](<textR5.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR5.png)](<textR5.png>)  
  
**限定字数**

限定输入的字数，默认没开启该功能

  * **最少** 输入的字数没达到最少限定，给出提示
  * **最多** 超过限定的最多字数输入不上

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR6.1.png)](<textR6.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR6.png)](<textR6.png>)  
  
**扫码录入**

  * 默认不开启，开启后，在运行时用设备扫码后会替换掉原值、支持扫码事件
  * 支持的UI:单行、多行、数值
  * 主子表都支持
  * 支持的应用端：钉钉、企业微信、飞书、移动门户、WeLink

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.1.1.png)](<textR7.1.1.png>)  
---  
  
**辅助录入**

当用户输入字符时即时提供命中率参考列表，默认没开启该功能

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.1.png)](<textR7.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.png)](<textR7.png>)  
  
  * 数据源-自定义

    * **单个添加** 每次只能添加一个
    * **批量添加** 批量编辑，每行对应一个选项。如果自定义取值，格式为：值:显示，注意使用英文冒号':'
    * **颜色** 默认开启，添加时默认给添加的常量值添加颜色，`单行`不支持颜色开关，`单选组`、`单选列表`、`复选组`支持颜色开关
    * **自定义取值** 开启自定义取值，格式为：值:显示，注意使用英文冒号':'
    * **还支持拖动排序、设置默认值、删除添加的项等操作**

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7_1.png)](<textR7_1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.1.1.png)](<textR7.1.1.png>)  
  * 数据源-关联表单

    * **表单** 必填，列出的是与当前应用相关联的所有应用的表单，可以多选，最多选5个表单
    * **关联** 选择多个表单才显示`关联`这个属性且必填,可以添加多个关联，但同一个存储、字段不能重复选择
    * **过滤** 单个表单过滤列出的是与表单关联的存储字段，多个表单过滤列出的是配置关联的存储字段，条件值支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)、$[字段名]，例如$[ORDERTYPE],该字段名为当前字段所在BO表中字段名，可以配置多个，多个过滤条件组合可以是and也可以是or的关系；还可以分别选择按账户或按部门过滤
    * **排序** 选择存储字段同过滤，支持升序、降序排序
    * **值** 选择存储字段同过滤，必须填写
    * **显示** 选择存储字段同过滤，可不填写，如不填写，将默认为取值字段值

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.2.1.png)](<textR7.2.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.2.png)](<textR7.2.png>)  
  * 数据源-关联存储

    * **存储** 必填，列出的是与当前应用相关联的所有应用的存储，可以多选，最多选5个存储
    * **其它配置项与关联表单相同**

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.3.1.png)](<textR7.3.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.3.png)](<textR7.3.png>)  
  * 数据源-关联字典

    * **字典** 必填，显示基础字典中当前应用及关联应用的所有字典名称
    * **数据过滤** 当前键值字典支持的属性过滤，有关各字段名介绍参见<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/appendix/table.html>, 条件值支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)、$[字段名]，例如$[ORDERTYPE],该字段名为当前字段所在BO表中字段名

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.4.1.png)](<textR7.4.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.4.png)](<textR7.4.png>)  
  
> 需要安装[基础字典](<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/>)应用，且关联该应用

  * 数据源-SQL数据

    * **数据源** `本地数据源`，数据来自当前AWS连接的本地数据库  
`CC 数据源`，数据来自在连接服务Database适配器配置的外部数据库，目前支持的是通过[RDS - 连接关系型数据库服务](<https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rds.html>)配置外部数据库
    * **SQL语句** 一个完整的select SQL语句，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)、$[字段名]，例如【… where orderType=$[ORDERTYPE]】,该字段名为当前字段所在BO表中字段名
    * **值** 在SQL记录集存在的字段名，必须填写
    * **显示值** 在SQL记录集存在的字段名，可不填写，如不填写，将默认为取值字段值
    * **值转换** 当配置显示字段名与取值字段名不同时，用于后台字段名与取值字段名的快速转换。一个标准的SELECT查询，查询结果为应为显示字段名和取值字段名

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.5.1.png)](<textR7.5.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.5.png)](<textR7.5.png>)  
  * 数据源-数据服务

    * **数据服务** 来自`连接服务-数据`列表中的数据，只显示当前应用及关联应用的`连接服务-数据`
    * **数据集位置** 根据选择的数据服务，选择对应的数据集,数据集只支持数组类型的
    * **值** 选择的数据服务记录存在的名称，必须填写
    * **显示** 选择的数据服务记录存在的名称
    * **参数** 选择的数据服务参数

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.6.1.png)](<textR7.6.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR7.6.png)](<textR7.6.png>)  

**数据服务配置分页与不配置分页在组件中运行时获取数据的方式**

组件是否支持分页 | 数据服务是否配置分页 | 获取数据方式   
---|---|---  
单行、列表、单选、复选、树形字典等不支持分页 | 数据服务配置分页 | 获取数据服务返回的第一页数据  
数据服务不配置分页 | 获取数据服务返回所有数据的前500条  
网格字典、参考录入支持分页 | 数据服务配置分页 | 获取数据服务返回的所有数据，按组件分页显示  
数据服务不配置分页 | 获取数据服务返回所有数据的前500条，组件设计器下设置分页属性隐藏  
  
  * 数据源-数据流

需要安装 [com.actionsoft.apps.dataflow（数据流）](<https://docs.awspaas.com/apps/com.actionsoft.apps.dataflow/index.html>)应用及对应的服务，在上层中使用与数据服务一致

**链接选项**

链接选项提供关联表单、关联子表、自定义URL三个链接选项，默认关联表单。在表单运行中，只有字段只读时有效，字段值变蓝色，支持链接打开对应表单页面，可以是流程表单，也可以是DW表单。如果链接的有多个相同的字段值，取最近的

  * **表单** 列表显示当前应用、当前应用的父应用及当前应用关联应用的表单模型
  * **关联** 关联字段，链接选项选主表单，默认该表单主表相同字段名，单选;选子表记录，默认该表单子表首个相同字段名，单选,也可以下拉单选不同的字段名；取值字段，默认当前$[字段名]，支持@公式
  * **表单状态** 链接表单的三种状态：常规、只读、可编辑，根据流程操作权限打开表单页面
  * **窗口位置** 链接表单打开表单的两种方式：新窗口、侧边栏

    * **侧边栏标题** 窗口位置选择侧边栏显示`侧边栏标题`项
    * **侧边栏宽度** 窗口位置选择侧边栏显示`侧边栏宽度`项，默认`适度`，还可以选择`宽`或者`窄`

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR8.png)](<textR8.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR8.1.gif)](<textR8.1.gif>)  

**控制属性**

  * **必填**

若字段设置非空且填写表单时值未输入，不允许保存

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR9.png)](<textR9.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR9.1.png)](<textR9.1.png>)  

> [人工任务属性-表单应用-操作权限](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/authority.html>)中配置`保存时不校验表单`，这时字段虽然配置了必填，但在运行时，表单上点保存按钮是不校验必填的

  * **只读**

运行时，表单对应字段不能编辑，是只读状态

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR9.2.png)](<textR9.2.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR9.3.png)](<textR9.3.png>)  
  * **清除**

仅在字段可编辑时刻有效，鼠标划动在输入框，在右侧显示清除的操作图标

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR9.4.png)](<textR9.4.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR9.5.png)](<textR9.5.png>)  

> 同时勾选必填、只读，运行时，必填不校验；同时勾选只读、清空时，清空操作不显示

**不允许重复录入**

默认不开启，开启后，相当于设置当前表单存储的唯一索引，保存表单设计器，会把设置的字段索引信息同步到对应的[BO存储-索引](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/>)中，从[BO存储-索引](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-bo-vue/table/>)中配置的索引信息也会同步到表单设计器的字段组件中来

  * **自定义提示语**

表单运行校验出现重复录入内容的提示信息

  * **组合字段不允许重复录入**

    * 开启`不允许重复录入`，才显示`组合字段不允许重复录入`属性
    * 默认不开启，开启后，至少包含2个或2个以上字段
    * 添加字段已在其他`组合字段不允许重复录入`中添加过，在添加时会提示`索引字段和其他索引字段交叉`，即同一字段不能重复添加
    * 删除组合字段，当前字段不能删除

配置 | 同步到BO存储-索引 | 运行  
---|---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR9.6.png)](<textR9.6.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR9.8.png)](<textR9.8.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR9.7.png)](<textR9.7.png>)  
**宽度** 设置输入框的宽度，根据表单设计区域大小合理的配置字段输入框宽度，提供了6种选项，默认是1  配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR10.png)](<textR10.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR10.1.png)](<textR10.1.png>)  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR10.2.png)](<textR10.2.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR10.3.png)](<textR10.3.png>)  
  
**提示文字**

仅在字段可编辑时刻有效。若字段从数据源读取值为NULL或空串时，在编辑区将自动显示该提示说明。输入要求支持$[字段名],例如$[ORDERTYPE],该字段名为当前字段所在BO表中字段名;还支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR11.png)](<textR11.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR11.1.png)](<textR11.1.png>)  
  
**帮助说明**

字段标题问题图标鼠标经过时，系统自动显示该提示说明，鼠标移走，提示内容消失。可帮助用户在填写数据时识别字段项含义，提高表单数据的正确性和工作效率。输入要求支持$[字段名],例如$[ORDERTYPE],该字段名为当前字段所在BO表中字段名;还支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)。

配置 | 运行  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR12.png)](<textR12.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textR12.1.png)](<textR12.1.png>)  
  
> 子表和移动表单不支持帮助说明，只有主表支持帮助说明

**字段规则**

只显示当前字段有关的规则，详细配置参见[表单规则](<../gz>)

> 当人工审核菜单未勾选是否校验表单项或表单应用未勾选保存时校验数据项时，办理流程或保存表单时，不执行以上字段属性校验