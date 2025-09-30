# Ajax请求 · AWS PaaS文档中心

## Ajax请求

AWS在JQuery ajax的基础上对常用的异步请求方法进行了封装，对Web开发者提供了4类常见异步请求方式，并对底层进行了统一的处理，如异常拦截。

  * request
  * load
  * post
  * get

### 方法说明：

方法 | 概述 | 参数说明  
---|---|---  
awsui.ajax.request | 通过 HTTP 请求加载远程数据。  
参考jQuery.ajax()。 | **url,[settings]**  
String,Object   
**url** :一个用来包含发送请求的URL字符串。  
**settings** :AJAX 请求设置。所有选项都是可选的。  
awsui.ajax.load | 载入远程 HTML 文件代码并插入至 DOM 中。  
默认使用 GET 方式 - 传递附加参数时自动转换为 POST 方式。 | **url,[data,[callback]]**  
String,Map/String,Callback  
**url** :待装入 HTML 网页网址。  
**data** :发送至服务器的 key/value 数据。  
**callback** :载入成功时回调函数。  
awsui.ajax.post | 通过远程 HTTP POST 请求载入信息。  
这是一个简单的 POST 请求，请求成功时可调用回调函数。 | **url,[data],[callback],[type]**  
String,Map,Function,String  
**url** :发送请求地址。  
**data** :待发送 Key/value 参数。  
**callback** :发送成功时回调函数。  
**type** :返回内容格式，xml, html, script, json, text, _default。  
awsui.ajax.get | 通过远程 HTTP GET 请求载入信息。  
这是一个简单的 GET 请求。请求成功时可调用回调函数。 | **url,[data],[callback],[type]**  
String,Map,Function,String  
**url** :发送请求地址。  
**data** :待发送 Key/value 参数。  
**callback** :发送成功时回调函数。  
**type** :返回内容格式，xml, html, script, json, text, _default。  
awsui.ajax.ok | 验证是否为返回状态是否为成功。 | **data** :ajax请求后的返回对象。  
awsui.ajax.responseObject | 验证是否为**ResponseObject** 对象。 | **data** :字符串或对象。  
awsui.ajax.alert | 弹出请求提示消息 | **data, model, callback**   
Object, boolean,Function   
**data** : 异步请求返回对象。  
**model** : 消息提示框的展示模式，是否为模态。  
**callback** :弹出消息提示后回调函数。  
  
### 示例代码

**awsui.ajax.request 示例**
    
    
    awsui.ajax.request({
        type: "POST",
        url: "./jd?sid="+sid+"&cmd=%AppId%_calculation",
        data: "number1=15&number2=1032&sign=+",
        ok : function(r) {
            //请求处理成功
        },
        err : function(r){
            //请求处理错误
        }
    });
    

**awsui.ajax.load 示例**
    
    
    awsui.ajax.load("./jd?sid="+sid+"&cmd=%AppId%_calculation", { number1: 15, number2: 1032, sign: '+' }, function(data){
        awsui.ajax.alert(data, true, function(){ alert('callback'); });
    });
    

**awsui.ajax.post 示例**
    
    
    awsui.ajax.post("./jd?sid="+sid+"&cmd=%AppId%_calculation", { number1: 15, number2: 1032, sign: '+' }, function(data) {
        awsui.ajax.alert(data, true, function(){ alert('callback'); });
    }, 'json');
    

**awsui.ajax.get 示例**
    
    
    awsui.ajax.get("./jd?sid="+sid+"&cmd=%AppId%_calculation", { number1: 15, number2: 1032, sign: '+' }, function(data) {
        if(awsui.ajax.responseObject(data))
            awsui.ajax.alert(data, true, function(){ alert('callback'); });
    }, 'json');
    

**awsui.ajax.ok 示例**
    
    
    if(awsui.ajax.ok(data))
        alert(data['msg']);
    

**awsui.ajax.responseObject 示例**
    
    
    if(awsui.ajax.responseObject(data))
        awsui.ajax.alert(data, true, function(){ alert('callback'); });
    

**awsui.ajax.alert 示例**
    
    
    awsui.ajax.alert(data, true, function(){ alert('callback'); });
    

### 后端接参
    
    
    /**
     * Ajax数值计算
     *
     * @param me 用户上下文
     * @param number1 数字1
     * @param number2 数字2
     * @param sign 运算符
     */
    @Mapping("%AppId%_calulation")
    public String calculation(UserContext me, int number1, int number2, String sign) {
        TestWeb web = new TestWeb(me);
        return web.calculation(number1, number2, sign);
    }
    

### View层逻辑处理
    
    
    public class TestWeb extends ActionWeb {
    
        public TestWeb() {
        }
    
        public TestWeb(UserContext ctx) {
            super(ctx);
        }
    
        public String calculation(int number1, int number2, String sign) {
            ResponseObject ro = ResponseObject.newOkResponse();
            // 处理逻辑
            // ……
            // ro.put("newNum",newNum);
            return ro.toString();
        }
    }