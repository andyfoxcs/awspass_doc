# FORM_BEFORE_LOAD | AWS 流程事件开发参考指南

## FORM_BEFORE_LOAD

### 表单构建前被触发

项 | 说明  
---|---  
抽象类 | ExecuteListener  
接口 | ExecuteListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
在新版VUE表单引擎中，表单构建前事件会被调用两次：

  * 访问页面触发一次
  * 获取JSON结构时触发一次

通过`$FORM_SOURCE`参数来获取调用的场景
    
    
    String source = ctx.getParameterOfString("$FORM_SOURCE");
    if (source.equals("PAGE")) {
      // 页面触发调用
    }
    if (source.equals("JSON")) {
      // JSON结构触发调用
    }
    

通过`$FORM_ENGINE`参数来判断是新版本VUE引擎调用，还是jQuery引擎调用
    
    
    String engine = ctx.getParameterOfString("$FORM_ENGINE");
    if (engine.equals("VUE")) {
      // VUE引擎
    }
    if (engine.equals("jQuery")) {
      // jQuery引擎
    }
    

### 全局表单构建前事件

> 仅处理VUE表单的PAGE调用机制触发

通过给`AWS PaaS基础门户`创建参数，参数名：`commonFormBeforeLoadEventImpl`，注册一个类，格式：`应用ID:类全路径`，来实现给所有VUE表单的`PAGE`调用时触发

新版本表单页面中，提供了4个扩展点，用于扩展表单页面结构，注入外部js文件或者css样式

  * `HeadExtend1`：这个标签注入到<head>内部，<title>后面，<script>之前
  * `HeadExtend2`：这个标签注入到<head>内部，<script>后面，这个<script>是表单内容需要使用的初始变量
  * `BodyExtend1`：这个标签注入到<body>内部，紧邻<body>后面
  * `BodyExtend2`：这个标签注入到<body>内部，<body>结束标签的最前面

在表单构建前事件中，可以给这4个参数进行复制操作，引擎会将这些内容直接写入到页面中。
    
    
    String HeadExtend1 = "<link rel=\"stylesheet\" type=\"text/css\" href=\"../stylesheet.css\" title=\"Style\">";
    ctx.setParameter("HeadExtend1",HeadExtend1);
    

在表单加载前事件中，能够获取到BO表记录ID，可以查询业务数据，通过实现业务逻辑和用户结合，做出控制表单读、写，字段读、写的状态控制。
    
    
    //获得当前表单数据源的BO表Id
    String boId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BOID);
    //获得当前表单模型定义Id
    String formDefId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_FORMID);
    

### 常见触发场景

**1.用户打开表单时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/form_event/4.png)

### 场景：动态设置字段权限
    
    
    ctx.addFormReadOnlyPolicy("BO表名");//针对该表设置一个只读策略，该表全部字段有效
    ctx.addFormReadOnlyPolicy("BO表名", "字段名");//针对字段设置一个只读策略
    
    ctx.addFormEditablePolicy("BO表名");//针对该表设置一个可编辑策略，该表全部字段有效
    ctx.addFormEditablePolicy("BO表名", "字段名");//针对字段设置一个可编辑策略
    
    ctx.addFormHiddenPolicy("BO表名", "字段名");//针对字段设置一个隐藏策略
    ctx.addFormDisplayPolicy("BO表名", "字段名");//针对字段设置一个显示策略
    
    ctx.addGridHiddenPolicy("BO表名", "字段名");//程序指定子表列的BO字段隐藏（优先级最高）。仅适用于人工节点的表单权限场景
    ctx.addGridDisplayPolicy("BO表名", "字段名");//程序指定子表列的BO字段显示（优先级最高）。仅适用于人工节点的表单权限场景
    
    ctx.addFormNotNullPolicy("BO表名", "字段名");//针对字段设置一个必填策略
    ctx.addFormNullablePolicy("BO表名", "字段名");//针对字段设置一个可填策略
    
    ctx.setFieldTitlePolicy("BO表名", "字段名", "新标题");//程序指定BO字段标题（优先级最高）。仅适用于人工节点的表单权限场景
    
    ctx.addGridColumnPolicy("BO表名", List<String> gridColumnPolicy);//程序指定子表列头的字段信息（可控制显示顺序，优先级最高，高于子表列字段的显示隐藏策略）。仅适用于人工节点的表单权限场景
    

