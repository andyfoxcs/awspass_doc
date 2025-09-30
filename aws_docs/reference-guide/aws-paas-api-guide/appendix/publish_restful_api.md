# 封装和发布RESTful API · AWS PaaS文档中心

# 封装和发布RESTful API

> 该章节内容仅适用于6.3.GA及后续版本

## 步骤

  1. 在您的App Java工程中编写Java类
  2. 使用Java注解定义服务
  3. 发布和浏览服务
  4. 配置身份策略(适用于6.4.1及后续版本)
  5. 配置访控策略(可选)(适用于6.4.1及后续版本)
  6. 配置流控策略(可选)(适用于6.4.1及后续版本)
  7. 测试发布的API
  8. 上下线服务(适用于6.4.1及后续版本)

### 步骤1：在您的App Java工程中编写Java类

获得本地开发环境，[请移步这里](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/ide/README.html>)。

### 步骤2：使用Java注解定义服务

RESTful服务类是一个普通pojo类，AWS的RESTful支持使用如下3类注解定义服务：

注解类型 | 说明  
---|---  
AWS RESTful注解 | **restful服务类需提供@Controller注解。 注解属性apiName定义本API唯一ID，该id在系统中将作为服务调用地址的一部分, 不允许包含空格等特殊符号； 注解属性type为常量:HandlerType.RESTFUL** ，含有该标志的服务在app启动时自动注册。  
JAX-RS注解 | 主持JAX-RS 1.1、2.0、[2.1](<https://www.jcp.org/en/jsr/detail?id=370>)主要功能。例如@Path，javax.ws.rs.Path是JAX-RS的路径注解，用于定义服务地址，更多注解可参考：[概述](<https://wenku.baidu.com/view/098bad36700abb68a882fb51.html?fr=search>)  
Swagger注解 | 例如 @OpenAPIDefinition ，io.swagger.v3.oas.annotations.OpenAPIDefinition是Swagger的注解，用于描述接口信息，支持[OpenAPI Specification V3](<https://swagger.io/specification/>)注解  
JAX-RS常见注解 | 说明  
---|---  
@GET | 指示方法使用HTTP GET访问，常用于查询，应做到幂等  
@POST | 指示方法使用HTTP POST访问，常用于资源的创建  
@PUT | 指示方法使用HTTP PUT访问，常用于资源的更新  
@DELETE | 指示方法使用HTTP DELETE访问，常用于资源的删除  
@PATCH | 指示方法使用HTTP PATCH访问，常用于资源的部分内容更新  
@HEAD | 指示方法使用HTTP HEAD访问，和GET类型，但没有响应数据  
@OPTIONS | 指示方法使用HTTP OPTIONS访问，较少使用，获得当前资源支持的操作  
@Path | 标注资源类或者方法的相对路径  
@PathParam | 可接收url路径参数  
@QueryParam | 可接收url中QueryString参数  
@FormParam | 可接收x-www-form-urlencoded参数  
@MatrixParam | 可接收url中;分割片段的参数  
@DefaultValue | 参数不存在时的默认值  
@Consumes | 输入参数的类型，例如@Consumes(MediaType.APPLICATION_FORM_URLENCODED)接收表单提交类型参数  
@Produces | 响应结果的类型，可加在类上或者方法上，例如@Produces({MediaType.APPLICATION_JSON})指示返回json格式数据  
@javax.inject.Singleton | 指示创建单例服务对象  
  
**示例**
    
    
    package com.actionsoft.apps.poc.api.local.restfulapi;
    
    import com.actionsoft.bpms.server.bind.annotation.Controller;
    import com.actionsoft.bpms.server.bind.annotation.HandlerType;
    
    import javax.ws.rs.*;
    import javax.ws.rs.core.Response;
    
    
    @Controller(type = HandlerType.RESTFUL, apiName = "helloapi", desc = "这是RESTful API示例")
    @Path("/hello")
    public class SayHello {
    
        @GET
        public String sayHello() {
            return "hello,world! - get";
        }
    
        @POST
        public String sayHelloPost() {
            return "hello,world!- post  ";
        }
    
    
        @Path("/param/{name}")
        @GET
        public String sayHelloparam(@PathParam("name") String name) {
            return "hello,world!-param  " + name;
        }
    
        @Path("/param2/{name}/{name2}")
        @GET
        public String sayHelloparam2(@PathParam("name") String name, @PathParam("name2") String name2)     {
            return "hello,world!-param2  " + name + "," + name2;
        }
    
        @Path("/QueryParam")
        @GET
        public String sayHelloQueryParam(@QueryParam("name") String name) {
            return "hello,world!-QueryParam  " + name;
        }
    
        @Path("/QueryParam2")
        @GET
        public String sayHelloQueryParam2(@QueryParam("name") String name, @QueryParam("name2") String name2) {
            return "hello,world!-QueryParam2  " + name + "," + name2;
        }
    
        @Path("/FormParam")
        @GET  //表单submit提交里的form参数。 postman 是在body里传参模拟
        public Response sayHelloFormParam(@FormParam("name") String name) {
            return Response.ok("hello,world!-FormParam  " + name).build();
        }
    
        @Path("/MatrixParam")
        @GET
        public Response sayHelloMatrixParam(@MatrixParam("name") String name, @MatrixParam("name2") String name2) {
            return Response.ok("hello,world!-MatrixParam " + name + "  " + name2).build();
        }
    
        @Path("/DefaultValue")
        @GET
        public Response sayHelloDefaultValue(@DefaultValue("name") String name, @DefaultValue("name2") String name2) {
            name = "abc";
            name2 = "123";
            return Response.ok("hello,world!-DefaultValue  " + name + "  " + name2).build();
        }
    
        @POST
        @Produces({MediaType.APPLICATION_JSON})  //此类后台可以接收json格式的String参数
        public String sayHelloPostBody(@RequestBody String  str) {
            System.out.println("----------");
            return "hello,world!- post  " + str;
        }
    
    }
    

### 步骤3：发布和浏览服务

将编写的程序编译成jar，存放到您自己的应用lib目录下（假设应用名称是com.abc.apps.do，那么路径应该在%AWS-HOME%/apps/install/com.abc.apps.do/lib），如果开发者引用了三方jar资源，也一同存放到该目录下。

然后进入CC连接服务，选择`发布 > HTTP API`发布RESTFul API。

  * 服务ID不允许包含空格等特殊符号
  * 服务ID将作为RESTFul API访问地址的一部分

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/restful1.gif)](<restful1.gif>)

