# 代码示例 · AWS PaaS文档中心

# 代码示例

以下代码取自`com.actionsoft.apps.poc.plugin`应用的Plugins类
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.aslp.MyNameASLP;
    import com.actionsoft.apps.poc.plugin.at.MyLenExpression;
    import com.actionsoft.apps.poc.plugin.dc.MyFileProcessor;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.ACPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.ASLPPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.AtFormulaPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.DCPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.HttpASLP;
    import com.actionsoft.bpms.commons.security.ac.model.ACAccessMode;
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            // 注册AT公式
            list.add(new AtFormulaPluginProfile("字符串", "@myLen(*str)", MyLenExpression.class.getName(), "我的字符串长度", "返回字符串长度"));
            // 注册DC
            list.add(new DCPluginProfile("mydoc", MyFileProcessor.class.getName(), "文件存放到该应用的mydoc根目录下", false));
            // 注册AC权限
            ACAccessMode[] accessModes = { new ACAccessMode("权限1", 0), new ACAccessMode("权限2", 1) };
            String[] assignmentTypes = { ACPluginProfile.ASSN_TYPE_COMPANY, ACPluginProfile.ASSN_TYPE_DEPARTMENT, ACPluginProfile.ASSN_TYPE_ROLE, ACPluginProfile.ASSN_TYPE_TEAM, ACPluginProfile.ASSN_TYPE_USER };
            list.add(new ACPluginProfile("poc.plugin.myACTest", "我的AC权限测试", assignmentTypes, accessModes, false, true, null));
            // 注册ASLP
            // 只允许在同一个PaaS内的其他应用调用
            list.add(new ASLPPluginProfile("myName", MyNameASLP.class.getName(), "猜猜我是谁", null));
            // 调用者提供AWS会话，通过http访问
            list.add(new ASLPPluginProfile("myName1", MyNameASLP.class.getName(), "猜猜我是谁", new HttpASLP(HttpASLP.AUTH_AWS_SID)));
            // 调用者提供一个串为hehe的暗号，该暗号被定义在MY_KEY变量中，通过http访问
            list.add(new ASLPPluginProfile("myName2", MyNameASLP.class.getName(), "猜猜我是谁", new HttpASLP(HttpASLP.AUTH_KEY, "MY_KEY")));
            // 调用者有应用服务提供方提供的cer公钥文件，通过http访问
            list.add(new ASLPPluginProfile("myName3", MyNameASLP.class.getName(), "猜猜我是谁", new HttpASLP(HttpASLP.AUTH_RSA)));
            return list;
        }
    }
    

## 检查

如果一切顺利，你的插件应用已经注册到该App的资源中。如果你的AWS PaaS安装了`com.actionsoft.apps.poc.plugin`应用，可以在AWS CONSOLE的`应用管理`中打开该应用窗口，查看`资源`项如下：

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/app_plugin/resource.png)](<resource.png>)