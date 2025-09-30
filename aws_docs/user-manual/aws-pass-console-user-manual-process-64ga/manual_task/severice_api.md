# 服务API · AWS PaaS文档中心

## 服务API

### 方案41：服务API/用户来自SOAP服务

通过CC SOAP连接，从Web服务中读取账户列表，多个账户空格隔开。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa27.png)](<fa27.png>)

项 | 说明  
---|---  
服务 | 显示当前应用所有【SOAP 连接Web Service服务】类型的服务  
参数 | 必填项，可在路由方案开发的类中使用该参数，由该参数判断路由结果  
  
**_SOAP 连接Web Service服务说明_**

  1. 进入`应用开发>连接服务`，新建`Service Regist 服务注册`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa27-1.png)](<fa27-1.png>)

  2. Java代码如下
         
         package com.actionsoft.luyou;
         
          import javax.jws.WebParam;
          import javax.jws.WebService;
         
          @WebService(serviceName = "SOAPLuYou")
          public class SOAPLuYou {
         
              public String getAWSUser(@WebParam(name = "str1") String str){
                  if(str.equals("AWS")){ //str为路由方案中参数
                      return "admin aws-test";
                  }else {
                      return null;
                  }
              }
          }
         

  3. 新建`SOAP 连接Web Service服务`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa27-2.png)](<fa27-2.png>)

#### 延伸阅读

  * [封装和发布自己的SOAP API](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_soap_api.html>)
  * [AWS CC连接中心参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide>)

### 方案42：服务API/用户来自REST服务

通过CC HTTP连接，从Web服务中读取账户列表，多个账户空格隔开。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa28.png)](<fa28.png>)

项 | 说明  
---|---  
服务 | 显示当前应用所有【HTTP 连接Web服务】类型的服务  
参数 | 必填项，可在路由方案开发的类中使用该参数，由该参数判断路由结果  
  
**_HTTP 连接Web服务说明_**

  1. 进入`应用开发>连接服务`，新建`HTTP 连接Web服务`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/fa28-1.png)](<fa28-1.png>)

  2. JSP页面代码如下
         
         <%
         // 返回必须是JSON格式，且key（result、msg、data{participants:}）固定,participants表示返回的账户，多个账户间用空格隔开
         JspWriter out1 = pageContext.getOut();
         out1.print("{\"result\":\"ok\",\"msg\":\"成功\",\"data\":{\"participants\":\"admin aws-test\"}}");
         out1.flush(); //刷新缓冲区
         %>
         

#### 延伸阅读

  * [封装和发布自己的HTTP API](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_http_api.html>)
  * [AWS CC连接中心参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide>)