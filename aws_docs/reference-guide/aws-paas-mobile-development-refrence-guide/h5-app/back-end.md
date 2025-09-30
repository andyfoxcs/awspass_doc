# 后端开发 | AWS 移动开发参考指南

# 后端开发

  1. 创建Web应用
  2. 后端开发

## 1\. 创建Web应用

_步骤_

登录AWS控制台， 在「应用管理>应用开发」 页面，点击 「创建新应用」 ， 假设应用ID是`com.actionsoft.apps.poc.h5`

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/h5-app/createweb.png)

## 2\. 后端开发

> 阅读本节内容时您需要首先了解AWS MVC编程框架， 详见[AWS MVC框架参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/index.html>)。

#### 2.1 实现后端控制器

_假设有两个CMD分别返回了待办任务列表和已办任务列表，下面是其Controller示例_
    
    
    @Controller
    public class HelloController {
        //模拟待办任务列表
        @Mapping("com.actionsoft.apps.poc.h5_todo")
        public String getTodoTask(UserContext me, String title) {
            ResponseObject ro = ResponseObject.newOkResponse();
            JSONArray jsonArray = new JSONArray();
    
            JSONObject task = new JSONObject();
            task.put("taskTitle", "张超的报销申请");
            task.put("taskTime", "16:32");
            task.put("taskOwner", "李明");
            jsonArray.add(task);
    
            task = new JSONObject();
            task.put("taskTitle", "付款申请");
            task.put("taskTime", "昨天 15:32");
            task.put("taskOwner", "李明");
            jsonArray.add(task);
    
            task = new JSONObject();
            task.put("taskTitle", "李林的请假申请");
            task.put("taskTime", "前天 15:33");
            task.put("taskOwner", "李林");
            jsonArray.add(task);
    
            ro.put("taskList", jsonArray);
            return ro.toString();
        }
    
        //模拟已办任务列表
        @Mapping("com.actionsoft.apps.poc.h5_history")
        public String getHistoryTask(UserContext me, String title) {
            ResponseObject ro = ResponseObject.newOkResponse();
            JSONArray jsonArray = new JSONArray();
    
            JSONObject task = new JSONObject();
            task.put("taskTitle", "付款申请");
            task.put("taskTime", "昨天 17:32");
            task.put("taskOwner", "李明");
            jsonArray.add(task);
    
            task = new JSONObject();
            task.put("taskTitle", "张三的报销申请");
            task.put("taskTime", "昨天 16:32");
            task.put("taskOwner", "李明");
            jsonArray.add(task);
    
    
            task = new JSONObject();
            task.put("taskTitle", "李林的请假申请");
            task.put("taskTime", "前天 12:33");
            task.put("taskOwner", "李林");
            jsonArray.add(task);
    
            ro.put("taskList", jsonArray);
            return ro.toString();
        }
    }
    

#### 2.2 Web层配置文件配置CMD

每个AWS App的Web资源被独立的定义在webapp根目录apps/%AppId%下。

_下面是对应的action.xml示例_
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <aws-actions>
        <cmd-bean name="com.actionsoft.apps.poc.h5_todo">
            <param name="title" />
        </cmd-bean>
    
        <cmd-bean name="com.actionsoft.apps.poc.h5_history">
            <param name="title" />
        </cmd-bean>
    
    </aws-actions