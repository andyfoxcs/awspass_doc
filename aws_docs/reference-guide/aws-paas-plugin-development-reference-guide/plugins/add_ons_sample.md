# 代码示例 · AWS PaaS文档中心

## 代码示例

源码见`扩展插件概念验证`应用

### mainPage

> com.actionsoft.apps.poc.plugin.web.SampleWeb#mainPage
    
    
    // add-ons home
    public String mainPage(UserContext context) {
        StringBuilder sb = new StringBuilder();
        sb.append("<b>Hi, This Is A ADD-ONS Application! System.getProperties()</b><hr/>");
        Set keys = System.getProperties().keySet();
        for (Object key : keys) {
            sb.append(key.toString()).append("&nbsp;-&nbsp;").append(System.getProperties().getProperty((String) key)).append("<br/>");
        }
        return sb.toString();
    }
    

### 将SampleWeb注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.web.SampleWeb;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.AddOnsPluginProfile;
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            // 注册ADD-ONS
            list.add(new AddOnsPluginProfile(SampleWeb.class.getName()));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`控制台ADD-ONS`，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/add-ons-2.png)](<add-ons-2.png>)

进入`AWS CONSOLE > 工具附加`，在`工具列表`点击`扩展插件概念验证`，显示如下内容
    
    
    java.runtime.name - Java(TM) SE Runtime Environment
    java.vm.version - 24.60-b09
    java.vm.vendor - Oracle Corporation
    java.vendor.url - http://java.oracle.com/
    file.encoding.pkg - sun.io
    user.country - CN
    ...