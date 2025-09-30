# 代码示例 · AWS PaaS文档中心

## 代码示例

## TitleSeparatorTheme主类

**实现FormTheme接口**
    
    
    package com.actionsoft.apps.form.theme.sample;
    
    import java.util.Map;
    
    import com.actionsoft.apps.form.theme.sample.device.MobileThemeImpl;
    import com.actionsoft.apps.form.theme.sample.device.PcThemeImpl;
    import com.actionsoft.bpms.form.design.model.FormItemModel;
    import com.actionsoft.bpms.form.design.model.FormModel;
    import com.actionsoft.bpms.form.design.theme.FormTheme;
    
    /**
     * 带有标题分隔线的风格实现类
     *
     */
    public class TitleSeparatorTheme implements FormTheme {
    
        public TitleSeparatorTheme() {
    
        }
    
        /**
         * 获取PC表单内容，如果formItemModel为null则当前表单为主表，不为空则当前表单为主表
         *
         * @param themeAppId 当前主题的AppId
         * @param formModel 表单模型
         * @param formItemModel 表单中的表单项模型
         * @param params 扩展参数
         * @return
         */
        @Override
        public String getContent(String themeAppId, FormModel formModel, FormItemModel formItemModel, Map<String, String> params) {
            String formId = "";
            String formItemId = "";
            if (formModel != null) {
                formId = formModel.getId();
            }
            if (formItemModel != null) {
                formItemId = formItemModel.getId();
            }
            // pc表单可以设置不同的布局类型
            String layoutType = params.get("layoutType");
            String pcTemplateFileName = "pc.main.htm";
            PcThemeImpl pc = new PcThemeImpl(pcTemplateFileName, formId, formItemId);
            return pc.getContent(themeAppId, formModel, formItemModel, layoutType);
        }
    
        /**
         * 获取PC表单内容，如果formItemModel为null则当前表单为主表，不为空则当前表单为主表
         *
         * @param themeAppId 当前主题的AppId
         * @param formModel 表单模型
         * @param formItemModel 表单中的表单项模型
         * @param extParams 扩展参数
         * @return
         */
        public String getMobileContent(String themeAppId, FormModel formModel, FormItemModel formItemModel, Map<String, String> extParams) {
            String formId = "";
            String formItemId = "";
            if (formModel != null) {
                formId = formModel.getId();
            }
            if (formItemModel != null) {
                formItemId = formItemModel.getId();
            }
            String layoutType = extParams.get("layoutType");
            String pcTemplateFileName = "mobile.main.htm";
            MobileThemeImpl mobile = new MobileThemeImpl(pcTemplateFileName, formId, formItemId);
            return mobile.getContent(themeAppId, formModel, formItemModel, layoutType);
        }
    
    }
    

## 针对设备的内容实现

### PcThemeImpl类

