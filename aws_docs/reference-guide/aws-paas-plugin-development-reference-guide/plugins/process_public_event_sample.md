# 代码示例 · AWS PaaS文档中心

## 代码示例

源码见`扩展插件概念验证`应用

### MyNotification

> com.actionsoft.apps.poc.plugin.process.MyNotification
    
    
    package com.actionsoft.apps.poc.plugin.process;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ProcessPubicListener;
    import com.actionsoft.bpms.bpmn.engine.model.run.delegate.TaskInstance;
    
    public class MyNotification extends ProcessPubicListener {
    
        @Override
        public void call(String eventName, TaskInstance taskInst, ProcessExecutionContext ctx) {
            //注意事项：
            //流程类：eventName以PROCESS开头的
            //taskInst参数的值是null，注意判断
            //请使用ctx参数获取流程实例对象
    
            //任务类：eventName以TASK开头的
            //taskInst不为空
            //
            //流程撤销时，会触发TASK_DELETE事件，这时taskInst参数值是一个空对象，
            //taskInst.getId()的是null，可以使用UtilString.isEmpty(taskInst.getId())判断，
            //ctx参数中会将该流程实例中的所有任务实例传递，包括待办和已办
            Map<String, Object> parameters = ctx.getParameters();
            if (parameters != null) {
                //这个list即是撤销时全部删除的任务实例
                List<HistoryTaskInstance> list = (List<HistoryTaskInstance>) parameters.get("taskList");
            }
    
            System.out.println("我监听到[" + eventName + "]" + taskInst);
    
            //任务在执行交接(TASK_TRANSFER)时，会触发事件，这时taskInst参数值是一个空对象，
            //taskInst.getId()的是null，可以使用UtilString.isEmpty(taskInst.getId())判断，
            //ctx参数中会提供移交信息，包括交接人，被交接人，流程组ID及流程定义ID信息
            Map<String, Object> parameters = ctx.getParameters();
            //交接人一定存在
            if (parameters.containsKey("FROM")) {
                //...
            }
            //被交接人一定存在
            if (parameters.containsKey("TO")) {
                //...
            }
    
            //任务在执行转办(TASK_DELEGATE)时，会触发事件，这时taskInst参数值是一个转办后办理人的任务实例
            //ctx参数中会提供旧的任务实例
            Map<String, Object> parameters = ctx.getParameters();
            //旧的任务实例
            if (parameters.containsKey("OLD_TASKINST")) {
                //...
            }
    
            //流程组定义ID需要判断是否存在，一个List，取决于迁移API调用者
            if (parameters.containsKey("PROCESSGROUPID")) {
                //List<String> processGroupIdList = (List<String>) parameters.get("PROCESSGROUPID");
            }
            //流程定义ID需要判断是否存在，取决于迁移API调用者
            if (parameters.containsKey("PROCESSDEFID")) {
                //...
            }
        }
    
    }
    

### 将MyNotification注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.process.MyNotification;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.ProcessPublicEventPluginProfile;
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            // 注册流程全局事件监听器
            list.add(new ProcessPublicEventPluginProfile(MyNotification.class.getName(), "我的全局监听器"));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`MyNotification`，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/process-2.png)](<process-2.png>)

模拟创建或执行一些人工任务，会在AWS CONSOLE命令行看到如下Debug信息
    
    
    我监听到[TASK_CREATE][A][userTask][e435bb09-ee88-4475-b6cd-4a3ac39c3d11][(U1)API-1416718701903]
    我监听到[TASK_DELETE][A][userTask][e435bb09-ee88-4475-b6cd-4a3ac39c3d11][(U1)API-1416718701903]
    我监听到[TASK_COMPLETE][A][userTask][e435bb09-ee88-4475-b6cd-4a3ac39c3d11][(U1)API-1416718701903]