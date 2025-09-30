# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 继承`AppCustomActionInterface`抽象类，实现处理逻辑
  2. 用`AppCustomActionPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### AppCustomActionInterface接口

开发者可继承这个类完成应用管理事件扩展的开发。

> com.actionsoft.apps.lifecycle.event.AppCustomActionInterface
    
    
    package com.actionsoft.apps.lifecycle.event;
    
    import com.actionsoft.apps.lifecycle.dist.DistContext;
    import com.actionsoft.apps.resource.AppContext;
    
    /**
     *自定义事件动作
     */
    public interface AppCustomActionInterface {
    
        /**
         * 应用分发的扩展自定义动作事件
         *
         * @param app
         * @param distCtx
         */
        public void dist(AppContext app, DistContext distCtx);
    
        /**
         * 应用安装的扩展自定义动作事件，该事件执行的时间点是安装后的第一次启动
         *
         * @param newApp
         */
        public void install(AppContext newApp);
    
        /**
         * 应用升级的扩展自定义动作事件，该事件执行的时间点是升级后的第一次启动
         *
         * @param newApp
         */
        public void upgrade(AppContext newApp);
    
    }
    

### 注册语法

由`AppCustomActionPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册
    list.add(new AppCustomActionPluginProfile(BOEAppCustomAction.class.getName()));
    

  * `clazz` 实现类路径