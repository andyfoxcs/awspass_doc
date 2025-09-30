# 使用CXF客户端 · AWS PaaS文档中心

# 使用CXF客户端

CXF支持JAX-WS Proxy和JAX-WS Dispatch的服务调用方式。本章提供CXF安全验证的代码样例，但因为Proxy和Dispatch安全验证的处理方式差距不大，所以我们此处仅提供CXF使用JAX-WS Proxy方式调用服务的示例。

更详细的CXF服务调用也可参见：<http://cxf.apache.org/docs/how-do-i-develop-a-client.html#HowdoIdevelopaclient?-BuildingClients。>

## JAX-WS Proxy方式调用服务

### 环境准备

  * JDK1.6或以上版本
  * CXF运行类库。建议使用AWS PaaS平台默认提供的CXF类库，该类库文件在：`%AWS-HOME%/bin/lib/ws/cxf-2.7.12`目录
  * JAVA日志组件类库。`%AWS-HOME%/bin/lib/commons-logging-1.1.1.jar`

### 场景

调用`appApi`服务的isInstalled方法判断AWS PaaS是否安装了某个应用。

**假定服务端配置用户名密码认证、密码加密传输**
    
    
    用户名：Salesforce#1
    密码：0a799959-8327
    

### 步骤

  1. 获得服务和代理对象。如何获得服务和代理对象可以参考`使用JDK客户端`中`JAX-WS Proxy方式调用服务`章节。**CXF自己提供了一个WSDL2Java的工具也可以实现JDK wsimport类似的功能，如果您想使用这种方式，需要下载CXF，在bin目录下找到该命令。**  
  

  2. 通过代理对象调用服务  

**关于服务安全**

CXF有2个和安全相关的拦截器：

  * WSS4JInInterceptor(负责处理接收的消息)
  * WSS4JOutInterceptor（负责处理发送的消息）

需要将JAX-WS和CXF框架结合起来，这样就可以使用CXF框架处理服务安全了。结合的方法如下：

调用方式 | CXF框架和JAX-WS结合方式  
---|---  
JAX-WS Proxy | 在代理对象上得到CXF客户端：  
Client client = ClientProxy.getClient(port);  
port为代理对象，参考`使用JDK客户端`中`JAX-WS Proxy方式调用服务`了解如何获得此对象  
JAX-WS Dispatch | 将Dispatch对象强转为CXF Dispatch实现获得Client对象：  
Client client = ((DispatchImpl) dip).getClient();  
dip为Dispatch对象，参考`使用JDK客户端`中`JAX-WS Dispatch方式调用服务`了解如何获得此对象  
  
然后通过CXF client对象就可以增加各种拦截器处理消息了：
    
    
    client.getOutInterceptors().add(interceptor);
    

**完整的CXF示例代码**
    
    
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    import javax.security.auth.callback.Callback;
    import javax.security.auth.callback.CallbackHandler;
    import javax.security.auth.callback.UnsupportedCallbackException;
    
    import org.apache.cxf.endpoint.Client;
    import org.apache.cxf.frontend.ClientProxy;
    import org.apache.cxf.ws.security.wss4j.WSS4JOutInterceptor;
    import org.apache.ws.security.WSConstants;
    import org.apache.ws.security.WSPasswordCallback;
    import org.apache.ws.security.handler.WSHandlerConstants;
    
    import com.actionsoft.sdk.service.AppApi;
    import com.actionsoft.sdk.service.AppApiPortType;
    import com.actionsoft.sdk.service.BoolResponse;
    
    public class AppApiClient {
    
        public static void main(String[] args) {
            // 构造拦截器，设置用户名密码属性和认证类型
            Map<String, Object> outProps = new HashMap<String, Object>();
            outProps.put(WSHandlerConstants.ACTION,
            WSHandlerConstants.USERNAME_TOKEN);
            //outProps.put(WSHandlerConstants.PASSWORD_TYPE,
            WSConstants.PW_TEXT);//密码明文还是密文，不设置时默认密文
            outProps.put(WSHandlerConstants.USER, "Salesforce#1");
            outProps.put(WSHandlerConstants.PW_CALLBACK_REF, new UTSetPasswordCallback());
            WSS4JOutInterceptor interceptor = new WSS4JOutInterceptor(outProps);
            // 注入cxf的拦截器增加用户名密码
            AppApi api = new AppApi();
            AppApiPortType port = api.getAppApiPort();
            Client client = ClientProxy.getClient(port);
            client.getOutInterceptors().add(interceptor);
            // 服务方法调用
            BoolResponse r = port.isInstalled("com.actionsoft.apps.notification");
            // 业务异常判断
            if (r.getErrorCode() == null) {
                System.out.println(r.isData());
            } else {
                System.out.println(r.getErrorCode() + "," + r.getMsg());
            }
        }
    
        private static class UTSetPasswordCallback implements CallbackHandler {
            public void handle(Callback[] callbacks)
            throws IOException, UnsupportedCallbackException {
                for (int i = 0; i < callbacks.length; i++) {
                    WSPasswordCallback pc = (WSPasswordCallback) callbacks[i];
                    if ("Salesforce#1".equals(pc.getIdentifier())) {
                        pc.setPassword("0a799959-8327");
                        return;
                    }
                }
            }
        }
    }
    

> CXF通过支持WS-Security规范提供服务安全支持。包括用户名密码认证，基于X509的认证、签字、加密，如果您需要用到这些，**请参考CXF安装包samples目录下ws_security中程序示例** 。

## Simple Frontend Client Proxy(CXF私有调用方式)

这类调用方式依赖CXF类库

**代码示例**
    
    
    import org.apache.cxf.frontend.ClientProxyFactoryBean;
    ...
    
    ClientProxyFactoryBean factory = new ClientProxyFactoryBean();
    factory.setServiceClass(AppApiPortType.class);
    factory.setAddress("http://localhost:8088/portal/r/s?service=appApi");
    AppApiPortType client = (AppApiPortType) factory.create();
    

## Dynamic Client(CXF私有调用方式，不推荐使用)

这类调用方式性能较差，对复杂对象的构造复杂

**代码示例**
    
    
    JaxWsDynamicClientFactory dcf = JaxWsDynamicClientFactory.newInstance();
    Client client = dcf.createClient("http://localhost:8088/portal/r/s?service=appApi&wsdl=true");
    
    Object[] res = client.invoke("isInstalled", "com.actionsoft.apps.notification");
    System.out.println("response: " + res[0]);