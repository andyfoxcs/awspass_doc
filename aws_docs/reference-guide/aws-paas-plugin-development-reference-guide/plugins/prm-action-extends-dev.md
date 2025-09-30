# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现`PRMActionExtendsInterface`接口initHtmlJavaScript()，getActions(processInst, taskInst)方法
  2. 用`PRMActionExtendsPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)。通过设置注册插件语法中的`scope`参数值，控制扩展按钮作用范围，具体参见下方的注册语法注册语法参数说明
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### PRMActionExtendsInterface接口

开发者可实现这个接口完成你的实例运行管理动作扩展操作。

> com.actionsoft.bpms.maintain.plugin.PRMActionExtendsInterface
    
    
    /**
     * 实例运行管理动作扩展接口
     */
    public interface PRMActionExtendsInterface {
    
        /**
         * 可以引用一些HTML片段，或者JavaScript片段
         * 1. <div>实例扩展按钮</div>
         * 2. <script src='xxx.js'></script>
         * 3. <script>function xxx(){...}</script>
         * @return
         */
        public String initHtmlJavaScript();
    
        /**
         * 返回一系列的动作数组，每个JSONObject是一个按钮
         *
         * id:唯一标识
         * text:按钮名称
         * title:按钮的描述信息，作为鼠标提示展
         * event:事件，通常是一个onclick动作，形如：<code>onclick='alert(1);'</code>
         * style:内联样式列表
         * url:链接
         * target:url打开目标 `sidebar` 侧边栏打开， `blank` 新窗口打开，  `self` 当前窗口打开，  `parent` 父窗口打开，  `top` 整个窗口中打开
         * orderIndex:排序顺序
         *
         * @return 每个JSONObject是一个按钮的JSONArray
         */
        public JSONArray getActions(ProcessInstance processInst, TaskInstance taskInst);
    }
    

### PRMActionExtendsInterface initHtmlJavaScript()返回值说明

  * 根据需要返回自定义html片段，例如:`<div id='dialog'></div>`
  * 根据需要自定义js方法，例如：`<script src='index.js'></script><script>function opendDialog(){$("#dialog").dialog();}</script>`

### PRMActionExtendsInterface getActions()返回参数说明

参数 | 说明 | 备注  
---|---|---  
processInst | 流程实例 ，开发者可以使用该参数获取对应的流程实例数据用于按钮事件的实现 | 注意：需要判断当前实例是否为null  
taskInst | 任务实例，开发者可以使用该参数获取对应的任务实例数据用于按钮事件的实现 | 注意：需要判断当前实例是否为null  
  
### PRMActionExtendsInterface getActions()返回json键值说明

key | 说明  
---|---  
id | 唯一标识  
text | 按钮名称  
title | 按钮的描述信息，作为鼠标提示展示  
event | 事件，通常是一个onclick动作，形如：`onclick='alert(1);'` ,  
style | 内联样式列表  
url | 按钮点击链接,url 打开方式根据`target`属性值，若`target`值未设置，默认新窗口打开。url链接事件与event事件不可同时存在  
target | 窗口打开方式。 `sidebar` 侧边栏打开， `blank` 新窗口打开， `self` 当前窗口打开， `parent` 父窗口打开， `top` 整个窗口中打开  
orderIndex | 自定义按钮排序顺序,建议序号间隔按10倍数设置，方便排序  
  
### 注册语法

由`PRMActionExtendsPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册PRMActionExtends
    list.add(new PRMActionExtendsPluginProfile(id, name,clazz,desc,scope));
    

  * `id`唯一标识
  * `name`名称
  * `clazz`实现类路径，如`com.actionsoft.apps.poc.plugin.web.SuperExtendsWeb`
  * `desc`描述
  * `scope`按钮作用范围 `all` 流程实例 任务实例均实现展示，`process` 流程实例 ，`task` 任务实例