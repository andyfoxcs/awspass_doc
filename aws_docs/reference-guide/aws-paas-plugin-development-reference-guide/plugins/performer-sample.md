# 代码示例 · AWS PaaS文档中心

## 代码示例

### 自定义路由方案示例

#### 继承HumanPerformerAbst抽象类，实现HumanPerformerInterface接口
    
    
    package com.actionsoft.apps.zhanghf.route;
    
    import java.util.Map;
    
    import com.actionsoft.bpms.bpmn.engine.model.def.UserTaskModel;
    import com.actionsoft.bpms.bpmn.engine.model.run.delegate.ProcessInstance;
    import com.actionsoft.bpms.bpmn.engine.model.run.delegate.TaskInstance;
    import com.actionsoft.bpms.bpmn.engine.performer.HumanPerformerAbst;
    import com.actionsoft.bpms.bpmn.engine.performer.HumanPerformerInterface;
    import com.actionsoft.bpms.server.UserContext;
    
    /**
     * @author zhanghf
     */
    public class CustomRoute extends HumanPerformerAbst implements HumanPerformerInterface {
        @Override
        public String getSetting(UserContext user, Map<String, Object> params) {
            StringBuilder setting = new StringBuilder();
            setting.append("<tbody id='CustomRoute-custommenu' style='display:none;'>");
            setting.append("<tr>");
            setting.append("    <td>配置界面参数示例</td>");
            setting.append("    <td align='left'>");
            setting.append("        <input type='text' id='CustomRoute' name='CustomRoute' class='txt' style='width:265px;' value='' />");
            setting.append("    </td>");
            setting.append("</tr>");
            setting.append("<tr>");
            setting.append("    <td>配置界面参数示例2</td>");
            setting.append("    <td align='left'>");
            setting.append("        <input type='text' id='CustomRoute2' name='CustomRoute' class='txt' style='width:265px;' value='' />");
            setting.append("    </td>");
            setting.append("</tr>");
            setting.append("<tr>");
            setting.append("    <td>配置界面参数示例3</td>");
            setting.append("    <td align='left'>");
            setting.append("        <input type='text' id='CustomRoute3' name='CustomRoute' class='txt' style='width:265px;' value='' />");
            setting.append("    </td>");
            setting.append("</tr>");
            setting.append("<tr>");
            setting.append("    <td>配置界面参数示例4</td>");
            setting.append("    <td align='left'>");
            setting.append("        <input type='text' id='CustomRoute4' name='CustomRoute' class='txt' style='width:265px;' value='' />");
            setting.append("    </td>");
            setting.append("</tr>");
            setting.append("</tbody>");
            setting.append("<script>");
            setting.append("putCustomParams('com.actionsoft.apps.zhanghf.route.CustomRoute', {");
            setting.append("    show: ['CustomRoute'],");
            setting.append("    init: function(value) {");
            setting.append("        $('#CustomRoute').val(getValueByName('CustomRoute'));");
            setting.append("    },");
            setting.append("    validateCall: function() {");
            setting.append("        if ($('#CustomRoute:visible').val() == '') {");
            setting.append("            $.simpleAlert('不允许为空', 'info', 2000);");
            setting.append("            return true;");
            setting.append("        }");
            setting.append("    },");
            setting.append("    returnJson: function(p) {");
            setting.append("        p['CustomRoute'] = $('#CustomRoute').val();");
            setting.append("        p['CustomRoute2'] = $('#CustomRoute2').val();");
            setting.append("        p['CustomRoute3'] = $('#CustomRoute3').val();");
            setting.append("        p['CustomRoute4'] = $('#CustomRoute4').val();");
            setting.append("    }");
            setting.append("});");
            setting.append("</script>");
            return setting.toString();
        }
    
        @Override
        public String getHumanPerformer(UserContext user, ProcessInstance processInst, TaskInstance taskInst, UserTaskModel userTaskDefModel, Map<String, Object> params) {
            System.out.println(params);
            return "lb cc sq";
        }
    }
    

#### getSetting

> com.actionsoft.apps.zhanghf.route.CustomRoute#getSetting

该方法返回一个段Html和JavaScript片段，用于这个路由方案的自定义参数控制 包括两个部分：