**配置API在线文档说明**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/restful3.png)](<restful3.png>)

### 步骤4：配置身份策略

进入CC连接服务 > 策略，创建身份策略，策略类型为HTTP。 创建成功后，将策略配置到上述发布的RESTful API。 如果不配置身份策略，则在调用时，可传入AWS PaaS平台内存在的任意身份策略。 RESTful API 不支持无身份策略调用。

假设access_key为`Salesforce#1` ，secret为`0a799959-8327`

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/restful2.gif)](<restful2.gif>)

### 步骤5：配置访控策略(可选)

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
    
    
    package com.actionsoft.apps.poc.api.local.restfulapi;
    
    import com.actionsoft.bpms.cc.api.PermRequire;
    import com.actionsoft.bpms.cc.api.RequireType;
    import com.actionsoft.bpms.cc.api.perm.PermInstId;
    import com.actionsoft.bpms.cc.api.perm.PermRole;
    import com.actionsoft.bpms.cc.api.perm.PermUser;
    import com.actionsoft.bpms.server.bind.annotation.Controller;
    import com.actionsoft.bpms.server.bind.annotation.HandlerType;
    
    import javax.ws.rs.*;
    import javax.ws.rs.core.Response;
    
    
    @Controller(type = HandlerType.RESTFUL, apiName = "helloapi", desc = "这是RESTful API示例")
    @Path("/hello")
    @PermRequire({RequireType.APP, RequireType.CUSTOM, RequireType.ORG, RequireType.BO, RequireType.PROCESS, RequireType.ALL})
    // 访控类型注解，根据需要调整
    public class SayHello {
    
        @GET
        public String sayHello() {
            return "hello,world! - get";
        }
    
        @POST
        public String sayHelloPost() {
            return "hello,world!- post  ";
        }
    
    
        @Path("/param/{name}")
        @GET  //name参数，增加@PermUser注解，表示name校验组织权限
        public String sayHelloparam(@PermUser @PathParam("name") String name) {
            return "hello,world!-param  " + name;
        }
    
        @Path("/param2/{name}/{name2}")
        @GET  //name2 参数增加@PermRole注解，表示name2参数校验组织权限
        public String sayHelloparam2(@PathParam("name") String name, @PermRole @PathParam("name2") String name2) {
            return "hello,world!-param2  " + name + "," + name2;
        }
    
        @Path("/QueryParam")
        @GET
        //name参数增加 @PermInstId 注解，表示name校验流程范围
        public String sayHelloQueryParam(@PermInstId @QueryParam("name") String name) {
            return "hello,world!-QueryParam  " + name;
        }
    
        @Path("/QueryParam2")
        @GET
        public String sayHelloQueryParam2(@QueryParam("name") String name, @QueryParam("name2") String name2) {
            return "hello,world!-QueryParam2  " + name + "," + name2;
        }
    
        @Path("/FormParam")
        @GET
        public Response sayHelloFormParam(@FormParam("name") String name) {
            return Response.ok("hello,world!-FormParam  " + name).build();
        }
    
        @Path("/MatrixParam")
        @GET
        public Response sayHelloMatrixParam(@MatrixParam("name") String name, @MatrixParam("name2") String name2) {
            return Response.ok("hello,world!-MatrixParam " + name + "  " + name2).build();
        }
    
        @Path("/DefaultValue")
        @GET
        public Response sayHelloDefaultValue(@DefaultValue("name") String name, @DefaultValue("name2") String name2) {
            name = "abc";
            name2 = "123";
            return Response.ok("hello,world!-DefaultValue  " + name + "  " + name2).build();
        }
    
      @POST
        @Produces({MediaType.APPLICATION_JSON})  //此类后台可以接收json格式的String参数
        public String sayHelloPostBody(@RequestBody String  str) {
            System.out.println("----------");
            return "hello,world!- post  " + str;
        }
    
    }
    

