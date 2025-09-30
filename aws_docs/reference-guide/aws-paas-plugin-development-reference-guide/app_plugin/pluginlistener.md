# PluginListener · AWS PaaS文档中心

# PluginListener
    
    
    com.actionsoft.apps.listener.PluginListener
    

`PluginListener`是AWS PaaS注册扩展插件的总接口，每个App只允许提供一个`PluginListener`的实现，用来汇聚该App所开发的全部插件。

> 建议在你的App Java package根下，创建一个名为`Plugins`的类。如你的AppId为`com.abc.apps.crm`，类路径看起来如下
>     
>     
>     com.abc.apps.crm.Plugins
>     

## 开发步骤

  1. 创建一个App应用或使用已存在的应用
  2. 在该App应用中开发某插件接口的实现类（见**[插件开发](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/>)** 章节）
  3. 在该App应用中开发`PluginListener`接口实现类，注册插件配置
  4. 在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项
  5. 场景模拟，调试

[![开发步骤](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/app_plugin/flow.png)](<flow.png>)

## 在AWS CONSOLE中完成配置

[![配置应用监听器](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/app_plugin/amc.png)](<amc.png>)

## PluginListener接口说明
    
    
    public interface PluginListener {
    
        /**
         * 返回该App插件注册列表， 这个列表是开发者对各种插件描述接口实现类
         *
         * @param context App应用对象
         * @see AWSPluginProfile
         *      插件注册描述接口，平台提供对应的XXPluginProfile（如@公式是AtFormulaPluginProfile）
         */
        public List<AWSPluginProfile> register(AppContext context);
    }