**实现PcFormTheme抽象类**
    
    
    package com.actionsoft.apps.form.theme.sample.device;
    
    import java.util.Map;
    
    import com.actionsoft.bpms.bo.design.cache.BOCache;
    import com.actionsoft.bpms.bo.design.model.BOModel;
    import com.actionsoft.bpms.commons.htmlframework.HtmlPageTemplate;
    import com.actionsoft.bpms.form.design.cache.FormCache;
    import com.actionsoft.bpms.form.design.constant.LayoutConstant;
    import com.actionsoft.bpms.form.design.layout.LayoutFactory;
    import com.actionsoft.bpms.form.design.model.FormItemModel;
    import com.actionsoft.bpms.form.design.model.FormModel;
    import com.actionsoft.bpms.form.design.theme.device.pc.PcFormTheme;
    import com.actionsoft.bpms.form.design.util.ThemeUtil;
    
    /**
     * 风格具体内容实现类
     *
     */
    public class PcThemeImpl extends PcFormTheme {
        public PcThemeImpl(String templateFileName, String formId, String formItemId) {
            super(templateFileName, formId, formItemId);
        }
    
        /**
         * 获取Pc设备内容
         *
         * @param themeAppId
         * @param formModel
         * @param formItemModel
         * @param layoutType
         * @return
         */
        public String getContent(String themeAppId, FormModel formModel, FormItemModel formItemModel, String layoutType) {
            String formId = formModel.getId();
            String fromItemId = "";
            if (formItemModel != null) {
                fromItemId = formItemModel.getId();
            }
            // 表单名称
            String formName = "";
            String templateHtml = htmlTemplateName;
            // 主表
            if (formItemId.equals("")) {
                formName = formModel.getTitle();
            } else {
                // 子表
                FormItemModel item = FormCache.getInstance().getItemModel(formItemModel.getId());
                BOModel boModel = BOCache.getInstance().getModel(item.getBoModelId());
                if (boModel != null) {
                    formName = boModel.getTitle();
                }
                templateHtml = "pc.sub.htm";
    
            }
            // 获取基本的macroLibraries 包含标题背景色等信息
            Map<String, Object> macroLibraries = super.getPCBaseMacroLibraries(themeAppId, formName, layoutType);
    
            // 返回布局内容
            String content = ThemeUtil.getLayoutContent(PcThemeImpl.class, templateHtml, formId, fromItemId, layoutType);//这个方法，会自动调用下面对应四个重写的方法
            macroLibraries.put("CONTENT", content);
            return HtmlPageTemplate.formStyleMerge(themeAppId, templateHtml, macroLibraries);
        }
    
        /**
         * 重写单列
         */
        @Override
        public String getColumnOne(String formId, String fromItemId) {
            StringBuilder columnOneTable = new StringBuilder();
            FormItemModel itemModel = null;
            if (fromItemId.equals("")) {
                itemModel = FormCache.getInstance().getMastFormItemModel(formId);
            } else {
                itemModel = FormCache.getInstance().getItemModel(fromItemId);
            }
            if (itemModel != null) {
                BOModel boModel = BOCache.getInstance().getModel(itemModel.getBoModelId());
                List<BOItemModel> h = BOCache.getInstance().getBOItemList(boModel);
                for (BOItemModel model : h) {
                    columnOneTable.append(" <tr id='"+model.getId().replaceAll("-", "_")+"'>");
                    columnOneTable.append("<td class='awsui-ux-title'>");
                    columnOneTable.append("<label id='" + model.getName() + "Label'  for='" + model.getName() + "' class='aws-form-ux-label'>" +"[I18N#"+ model.getTitle()+"]" + "</label></td>");
                    columnOneTable.append("<td class='aws-form-ux-content'>" + FormDesignerConstant.FORM_PREFIX + model.getName() + "]</td>");
                    columnOneTable.append("</tr>");
                }
                if (fromItemId.equals("")) {
                    List<FormItemModel> subList = FormDesignUtil.getSubItemModelsByFromId(formId);// FormCache.getInstance().getSubFormItemList(formId);
                    List<FormItemModel> allSubFormList=FormCache.getInstance().getSubFormItemList(formId);
                    int index=1;
                    for (FormItemModel obj : allSubFormList) {
                        FormItemModel o=obj;
                        for (int i = 0; i < subList.size(); i++) {
                            columnOneTable.append(" <tr>");
                            FormItemModel subItemModel = subList.get(i);
                            if(o.getId().equals(subItemModel.getId())){
                                // 普通子表添加滚动条
                                String style = "";
                                columnOneTable.append("<td  colspan = '2' " + style + "  class = 'aws-form-ux-gridbg'><div class = 'aws-form-ux-grid' " + style + ">" + FormDesignerConstant.FORM_PREFIX + "Grid").append(index).append("]</div>");
                                columnOneTable.append("</td></tr>");
                                break;
                            }
                        }
                        index++;
                    }
                }
            } else {
                columnOneTable.append("没有定义表单项");
            }
            return columnOneTable.toString();
        }
    
        @Override
        public String getColumnTwo(String formId, String fromItemId) {
            //两列结构，可以参考一列的代码，主要目的是达到每行的tr中，出现4个td元素
            return "";
        }
    
        @Override
        public String getColumnThree(String formId, String fromItemId) {
            //三列结构，可以参考一列的代码，主要目的是达到每行的tr中，出现6个td元素
            return "";
        }
    
        @Override
        public String getColumnFour(String formId, String fromItemId) {
            //四列结构，可以参考一列的代码，主要目的是达到每行的tr中，出现8个td元素
            return "";
        }
    
    }
    

