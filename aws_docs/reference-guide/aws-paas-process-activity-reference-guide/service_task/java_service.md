# 调用普通Java服务 | AWS BPMN2 Activity参考指南

# 调用普通Java服务

调用一个外部Java类。如果具有通用性，建议封装成公共[流程服务](<process_service.html>)。

![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/code.png)

> 注意：程序员开发的Java服务类，编译后的jar包资源必须与该流程模型处于同一个AWS PaaS应用

### 开发

继承[ServiceDelegate](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/servicetask/ServiceDelegate.html>)抽象类，实现[InterruptListenerInterface](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/listener/InterruptListenerInterface.html>)接口的execute()方法。

这是一个标准的AWS[中断类](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/introduction/interface.html>)事件编程，与其他流程事件开发过程相似，此处不再详细介绍。

**ServiceDelegate提供的主要方法：**

  * **getProcessVariable** 读取一个流程变量的值，同一次事件内多次读取时做了临时缓存优化
  * **getBODatas** 读取指定流程的BO表数据记录，同一次事件内多次读取时做了临时缓存优化

**异常处理**

  * Java程序抛出异常，按[异常策略](<exception.html>)处理

### 注册

  1. 在流程设计器打开系统任务的属性
  2. 服务类型选择`普通服务`
  3. 在`服务实现`填入开发好的Java类全路径

### Sample Code
    
    
    public class TestService extends ServiceDelegate {
    
        public TestService() {
            // TODO Auto-generated constructor stub
        }
    
        @Override
        public boolean execute(ProcessExecutionContext ctx) throws Exception {
            // your java code
            return true;
        }
    }
    

### 延伸阅读

  * [如何开发流程事件？](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/introduction/how.html>)
  * [ServiceDelegate抽象类JavaDoc](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/servicetask/ServiceDelegate.html>)