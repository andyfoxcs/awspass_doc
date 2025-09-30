# 常规门户示例 · AWS PaaS文档中心

## 常规门户示例

这是一个最朴素的门户首页。当用户登录系统后，获得可访问的功能。

源码见`扩展插件概念验证`应用

### MySkins

> com.actionsoft.apps.poc.plugin.skins.MySkins
    
    
    package com.actionsoft.apps.poc.plugin.skins;
    
    import java.util.LinkedHashMap;
    import java.util.Map;
    
    import net.sf.json.JSONArray;
    import net.sf.json.JSONObject;
    
    import com.actionsoft.bpms.commons.htmlframework.HtmlPageTemplate;
    import com.actionsoft.bpms.commons.portal.skins.AbstPortalSkins;
    import com.actionsoft.bpms.commons.portal.skins.PortalSkinsInterface;
    import com.actionsoft.bpms.server.UserContext;
    import com.actionsoft.bpms.util.UtilString;
    import com.actionsoft.exception.AWSException;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.PortalAPI;
    
    public class MySkins extends AbstPortalSkins implements PortalSkinsInterface {
    
        /**
         * 登录成功后首页面
         */
        public String getHomePage(UserContext me) {
            StringBuilder sb = new StringBuilder();
            // 取当前用户可访问的全部功能。实际场景建议用getNavList逐级读取
            JSONArray navTree = SDK.getPortalAPI().getNavTree(me);
            for (int i = 0; i < navTree.size(); i++) {
                JSONObject system = navTree.getJSONObject(i);
                String systemName = system.getString("name");
                String systemUrl = system.getString("url");
                // 目标。mainFrame关键字表示打开到你指定的门户工作区，_blank表示浏览器新窗口
                String systemTarget = system.getString("target");
                if (!UtilString.isEmpty(systemUrl) && !systemUrl.equals("/")) {
                    systemName = "*" + systemName;
                } else {
                    systemUrl = "";
                }
                sb.append("<option value=\"").append(systemUrl).append("\">").append(systemName).append("</option>\n");
                // 该子系统的所有目录
                JSONArray directories = system.getJSONArray("directory");
                for (int ii = 0; ii < directories.size(); ii++) {
                    JSONObject directory = directories.getJSONObject(ii);
                    String directoryName = directory.getString("name");
                    String directoryUrl = directory.getString("url");
                    // 目标。mainFrame关键字表示打开到你指定的门户工作区，_blank表示浏览器新窗口
                    String directoryTarget = directory.getString("target");
                    if (!UtilString.isEmpty(directoryUrl) && !directoryUrl.equals("/")) {
                        directoryName += "*";
                    } else {
                        directoryUrl = "";
                    }
                    sb.append("<option value=\"").append(directoryUrl).append("\">").append(systemName).append("/").append(directoryName).append("</option>\n");
                    // 该目录的所有功能
                    JSONArray functions = directory.getJSONArray("function");
                    for (int iii = 0; iii < functions.size(); iii++) {
                        JSONObject function = functions.getJSONObject(iii);
                        String functionName = function.getString("name");
                        String functionUrl = function.getString("url");
                        // 目标。mainFrame关键字表示打开到你指定的门户工作区，_blank表示浏览器新窗口
                        String functionTarget = function.getString("target");
                        if (!UtilString.isEmpty(functionUrl) && !functionUrl.equals("/")) {
                            functionName += "*";
                        } else {
                            functionUrl = "";
                        }
                        sb.append("<option value=\"").append(functionUrl).append("\">").append(systemName).append("/").append(directoryName).append("/").append(functionName).append("</option>\n");
                    }
                }
            }
            // user info
            String userInfo = me.getUserName();
            // template merge
            Map<String, Object> macroLibraries = new LinkedHashMap<String, Object>();
            macroLibraries.put("userInfo", userInfo);
            macroLibraries.put("nav-list", sb.toString());
            macroLibraries.put("sid", me.getSessionId());
            return HtmlPageTemplate.merge("com.actionsoft.apps.poc.plugin", "portal-index.htm", macroLibraries);
        }
    
        /**
         * 退出提示页面
         */
        public String getLogoutPage(UserContext me) {
            PortalAPI portalApi = SDK.getPortalAPI();
            // 关闭session
            boolean isClosed = portalApi.closeSession(me.getSessionId());
            if (!isClosed) {
                throw new AWSException("Session关闭异常");
            }
            // 调转到你的登出页面
            return "logout sucess!";
        }
    }
    

### portal-index.htm模版

> com.actionsoft.apps.poc.plugin/template/page/portal-index.htm
    
    
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="../commons/css/awsui.css"/>
    <script type="text/javascript" src="../commons/js/jquery/scripts/jquery.js"></script>
    <script type="text/javascript" src="../commons/js/awsui.js"></script>
    <title>Welcome My Portal!</title>
    <script type="text/javascript">
    //打开功能
    function navUrl(url){
        if(url==''){
             $.simpleAlert('这是个功能分类!');
        }else{
            mainFrame.location=url;
        }
    }
    
    //退出账户
    function logout(){
        frmMain.cmd.value="com.actionsoft.apps.poc.plugin_portal_logout";
        frmMain.target="_self";
        frmMain.submit();
    }
    
    //自动适应浏览器窗口
    $(document).ready(function() {
        $("#mainFrame").height($(window).height()-45);
        $("#mainFrame").width($(window).width());
        $("#select-function").width(300);
    });
    </script>
    </head>
    <body style="margin:0px">
    <form id="frmMain" name="frmMain">
    <table width=100%>
    <tr><td width=30%>
    <select class="awsui-select" id="select-function" onchange="navUrl(this.value)">
        <option value="">请选择操作</option>
        <#nav-list>
    </select>
    <td width=70% align=right>hi,<#userInfo>&nbsp;&nbsp;<a href='' onclick="logout();return false;">退出</a>&nbsp;&nbsp;</td>
    </tr>
    </table>
    <iframe src="" id=mainFrame name=mainFrame width="100%"></iframe>
    <input type="hidden" name="cmd"/>
    <input type="hidden" name="sid" value="<#sid>"/>
    </form>
    </body>
    </html>
    

### 将MySkins注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.skins.MySkins;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.SkinsPluginProfile;
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            // 注册门户主题风格
            list.add(new SkinsPluginProfile(MySkins.class.getName(), false));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

### 验证

进入`AWS CONSOLE > 公共设施 > 主题风格`，如出现`扩展插件概念验证`，说明注册成功。打开应用策略对话框，设置使用该主题的用户范围。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/portal-4.png)](<portal-4.png>)

以测试用户身份登录前端，返回如下门户首页

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/portal-5.png)](<portal-5.png>)