该类中实现了表单的具体内容，其中`getContent`方法可基本按照该示例代码编写。方法`ThemeUtil.getLayoutContent`会根据`FormThemePluginProfile`中注册的`layoutMap`参数分别调用`getColumnOne`，`getColumnOne`，`getColumnOne`，`getColumnOne`方法，示例代码中，是调用平台默认的生成对应列结构的代码，实际开发中，可根据自身的需求，实现该部分代码。 实现时，需要注意以下几点内容：

1.**DOM元素的ID**

在生成tr的时候，可将boItemModel的ID，设置到tr的id属性上，这样，在表单中的javascript代码，可以很方便的根据这个ID来控制表单元素

2.**字段标题**

字段标题使用如下的代码：
    
    
    <label id='XXXLabel'  for='XXX' class='aws-form-ux-label'>字段标题</label>
    

其中`XXX`是一个字段名称，**注意** ：`id`的格式是`字段名`加`Label`，这样，方便在javascript端处理这个UI组件的时候，方便找到对应的标题，进行控制

3.**字段标题国际化**

字段标题国际化的时候，可以使用`[I18N#XXXX]`的形式处理字段标题，`XXXX`是一个具体字段标题。

4.**子表**

子表在模版中使用`[GridX]`表示，其中`X`是一个编号，从`1`开始。**注意** ：在子表外面，需要增加一个div，这样，在表单上，当子表的宽度超过表单最大的宽度，表单引擎会自动将该子表进行左右滚动显示。
    
    
    <div class='aws-form-ux-grid'>[Grid1]</div>
    

