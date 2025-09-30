# 代码示例 · AWS PaaS文档中心

# 代码示例

### 模拟发送消息代码片段
    
    
            AppContext notificationApp = SDK.getAppAPI().getAppContext("com.actionsoft.apps.notification");
            if (notificationApp != null) {
                String sourceAppId = "com.actionsoft.apps.poc.plugin";
                // 服务地址
                String aslp = "aslp://com.actionsoft.apps.notification/sendMessage";
                HashMap<String, Object> params = new HashMap<String, Object>();
                params.put("sender", "admin");
                params.put("targetIds", "admin");
                params.put("myVar", "1");// 自定义变量
                HashMap<String, String> data = new HashMap<>();
                data.put("myVar", "1");// 自定义变量
                data.put("data", "应用发出的测试消息!");// 自定义变量
                params.put("content", JSONObject.fromObject(data).toString());
                params.put("level", "info");
                params.put("systemName", MyFormatter.DEMO_NAME);
                SDK.getAppAPI().callASLP(SDK.getAppAPI().getAppContext(sourceAppId), aslp, params);
            }
    

### 接收到的消息示例

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/notification-4.png)](<notification-4.png>)

### MyFormatter
    
    
    package com.actionsoft.apps.poc.plugin.notification;
    
    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    
    import com.actionsoft.bpms.client.notification.NotificationMessageFormatter;
    import com.actionsoft.bpms.commons.mvc.view.ResponseObject;
    import com.actionsoft.bpms.server.UserContext;
    
    import net.sf.json.JSONObject;
    
    public class MyFormatter implements NotificationMessageFormatter {
    
        public final static String DEMO_NAME = "AWS插件->演示消息通知";
    
        /**
         * @param user 通知查看人
         * @param content 发送的原始内容
         * @return ResponseObject，包含content和buttons两个变量
         */
        public ResponseObject parser(UserContext user, String content) {
            // 逻辑处理，开发者自定义的格式，见发送时的封装
            JSONObject json = JSONObject.fromObject(content);
            String myVar = json.getString("myVar");
            String data = json.getString("data");
            // 封装结果
            ResponseObject ro = ResponseObject.newOkResponse();
            ro.put("content", data + "//myVar=" + myVar);
            List<Map<String, String>> buttons = new ArrayList<>();
            Map<String, String> button1 = new HashMap<>();
            button1.put("name", "查看");
            String url = "http//www.baidu.com";
            button1.put("action", url);
            button1.put("target", "_blank");// 新窗口，不常用。只允许三个常量：_blank/mainFrame/ajax
            button1.put("color", "blue");// 只允许三个常量：blue/white/red
            buttons.add(button1);
            ro.put("buttons", buttons);
            return ro;
        }
    
    }
    

### 将MyFormatter注册至PluginListener监听器
    
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
        Map<String, Object> params1 = new HashMap<String, Object>();
        params1.put("systemName", MyFormatter.DEMO_NAME);
        params1.put("icon", "../apps/com.actionsoft.apps.poc.plugin/img/icon96.png");
        params1.put("formatter", MyFormatter.class.getName());
        list.add(new AppExtensionProfile(MyFormatter.DEMO_NAME,     "aslp://com.actionsoft.apps.notification/registerApp", params1));
        return list;
        }
    }