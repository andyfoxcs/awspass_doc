# 代码示例 · AWS PaaS文档中心

## 代码示例

**UI组件中使用JSON组件是FastJSON，开发中注意包的引用**

### 构造方法

> com.actionsoft.apps.formui.sample.FormUISampleImpl#FormUISampleImpl
    
    
    public FormUISampleImpl(UIContext context) {
        super(context);
    }
    

### getInitScript

> com.actionsoft.apps.formui.sample.FormUISampleImpl#getInitScript

该方法返回一个JavaScript片段代码，该代码会由表单引擎调用，完成对组件的初始化动作

**注意** 返回的js片段需要自行定义，可以存在于表单中，也可以定义到`getCustomUIJoinScript`方法引入的js文件中
    
    
    public String getInitScript(UIContext context, boolean readOnly) {
        BOItemModel boItemModel = context.getBoItemModel();
        JSONObject configJson = super.getConfigJson(boItemModel, context);
        return "initUI('" + boItemModel.getName() + "'," + SDK.getRuleAPI().executeAtScript(configJson.toString(), context) + "))";
    }
    

### getUI

> com.actionsoft.apps.formui.sample.FormUISampleImpl#getUI

示例是一个简单的文本框，如果实际场景是一个复杂的UI组件，可根据实际情况结合getInitScript方法中的初始化JavaScript代码处理
    
    
    public String getUI(UIContext context, boolean readOnly) {
        StringBuilder html = new StringBuilder();
        BOItemModel boItemModel = context.getBoItemModel();
        String boItemName = boItemModel.getName();
        //
        JSONObject configJson = getConfigJson(boItemModel, context);
        // 获取流程实例ID
        ProcessInstance processInst = context.getProcessInstance();
        // 获取任务实例ID
        TaskInstance taskInst = context.getTaskInstance();
        if (!readonly) {
            if (!boItemModel.isNullable()) {
                html.append("<span class='required'>");
            }
            html.append("<input name='" + boItemModel.getName() + "' id='" + boItemModel.getName() + "' type='text' value='" + context.getValue() + "' > ");
        } else {
            html.append(getHiddenUI(context)).append(Html.escape(context.getValue()));
        }
        if (!readonly && !boItemModel.isNullable()) {
            html.append("</span>");
        }
        return html.toString();
    }
    

### getValidateScript

> com.actionsoft.apps.formui.sample.FormUISampleImpl#getValidateScript

该方法为校验组件的方法，如是否必填，值的格式等，可根据实际情况选择是否处理，如果不校验，则返回`null`或者`""`

**注意** 返回的js片段需要自行定义，可以存在于表单中，也可以定义到`getCustomUIJoinScript`方法引入的js文件中
    
    
    public String getValidateScript(UIContext context, boolean readonly) {
        BOItemModel boItemModel = context.getBoItemModel();
        JSONObject configJson = super.getConfigJson(boItemModel, context);
        String boName = "";
        BOModel model = BOCache.getInstance().getModel(boItemModel.getBoModelId());
        if (model != null) {
            boName = model.getName();
        }
        return "validateSample('" + boName + "','" + boItemModel.getName() + "','" + boItemModel.getTitle() + "'," + configJson.toString() + ", cellvalue, record)\n";
    }
    

### getCustomUIJoinScript

> com.actionsoft.apps.formui.sample.FormUISampleImpl#getCustomUIJoinScript

该方法用于引入组件需要的JavaScript文件和CSS文件，表单引擎已经处理，多个相同组件时，不会重复引用，如果没有可不重写该方法 以下组件是以电子印章组件为例，引入cachet相关的css和js文件。
    
    
        public String getCustomUIJoinScript(UIContext context) {
            StringBuilder html = new StringBuilder();
            html.append("<link rel='stylesheet' href='../apps/com.actionsoft.apps.formui.cachet/css/ui/com.actionsoft.apps.formui.cachet.ui.css'>\n");
            html.append("<script type='text/javascript' src='../apps/com.actionsoft.apps.formui.cachet/js/com.actionsoft.apps.formui.cachet.form.run.js'></script>\n");
            return html.toString();
        }
    

### getGridDisplayHtmlValue

> com.actionsoft.apps.formui.sample.FormUISampleImpl#getGridDisplayHtmlValue

**注意**

