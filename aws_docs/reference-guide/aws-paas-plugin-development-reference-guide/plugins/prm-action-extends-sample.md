# 代码示例 · AWS PaaS文档中心

# 代码示例

### 代码示例
    
    
    package com.actionsoft.apps.addons.superman;
    
    import com.actionsoft.bpms.bpmn.engine.model.run.delegate.ProcessInstance;
    import com.actionsoft.bpms.bpmn.engine.model.run.delegate.TaskInstance;
    import com.actionsoft.bpms.maintain.plugin.PRMActionExtendsInterface;
    import com.actionsoft.bpms.util.UUIDGener;
    import com.alibaba.fastjson.JSONArray;
    import com.alibaba.fastjson.JSONObject;
    
    public class SuperExtendsWeb implements PRMActionExtendsInterface {
        @Override
        public String initHtmlJavaScript() {
            return "<div id='dialogText'></div><script type='text/javascript' src='index.js'></script><script>function opendialog(){$('#dialogText').dialog({width:200,height:100,title:'自定义弹出窗口'});}</script>";
        }
    
        @Override
        public JSONArray getActions(ProcessInstance processInst, TaskInstance taskInst) {
            JSONArray arr = new JSONArray();
            JSONObject obj = new JSONObject();
            String processInstId = "";
            String taskId = "";
            if(processInst!=null){
                processInstId = processInst.getId();
                if(!processInst.isEnd()){  //根据需要判断流程实例状态，更多方法参加java-doc-api
                    obj.put("id", UUIDGener.getUUID());
                    obj.put("text", "实例扩展测试一");
                    obj.put("title", "实例扩展测试一");
                    obj.put("url", "https://www.actionsoft.com.cn/");
                    obj.put("target", "sidebar");
                    obj.put("style", "background:blue");
                    obj.put("orderIndex", 4);
                    arr.add(obj);
                }
            }
    
            if(taskInst!=null){
                taskId = taskInst.getId();
                if(!taskInst.isHistoryTask()){ //根据需要判断任务实例状态，更多方法参加java-doc-api
                    JSONObject obj2 = new JSONObject();
                    obj2.put("id", UUIDGener.getUUID());
                    obj2.put("text", "实例扩展测试二");
                    obj2.put("title", "实例扩展测试二");
                    obj2.put("event", "opendialog('"+taskId+"')");
                    obj2.put("style", "");
                    obj.put("orderIndex", 5);
                    arr.add(obj2);
                }
            }
    
            JSONObject obj3 = new JSONObject();
            obj3.put("id", UUIDGener.getUUID());
            obj3.put("text", "实例扩展测试三");
            obj3.put("url", "https://www.actionsoft.com.cn/");
            obj3.put("target", "blank");
            arr.add(obj3);
            return arr;
        }
    }
    

### 注册

由`PRMActionExtendsPluginProfile`类完成向AWS PaaS的注册。
    
    
    list.add(new PRMActionExtendsPluginProfile("prmextends", "运维扩展按钮", SuperExtendsWeb.class.getName(), "实例扩展测试", "all"));