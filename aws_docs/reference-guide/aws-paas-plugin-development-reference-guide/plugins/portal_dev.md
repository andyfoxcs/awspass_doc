# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 继承`AbstPortalSkins`抽象类，实现个人登录后的首页面
  2. 用`SkinsPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 在`AWS CONSOLE > 公共设施 > 主题风格`中，设置该门户的`应用策略`
  4. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### AbstPortalSkins抽象类

开发者可继承这个类完成登录后首页的开发。这是一个从0到1的过程，需要你至少熟练的掌握AWS MVC开发框架，并完成你设定的目标。

> com.actionsoft.bpms.commons.portal.skins.PortalSkinsInterface
    
    
    public interface PortalSkinsInterface {
    
        /**
         * 登录后首页面，在用户完成登录验证后由该方法接管
         *
         * @param me 当前操作人上下文
         * @return 登录后的首页面
         */
        public String getHomePage(UserContext me);
    
    }
    

### 注册语法

由`SkinsPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册门户主题风格
    list.add(new SkinsPluginProfile(clazz, portletContainer));
    

  * `clazz`-实现类路径，如`com.actionsoft.apps.poc.plugin.skins.MySkins`
  * `portletContainer`-是否提供标准的Portal布局和Portlet。开启此项在CONSOLE主题管理中提供对桌面门户的相关配置功能

**内置的常见前端编程框架**

框架 | 资源位置  
---|---  
JQuery 1.10.2 | ../commons/js/jquery/scripts/  
Bootstrap 3.3.7 | ../commons/plug-in/bootstrap/  
EChart 3.5.1 | ../commons/js/jquery/scripts/ui/echarts/  
CKEditor 4.2.2 | ../commons/plug-in/ckeditor/  
  
### 相关资源

  * com.actionsoft.sdk.local.api.PortalAPI
  * com.actionsoft.sdk.local.api.ORGAPI
  * com.actionsoft.sdk.local.api.PermAPI
  * com.actionsoft.sdk.local.api.AppAPI
  * com.actionsoft.sdk.local.api.TaskQueryAPI
  * com.actionsoft.sdk.local.api.HistoryTaskQueryAPI
  * com.actionsoft.sdk.local.api.RuleAPI
  * com.actionsoft.sdk.local.api.ConfAPI
  * com.actionsoft.bpms.util.DBSql
  * 《AWS MVC框架参考指南》