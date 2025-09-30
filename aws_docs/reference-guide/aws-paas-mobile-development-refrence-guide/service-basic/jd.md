# /jd请求 | AWS 移动开发参考指南

### AWS MVC的/jd请求

./jd的请求结果是一个Json结构。

下面是一个请求的例子
    
    
    http://localhost:8088/portal/r/jd?cmd=com.actionsoft.apps.helloh5_say_hello&hello=Hello AWS
    

**说明**

  * 使用`./jd`请求一个json数据结果
  * 你获得了“**Hello AWS** ”

    
    
    {
        "data": {
            "hello": "Hello AWS"
        },
        "msg": "",
        "id": ":RO;",
        "result": "ok"
    }
    

> **返回结果**

字段 | 说明  
---|---  
data | 业务数据， 值是一个json对象  
msg | 消息提示  
id | 标志当前对象为ResponseObject对象，awsui.js使用  
result | `ok`（操作成功）， `error`（服务端发生错误，错误描述在`msg`项）， `warning`（服务端发生警告，警告描述在`msg`项）  
  
#### 后端接参
    
    
        @Mapping("com.actionsoft.apps.helloh5_say_hello")
        public String helloH5(UserContext me, String hello) {
            HelloWeb helloWeb = new HelloWeb(me);
            return helloWeb.sayHello(hello);
        }
    

#### View层逻辑处理
    
    
    public class HelloWeb extends ActionWeb {
    
        public HelloWeb(UserContext userContext) {
            super(userContext);
        }
    
        public String sayHello(String hello){
             ResponseObject ro = ResponseObject.newOkResponse();
             ro.put("hello", hello);
             return ro.toString();
        }
    
    }