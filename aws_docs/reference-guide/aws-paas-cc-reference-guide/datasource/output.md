# 输出 · AWS PaaS文档中心

# 输出

配置Data Service输出与HTTP接口的返回参数的映射关系。

## 响应结果

响应结果是指调用HTTP接口后的返回信息。

### header

配置响应结果中的header参数。

### result

配置响应结果参数。

### sla

SLA是DS引擎执行的结果监控信息。

#### inTimes

输入参数构造耗时，单位毫秒

#### outTimes

输出数据构造耗时，单位毫秒

#### totalTimes

总耗时，单位毫秒

### 添加/修改/删除参数

在左侧响应结果，支持根节点 `header`、`result` 和 参数类型为Object的节点添加子节点 。

  * 根节点 `header`、`result`，光标移至`header`、`result`所在行点击右侧+按钮，打开添加参数窗口
  * Object类型参数，光标移至Object类型参数所在行右侧[![](http-input3.png)](<http-input3.png>)图标弹出列表选择`添加参数`，打开添加参数窗口

[![](http-output1.png)](<http-output1.png>)

[![](http-output2.png)](<http-output2.png>)

在添加参数窗口中填写相关属性后，点击保存按钮进行添加。

[![](http-output3.png)](<http-output3.png>)

项 | 说明  
---|---  
参数名 | 参数名，仅支持数字、字母、下划线、中划线。同一节点下的子节点参数名不允许重复  
标题 | 参数名标题，用于快速了解参数的意义  
类型 | 参数类型，详见[输入章节>参数类型](<input.html#a>)  
  
**修改**

光标移至要修改的参数所在行右侧[![](http-input3.png)](<http-input3.png>)图标弹出列表选择`修改参数`，打开修改参数窗口进行修改。

  * 当参数与请求参数已连线，配置映射关系后不允许修改参数类型
  * Object类型参数，已存在子节点时，不允许修改参数类型

[![](http-output4.png)](<http-output4.png>)

**删除**

光标移至要删除的参数所在行右侧[![](http-input3.png)](<http-input3.png>)图标弹出列表选择`删除参数`，进行删除。 删除参数时，如果其下有子节点将一并删除。

[![](http-output5.png)](<http-output5.png>)

### 参数类型

参见[输入章节>参数类型](<input.html#a>)

### 导入结构

导入结构是根据HTTP接口提供方提供的接口返回信息快速为DS模型创建响应结果和DataService输出参数并自动完成连线。点击右上角导入按钮打开导入结构窗口：

[![](http-output6.png)](<http-output6.png>)

导入的详细操作骤参见[输入章节>导入结构](<input.html#i>)

## Data Service输出

Data Service输出是 HTTP DS引擎执行后的返回参数配置。

### result

配置DS引擎执行后输出参数。一般建议参数名和参数类型与响应结果中result和header中配置的参数名和参数类型一致。

SLA是DS引擎执行的结果监控信息。

#### inTimes

输入参数构造耗时，单位毫秒

#### outTimes

输出数据构造耗时，单位毫秒

#### totalTimes

总耗时，单位毫秒

### 添加/修改/删除参数

配置DS引擎执行后的输出参数。一般建议参数名和参数类型与响应结果中result和header中配置的参数名和参数类型一致。

**添加**

在右侧Data Service输出，支持根节点`result` 和 参数类型为Object的节点添加子节点 。

  * 根节点 `result`，光标移至`result`所在行点击右侧+按钮，打开添加参数窗口
  * Object类型参数，光标移至Object类型参数所在行右侧[![](http-input3.png)](<http-input3.png>)图标弹出列表选择`添加参数`，打开添加参数窗口

[![](http-output9.png)](<http-output9.png>)

[![](http-output8.png)](<http-output8.png>)

在添加参数窗口中填写相关属性后，点击保存按钮进行添加。

[![](http-output10.png)](<http-output10.png>)

项 | 说明  
---|---  
参数名 | 参数名，仅支持数字、字母、下划线、中划线。同一节点下的子节点参数名不允许重复  
标题 | 参数名标题，用于快速了解参数的意义  
类型 | 参数类型，详见[输入章节>参数类型](<input.html#a>)  
数据清洗 | 对调用HTTP接口后返回的输出数据项进行处理，例如：将返回的0,1等状态值，显示为男，女，  
详细操作参见下方  
  
**修改**

同上 响应结果 修改参数。

**删除**

同上 响应结果 修改参数。

### 参数类型

参见[输入章节>参数类型](<input.html#a>)

### 数据清洗

数据清洗是指为输出数据项进行处理。例如：字典翻译（如1代表男，0代表女）、值转换（如将long的Timestamp值转换成日期）、复杂值处理（如脱敏手机号，只保留前后3位）、去重（如将无效记录剔除）等。

清洗方式支持`公式`和`Java程序`两种。

#### 公式

通过@公式对输出数据进行处理。

  1. 仅支持简单类@公式
  2. 取普通字段值$[result.object1.key1]
  3. 取数组字段值$[result.object1.array1[index].key1]

[![](http-output11.png)](<http-output11.png>)

#### Java程序

通过Java事件对输出数据进行处理。 事件需要实现`com.actionsoft.bpms.cc.ds.ValueFunction`接口。

示例：
    
    
    import java.text.SimpleDateFormat;
    import java.util.Date;
    
    import com.actionsoft.bpms.cc.ds.ValueFunction;
    import com.actionsoft.messaging.MessageContext;
    
    public class DataConvertDemo implements ValueFunction {
         /**
         * 示例：对时间戳进行格式化，并追加其他字段值进行一句话描述
         *
         * @param obj 当前字段值，对应类型的Java Object
         * @param ctx 当前引擎上下文，使用ctx.getProperty(JSONPath语法)获取其他字段值
         * @param indexes 数组场景时，表示当前值在数组中的下标，indexes下标值对应相应层级的数组，非数组场景时为null
         * @return 转换后的值
         */
        @Override
        public Object process(Object obj, MessageContext ctx, int... indexes) {
             Long createTime = (Long) obj; //1635418181000
             Date date = new Date(createTime);
             SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy年MM月dd日");
             String formatDate = dateFormat.format(date); //2021年10月28日18时49分
             String tagName = ctx.getProperty("result.data.moduleList[" + indexes[0] + "].pageList[" + indexes[1] + "].tagName", String.class); //炎黄盈动
             return "于" + formatDate + "创建标签:" + tagName; //于2021年10月28日创建标签:炎黄盈动
        }
    }
    

### 分页查询

当HTTP接口支持分页查询时，可开启分页查询，输出页签分页查询配置与输入页签中[分页查询](<input.html#p>)配置是同步的，即在一方开启后，另一方会自动同步开开启。开启后，在输出页签 Data Service输入自动增加 `page.total`参数节点,表示总记录数。

[![](http-output7.png)](<http-output7.png>)

## 连线

将响应结果与Data Service输出进行映射。未连线的参数不进行输出。

### 添加连线

参见[输入>添加连线](<input.html#l1>)。

### 删除连线

参见[输入>删除连线](<input.html#l2>)。

### 自动关联

参见[输入>自动关联](<input.html#l3>)。

### 取消关联

参见[输入>取消关联](<input.html#l4>)。

## 错误规则

由于服务端接口返回信息多样性，用户自定义返回错误规则。如果不配置， 响应状态码为200， result为ok时，errorcode为0，表示DS请求正常

[![](http-output13.png)](<http-output13.png>)

点击错误规则按钮，弹出对话框中自定义错误规则。

  * 错误条件，配置自定义表示出错的条件，默认为httpResponseCode 不等于200，用户可根据接口实际的返回值自定义。多个条件之间为或者的关系。
  * 错误码，自定义返回结果中errorcode的值。
  * 错误信息，自定义返回结果中msg的值。错误码和错误信息可以写一个固定的值，也可以选择一个输出参数，动态返回参数值

[![](http-output14.png)](<http-output14.png>)