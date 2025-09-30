# 模板开发模式 | AWS 移动开发参考指南

# 模板开发模式

  1. 实现H5页面
  2. 添加H5应用

## 1\. 实现H5页面

> 阅读本节内容时您需要首先了解AWS MVC编程框架， 详见[AWS MVC框架参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/index.html>)。

#### 1.1 实现后端控制器

假设添加的H5应用ID为`com.actionsoft.apps.poc.h5`, URL为`cmd=com.actionsoft.apps.poc.h5_test_home`, 下面是其Controller示例
    
    
    @Controller
    public class HelloController {
        // Test1
        @Mapping("com.actionsoft.apps.poc.h5_test_home")
        public String testHome(UserContext me, String string1) {
            HelloWeb abc= new HelloWeb(me);
            return abc.getHome(string1);;
        }
    
    }
    

#### 1.2 组装页面

在View层程序中完成模版处理的示例
    
    
    public class HelloWeb extends ActionWeb {
        public HelloWeb (UserContext uc) {
            super(uc);
        }
        public String getHome(String string1) {
            String uid = getContext().getUID();
            Map<String, Object> macroLibraries = new HashMap<String, Object>();
            macroLibraries.put("sid", super.getContext().getSessionId());
            macroLibraries.put("title", "Hello, " + string1);
            macroLibraries.put("activeTasks", SDK.getTaskQueryAPI().target(uid).count());
            macroLibraries.put("historyTasks", SDK.getHistoryTaskQueryAPI().owner(uid).count());
            macroLibraries.put("trackProcess", SDK.getProcessQueryAPI().createBy(uid).count());
            return HtmlPageTemplate.merge("com.actionsoft.apps.wechat.demo", "hello.html", macroLibraries);
        }
    
    }
    

HTML模板示例
    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no" />
        <title></title>
        <script src="../commons/plug-in/mui/js/mui.min.js"></script>
        <link href="../commons/plug-in/mui/css/mui.min.css" rel="stylesheet"/>
        <script type="text/javascript" charset="utf-8">
              mui.init();
        </script>
    </head>
    <body>
    <form id='frmMain' method='post' name='frmMain'>
    <h5 class="mui-content-padded"><#title></h5>
        <ul class="mui-table-view mui-table-view-chevron">
        <li class="mui-table-view-cell">
            <a class="mui-navigate-right">
                <span class="mui-badge mui-badge-red"><#activeTasks></span>
                待办任务
            </a>
        </li>
        <li class="mui-table-view-cell">
            <a class="mui-navigate-right">
                <span class="mui-badge mui-badge-green"><#historyTasks></span>
                已办任务
            </a>
        </li>
        <li class="mui-table-view-cell">
            <a class="mui-navigate-right">
                <span class="mui-badge mui-badge-green"><#trackProcess></span>
                发起流程
            </a>
        </li>
    </ul>
    
    <h5 class="mui-content-padded">图标左对齐</h5>
    <div class="mui-card">
        <form class="mui-input-group">
            <div class="mui-input-row mui-checkbox mui-left">
                <label>Checkbox</label>
                <input name="checkbox" type="checkbox">
            </div>
            <div class="mui-input-row mui-checkbox mui-left">
                <label>Checkbox</label>
                <input name="checkbox" type="checkbox" checked>
            </div>
        </form>
    </div>
    <h5 class="mui-content-padded">图标右对齐</h5>
    <div class="mui-card">
        <form class="mui-input-group">
            <div class="mui-input-row mui-checkbox">
                <label>Checkbox</label>
                <input name="checkbox1" type="checkbox">
            </div>
            <div class="mui-input-row mui-checkbox">
                <label>Checkbox</label>
                <input name="checkbox1" type="checkbox" checked>
            </div>
        </form>
    </div>
    <h5 class="mui-content-padded">输入框</h5>
    <div class="mui-input-row">
                <label>Input</label>
                <input type="text" placeholder="普通输入框">
            </div>
            <div class="mui-input-row">
                <label>Input</label>
                <input type="text" class="mui-input-clear" placeholder="带清除按钮的输入框">
            </div>
            <div class="mui-input-row">
                <label>Input</label>
                <input type="text" class="mui-input-speech mui-input-clear" placeholder="语音输入">
            </div>
        </form>
        <div class="mui-input-row" style="margin: 10px 5px;">
            <textarea rows="5" placeholder="多行文本框"></textarea>
        </div>
    
    <nav class="mui-bar mui-bar-tab">
        <a class="mui-tab-item mui-active">
            <span class="mui-icon mui-icon-home"></span>
            <span class="mui-tab-label"></span>
        </a>
        <a class="mui-tab-item">
            <span class="mui-icon mui-icon-phone"></span>
            <span class="mui-tab-label">Function 1</span>
        </a>
        <a class="mui-tab-item">
            <span class="mui-icon mui-icon-email"></span>
            <span class="mui-tab-label">Function 2</span>
        </a>
        <a class="mui-tab-item">
            <span class="mui-icon mui-icon-gear"></span>
            <span class="mui-tab-label">Function 3</span>
        </a>
    </nav>
    
    <input type="hidden" id="sid" name="sid" value="<#sid>"/>
    </form>
    </body>
    </html>
    

#### 1.3 Web层配置文件配置CMD

每个AWS App的Web资源被独立的定义在webapp根目录apps/%AppId%下。 下面是对应的action.xml示例
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <aws-actions>
    
        <cmd-bean name="com.actionsoft.apps.poc.h5_test_home">
            <param name="string1" />
        </cmd-bean>
    
    </aws-actions
    

## 2\. 添加H5应用

在AWS控制台`移动应用管理` -> `移动应用列表` 页面中，可以添加H5应用, 此处H5应用URL的值应为`cmd=com.actionsoft.apps.poc.h5_test_home`。

添加H5应用的详细步骤可参考[这里](<../appendix/add-h5.html>)。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/h5-app/basic.png)