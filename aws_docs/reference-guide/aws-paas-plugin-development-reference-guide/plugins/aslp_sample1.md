# 服务封装示例 · AWS PaaS文档中心

## 服务封装示例

源码见`扩展插件概念验证`应用

### MyNameASLP

> com.actionsoft.apps.poc.plugin.aslp.MyNameASLP
    
    
    package com.actionsoft.apps.poc.plugin.aslp;
    
    import java.util.Map;
    
    import com.actionsoft.apps.resource.interop.aslp.ASLP;
    import com.actionsoft.apps.resource.interop.aslp.Meta;
    import com.actionsoft.bpms.commons.mvc.view.ResponseObject;
    
    public class MyNameASLP implements ASLP {
    
        public MyNameASLP() {
        }
    
        @Meta(parameter = { "name:'yourName',required:true,desc:'你的名字'" })
        public ResponseObject call(Map<String, Object> params) {
            ResponseObject ro = ResponseObject.newOkResponse();
            ro.put("data", "Hi " + params.get("yourName") + " , My name is AWS!");
            return ro;
        }
    
    }
    

### 将ASLP注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.aslp.MyNameASLP;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.ASLPPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.HttpASLP;
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
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
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现下图相关ASLP服务，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/aslp-1.png)](<aslp-1.png>)