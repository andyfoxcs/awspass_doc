# 异常处理 · AWS PaaS文档中心

# 异常处理

主要面对两类异常的处理，系统异常和业务异常。

  * 系统异常可以通过捕获SOAP客户端异常进行处理。通常由Web服务框架抛出，可能是服务未启动、服务不可用、框架捕获的未处理异常等
  * 业务异常需要检查服务返回对象的errorCode参数是否为null或者空。错误码[参见这里](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/error-code.html>)

应当对SOAP处理结果进行检查，当存在 [AWS服务特定错误码](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/error-code.html>)（如下）的请求结果时，表示该服务未被执行，可以重试。但是，如果是客户端错误 (4xx) 表示您需要对请求本身进行修改，纠正该问题，然后再重试。

**特定的错误码**

  * 590（AWS Instance Server连接失败）
  * 591（处理AWS Instance Server响应时发生错误）
  * 760（服务正在启动(Instance Starting)）
  * 761（服务正在关闭(Instance Stoping)）
  * 762（服务脱机(Instance Offline)）
  * 770（应用正在启动(App Starting)）
  * 771（应用正在关闭(App Stoping)）
  * 772（应用脱机(App Offline)）
  * 800（许可配额限制(Quota Limit)）