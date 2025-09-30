# 输入 · AWS PaaS文档中心

# 输入

配置HTTP接口的请求参数，DS引擎在执行时会有一层转换，因此此处需要配置Data Service输入与HTTP接口请求参数的映射关系。

## Data Service输入

Data Service输入是DS引擎执行时读取的请求信息，参入名和参数类型建意与右则请求参数中一一对应。

### 添加/修改/删除参数

**添加**

在左侧Data Service输入，支持根节点 `parameters` 和 参数类型为Object的节点添加子节点 。

  * parameters，光标移至parameters所在行点击右侧+按钮，打开添加参数窗口
  * Object类型参数，光标移至Object类型参数所在行右侧[![](http-input3.png)](<http-input3.png>)图标弹出列表选择`添加参数`，打开添加参数窗口

[![](http-input1.png)](<http-input1.png>)

[![](http-input2.png)](<http-input2.png>)

在添加参数窗口中填写相关属性后，点击保存按钮进行添加。

[![](http-input4.png)](<http-input4.png>)

项 | 说明  
---|---  
参数名 | 参数名，仅支持数字、字母、下划线、中划线。同一节点下的子节点参数名不允许重复  
标题 | 参数名标题，用于快速了解参数的意义  
类型 | 参数类型，详见下方介绍  
来源 | 支持调用方给定和系统给定，详见下方介绍  
默认值 | 参数默认值。来源为系统给定时，必填  
  
**修改**

光标移至要修改的参数所在行右侧[![](http-input3.png)](<http-input3.png>)图标弹出列表选择`修改参数`，打开修改参数窗口进行修改。

  * 当参数与请求参数已连线，配置映射关系后Boolean类型不允许修改参数类型
  * Array Object和Object类型参数，修改参数类型后，子节点会自动消失
  * 字符串和数值的基础类型可以相互转换

[![](http-input5.png)](<http-input5.png>)

**删除**

光标移至要删除的参数所在行右侧[![](http-input3.png)](<http-input3.png>)图标弹出列表选择`删除参数`，进行删除。 删除参数时，如果其下有子节点将一并删除。

[![](http-input6.png)](<http-input6.png>)

### 参数类型

参数类型，支持数组、对象、字符串、数值、布尔。

  * 数组类型，在DS引擎执行时，可以传入多个数组。每个数组的类型支持对象、字符串、数值、布尔
  * 对象类型，在DS引擎执行时，可以传入有多个属性的一个对象。对象类型的参数可以添加子节点参数。
  * 字符串类型，在DS引擎执行时，只能传入字符串
  * 数值类型，支持Integer、Long、BigDecimal、Double
  * 布尔类型，布尔类型true 或 false

### 参数来源

  * `调用方给定`，该参数在DS引擎执行时，参数值由调用者传入。
  * `系统给定`，参数来源为系统给定时，默认值必填。指该参数在DS引擎执行时，不会使用由调用者传入的值，DS引擎自动以配置的默认值执行。

[![](http-input7.png)](<http-input7.png>)

> 参数类型为对象、数组>对象时，参数来源只能为调用方给定，且不能配置默认值。

#### 必填

必填是指在DS引擎执行时，如果判断该参数传入的值为NULL 或者没有为该参数传入值，则DS引擎直接抛出错误，不向接口发送请求。

[![](http-input9.png)](<http-input9.png>)

[![](http-input8.png)](<http-input8.png>)

[![](http-input33.png)](<http-input33.png>)

### 分页查询

当HTTP接口请求参数包含分页信息时，可在Data Service输入开启`支持分页查询`，开启后

  1. 会在输入页签`Data Service输入`列表增加page.size 和page.index参数，可直接与右侧请求参数列表中表示分页信息的参数进行连线映射
  2. 会在[输出](<output.html>)页签`Data Service输出`列表中增加result.page.total参数

[![](http-input10.png)](<http-input10.png>)

## 请求参数

请求参数是调用HTTP 接口时的入参参数。参数名和参数类型必须与接口提供方提供的入参要求完全一致。

### 添加/修改/删除参数

配置调用HTTP接口时的入参参数。入参参数支持header、pathParameters、queryParameters、bodyParameters。 有关header及不同paramters的相关含义、介绍、使用等如果不了解请线下自行学习。阅读本文档已默认您已对HTTP API相关知识有一定的知识背景。

[![](http-input15.png)](<http-input15.png>)

