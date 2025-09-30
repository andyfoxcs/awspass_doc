# 异常处理 | AWS 流程事件开发参考指南

## 异常处理

开发者应负责对自己代码的异常捕获和处理，除非你认为捕获也无法给出解决方案，可以继续抛出后交给引擎处理。事件要处理的异常分为两类：

  * 系统异常 不能处理的系统运行错误，如网络、IO异常，异常会中断操作
  * 业务异常 包含业务错误码的BPMNError，能够被流程引擎捕获处理

异常信息会被记录，并根据请求类型包装成格式化错误码和信息返回给调用者：

  * 来自用户操作 包装格式：HTML Document
  * 来自API JSON请求 包装格式：JSON Document
  * 来自API XML请求 包装格式：XML Document

### 建议

  * 如果一定要捕获，请明确catch异常的对象类型，避免使用catch (Exception e){...}捕获所有异常
  * 业务异常，请包装成BPMNError抛出(*替代AWS5中的MessageQueue)

> 有关异常处理，请参见<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/exception/README.html>