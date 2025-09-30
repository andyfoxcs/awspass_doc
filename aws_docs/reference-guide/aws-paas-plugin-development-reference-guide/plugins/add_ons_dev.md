# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现`AddOnsInterface`接口mainPage()方法
  2. 用`AddOnsPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### AddOnsInterface接口

开发者可实现这个接口完成你的ADD-ON应用入口界面。

> com.actionsoft.bpms.commons.addons.AddOnsInterface
    
    
    public interface AddOnsInterface {
    
        /**
         * 返回该应用的入口处理页面
         *
         * @param context 操作者
         * @return 一个完整的HTML页面
         */
        public abstract String mainPage(UserContext context);
    }
    

### 注册语法

由`AddOnsPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册ADD-ONS
    list.add(new AddOnsPluginProfile(clazz));
    

  * `clazz`-实现类路径，如`com.actionsoft.apps.poc.plugin.web.SampleWeb`

### 相关资源

开发一个实用的控制台插件，你可以有足够的想象力和无限的技术边界。深入全面的掌握AWS PaaS平台已有工具痛点需求，对要扩展的工具价值有充分的用户调研和方案设计，一定是一个优秀的ADD-ONS App。

  * [ AWS SDK API](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)
  * [AWS MVC框架参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/index.html>)