# 代码示例 · AWS PaaS文档中心

## 代码示例

源码见`扩展插件概念验证`应用

### ProcessorWechatMessage
    
    
    package com.actionsoft.apps.poc.plugin.wechat;
    
    import com.actionsoft.bpms.commons.wechat.WechatProcessor;
    import com.actionsoft.bpms.commons.wechat.bean.WechatInMessage;
    import com.actionsoft.bpms.commons.wechat.bean.WechatOutTextMessage;
    
    public class ProcessorWechatMessage implements WechatProcessor {
    
        public WechatOutMessage handleMessage(WechatInMessage msg) {
            System.out.println("接收到的信息");
            System.out.println(msg.getEvent());
            System.out.println(msg.getEventKey());
            System.out.println(msg);
    
            // 回复文本消息
            WechatOutTextMessage txtMsg = new WechatOutTextMessage(msg);
            txtMsg.setContent("Hi，" + msg.getContent());
            return txtMsg;
        }
    }
    

### 将ProcessorWechatMessage注册至PluginListener监听器

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
            // 注册企业微信事件处理接口
            list.add(new WechatPluginProfile(ProcessorWechatMessage.class.getName(),
            "处理各种微信消息"));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`微信消息处理器`，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/wechat-2.png)](<wechat-2.png>)