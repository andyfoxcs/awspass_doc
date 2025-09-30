# 代码示例 · AWS PaaS文档中心

# 代码示例

源码见`扩展插件概念验证`应用

## MyLenExpression

> com.actionsoft.apps.poc.plugin.at.MyLenExpression
    
    
    package com.actionsoft.apps.poc.plugin.at;
    
    import com.actionsoft.bpms.commons.at.AbstExpression;
    import com.actionsoft.bpms.commons.at.ExpressionContext;
    
    /**
     * 返回字符串长度
     */
    public class MyLenExpression extends AbstExpression {
    
        public MyLenExpression(final ExpressionContext atContext, String expressionValue) {
            super(atContext, expressionValue);
        }
    
        public String execute(String expression) {
            // 取第1个参数
            String str = getParameter(expression, 1);
            return String.valueOf(str.length());
        }
    }
    

## 将@myLen注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.at.MyLenExpression;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.AtFormulaPluginProfile;
    
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
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

## 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`@myLen`，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/at-4.png)](<at-4.png>)

进入AWS CONSOLE控制台 > 业务建模，在表单某字段默认值，输入@myLen(AWSPaaS)，新建流程实例，该字段默认值为7。