> 如果主表单被设置为只读，字段设置为可编辑，字段的优先级会高于表单的控制，这种情况下结果是：字段最终会可编辑。

**字段权限在AWS各种策略中得优先次序，后台规则**

级别 | 描述  
---|---  
第1优先级 | 表单加载前事件策略(字段级别)，判断是否存在字段级的设置，  
字段的设置，高于BO表级别的设置  
第2优先级 | 表单加载前事件策略(BO表级别)，判断安全策略中是否存在主表表名或者子表表名的策略，  
如果存在，设置了true，即只读，则每个字段都只读  
第3优先级 | 判断权限组的数据权限  
第4优先级 | 表单应用中字段分级权限设置只读权限的  
第5优先级 | 表单应用中设置了字段只读的  
第6优先级 | BO模型中字段是否允许编辑  
第7优先级 | 表单应用中表单（主表和子表）是否可修改  
  
**注意**

虽然代码的优先级高于表单应用中的配置，但是有一种场景不支持，即：  
**当表单应用中`主/子表`设置为不可编辑时，设置的该表可编辑，或者该表中某字段可编辑，将不起作用**

**前端`表单规则`在上述后台规则处理完后，表单加载后会根据规则进行判断处理**

### 场景：初始化表单BO数据
    
    
    //插入数据
    SDK.getBOAPI().create(boName, recordData, processInst, userContext)
    //更新数据
    SDK.getBOAPI().update(boName,recordData);
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.form.event;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.bpms.bpmn.engine.listener.ListenerConst;
    
    public class TestFormBeforeLoad extends ExecuteListener {
    
        public void execute(ProcessExecutionContext ctx) throws Exception {
            //参数获取
            //注意：除特殊说明外，下列参数仅在该事件中场景有效
            //记录ID
            String boId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BOID);
            //BO表记录，注意：该记录的数据如果被修改，将会体现到表单上，修改后不会直接持久化到数据库中
            BO boData = (BO) ctx.getParameter(ListenerConst.FORM_EVENT_PARAM_BODATA);
            // 可以为boData中的字段进行赋值
            if (boData == null) {
                boData = new BO();
                boData.set("PCNO", "123");
            } else {
                boData.set("PCNAME", "名称");
            }
            // 如果需要展示在表单上，需要调用如下代码。注意：此操作不会更新数据库中的数据
            // ctx.setParameter(ListenerConst.FORM_EVENT_PARAM_BODATA, boData);
    
            //表单ID
            String formId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_FORMID);
            //BO表名
            String boName = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
    
            ctx.addFormReadOnlyPolicy("BO表名");//针对该表设置一个只读策略，该表全部字段有效
            ctx.addFormReadOnlyPolicy("BO表名", "字段名");//针对字段设置一个只读策略
    
            ctx.addFormEditablePolicy("BO表名");//针对该表设置一个可编辑策略，该表全部字段有效
            ctx.addFormEditablePolicy("BO表名", "字段名");//针对字段设置一个可编辑策略
    
            ctx.addFormHiddenPolicy("BO表名", "字段名");//针对字段设置一个隐藏策略
            ctx.addFormDisplayPolicy("BO表名", "字段名");//针对字段设置一个显示策略
    
            ctx.addGridHiddenPolicy("BO表名", "字段名");//程序指定子表列的BO字段隐藏（优先级最高）。仅适用于人工节点的表单权限场景
            ctx.addGridDisplayPolicy("BO表名", "字段名");//程序指定子表列的BO字段显示（优先级最高）。仅适用于人工节点的表单权限场景
    
            ctx.addFormNotNullPolicy("BO表名", "字段名");//针对字段设置一个必填策略
            ctx.addFormNullablePolicy("BO表名", "字段名");//针对字段设置一个可填策略
    
            ctx.setFieldTitlePolicy("BO表名", "字段名", "新标题");//程序指定BO字段标题（优先级最高）。仅适用于人工节点的表单权限场景
    
            List<String> gridColumnPolicy = new ArrayList<String>();// 定义一个字符串类型的List
            gridColumnPolicy.add("字段1");//将需要显示的字段，按照实际需求的顺序放入List
            gridColumnPolicy.add("字段3");
            gridColumnPolicy.add("字段5");
            gridColumnPolicy.add("字段2");
            gridColumnPolicy.add("字段4");
            gridColumnPolicy.add("字段6");
            //调用以下策略，子表将按照该策略，展示子表列的展示
            //ctx.addGridColumnPolicy("BO表名", gridColumnPolicy);//程序指定子表列头的字段信息（可控制显示顺序，优先级最高，高于子表列字段的显示隐藏策略）。仅适用于人工节点的表单权限场景
    
        }
    }
    

