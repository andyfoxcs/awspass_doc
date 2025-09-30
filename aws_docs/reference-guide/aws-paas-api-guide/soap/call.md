# 调用服务 · AWS PaaS文档中心

# 调用服务

SOAP API的调用需要Web Service客户端框架，有多种框架选择(不建议同时用多个框架，避免出现类库冲突)，例如：

  * [Apache CXF](<http://cxf.apache.org/>)
  * [Apache Axis2](<http://axis.apache.org/axis2/java/core/>)
  * JDK1.8。不支持WS-*规范，无法方便的处理WS-Security安全

JAX-WS(Java API for XML-Based Web Services、JSR224)提供了2种调用服务的方式：

  * JAX-WS Proxy
  * JAX-WS Dispatch

## 示例

  * [使用SoapUI工具](<soapui.html>)
  * [使用CXF客户端](<cxf.html>)
  * [使用JDK客户端](<java_client.html>)