**添加**

在右侧请求参数，支持根节点 `header、pathParameters、queryParameters、bodyParameters` 和 参数类型为Object的节点添加子节点 。

  * 根节点，光标移至`header、pathParameters、queryParameters、bodyParameters`所在行点击右侧+按钮，打开添加参数窗口
  * Object类型参数，光标移至Object类型参数所在行右侧[![](http-input3.png)](<http-input3.png>)图标弹出列表选择`添加参数`，打开添加参数窗口

[![](http-input11.png)](<http-input11.png>)

[![](http-input12.png)](<http-input12.png>)

在添加参数窗口中填写相关属性后，点击保存按钮进行添加。

[![](http-input13.png)](<http-input13.png>)

项 | 说明  
---|---  
参数名 | 参数名，仅支持数字、字母、下划线、中划线。同一节点下的子节点参数名不允许重复  
标题 | 参数名标题，用于快速了解参数的意义  
类型 | 参数类型  
  
**修改**

同上 Data Service输入 修改参数。

**删除**

同上 Data Service输入 删除参数。

### header

调用HTTP接口时，需要传入的header参数。等同于在连接器中添加的header类型参数。header只能添加基础类型(字符、数值、布尔)参数。

[![](http-input14.png)](<http-input14.png>)

#### cookie

调用HTTP接口时如果需要cookie参数，则在此节点下添加相关参数。

### pathParameters

pathParameters仅支持基础类型参数。添加的pathParameters参数，必须在连接器中URL配置，格式为{pathParametersKey}。如下图：

[![](http-input15.png)](<http-input15.png>)

[![](http-input16.png)](<http-input16.png>)

### queryParameters

HTTP 接口请求参数中的query参数添加到queryParameters下面。

### bodyParameters

HTTP 接口请求参数中的body参数添加到bodyParameters下面。请求方法为GET和DELETE时不支持bodyParameters。

> HTTP接口的请求参数方式、类型等细节确定，需由接口提供方明确给出。

### 参数类型

同上 Data Service输入 参数类型。

### 导入结构

导入结构是根据HTTP接口提供方提供的接口请求入参信息快速为DS模型创建请求参数和DataService输入参数并自动完成连线。点击右上角导入按钮打开导入结构窗口：

[![](http-input18.png)](<http-input18.png>)

[![](http-input19.gif)](<http-input19.gif>)

[![](http-input20.gif)](<http-input20.gif>)

#### 导入类型

导入类型支持JSON、OAS2.0、OAS3.0三种。

  1. 导入相应类型时，要求从URL地址中请求到的结构或输入的信息与导入类型一致，否则点击下一步按钮获取结构预览会失败。
  2. 导入OAS2.0 和 OAS3.0类型，要求连接器URL中正确配置方法地址

[![](http-input21.png)](<http-input21.png>)

[![](http-input22.png)](<http-input22.png>)

[![](http-input23.png)](<http-input23.png>)

[![](http-input24.png)](<http-input24.png>)

#### 导入方式

导入方式支持URL地址和文本两种。

  1. URL地址，输入请求结构地址，点击请求结构获取相应内容并自动填充到文本框中 [![](http-input25.png)](<http-input25.png>)
  2. 文本，手动输入请求结构内容 [![](http-input26.png)](<http-input26.png>)

## 连线

将Data Service的输入与HTTP接口请求参数关联起来，DS引擎在执行时会自动通过映射关系将Data Service输入信息转换为HTTP接口的请求参数，进一步调用HTTP接口。 未进行连线的参数不会被DS引擎使用。

### 添加连线

按住鼠标不放，进行拖动进行连线。在进行连线时建意左右两侧连线参数类型保持一致。注意：Object、Array 类型不能连线 

[![](http-input27.gif)](<http-input27.gif>)

[![](http-input28.png)](<http-input28.png>)

### 删除连线

删除连线后，对应参数不会参与DS引擎执行，HTTP接口的对应请求参数字段不会有入参。

[![](http-input29.png)](<http-input29.png>)

### 自动关联

当左侧ataService输入和右侧请求参数两边参数名一致且参数类型支持映射时，可通过自动关联快速进行连线。

[![](http-input30.png)](<http-input30.png>)

### 取消关联

取消关联后，对应参数不会参与DS引擎执行，HTTP接口的对应请求参数字段不会有入参。

[![](http-input31.png)](<http-input31.png>)