### MobileThemeImpl类
    
    
    package com.actionsoft.apps.form.theme.sample.device;
    
    import java.util.List;
    import java.util.Map;
    
    import com.actionsoft.bpms.bo.design.cache.BOCache;
    import com.actionsoft.bpms.bo.design.model.BOItemModel;
    import com.actionsoft.bpms.bo.design.model.BOModel;
    import com.actionsoft.bpms.commons.htmlframework.HtmlPageTemplate;
    import com.actionsoft.bpms.form.design.cache.FormCache;
    import com.actionsoft.bpms.form.design.constant.FormDesignerConstant;
    import com.actionsoft.bpms.form.design.model.FormItemModel;
    import com.actionsoft.bpms.form.design.model.FormModel;
    import com.actionsoft.bpms.form.design.theme.device.mobile.MobileFormTheme;
    import com.actionsoft.bpms.form.design.util.FormTemplateUtil;
    import com.actionsoft.bpms.form.design.util.GenerateFormTemplateUtil;
    
    /**
     * 风格具体内容实现类
     *
     */
    public class MobileThemeImpl extends MobileFormTheme {
        public MobileThemeImpl(String templateFileName, String formId, String formItemId) {
            super(templateFileName, formId, formItemId);
        }
    
        /**
         * 获取手机设备内容
         *
         * @param themeAppId
         * @param formModel
         * @param formItemModel
         * @param layoutType
         * @return
         */
        public String getContent(String themeAppId, FormModel formModel, FormItemModel formItemModel, String layoutType) {
            // 表单名称
            String formName = "";
            String templateHtml = htmlTemplateName;
            // 主表
            if (formItemId.equals("")) {
                formName = formModel.getTitle();
            } else {
                // 子表
                FormItemModel item = FormCache.getInstance().getItemModel(formItemModel.getId());
                BOModel boModel = BOCache.getInstance().getModel(item.getBoModelId());
                if (boModel != null) {
                    formName = boModel.getTitle();
                }
                templateHtml = "mobile.sub.htm";
            }
            // 获取基本的macroLibraries 包含标题背景色等信息
            Map<String, Object> macroLibraries = super.getMobileBaseMacroLibraries(themeAppId, formName);
            // 返回布局内容
            String content = getColumnOneTable(formModel, formItemModel);
            macroLibraries.put("CONTENT", content);
            return HtmlPageTemplate.formStyleMerge(themeAppId, templateHtml, macroLibraries);
        }
    
        /**
         * 获取单行样式table样式(手机 标题在上字段在下)
         *
         * @param formId 表单Id
         * @return
         */
        public String getColumnOneTable(FormModel formModel, FormItemModel formItemModel) {
            String formId = formModel.getId();
            StringBuilder columnOneTable = new StringBuilder();
            GenerateFormTemplateUtil uti = new GenerateFormTemplateUtil();
            FormModel fromModel = FormCache.getInstance().getModel(formId);
            boolean isNull = uti.init(formId);
            if (!isNull) {
                return FormTemplateUtil.getHtmlFile(fromModel.getAppId(), null);
            }
            FormItemModel itmeModel = FormCache.getInstance().getMastFormItemModel(formId);
            if (formItemModel != null) {
                itmeModel = formItemModel;
            }
            if (itmeModel != null) {
                BOModel boModel = BOCache.getInstance().getModel(itmeModel.getBoModelId());
                List<BOItemModel> h = BOCache.getInstance().getBOItemList(boModel);
                for (BOItemModel model : h) {
                    columnOneTable.append("<tr>");
                    columnOneTable.append("<td class='awsui-ux-title' style='padding-left:0px;'> ");
                    columnOneTable.append("<label id='" + model.getName() + "Label' for='" + model.getName() + "'>" + model.getTitle() + "</label></td>");
                    columnOneTable.append("</tr>");
                    columnOneTable.append("<tr>");
                    columnOneTable.append("<td>" + FormDesignerConstant.FORM_PREFIX + model.getName() + "]</td>");
                    columnOneTable.append("</tr>");
                }
                List<FormItemModel> subList = FormCache.getInstance().getSubFormItemList(formId);
                for (int i = 0; i < subList.size(); i++) {
                    columnOneTable.append("<tr class = 'tr1'><td   colspan = '4' class = 'aws-form-ux-gridbg '>" + FormDesignerConstant.FORM_PREFIX + "Grid").append(i + 1).append("]</td></tr>");
                }
            } else {
                columnOneTable.append("没有定义主表单");
            }
            return columnOneTable.toString();
        }
    
    }
    

## 表单模版（母版模版）

实现FormTheme接口的两个方法中，出现了`pc.main.htm`或者`mobile.main.htm`这样的模版，该模版作为表单的母板存在，生成的表单内容根据该模板的主题结构生成。

