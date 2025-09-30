# 异常处理 · AWS PaaS文档中心

## 异常处理

当异常被AWS MVC顶层框架捕获后，会根据cmd请求类型处理成客户端能够理解的文档格式。

请求类型 | 格式  
---|---  
./w | HTML Document  
./jd | JSON Document  
./xd | XML Document  
  
### Java Exception处理

当发生底层Java异常或其他非`AWSException`异常时，AWS MVC将该异常封装成`500`错误。

### 异常日志

捕获的异常被记录至AWS logs目录下，详细参见 <https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/index.html>

### HTML Document警告页面

[![html异常页面](https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/html.png)](<html.png>)

### JSON Document数据结构

[![JSON数据结构](https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/json.png)](<json.png>)

### XML Document数据结构

[![XML数据结构](https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/xml.png)](<xml.png>)