该方法是一个标准的实现方式，在父类中已经定了该方法并实现如下。如果你的UI组件中，不需要特殊显示，则不需要重写该方法
    
    
    @Override
    public String getGridDisplayHtmlValue(UIContext context, boolean readonly, String eventStart, String eventEnd) {
        StringBuilder columnHtml = new StringBuilder();
        String currentData = context.getValue();
        columnHtml.append(eventStart);
        currentData = new UtilString(currentData).replace("__eol__", "<br>");
        currentData = new UtilString(currentData).replace("\n", "<br>");
        columnHtml.append(currentData);
        columnHtml.append(eventEnd);
        return columnHtml.toString();
    }
    

### getEditGridDisplayValue

> com.actionsoft.bpms.ui.base.AbstractUIComponent#getEditGridDisplayValue

该方法用于Ajax子表中显示规则的处理

**注意**

该方法不是一个必须重写的方法

该方法通常用于UI组件采用K/V机制存储的数据，在该方法中，可以通过formEngineContext参数，获取上下文对象，然后进行相关的值转换。

下面代码是平台中地址簿的Ajax子表的实现，仅供说明formEngineContext的使用方法，具体代码请自行实现。
    
    
    @Override
    public String getEditGridDisplayValue(FormEngineContext formEngineContext) {
        String value = getContext().getValue();
        BOItemModel boItemModel = getContext().getBoItemModel();
        JSONObject config = super.getConfigJson(boItemModel, getContext());
        AddressBookWeb web = new AddressBookWeb(formEngineContext.getUserContext());
        String html = web.getGridValue(boItemModel.getName(), value, config);
        return html;
    }
    

### getEditGridUIEditorFn

> com.actionsoft.apps.formui.sample.FormUISampleImpl#getEditGridUIEditorFn

该方法用于UI组件需要在Ajax子表中展示时
    
    
    @Override
    public String getEditGridUIEditorFn(UIContext context, boolean readonly) {
        BOItemModel boItemModel = context.getBoItemModel();
        BOModel boModel = BOCache.getInstance().getModel(boItemModel.getBoModelId());
        //函数的参数表
        String jsString = Html.toCallJS("sampleEditor", new Object[] { Html.toJSObj("ui"), boModel.getName(), boItemModel.getName(), boItemModel.getComponentId(), Html.toJSObj(super.getConfigJson(boItemModel, context).toString()), SDK.getRuleAPI().executeAtScript(boItemModel.getComponentExtendCode(), context), SDK.getRuleAPI().executeAtScript(boItemModel.getTooltip(), context) });
        return jsString;
    }
    

> JavaScript代码
    
    
    //ui，在JS中是一个对象
    //BO表名
    //BO字段名
    //UI组件的ID信息
    //组件的配置信息
    //组件的扩展代码
    //组件的帮助说明信息
    function sampleEditor(ui, boDefName, boItemDefName, uiId, uiSetting, componentExtendCode, tooltip) {
        var $cell = ui.$cell, data = ui.data, rowIndx = ui.rowIndxPage, colIndx = ui.colIndx;
        var record = AWSGrid.getGrid(boDefName).awsGrid("getRowData", rowIndx);
        var dataCell = $.trim(data[rowIndx][colIndx]);
        if (tooltip == undefined) {
            tooltip = "";
        }
        $cell.append("<input title='" + tooltip + "' "+componentExtendCode+" style='padding:0px;width:100%;margin:0px !important;height: 23px;' id='Address_" + boItemDefName + "' class='aws-grid-editor-default' type='text' value='" + dataCell + "'/>");
        //input形成后，再进行后续的渲染处理即可
    }
    

### getEditGridUIRenderFn

> com.actionsoft.apps.formui.sample.FormUISampleImpl#getEditGridUIRenderFn

该方法用于UI组件需要在Ajax子表中展示时
    
    
    @Override
    public String getEditGridUIRenderFn(UIContext context, boolean readonly) {
        BOItemModel boItemModel = context.getBoItemModel();
        BOModel boModel = BOCache.getInstance().getModel(boItemModel.getBoModelId());
        String js = Html.toCallJS("sampleRender", new Object[] { Html.toJSObj("ui"), boModel.getName(), boItemModel.getName(), boItemModel.getComponentId(), boItemModel.getId(), readonly, Html.toJSObj(super.getConfigJson(boItemModel, context).toString()) });
        return js;
    }
    

> JavaScript代码
    
    
    //ui 在JS中是一个对象
    //boDefName BO表名
    //boItemDefName BO字段名
    //uiId UI组件的ID信息
    //uiSetting 组件的配置信息
    function sampleRender(ui, boDefName, boItemDefName, uiId, uiSetting) {
        var record = ui.rowData;
        var dataIndx = ui.dataIndx;
        var value = record[dataIndx];
        //根据实际需求，返回要展示的内容
        return "<span id='" + boItemDefName + "' name='" + boItemDefName + "'>" + value + "</span>";
    }
    

