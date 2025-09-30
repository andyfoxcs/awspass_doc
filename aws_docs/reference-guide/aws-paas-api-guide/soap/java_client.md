# 使用JDK客户端 · AWS PaaS文档中心

# 使用JDK自带WebService框架

本章节介绍如何在不使用第三方框架的情况下，用JDK调用Web Service。

**注意：**

  * JDK1.6或更高版本才提供Web Service实现。
  * 目前JDK对WS-*规范的支持不够完善，例如发送WS-Security规范要求的用户名密码时需要借助其它服务框架，因此本章没有安全验证。 _（AWS PaaS提供的官方SOAP API要求必须有用户名密码验证，因此本章节调用方式不支持由AWS PaaS提供的官方SOAP API）_

## JAX-WS Proxy方式调用服务

#### 调用步骤

**1.准备JDK1.6或以上版本**

**2.生成服务客户端文件**

使用JDK bin目录下的wsimport命令生成服务客户端文件，如果不指定。

**示例**
    
    
    wsimport -keep -clientjar app_service_client.jar "http://localhost:8088/portal/r/s?service=appApi&wsdl=true"
    

命令行参数说明:

  * keep 指示不删除生成的java源文件
  * clientjar 指示编译生成的java源文件并打包为app_service_client.jar，该Jar用于引入到被调用工程JAR类库中

> 可以使用-d参数指示文件目录，默认文件位置是当前工作目录

**3.获得服务和代理对象**

在生成的app_service_client.jar中有2个重要的类，如下：

项 | 说明  
---|---  
AppApi | AppApi是服务类，继承javax.xml.ws.Service，它的名字默认和wsdl中服务名称对应，wsdl:service的name属性，该类用于创建服务对象实例  
AppApiPortType | AppApiPortType类是该服务的SEI(service endpoint interface)，可以得到代理对象实例  
  
AppApi的构造函数中可以指定3个参数：

项 | 说明  
---|---  
java.net.URL wsdlDocumentLocation | WSDL路径，默认使用app_service_client.jar中备份的生成源WSDL  
QName serviceName | 该参数指定调用哪个服务  
WebServiceFeature... features | 服务的特殊功能或者处理，例如MTOMFeature可以指定是否优化附件传输  
  
通过生成的服务类获得代理对象的代码示例：
    
    
    AppApi api = new AppApi();
    AppApiPortType port = api.getAppApiPort();
    

通过javax.xml.ws.Service和SEI得到代理对象：
    
    
    URL wsdlURL = new URL("http://localhost:8088/portal/r/s?service=appApi&wsdl=true");
    QName SERVICE_NAME = new QName("http://service.sdk.actionsoft.com/", "AppApi");
    Service service = Service.create(wsdlURL, SERVICE_NAME);
    AppApiPortType client = service.getPort(AppApiPortType.class);
    

**4.通过代理对象调用服务**
    
    
    AppApiPortType client = service.getPort(AppApiPortType.class);
    BoolResponse result = client.isInstalled("com.actionsoft.apps.notification");
    

## JAX-WS Dispatch方式调用服务

### 调用步骤

**1.准备JDK1.6或以上版本**

**2.获得服务和Dispatch对象**

  * 获得服务对象的方式可以参考`JAX-WS Proxy方式调用服务`
  * Dispatch对象可以通过服务对象获得，支持payload和message 2种模型，其中：

项 | 说明  
---|---  
payload | 关心SOAP消息中的body部分，可以通过把带有JAXB注解的Java对象或者XML source两种方法传递给dispatch来调用Web service  
message | 需要传入整个的soap消息的xml内容  
  
**3.通过Dispatch对象调用服务**

代码示例：
    
    
    import java.net.URL;
    import javax.xml.transform.Source;
    import javax.xml.ws.Dispatch;
    import javax.xml.ws.Service;
    ...
    
    URL wsdlURL = new URL("http://localhost:8088/portal/r/s?service=appApi&wsdl=true");
    Service service = Service.create(wsdlURL,
    new QName("http://service.sdk.actionsoft.com/", "AppApi"));
    Dispatch<Source> disp = service.createDispatch(
    new QName("http://service.sdk.actionsoft.com/",
    "AppApiPort"), Source.class, Service.Mode.PAYLOAD);
    
    Source request = new StreamSource("<appId>com.actionsoft.apps.notification</appId>")
    Source response = disp.invoke(request);