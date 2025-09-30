# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现`AbstractUIComponent`抽象类
  2. 用`FormUIPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

**UI组件中使用JSON组件是FastJSON，开发中注意包的引用**

### AbstractUIComponent抽象类

开发者可实现这个接口完成你的UI组件开发。

> com.actionsoft.bpms.ui.base.AbstractUIComponent
> 
> 关于方法中参数UIContext的说明，请参考以**aws-api-doc**
    
    
    public abstract class AbstractUIComponent {
    
        /**
         * 生成初始化组件的JavaScript代码
         *
         * @param context
         * @param readonly
         * @return
         */
        public String getInitScript(UIContext context, boolean readonly);
    
        /**
         * 生成UI组件的Html代码
         *
         * @param context
         * @param readonly
         * @return
         */
        public String getUI(UIContext context, boolean readonly);
    
        /**
         * 生成UI组件的校验JavaScript代码
         *
         * @param context
         * @param readonly
         * @return
         */
        public String getValidateScript(UIContext context, boolean readonly);
    
    
        /**
         * 返回自定义的JavaScript引入的代码
         * 如果组件需要引入自己的js文件，则需要重写该方法
         *
         */
        public String getCustomUIJoinScript(UIContext context) {
            return "<script type='text/javascript' src='../apps/xx/js/xxx.js'></script>";
        }
    
        /**
         * 返回这个UI组件在普通子表和折列子表的Html片段，如果组件有特殊显示要求，可以重写该方法
         *
         * @param context UI组件上下文
         * @param eventStart 用于每行数据打开子表页面的链接，通常是一个<a>开头的部分
         * @param eventEnd 用于每行数据打开子表页面的链接，通常是一个<a>结尾的部分
         * @return
         */
        public String getGridDisplayHtmlValue(UIContext context, boolean readonly, String eventStart, String eventEnd);
    
        /**
         * 返回Ajax子表中组件编辑器的JavaScript函数
         * 如果UI组件需要用到Ajax子表中，需要重写该方法
         *
         * @param context
         * @param readonly
         * @return
         */
        @Override
        public String getEditGridUIEditorFn(UIContext context) {
            return "";
        }
    
        /**
         * 返回Ajax子表中组件渲染的JavaScript函数
         * 如果UI组件需要用到Ajax子表中，需要重写该方法
         *
         * @param context
         * @param readonly
         * @return
         */
        @Override
        public String getEditGridUIRenderFn(UIContext context) {
            return "";
        }
    
        /**
         * 返回Ajax子表中组件获取值的JavaScript函数
         * 如果UI组件需要用到Ajax子表中，需要重写该方法
         *
         * @param context
         * @return
         */
        @Override
        public String getEditGridUIGetEditCellDataFn(UIContext context) {
            return "";
        }
    
        /**
         * 该方法用于在BO建模时，UI组件的扩展参数的配置界面
         *
         * @return
         */
        public String getConfigWebPage(UIContext context)
    }
    

### 注意类中getGridDisplayHtmlValue方法

在`AbstractUIComponent`类中，方法`getGridDisplayHtmlValue`用于在主表单上，普通子表和折列子表的表格中显示的Html片段。通常情况下，该内容是这个字段的值，是一个可点击的链接（没有子表过滤事件控制链接的情况下），该抽象类中已经实现了标准的展示方式，如果你的UI组件中，需要一种特殊的展示方式，可重写该方法，否则，不需要处理该方法。

### 注册语法

由`FormUIPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册UI组件
    
    /**
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
    list.add(new FormUIPluginProfile("常规组件", "UI.Sample", FormUISampleImpl.class.getName(), "简单的示例", "", true, true, true, false, true, true, true, true, true));
    
    /**
    * 含有注册UI组件iconFont图标语法，调用:setIconFont(String iconFontClass,String iconFontCode,String iconFontColor)
    * @param iconFontClass icon图标class,默认是"awsui-iconfont"
    * @param iconFontCode icon图标的unicode
    * @param iconFontColor 图标颜色值
    * */
    list.add(new FormUIPluginProfile("常规组件", "UI.Sample", FormUISampleImpl.class.getName(), "含有注册icon图标的示例", "", true, true, true, false, true, true, true, true, true)..setIconFont("awsui-iconfont", "&#xe86b;", "#0c6e9f"));
    

  * `clazz`-实现类路径，如`com.actionsoft.apps.formui.sample.FormUISampleImpl`

### 图标定义

在`AWS->Console->业务建模->存储模型`中，每种UI组件都会对应一个比较形象的图标，该图标由开发者来定义。iconFont图标定义，开发者上传自定义的iconFont样式文件，并在UI组件注册处定义图标信息。

### 相关资源

开发一个实用的表单UI组件，你可以有足够的想象力和无限的技术边界。深入全面的掌握AWS PaaS平台已有工具痛点需求，对要扩展的工具价值有充分的用户调研和方案设计，一定是一个优秀的FormUI App。

  * AWS SDK API
  * 《AWS MVC框架参考指南》