### getEditGridUIGetEditCellDataFn

> com.actionsoft.apps.formui.sample.FormUISampleImpl#getEditGridUIGetEditCellDataFn

该方法用于UI组件需要在Ajax子表中展示时
    
    
    @Override
    public String getEditGridUIGetEditCellDataFn(UIContext context, boolean readonly) {
        BOItemModel boItemModel = context.getBoItemModel();
        BOModel boModel = BOCache.getInstance().getModel(boItemModel.getBoModelId());
        //
        String jsString = Html.toCallJS("sampleGetEditCellData", new Object[] { Html.toJSObj("ui"), boModel.getName(), boItemModel.getName(), boItemModel.getComponentId(), Html.toJSObj(super.getConfigJson(boItemModel, context).toString()) });
        return jsString;
    }
    

> JavaScript代码
    
    
    //ui 在JS中是一个对象
    //boDefName BO表名
    //boItemDefName BO字段名
    //uiId UI组件的ID信息
    //uiSetting 组件的配置信息
    function sampleGetEditCellData(ui, boDefName, boItemDefName, uiId, uiSetting) {
        var $cell = ui.$cell;
        //$cell.children()中包括editor方法处理过的input，根据实际需求，找到该input，取值，并返回
        return $cell.children().find("input[type=text]").val();
    }
    

### getConfigWebPage

> com.actionsoft.apps.formui.sample.FormUISampleImpl#getConfigWebPage

该方法是用于UI组件的配置界面。
    
    
    public String getConfigWebPage(UIContext context) {
        BOItemModel boItemModel = context.getBoItemModel();
        String componentSetting = boItemModel == null ? "0" : boItemModel.getComponentSetting();
        Map<String, Object> macroLibraries = new HashMap<String, Object>();
        macroLibraries.put("sid", context.getUserContext().getSessionId());
        macroLibraries.put("uid", context.getUserContext().getUID());
        macroLibraries.put("componentSetting", componentSetting);//必须放入，用于界面初始化使用
        //merge方法的第一个参数是AppId
        //第二个参数是当前组件的配置界面对应的HTML模版
        //第三个参数是HTML里面的待替换的标签库，这些标签可根据具体内容自行定义，不限于上面的这些
        return HtmlPageTemplate.merge("%AppId%", "com.actionsoft.apps.formui.sample.config.htm", macroLibraries);
    }
    

通过访问`AWS->Console->业务建模->业务模型库`，打开一个存储模型，点击其中一行`UI组件`列的->`->` 配置界面将会展示到下图红框中的位置 [![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/form_ui_config.png)](<form_ui_config.png>)

> 配置界面HTML模版
    
    
    <!DOCTYPE html>
    <html>
        <head>
            <title>UI组件单行</title>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <script type="text/javascript">
                //全局变量
                var sessionId = '<#sid>';
                var componentSetting=<#componentSetting>;//如果配置信息正确存储，这个变量就是一个JSON对象
            </script>
            <link rel="stylesheet" href="../commons/css/awsui.css"><!--平台公共的样式文件-->
            <!--引入需要的样式表文件-->
            <link rel="stylesheet" href="../apps/_bpm.platform/ui/common/text/css/console.m.ui.design.common.text.css">
            <script type="text/javascript" src="../commons/js/jquery/scripts/jquery.js"></script><!--平台公共的JS文件-->
            <script type="text/javascript" src="../commons/js/awsui.js"></script><!--平台公共的JS文件-->
            <!--UI组件公共的JS文件-->
            <script type="text/javascript" src="../apps/_bpm.platform/ui/console.m.ui.design.util.js"></script>
            <!--这里需要引入一个javascript文件或者定一个-->
            <script>
                //...配置相关的js代码，具体函数参考下面“配置界面HTML模版中的JavaScript代码”一节
            </script>
            <style>
                td {
                    padding: 2px 0px;height: 27px;
                }
            </style>
        </head>
        <!--根据组件的需要，设计表单内容，此处示例是一个空的内容-->
        <body style="overflow:hidden;">
            <form id='frmMain' name='frmMain'>
                <table style="border:0px;width:100%;" cellpadding="0" cellspacing="0">
                    </tbody>
                </table>
            </form>
            <input type="hidden" id='sid' name='sid' value='<#sid>' />
        </body>
    </html>
    

> 配置界面HTML模版中的JavaScript代码

注意：**必须定义`UIConfig.getConfigJson()`函数**，否则，在BO表建模时，配置UI组件的过程中，不能顺利的保存组件的配置信息

