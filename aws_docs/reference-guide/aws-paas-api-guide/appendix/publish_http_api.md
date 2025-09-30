# 封装和发布Web API · AWS PaaS文档中心

# 封装和发布自己的Web API

基于AWS PaaS的API架构，应用开发者可以使用Java语言封装和发布自己的Web API。

## 步骤

  1. 在您的App Java工程中编写Java类
  2. 使用Java注解，声明服务类型和参数结构
  3. 确定API请求的返回类型
  4. 发布和浏览服务
  5. 配置身份策略(适用于6.4.1及后续版本)
  6. 配置访控策略(可选)(适用于6.4.1及后续版本)
  7. 配置流控策略(可选)(适用于6.4.1及后续版本)
  8. 测试发布的API
  9. 上下线服务(适用于6.4.1及后续版本)

### 步骤1：在您的App Java工程中编写Java类

获得本地开发环境，[请移步这里](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/ide/README.html>)。

### 步骤2：使用Java注解，声明服务类型和参数结构

注解 | 说明  
---|---  
@Controller | 类注解，描述API分类、注释等  
@Mapping | 方法注解，描述API方法名、注释等  
@Param | 参数注解，描述API参数结构  
  
**com.actionsoft.bpms.server.bind.annotation.Controller**

该注解用于Java类，**必须使用** 。注解属性说明如下：

属性 | 是否必须 | 说明  
---|---|---  
type | 是 | Controller类型，当值为HandlerType.OPENAPI时为Web API  
apiName | 是 | Web API服务类别名称，例如：Process API  
desc | 否 | 该服务的描述信息  
  
**示例**
    
    
    @Controller(type = HandlerType.OPENAPI,
    apiName = "Demo API",desc = "API扩展开发演示")
    public class SayHello {
        ...
    }
    

**com.actionsoft.bpms.server.bind.annotation.Mapping**

该注解用于Java类方法，**必须使用** 。注解属性说明如下：

属性 | 是否必须 | 说明  
---|---|---  
value | 是 | api名称，全局不重复。必须以.分割多个空间。例如：org.user.create  
desc | 否 | 该api的描述信息  
authInfo | 否 | 该api特定的授权验证方式，和CC集成身份中的资源匹配授权，该描述用于引导管理员配置集成身份的授权  
  
**示例**
    
    
    @Mapping(value = "demo.say")
    public StringResponse say(){
        ...
    }
    

**com.actionsoft.bpms.server.bind.annotation.Param**

该注解用于方法的参数、类属性，不必须使用。注解属性说明如下：

属性 | 是否必须 | 说明  
---|---|---  
value | 否 | 参数名称，默认为方法的参数名  
required | 否 | 参数是否必须，默认为是  
desc | 否 | 参数的描写信息，值说明，示例等  
  
**示例**
    
    
    public StringResponse say(@Param(value = "str1",
    desc = "字符串1", required = true) String str1) {
        ...
    }
    

### 步骤3：确定API请求的返回类型

服务方法可以返回void或者返回一个com.actionsoft.bpms.api.common.ApiResponse子类。

> 不支持String、Integer等范围外类型的原因是，Web API被设计成结果响应式编程模式，即请求JSON时返回JSON、请求XML时返回XML。为此，开发者需遵循ApiResponse父类实现自己的对象封装。

常用的简单对象已提供在AWS PaaS开发框架中（`%AWS-HOME%/bin/lib/aws-api-common.jar`），封装的对象包括：

Java Object | 封装的对象  
---|---  
String | StringResponse  
Boolean | BoolResponse  
Integer | IntResponse  
Long | LongResponse  
Map | MapResponse  
List | ListMapResponse  
Object | ObjectResponse  
Integer Array | IntArrayResponse  
String Array | StringArrayResponse  
  
如要返回的对象不在上述范围之内，开发者可以基于ApiResponse实现自定义对象，**并在该类上增加@XmlRootElement注解** ，用于支持XML响应格式。

