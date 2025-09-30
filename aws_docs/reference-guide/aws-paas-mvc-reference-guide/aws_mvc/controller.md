# 后端控制器 · AWS PaaS文档中心

## 后端处理控制器

就这么简单，提交的请求已经被AWS MVC传输至AWS应用层。

AWS MVC的后端控制器以`@Controller`注解到普通的Java类，并为该方法增加`@Mapping("%Command%")`注解即可。控制器会负责将前端cmd参数名与该Java方法的参数名进行匹配和赋值，完成拦截、绑定和执行过程。

**下面是一个Controller示例**
    
    
    @Controller
    public class ABCController {
        // Test1
        @Mapping("%AppId%_xxx1")
        public String apiTestHome(UserContext me, String p1) {
            return "Hi,p1="+p1;
        }
    
        //Test2
        @Mapping("%AppId%_xxx2")
        public String apiInfo(UserContext me, String p2) {
            ABCWeb abc= new ABCWeb(me);
            return abc.getMainPage(p2);
        }
    }
    

### 注解

控制器只负责拦截、绑定和执行cmd方法，对于该方法的具体实现应交给View层处理，不建议直接在Controller中完成逻辑处理。

注解 | 说明  
---|---  
@Controller | 类注解。声明该类是一个后端处理控制器  
@Mapping | 方法注解。声明该方法将响应一个前端Web请求，参数值是该cmd值  
  
默认每个请求必须含有sid的会话信息，如开发者要求在无session场景下执行服务端请求，可参考如下语法
    
    
    @Mapping(value = "%AppId%_xxx3",
    session = false,
    noSessionEvaluate = "无安全隐患",
    noSessionReason = "用于MVC框架稳定性测试")
    

  * value，cmd的名称
  * session，是否拦截sessionId进行合法性校验
  * noSessionEvaluate，对安全隐患做出评估说明
  * noSessionReason，设计该cmd的原因或功效

> 被标记为无session验证的请求是非常不安全的，原因是AWS无法识别请求者身份。开发者应审慎评估该请求背后执行的逻辑规则，不会被用于恶意处理

### 参数映射

以下参数可以出现在方法参数中

参数 | 说明  
---|---  
UserContext对象类型 | 【可选】获取AWS用户会话对象  
RequestParams对象类型 | 【可选】获取请求参数，Key为变量名，Value为值  
clientIp变量名 | 【可选】String类型。客户端ip地址  
responseType变量名 | 【可选】String类型。请求结果类型(W/JD/XD...)见Message常量  
**%变量名%** | 【可选】cmd的参数名，支持String、Integer、Boolean、Long、Double类型。变量的命名来自具体请求中提供的参数  
  
### package包结构命名建议

  * /model/ 存放modelBean类
  * /dao/ 存放DAO类
  * /cache/ 存放cache类
  * /web/ 存放view类
  * /util/ 存放util或service逻辑处理类

### 注意事项

第一次创建Controller类并进行调试时，需要编译jar文件至该app的lib目录下，否则可能会提示找不到cmd异常。 _这是一个设计缺陷，我们计划在时间充分的时候修复_