下面的javascript内容，需要定义到上面的模版中，或者定一个到js文件中引入到上面的模版中
    
    
    //定义如下结构
    var UIConfig = {
        //获取UI组件的配置信息，由UI组件设置界面会调用
        //该函数必须实现
        getConfigJson : function() {
            var data = {};
            data.config1 = "";//具体配置项自行定义
            data.config2 = "";//具体配置项自行定义
            //返回组件的配置的json格式，json数据根据需求进行定义
            return awsui.encode(data);//一个字符串形式的json数据
        },
        //由于HTML页面的数据并不在Java代码中处理，需要该函数将组件的配置信息初始化到界面上
        initConfigJson : function() {
            //根据实际需求处理表单内容
        }
    }
    
    //页面准备好后的代码处理
    $(document).ready(function() {
        //调用初始化的方法，用于组件的配置信息回显到配置界面上
        UIConfig.initConfigJson();
        //后续的逻辑根据实际需求处理
        //...
    });
    

上述js文件中，`UIConfig.getConfigJson()`函数中，根据自己的配置属性，形成一个json结构，放入变量`data`中， 该配置最终会存储到`BOItemModel`模型中的`componentSetting`属性中，使用`getComponentSetting()`方法获取

> 配置信息JSON结构

运行时刻的Java代码中获取的JSON结构
    
    
    {
        "boDefId": "0c64cad8-3068-4106-ba5f-c5701ee0d163",//BO表唯一标识
        "boItemId": "fd7c270d-a171-4ea4-8416-1657430da9fc",//字段唯一标识
        "columnType": "TEXT",//字段类型，参考BOItemConst.MAP_TYPE_*
        "isNullable": true,//是否允许空，true--允许空，false--不允许空
        "length": "8",//整数位长度
        "decimalDigits": 2,//小数位长度
        "lengthStr": "10,2",//字段的长度设置
        ...//其余的属性都是自定义的属性
    }
    

### AbstractUIComponent常用方法

> getConfigJson(BOItemModel boItemModel, UIContext context)

UI组件实现类中，使用该方法获取组件的配置信息，该配置包含了上述公共的配置，如是否必填，字段类型，长度，是否包含小数 如果需要优化这些配置，可以在自己组件中重写该方法，建议调用调用父类的方法获取一个JSONObject对象，然后再增加更多的配置信息。父类中的方法，已经对配置中的@公式进行了解析。
    
    
    JSONObject uiConfig = super.getConfigJson(boItemModel, context);
    

> getHiddenUI(UIContext context, String value)

返回一个指定value的hidden表单域的HTML片段

> getHiddenUI(UIContext context)

根据字段本身的值，返回一个hidden表单域的HTML片段

> getReadonlyUI(UIContext context, String value)

UI组件只读时，通常是一个hidden域，然后展示一下该字段值，该方法返回一个指定value的hidden表单域加字段值的组合HTML片段

> getReadonlyUI(UIContext context)

UI组件只读时，通常是一个hidden域，然后展示一下该字段值，根据字段本身的值，返回一个hidden表单域加字段值的组合HTML片段

### 将SampleWeb注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            /**
             * FormUIPluginProfile参数说明
             * @param groupName 分类
             * @param id UI名，建议英文
             * @param clazz 实现类
             * @param title 简要说明
             * @param desc 详细说明
             * @param isSetting 是否有组件专有属性
             * @param isSetColumnWidth 是否允许设置显示宽度属性（表格列）
             * @param isSetWidth 是否允许设置可编辑时宽度属性
             * @param isSetHeight 是否允许设置可编辑时高度属性
             * @param isSetExtendCode 是否允许设置扩展代码属性
             * @param isSetAltText 是否允许设置鼠标提醒属性
             * @param isSupportGrid 是否支持子表
             * @param isSupportMobile 是否支持手机表单
             * @param isSetDisplayRule 是否支持显示规则属性
             */
            list.add(new FormUIPluginProfile("常规组件", "UI.Sample", FormUISampleImpl.class.getName(), "简单的UI示例", "", true, true, true, false, true, true, true, true, true));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`中的`监听器 > 插件`或AWS Developer中配置该App的`扩展插件`内容为`com.actionsoft.apps.formui.sample.plugin.Plugins`

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`FormUI组件`，展开后，是UI组件的名称，鼠标滑过该名称展示UI组件的实现类，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/form_ui-1.png)](<form_ui-1.png>)

UI组件在表单运行的效果如下

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/form_ui-2.png)](<form_ui-2.png>)