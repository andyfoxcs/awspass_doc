# 代码示例 · AWS PaaS文档中心

## 代码示例

源码见`扩展插件概念验证`应用

### 将poc.plugin.myACTest注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.at.MyLenExpression;
    import com.actionsoft.apps.poc.plugin.dc.MyFileProcessor;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.ACPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.AtFormulaPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.DCPluginProfile;
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
            // 注册AC权限
            ACAccessMode[] accessModes = { new ACAccessMode("权限1", 0), new ACAccessMode("权限2", 1) };
            String[] assignmentTypes = { ACPluginProfile.ASSN_TYPE_COMPANY, ACPluginProfile.ASSN_TYPE_DEPARTMENT, ACPluginProfile.ASSN_TYPE_ROLE, ACPluginProfile.ASSN_TYPE_TEAM, ACPluginProfile.ASSN_TYPE_USER };
            list.add(new ACPluginProfile("poc.plugin.myACTest", "我的AC权限测试", assignmentTypes, accessModes, false, true));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`我的AC权限测试`，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/ac-3.png)](<ac-3.png>)

### 客户端弹窗授权

> install/com.actionsoft.apps.poc.plugin/template/page/ac-sample.htm
    
    
    ...
    var dlg = FrmDialog.open({
        title : "我的权限设置",
        width : 700,
        height : 380,
        url : "./w",
        data : {
            sid : "<#sid>",
            cmd : "CLIENT_COMMON_AC_ACTION_OPEN",
            resourceId : "123",//业务对象Id
            resourceType : "poc.plugin.myACTest"//注册的AC资源类型，全局不重复
        },
        buttons : [{
                    text : '确定',
                    cls : "blue",
                    handler : function() {
                        dlg.win().saveAC();
                    }
                }, {
                    text : '关闭',
                    handler : function() {
                        dlg.close();
                    }
                }]
    });
    }
    ...
    

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/ac-4.png)](<ac-4.png>)

  * 可在`扩展插件概念验证`应用的`部署`访问`ACSample`功能
  * 提供完整的注册、授权、鉴权演示