#### HTML
    
    
    <tbody id="CustomRoute-custommenu" style="">
        <tr>
            <td>配置界面参数示例</td>
            <td align="left">
                <input type="text" id="CustomRoute" name="CustomRoute" class="txt" style="width:265px;" value="">
            </td>
        </tr>
        <tr>
            <td>配置界面参数示例2</td>
            <td align="left">
                <input type="text" id="CustomRoute2" name="CustomRoute" class="txt" style="width:265px;" value="">
            </td>
        </tr>
        <tr>
            <td>配置界面参数示例3</td>
            <td align="left">
                <input type="text" id="CustomRoute3" name="CustomRoute" class="txt" style="width:265px;" value="">
            </td>
        </tr>
        <tr>
            <td>配置界面参数示例4</td>
            <td align="left">
                <input type="text" id="CustomRoute4" name="CustomRoute" class="txt" style="width:265px;" value="">
            </td>
        </tr>
    </tbody>
    

**注意**

该html片段必须包含一个`tbody`，该元素默认设置隐藏，内部是一个或多个`tr`，其中`td`必须遵循如下格式：
    
    
    <!--表格是多行两列结构-->
    <tbody>
        <tr>
            <td></td>
            <td></td>
        </tr>
        ...
    </tbody>
    

或
    
    
    <!--表格是多行一列结构-->
    <tbody>
        <tr>
            <td colspan="2"></td>
        </tr>
        ...
    </tbody>
    

`tbody`上必须设置`id`属性，必须是该实现类的类名，以`-custommenu`结尾。

#### JavaScript

JavaScript主要目的是调用`putCustomParams`函数，该函数第一个参数是该路由方案类的全路径；第二个参数是一个Object对象，包括4个部分
    
    
    {
        show: ['CustomRoute'],
        init: function(value) {
            $('#CustomRoute').val(getValueByName('CustomRoute'));
        },
        validateCall: function() {
            if ($('#CustomRoute:visible').val() == '') {
                $.simpleAlert('不允许为空', 'info', 2000);
                return true;
            }
        },
        returnJson: function(p) {
            p['CustomRoute'] = $('#CustomRoute').val();
            p['CustomRoute2'] = $('#CustomRoute2').val();
            p['CustomRoute3'] = $('#CustomRoute3').val();
            p['CustomRoute4'] = $('#CustomRoute4').val();
        }
    }
    

  * show 一个数组，该路由方案需要展示的内容，必须是该类的类名
  * init 该路由方案参数的界面初始化函数，将已经设置的参数回显到界面元素上
  * validateCall 如果参数需要校验，需要提供该函数
  * returnJson 该函数将路由方案提供的参数，提供给流程设计器，用于保存

**技巧**

如果参数很复杂的情况，建议将上述HTML片段和JavaScript片段，放入HTML模版中，使用平台的模版机制调用，省去在Java中拼HTML代码的不便。
    
    
    return HtmlPageTemplate.merge("HTML模版文件名", new HashMap<String, Object>());
    

#### getHumanPerformer

> com.actionsoft.apps.zhanghf.route.CustomRoute#getHumanPerformer

该方法是流程引擎处理中最终的调用方法，引擎根据该方法的返回，指定任务的接收人

**关于兼任的格式处理**

如果返回值涉及到兼任信息，返回格式为`用户UID|兼任单位ID|兼任部门ID|兼任角色ID`，多个依然使用空格分隔

参数说明：

  * UserContext user 用户上下文对象
  * ProcessInstance processInst 流程实例
  * TaskInstance taskInst 任务实例
  * UserTaskModel userTaskDefModel 节点对象模型
  * Map params 流程界面配置提供的参数，具体格式见下方说明

    
    
    {
        "routeType": "com.actionsoft.apps.zhanghf.route.CustomRoute",
        "CustomRoute": "测试参数",
        "CustomRoute2": "测试参数2",
        "CustomRoute3": "测试参数3",
        "CustomRoute4": "测试参数4",
        "isHistoryRoute": false,
        "multiSelect": false,
        "multiSelectDisabledCheckBox": false
    }
    

调试代码时的参数信息

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/performer-3.png)](<performer-3.png>)