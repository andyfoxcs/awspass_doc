# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现`FormCommentExtendsInterface`抽象类
  2. 用`FormCommentExtendsPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

**插件中使用JSON组件是FastJSON，开发中注意包的引用**

### FormCommentExtendsInterface

开发者可实现这个接口完成你的审批记录扩展开发。

> com.actionsoft.bpms.form.engine.plugin.FormCommentExtendsInterface
> 
> 关于方法中参数UIContext的说明，请参考以**aws-api-doc**
    
    
    /**
     * 表单审批记录扩展接口
     */
    public interface FormCommentExtendsInterface {
        /**
         * 用于该扩展动作的JavaScript实现，只需要包含function定义，不需要<script></script>标签
         *
         * @return 表单审批记录扩展的JavaScript实现
         */
        public String getJavaScript();
    
        /**
         * 用于该扩展动作的html
         *
         * @return 表单审批记录扩展的html实现
         */
        public String getExtHtml();
    }
    

### 注册语法

由`FormCommentExtendsPluginProfile`类完成向AWS PaaS的注册。
    
    
    //审批记录扩展
    
    /**
     * @param id 全局唯一名称
     * @param name 中文名称
     * @param clazz 实现类
     * @param desc 描述
     */
    list.add(new FormCommentExtendsPluginProfile("mycomment", "DEMO审批记录扩展", MyFormCommentExtends.class.getName(), ""));
    

  * `clazz`-实现类路径，如`com.actionsoft.apps.formui.sample.FormUISampleImpl`