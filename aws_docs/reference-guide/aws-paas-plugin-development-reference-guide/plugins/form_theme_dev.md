# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现`FormTheme`接口的方法
  2. 用`FormThemePluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### FormTheme接口

开发者可实现这个接口完成你的ADD-ON应用入口界面。

> com.actionsoft.bpms.form.design.theme.FormTheme
    
    
    /**
     * 表单风格接口
     *
     */
    public interface FormTheme {
        /**
         * PC端风格内容
         *
         * @param themeAppId 风格AppId
         * @param formModel 表单对象
         * @param formItemModel 表单项对象
         * @param extParams 扩展参数 extParams.get("layoutType") 目前采用layoutType 扩展当前布局模式 ，其他参数可有开发者自行扩展
         *
         * @return
         */
        public String getContent(String themeAppId,  FormModel formModel, FormItemModel formItemModel, Map<String, String> extParams);
    
        /**
         * 手机端风格内容
         *
         * @param themeAppId 风格AppId
         * @param formModel 表单对象
         * @param formItemModel 表单项对象
         * @param extParams 扩展参数
         *
         * @return
         */
        public String getMobileContent(String themeAppId, FormModel formModel, FormItemModel formItemModel, Map<String, String> extParams);
    }
    

### 注册语法

由`FormThemePluginProfile`类完成向AWS PaaS的注册。
    
    
    Map<String, String> layoutMap = new LinkedHashMap<String, String>();
    // 以下4种layout用来控制表单展示时，表单展示对应的列来显示布局数据
    layoutMap.put(LayoutConstant.LAYOUT_COLUMNONE_TITLE, LayoutConstant.LAYOUT_COLUMNONE);//表单的一行显示一列字段信息，包括字段标题，字段的内容（一个输入框或者其他设置的组件，或者只读时的文字内容）
    layoutMap.put(LayoutConstant.LAYOUT_COLUMNTOW_TITLE, LayoutConstant.LAYOUT_COLUMNTOW);//表单的一行显示二列字段信息
    layoutMap.put(LayoutConstant.LAYOUT_COLUMNTHREE_TITLE, LayoutConstant.LAYOUT_COLUMNTHREE);//表单的一行显示三列字段信息
    layoutMap.put(LayoutConstant.LAYOUT_COLUMNFOUR_TITLE, LayoutConstant.LAYOUT_COLUMNFOUR);//表单的一行显示四列字段信息
    list.add(new FormThemePluginProfile("一个带有标题分隔线的主题风格", FieldBackgroundTheme.class.getName(), layoutMap));
    

  * `clazz`-实现类路径，如`com.actionsoft.apps.poc.plugin.web.SampleWeb`

### 设置参数

将应用打包部署好之后，在`AWS控制台`-`应用管理`找到已经注册好的表单主题风格应用，打开，切换到`参数`页签 添加`isDefault`参数，用于设置该表单风格是否默认。如果设置true，则会在表单设计界面处于第一位置；如果未设置，那么平台默认风格会排在首位。

**注意：平台中有且只有一个默认的表单风格，不能设置多个，请注意检查该参数。**

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/form-theme-2.png)](<form-theme-2.png>)

以平台默认提供的`字段背景风格`的主题为例，设置了默认值之后，创建表单时该主题风格会排在首位。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/form-theme-3.png)](<form-theme-3.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/form-theme-4.png)](<form-theme-4.png>)

### 相关资源

  * [ AWS SDK API](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)
  * [《AWS MVC框架参考指南》](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/index.html>)