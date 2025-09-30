# 开发示例 · AWS PaaS文档中心

## 开发示例

  1. 实现`FormToolbarActionExtendsInterface`抽象类，实现公式的处理逻辑
  2. 用`FormToolbarActionExtendsPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### FormToolbarActionExtendsInterface接口

开发者可继承这个类完成AT公式的开发。

> com.actionsoft.bpms.form.engine.plugin.FormToolbarActionExtendsInterface
    
    
    package com.actionsoft.bpms.form.engine.plugin;
    
    /**
     * 表单工具条动作扩展接口
     */
    public interface FormToolbarActionExtendsInterface {
        /**
         * 用于该扩展动作的JavaScript实现，只需要包含function定义，不需要<script></script>标签
         *
         * @return 表单工具条动作扩展的JavaScript实现
         */
        public String getJavaScript();
    }
    

### 注册语法

由`FormToolbarActionExtendsPluginProfile`类完成向AWS PaaS的注册。
    
    
    list.add(new FormToolbarActionExtendsPluginProfile("processbudgetJs", "流程预测", "gotoProcessBudgetPage();","../apps/com.actionsoft.apps.processbudget/img/processBudget.png", 0, 200, JsUtil.class.getName()));
    

  * `id` 唯一标识，为了避免重复，可以使用AppId作为前缀
  * `text` 菜单显示的文字内容
  * `method` 响应的动作，一个js函数。注意和html标签中的onclick的语法格式一致
  * `icon` 一个图标路径
  * `scope` 应用范围，-1：全部应用；0：仅流程运行环境应用；1：仅数据视图环境应用
  * `orderIndex` 菜单顺序，间隔10个单位，方便调整顺序
  * `clazz` 实现类

已经存在的顺序值：

功能 | 顺序值  
---|---  
流程跟踪图 | 10  
流程热力图 | 20  
生成测试用例 | 30  
收藏/取消收藏 | 40  
帮助说明 | 60  
条形码 | 一直排在最后  
  
### 示例代码
    
    
    package util;
    
    import com.actionsoft.bpms.form.engine.plugin.FormToolbarActionExtendsInterface;
    
    public class JsUtil implements FormToolbarActionExtendsInterface {
    
        //按钮目前仅支持打开url地址
        @Override
        public String getJavaScript() {
            String openUrl="./w?sid=xxxxx&cmd=CLIENT_BPM_FORM_MAIN_PAGE_OPEN&processInstId=xxxxx&openState=1&taskInstId=xxxxxx&formDefId=xxxxx&boId=xxxxx&displayToolbar=true";
            return openUrl;
        }
    }