**2.进入CC连接服务 > 策略，创建访控策略，策略类型为用于发布。 创建成功后，将策略配置到上述发布的RESTful API**

  1. 创建访控策略 [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/fk.png)](<fk.png>)
  2. 将访控策略绑定到已发布的SOAP API [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/restful6.png)](<restful6.png>)
  3. 为访控策略设置访问权限 [![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web4.png)](<web4.png>)

### 步骤6： 配置流控策略(可选)

进入CC连接服务 > 策略，创建流控策略。 创建成功后，将策略配置到上述发布的RESTful API**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/restful3.gif)](<restful3.gif>)

### 步骤7：测试发布的API

平台支持**HTTP Basic** 认证，在生产环境下建议使用HTTPS提供服务。

> 您可以使用Postman或者swagger ui等工具测试服务。

#### Postman

使用Postman调用RESTFul API参见[这里](<../restful/postman.html>)。

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/restful5.png)](<restful5.png>)

#### swagger UI

当您发布的RESTful API注解了 swagger3规范语法后，在发布的服务列表中 点击 `在线测试`可在线使用swagger ui进行测试，有关 Swagger的使用请参[见Swagger官网](<https://swagger.io/tools/swagger-ui/>)

> 如果触发流控或访控策略，则会提示"由于流控策略未通过，该请求被限制访问"或 "由于访控策略未通过，该请求被限制访问"

### 步骤9： 上下线服务

进入发布列表，点击服务上下线按钮，切换状态。 下线的服务，不允许调用。

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/web4.gif)](<web4.gif>)