**完整的API封装示例代码**
    
    
    package com.actionsoft.apps.poc.api.local.api;
    
    import javax.xml.bind.annotation.XmlRootElement;
    
    import com.actionsoft.bpms.api.common.ApiResponse;
    import com.actionsoft.bpms.server.bind.annotation.Controller;
    import com.actionsoft.bpms.server.bind.annotation.HandlerType;
    import com.actionsoft.bpms.server.bind.annotation.Mapping;
    import com.actionsoft.bpms.server.bind.annotation.Param;
    import com.actionsoft.sdk.service.response.StringResponse;
    
    @Controller(type = HandlerType.OPENAPI, apiName = "Demo API", desc = "API扩展开发演示")
    public class SayHello {
    
        // 返回简单String
        @Mapping(value = "demo.say")
        public StringResponse say(
        @Param(value = "str1",
        desc = "字符串1",
        required = true) String str1) {
            StringResponse r = new StringResponse();
            r.setData(str1);
            return r;
        }
    
        // 返回自定义的对象
        @Mapping(value = "demo.calc")
        public CalcResponse calc(
        @Param(value = "num1",
        desc = "数字1",
        required = true) Integer num1,
    
        @Param(value = "num2",
        desc = "数字2",
        required = true) Integer num2) {
            CalcResponse r = new CalcResponse(num1, num2);
            return r;
        }
    
    }
    
    @XmlRootElement
    class CalcResponse extends ApiResponse {
        private int num1;
        private int num2;
        private int num3;
    
        public CalcResponse(int num1, int num2) {
            super();
            this.num1 = num1;
            this.num2 = num2;
            // 计算相加
            num3 = num1 + num2;
        }
    
        public int getNum1() {
            return num1;
        }
    
        public void setNum1(int num1) {
            this.num1 = num1;
        }
    
        public int getNum2() {
            return num2;
        }
    
        public void setNum2(int num2) {
            this.num2 = num2;
        }
    
        public int getNum3() {
            return num3;
        }
    
        public void setNum3(int num3) {
            this.num3 = num3;
        }
    
    }
    

> ApiResponse中属性errorCode来自：com.actionsoft.bpms.api.common.ErrorType，当errorCode值非空时，请求出现业务异常

### 步骤4：发布和浏览服务

将编写的程序编译成jar，存放到您自己的应用lib目录下（假设应用名称是com.abc.apps.do，那么路径应该在%AWS-HOME%/apps/install/com.abc.apps.do/lib），如果开发者引用了三方jar资源，也一同存放到该目录下。

然后进入CC连接服务，选择`发布 > HTTP API`发布Web API。

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web1.gif)](<web1.gif>)

**配置API在线文档说明**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web1.png)](<web1.png>)

**查看在线文档**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web2.png)](<web2.png>)

### 步骤5：配置身份策略

进入CC连接服务 > 策略，创建身份策略，策略类型为HTTP。 创建成功后，将策略配置到上述发布的Web API。

如果不配置身份策略，则在调用时，可传入AWS PaaS平台内存在的任意身份策略。 Web API 不支持无身份策略调用。

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web2.gif)](<web2.gif>)

### 步骤6：配置访控策略(可选)

**1.修改API封装代码，增加访控注解，并编译jar放入应用lib目录下**

注解 | 说明  
---|---  
@PermRequire({}) | 类注解，{}内写支持的类型，如  
`@PermRequire({RequireType.APP,RequireType.ORG})`  
RequireType.ALL | 访控范围支持所有类型  
RequireType.APP | 访控范围支持应用  
RequireType.ORG | 访控范围支持组织  
RequireType.PROCESS | 访控范围支持流程  
RequireType.BO | 访控范围支持BO  
RequireType.CUSTOM | 访控范围支持自定义  
\--- | \---  
@PermApp | 方法参数注解，类型为应用，匹配应用ID  
@PermBO | 方法参数注解，类型为BO，匹配BO模型ID或BO表名称  
@PermTaskId | 方法参数注解，类型为流程，匹配任务实例ID  
@PermProcess | 方法参数注解，类型为流程，匹配流程定义ID  
@PermInstId | 方法参数注解，类型为流程，匹配流程实例ID  
@PermTeam | 方法参数注解，类型为组织，匹配群组ID  
@PermRole | 方法参数注解，类型为组织，匹配角色ID  
@PermUser | 方法参数注解，类型为组织，匹配用户UID  
@PermDepartment | 方法参数注解，类型为组织，匹配部门ID  
@PermCompany | 方法参数注解，类型为组织，匹配单位ID  
@PermCustom | 方法参数注解，类型为自定义，匹配英文逗号分隔的值  
  