### 场景：事件中改变一个字段的UI组件

事件中，可以改变一个字段UI配置，来改变表单界面上展示的内容。

**！！！注意！！！**

**代码中，一定要构造一个新的BOItemModel的模型，否则，直接修改Cache中获取的对象，会将原有模型修改掉。**
    
    
    //注意：一定要构造一个新的对象模型，否则会将原有的模型信息改掉
    BOItemModel newT1 = new BOItemModel();
    newT1.setModel(t1);
    

主要调用`setComponentId`方法和`setComponentSetting`方法

`setComponentId`的参数是一个常量，参考`UIConstant`类，注意常量名以NAME结尾的是名称，不是ID，**该ID仅 限平台注册的有效的AWSUI。

`setComponentSetting`的参数一个JSON字符串，可以通过一个已经的字段来获取这个配置信息，可新建一个临时字段，配置好UI的信息，调试代码将配置信息打印出来，然后获取配置内容，最后将该临时字段删除。

代码片段：
    
    
    BOItemModel combobox = BOCache.getInstance().getBOItemModelByItemName(boModel, "COMBOBOX");
    newT1.setComponentId(combobox.getComponentId());//必须设置
    newT1.setComponentSetting(combobox.getComponentSetting());//这里通过一个已经存在的UI组件来获取这个配置信息
    

### 开发示例
    
    
    package com.actionsoft.apps.poc.form.event;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.bpms.bo.design.cache.BOCache;
    import com.actionsoft.bpms.bo.design.model.BOItemModel;
    import com.actionsoft.bpms.bo.design.model.BOModel;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.bpms.bpmn.engine.listener.ListenerConst;
    
    public class TestFormBeforeLoadChangeUI extends ExecuteListener {
    
        public String getDescription() {
            return "表单加载前事件改变一个字段的UI组件配置";
        }
    
        public String getProvider() {
            return "Actionsoft";
        }
    
        public String getVersion() {
            return "1.0";
        }
    
        public void execute(ProcessExecutionContext ctx) throws Exception {
    
            String boName = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
            BOModel boModel = BOCache.getInstance().getModelByEntityName(boName);
    
            //获取当前BO表中T1这个字段的boItemModel对象，这里T1是假设是单行组件
            BOItemModel t1 = BOCache.getInstance().getBOItemModelByItemName(boModel, "T1");
            //注意：一定要构造一个新的对象模型，否则会将原有的模型信息改掉
            BOItemModel newT1 = new BOItemModel();
            newT1.setModel(t1);
    
            //获取当前BO表中COMBOBOX这个字段的boItemModel对象，这里COMBOBOX假设是列表组件
            BOItemModel combobox = BOCache.getInstance().getBOItemModelByItemName(boModel, "COMBOBOX");
            newT1.setComponentId(combobox.getComponentId());//必须设置
            newT1.setComponentSetting(combobox.getComponentSetting());//这里通过一个已经存在的UI组件来获取这个配置信息
    
            //将调整后的newT1这个对象放到一个list中，如果有多个字段按照上述方法分别处理后放入list，设置ctx的参数中
            List<BOItemModel> list = new ArrayList<>();
            list.add(newT1);
            ctx.setParameter(ListenerConst.FORM_EVENT_PARAM_CUSTOM_BOITEMMODEL, list);
        }
    }