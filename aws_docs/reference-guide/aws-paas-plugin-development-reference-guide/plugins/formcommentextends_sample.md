# 代码示例 · AWS PaaS文档中心

## 代码示例

### MyFormCommentExtends
    
    
    package com.actionsoft.apps.poc.plugin.comment;
    
    import com.actionsoft.bpms.form.engine.plugin.FormCommentExtendsInterface;
    
    public class MyFormCommentExtends implements FormCommentExtendsInterface {
        /**
         * 用于该扩展动作的JavaScript实现，只需要包含function定义，不需要<script></script>标签
         *
         * @return 表单审批记录扩展的JavaScript实现
         */
        public String getJavaScript() {
        "function test(){alert('这是审批记录扩展动作');}";
        }
    
        /**
         * 用于该扩展动作的html
         *
         * @return 表单审批记录扩展的html实现
         */
        public String getExtHtml() {
                return "<div style=\"float:right\"><button onclick=\"test()\" type=\"button\" class=\"awsui-btn awsui-btn-blue\" >审批记录扩展按钮</button></div>";
    
        }
    }
    

### 将WestoneFormCommentExtends注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.bpms.commons.security.processor.SecurityProcessorProfile;
    import com.actionsoft.bpms.form.engine.plugin.FormCommentExtendsPluginProfile;
    import com.actionsoft.apps.poc.plugin.comment.MyFormCommentExtends;
    
    public class Plugins implements PluginListener {
        @Override
        public List<AWSPluginProfile> register(AppContext appContext) {
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            list.add(new FormCommentExtendsPluginProfile("mycomment", "DEMO审批记录扩展", MyFormCommentExtends.class.getName(), ""));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

### 验证

打开表单在审批记录将显示`审批记录扩展按钮`。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/mycomment.png)](<mycomment.png>)