**完整的访控注解API封装示例代码**
    
    
    package com.actionsoft.apps.poc.api.local.api;
    
    import com.actionsoft.bpms.api.common.ApiResponse;
    import com.actionsoft.bpms.cc.api.PermRequire;
    import com.actionsoft.bpms.cc.api.RequireType;
    import com.actionsoft.bpms.cc.api.perm.PermCustom;
    import com.actionsoft.bpms.cc.api.perm.PermDepartment;
    import com.actionsoft.bpms.cc.api.perm.PermInstId;
    import com.actionsoft.bpms.cc.api.perm.PermUser;
    import com.actionsoft.bpms.server.bind.annotation.Controller;
    import com.actionsoft.bpms.server.bind.annotation.HandlerType;
    import com.actionsoft.bpms.server.bind.annotation.Mapping;
    import com.actionsoft.bpms.server.bind.annotation.Param;
    import com.actionsoft.sdk.service.response.StringResponse;
    
    import javax.xml.bind.annotation.XmlRootElement;
    
    @Controller(type = HandlerType.OPENAPI, apiName = "Demo API", desc = "API扩展开发演示")
    @PermRequire({RequireType.APP, RequireType.CUSTOM, RequireType.ORG, RequireType.BO, RequireType.PROCESS, RequireType.ALL})
    // 访控类型注解，根据需要调整
    public class SayHello {
    
        // 返回简单String
       //  str1参数增加 @PermUser @PermDepartment @PermInstId 注解，表示校验组织用户账号、部门、流程范围
        @Mapping(value = "demo.say")
        public StringResponse say( @PermUser @PermDepartment @PermInstId @Param(value = "str1", desc = "字符串1", required = true) String str1) {
            StringResponse r = new StringResponse();
            r.setData(str1);
            return r;
        }
    
        // 返回自定义的对象
        // num1 、num2参数增加@PermCustom注解，表示num1 num2会校验自定义范围，允许的自定义范围可在访控策略，自定义类型中配置，如不配置，则任意字符均可
        @Mapping(value = "demo.calc")
        public CalcResponse calc( @PermCustom @Param(value = "num1", desc = "数字1", required = true) Integer num1,
                                  @PermCustom @Param(value = "num2", desc = "数字2", required = true) Integer num2) {
            CalcResponse r = new CalcResponse(num1, num2);
            return r;
        }
    
    }
    
    @XmlRootElement
    class CalcResponse extends ApiResponse {
        private int num1;
        private int num2;
        private int num3;
    
        public CalcResponse(int num1, int num2) {
            super();
            this.num1 = num1;
            this.num2 = num2;
            // 计算相加
            num3 = num1 + num2;
        }
    
        public int getNum1() {
            return num1;
        }
    
        public void setNum1(int num1) {
            this.num1 = num1;
        }
    
        public int getNum2() {
            return num2;
        }
    
        public void setNum2(int num2) {
            this.num2 = num2;
        }
    
        public int getNum3() {
            return num3;
        }
    
        public void setNum3(int num3) {
            this.num3 = num3;
        }
    
    }
    

**2.进入CC连接服务 > 策略，创建访控策略，策略类型为用于发布。 创建成功后，将策略配置到上述发布的Web API**

  1. 创建访控策略 [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/fk.png)](<fk.png>)
  2. 将访控策略绑定到已发布的SOAP API [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web3.png)](<web3.png>)
  3. 为访控策略设置访问权限 [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web4.png)](<web4.png>))

> 有关访控策略的详细配置参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/service_policy.html>)

### 步骤7： 配置流控策略(可选)

进入CC连接服务 > 策略，创建流控策略。 创建成功后，将策略配置到上述发布的Web API**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web3.gif)](<web3.gif>)

> 有关流控策略的详细介绍参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/flow.html>)

### 步骤8： 测试发布的API

您可以用熟悉的方式去测试刚刚发布的API。使用Postman调用Web API，可参见[这里](<../http/postman.html>)。下面使用Java客户端模拟调用`demo.say`和`demo.calc`两个API
    
    
    import java.util.HashMap;
    import java.util.Map;
    
    import com.actionsoft.bpms.api.OpenApiClient;
    
    public class CallWebAPITest  {
        private static String apiServer = "http://localhost:8088/portal/openapi";
        //private static String apiServer = "http://localhost:8088/portal/api"; //6.4.1及后续版本
        private static String accessKey = "111";
        private static String secret = "abc";
    
        public static void say() {
            try {
                String apiMethod = "demo.say";
                Map<String, Object> args = new HashMap<String, Object>();
                args.put("str1", "Hi, AWS PaaS!");
                OpenApiClient client = new OpenApiClient(apiServer, accessKey, secret,
                OpenApiClient.FORMAT_JSON);
                String r = client.exec(apiMethod, args);
                System.out.println(r);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    
        public static void calc() {
            try {
                String apiMethod = "demo.calc";
                Map<String, Object> args = new HashMap<String, Object>();
                args.put("num1",5);
                args.put("num2",6);
                OpenApiClient client = new OpenApiClient(apiServer, accessKey, secret,
                OpenApiClient.FORMAT_JSON);
                String r = client.exec(apiMethod, args);
                System.out.println(r);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    
        public static void main(String args[]){
            say();
            calc();
        }
    
    }
    

**打印输出如下请求结果**
    
    
    {
      "data" : "Hi, AWS PaaS!",
      "result" : "ok"
    }
    
    {
      "num1" : 5,
      "num2" : 6,
      "num3" : 11,
      "result" : "ok"
    }
    

> 如果触发流控或访控策略，则会提示"由于流控策略未通过，该请求被限制访问"或 "由于访控策略未通过，该请求被限制访问"

### 步骤9： 上下线服务

进入发布列表，点击服务上下线按钮，切换状态。 下线的服务，不允许调用。

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web4.gif)](<web4.gif>)