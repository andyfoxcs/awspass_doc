# 代码示例 · AWS PaaS文档中心

## 代码示例

### BaiduEAIBehavior
    
    
    public class BaiduEAIBehavior {
    
        public ResponseObject getBehaviors(UserContext user, List<EAITaskInstance> instances) {
            Map<String, Map<String, String>> behaviors = new HashMap<>();
            for (EAITaskInstance instance : instances) {
                Map<String, String> behavior = new HashMap<>();
                // 假设该示例可自定义的actionParameter只提供了一个url
                // 通常可以由开发者自定义一个json串，用来传递更丰富的信息
                String url = instance.getActionParameter();
                // 对含有的@公式进行处理
    
                behavior.put("font-color", "red");// 字体颜色，如果不定义由工作台App默认给出
                behavior.put("background-color", "yellow");// 行背景颜色，如果不定义由工作台App默认给出
                behavior.put("icon", "../apps/com.actionsoft.apps.poc.api/img/baidu.png");// 16*16图标url地址，如果不定义由工作台App默认给出
                behavior.put("icon-title", "鼠标提示文字");// 图标鼠标提示文字,若不提供则没有文字提示
                behavior.put("title", instance.getTitle());// 标题，如果不定义由工作台App默认给出
                behavior.put("url", url);// 点击该行时的url地址，如果未提供，不支持点击事件
                behavior.put("type", "百度");// 任务类型,分组的基本类型分组依据,若不提供则按照应用系统名称（EXT1字段分组）
                behaviors.put(instance.getId(), behavior);
            }
    
            return ResponseObject.newOkResponse().put("behaviors", behaviors);
        }
    }
    

### 将BaiduEAIBehavior注册至PluginListener监听器
    
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            // 注册应用扩展点
            Map<String, Object> params3 = new HashMap<String, Object>();
            params3.put("applicationName", "百度");
            params3.put("behaviorClass", BaiduEAIBehavior.class.getName());
            list.add(new AppExtensionProfile("我的工作台->百度任务行为", "aslp://com.actionsoft.apps.workbench/registerEAIBehavior", params3));
            return list;
        }
    }
    

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/eai-task-1.png)](<eai-task-1.png>)

### 使用API模拟创建EAI任务
    
    
    SDK.getTaskAPI().createEAITaskInstance("百度", "0001", "admin", "admin", "这是百度的首页", "http://www.baidu.com?uid=@uid", 1);
    

### 验证

打开`我的工作台`在待办中创建了一个名为`这是百度的首页`的任务，点击可打开`百度网站`

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/eai-task-2.png)](<eai-task-2.png>)

> 如果是外部系统，通常打开的URL需要与AWS SSO进行单点登录集成，即用户可以在免登录直接处理该URL。集成方案请访问《[AWS SSO单点登录管理参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-sso-reference-guide/index.html>)》