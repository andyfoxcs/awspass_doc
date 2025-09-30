# 调用公共流程服务 | AWS BPMN2 Activity参考指南

# 调用公共流程服务

`流程服务`本质上也是一个外部Java类。与普通Java服务不同的是，`流程服务`具有如下特点：

  * 可以封装`输入`和`输出`标准，能与流程的上下文数据进行映射
  * 可以封装特定的参数配置页面（如`SQLScript`服务配置CC和SQL）
  * 封装的服务可以被关联的应用调用，实现跨应用复用

### 从流程服务库选择

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/21.png)

> 注意：默认只能访问父应用的流程服务，可以在应用的`manifest.xml`增加对其他应用的关联
    
    
      <requires>
        <require appId="xxx" notActiveHandler="none"/>
      </requires>
    

### InMapping设置

InMapping过程是将当前流程模型的`流程变量`、BO数据源字段、[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)作为参数值，映射给流程服务的`输入`参数。

当服务被调用时，InMapping负责参数向服务的传递。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/22.png)

##### 使用自定义常量

对于入参是特定常量，可以在映射画布上直接定义。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/23.png)

#####使用@公式 \--> 所有的[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)和@公式组合都可用于`输入`参数的映射。 ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/24.png)

### OutMapping设置

当服务被调用时，OutMapping负责将返回结果传递给当前流程实例的数据对象。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/25.png)

与InMapping相似，可以使用`自定义常量`作为返回结果。

### 开发流程服务

程序员可以基于接口开发实现，通过CC的`流程服务`进行注册。详细开发过程请[参考这里](<../appendix/process_service.html>)

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/code.png)

> 注意：程序员开发的Java服务类，编译后的jar包资源必须与该流程模型处于同一个AWS PaaS应用

### 延伸阅读

  * [HelperService抽象类JavaDoc](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/servicetask/HelperService.html>)
  * [如何封装CC的流程服务](<../appendix/process_service.html>)
  * [内置的SQLScript服务](<../appendix/sqlscript.html>)
  * [内置的邮件发送服务](<../appendix/sendmail.html>)
  * [内置的消息通知服务](<../appendix/notification.html>)