### pc.main.htm
    
    
    <!DOCTYPE html>
    <html>
        <head>
            <title>[#title]</title>
            <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
            <!--公共的js和css start-->
            [#AWSImport]
            [#AWSUIImport]
            <!--公共的js和css end-->
            <!--配色方案-->
            [#SCHEMECSS]
        </head>
        <body>
            <form id='frmMain' name='frmMain' method="post" >
                <div id='aws-form-container' class="aws-form-ux-container">
                    <table  id='aws-form-maintable' class="aws-form-ux-maintable" align="center" border=0 cellpadding=0 cellspacing=0 >
                        <tr id='aws-form-titlebg' class='aws-form-ux-titlebg'>
                            <!--若自定义模板title的 id -->
                            <td id='aws-form-title' class='aws-form-ux-header'> [#FORM:TITLE] </td>
                        </tr>
                        <tr>
                            <!-- 标题分隔线 -->
                            <td> <hr/> </td>
                        </tr>
    
                        <!--每个模板必须含有aws-form-ux-formcontent样式  否则无法应用配色风格-->
                        <tr class='aws-form-ux-formcontent' id='aws-form-formcontent' >
                            <td>
                            <table  width='100%' align='center' style='margin: 0px 0px;'>
                                <tr>
                                    <td>
                                    <table id='table_container' class="awsui-ux" width='100%' cellspacing='0' border=1 cellpadding='0'>
                                        [#COLGROUP]
                                        <tbody>
                                            [#CONTENT]
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr id='aws-form-bottom'>
                            <td class="aws-form-ux-bottom aws-form-ux-actionsoft">[#Actionsoft]</td>
                        </tr>
                    </table>
                </div>
            </form>
        </body>
    </html>
    

#### **特定标签**

**这些标签都是必须在表单中存在的，否则表单不能正常运行在AWS环境中**

  * **[#title]** 表单页面的标题，用于浏览器的展示
  * **[#AWSImport]** 表单用于引入必须的javascript文件和css文件
  * **[#AWSUIImport]** 表单用于引入UI组件使用的javascript文件和css文件
  * **[#SCHEMECSS]** 配色方案引入的css
  * **[#FORM:TITLE]** 表单的主标题
  * **[#COLGROUP]** 当表单多列的时候，列的配置信息，参考html中colgroup语法
  * **[#CONTENT]** 表单具体的展示内容
  * **[#Actionsoft]** AWS表单运行时刻的必要的参数，特定功能等

### pc.sub.htm

该模板用于子表模版中，唯一的区别是增加了`[#ToolBar]`标签，该标签在子表中，会被解析为一个带有`保存`，`新建`等操作的工具栏。
    
    
    <!DOCTYPE html>
    <html>
        <head>
            <title>[#title]</title>
            <!--字段背景风格App模板-->
            <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
            <!--公共的js和css start-->
            [#AWSImport]
            [#AWSUIImport]
            <!--公共的js和css end-->
            <!--配色方案-->
            [#SCHEMECSS]
        </head>
        <body style="overflow: hidden;">
            <form id='frmMain' name='frmMain' method="post" action="./w" >
                <div class="awsui-toolbar">
                    [#ToolBar]
                </div>
                <div id='aws-form-container' class="aws-form-ux-container">
                    <div id="FormGridRowPage" style="overflow: auto;">
                        <table  id='aws-form-maintable' class="awsui-ux aws-form-ux-maintable" align="center" border=1 cellpadding=0 cellspacing=0 >
                            <!--每个模板必须含有 aws-form-titlebg 和 title样式 否则无法应用配色风格-->
                            <tr id='aws-form-titlebg' class='aws-form-ux-titlebg'>
                                <!--若自定义模板title的 id -->
                                <td id='aws-form-title' class='aws-form-ux-header'> [#FORM:TITLE] </td>
                            </tr>
                            <tr>
                                <!-- 分隔线 -->
                                <td> <hr/> </td>
                            </tr>
                            <tr class="aws-form-ux-formcontent" id='aws-form-formcontent'>
                                <td>
                                <table  width='100%' align='center'>
                                    <tr>
                                        <td align='center'>
                                        <table id='table_container' class="awsui-ux table-striped" width='100%' cellspacing='0' border="1" cellpadding='0'>
                                            [#COLGROUP]
                                            <tbody>
                                                [#CONTENT]
                                            </tbody>
                                        </table></td>
                                    </tr>
                                </table></td>
                            </tr>
                            <tr class="aws-form-bottom">
                                <td class="aws-form-ux-bottom aws-form-ux-actionsoft">[#Actionsoft]</td>
                            </tr>
                        </table>
                    </div>
                </div>
            </form>
        </body>
    </html>
    

### mobile.main.htm

该模板用于手机模版中，在该模版中，可以引入Mobile样式框架
    
    
    <!DOCTYPE html>
    <html>
        <head>
            <title>[#title]-手机表单</title>
            <!--字段背景风格App模板-->
            <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
            <!--公共的js和css start-->
            [#AWSImport]
            [#AWSUIImport]
            <!--公共的js和css end-->
            <!--jquery_Mobile-->
            <script src='../commons/plug-in/jqueryMobile/jquery.mobile-1.4.3.min.js'></script>
            <link type='text/css' rel='stylesheet'  href='../commons/plug-in/jqueryMobile/jquery.mobile-1.4.3.css'>
            <link type='text/css' rel='stylesheet' href='../apps/_bpm.platform/css/model/aws-form-ux.css' >
            <!--jquery_Mobile-->
            <!--配色方案-->
            [#SCHEMECSS]
        </head>
        <body>
            <form id='frmMain' name='frmMain' method="post" >
                <div id='aws-form-container' class="aws-form-ux-container">
                    <table  id='aws-form-maintable' class="awsui-ux aws-form-ux-maintable" style="table-layout: auto;" align="center" border=0 cellpadding=0 cellspacing=0 >
                        <!--每个模板必须含有 aws-form-titlebg 和 title样式 否则无法应用配色风格-->
                        <tr id='aws-form-titlebg' class='aws-form-ux-titlebg'>
                            <!--若自定义模板title的 id -->
                            <td id='aws-form-title' class='aws-form-ux-header'> [#FORM:TITLE] </td>
                        </tr>
                        <tr>
                            <!-- 分隔线 -->
                            <td> <hr/> </td>
                        </tr>
                        <tr class="aws-form-ux-formcontent" id='aws-form-formcontent'>
                            <td>
                            <table  width='100%' align='center'>
                                <tr>
                                    <td>
                                    <table id='table_container'  class="awsui-ux table-striped" style="padding: 0px;" width='100%' cellspacing='0' cellpadding='0'>
                                        <tbody>
                                            [#CONTENT]
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr class="aws-form-bottom">
                            <td class="aws-form-ux-bottom aws-form-ux-actionsoft">[#Actionsoft]</td>
                        </tr>
                    </table>
                    </div>
            </form>
        </body>
    </html>
    

### mobile.sub.htm

该模板用于手机表单的子表中
    
    
    <!DOCTYPE html>
    <html>
        <head>
            <title>[#title]-手机子表单</title>
            <!--字段背景风格App模板-->
            <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
            <!--公共的js和css start-->
            [#AWSImport]
            [#AWSUIImport]
            <!--公共的js和css end-->
            <!--配色方案-->
            [#SCHEMECSS]
        </head>
        <body style="overflow: hidden;">
            <form id='frmMain' name='frmMain' method="post" action="./w" >
                <div class="awsui-toolbar">
                    [#ToolBar]
                </div>
                <div id='aws-form-container' class="aws-form-ux-container">
                    <div id="FormGridRowPage" style="overflow: auto;">
                        <table  id='aws-form-maintable' class="awsui-ux aws-form-ux-maintable" align="center" border=0 cellpadding=0 cellspacing=0 >
                            <!--每个模板必须含有 aws-form-titlebg 和 title样式 否则无法应用配色风格-->
                            <tr id='aws-form-titlebg' class='aws-form-ux-titlebg'>
                                <!--若自定义模板title的 id -->
                                <td id='aws-form-title' class='aws-form-ux-header'> [#FORM:TITLE] </td>
                            </tr>
                            <tr>
                                <!-- 分隔线 -->
                                <td> <hr/> </td>
                            </tr>
                            <tr class="aws-form-ux-formcontent" id='aws-form-formcontent'>
                                <td>
                                <table  width='100%' align='center'>
                                    <tr>
                                        <td align='center'>
                                        <table  id='table_container' class="awsui-ux table-striped" width='100%' cellspacing='0' cellpadding='0'>
                                            [#COLGROUP]
                                            <tbody>
                                                [#CONTENT]
                                            </tbody>
                                        </table></td>
                                    </tr>
                                </table></td>
                            </tr>
                            <tr class="aws-form-bottom">
                                <td class="aws-form-ux-bottom aws-form-ux-actionsoft">[#Actionsoft]</td>
                            </tr>
                        </table>
                    </div>
                </div>
            </form>
        </body>
    </html>