# HTTP - 连接Web服务 | AWS CC连接中心参考指南

# HTTP - 连接Web服务

HTTP（HyperText Transfer Protocol，超文本传输协议） 是一种可让开发者在程序和建模时直接访问PaaS外部Web URL服务的技术适配器。

主要功能

  * 支持符合HTTP 1.1/2.0规范的POST/GET/PUT/DELETE服务调用
  * 发布的API支持3.0.0 版本的 OpenAPI 规范
  * 提供CCAPI封装，方便开发者使用
  * 支持秘钥身份和CC环境变量，发布的API服务支持流控策略、访控策略
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关
  * 提供结果日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1
  * 使用该应用要求必须安装SOAP Connector应用

> 适用于企业内、外的移动互联网架构接口访问

## 1.配置

![](http1.png)

项 | 说明  
---|---  
名称 | 名称  
验证身份 | 使用用户名、密码验证调用  
URL地址 | URL地址  
请求方法 | 支持`POST、GET、PUT、DELETE`  
参数编码 | 默认为UTF-8  
连接超时 | 设置连接超时时间  
请求超时 | 设置连接超时时间  
最大并发数 | 设置最大并发数  
请求参数 | 配置请求参数  
  
## 2.调用

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

![](http2.png)

### API代码示例

在访问前，我们假设已创建了一个CC HTTP技术适配器，其分配的模型Id为00000000
    
    
    package com.actionsoft.cc.CCAPI;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.HttpAPI;
    
    public class HTTPAPITest extends ExecuteListener {
    
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
            //HTTP
            HttpAPI httpAPI = SDK.getCCAPI().getHttpAPI("00000000");
            String str =  httpAPI.get("https://demo.awspaas.com/r/jd?cmd=com.actionsoft.apps.www.news_query&group1=&group2=&year=&month=&firstRow=&rowCount");
            httpAPI.bodyForm("group2", "文档").post("https://demo.awspaas.com/r/jd?cmd=com.actionsoft.apps.www.news_query&group1=&year=&month=&firstRow=&rowCount");
            httpAPI.bodyForm (new String[][]{{"month","6"},{"year","2017"}}) .post("https://demo.awspaas.com/r/jd?cmd=com.actionsoft.apps.www.news_query&group1=&firstRow=&rowCount");
            httpAPI.query("group2", "文档").post("https://demo.awspaas.com/r/jd?cmd=com.actionsoft.apps.www.news_query&group1=&year=&month=&firstRow=&rowCount");
            httpAPI.query(new String[][]{{"month","6"},{"year","2017"}}).post("https://demo.awspaas.com/r/jd?cmd=com.actionsoft.apps.www.news_query&group1=&firstRow=&rowCount");
            //........
            httpAPI.close();
        }
    }
    

> HttpAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/HttpAPI.html>

## 3.平台使用场景

  1. 所有支持JSON数据源的UI组件，如列表、单选组、复选框、数据字典、树形字典
  2. 流程`人工任务`的参与者，路由方案使用`服务API/用户来自REST服务`，从URL结果指定执行人

## 4.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用HttpAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc HttpAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/HttpAPI.html>)说明。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log0.png)

### 记录访问请求到审计日志

开启后，将访问请求记录到审计日志，该日志存储在AWS PaaS平台SYS_AUDIT_LOG表中，可在`日志`页进行查看。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log.png)

### 记录返回结果到文件日志

开启后，将请求数据和返回结果记录到文件日志，该日志存储在AWS PaaS平台%AWS_HOME%/logs/目录下，默认每个文件日志最大为20M，最多存储20个文件，超出将自动清除最早日期文件。 log文件个数及单文件最大值可在%AWS_HOME%/bin/conf/aws-log4j.xml文件中配置。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log1.png)

## 5.监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`SLA服务质量监控`后，当调用RDSAPI时，将自动对`调用次数、出错次数、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/sla.png)

## 6.删除

在连接列表，光标移至需要删除的模型上，点击右侧删除按钮，按钮提示进行删除。

![](http3.png)

## 7.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 8.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>

## 9.发布HTTP API

详细参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_http_api.html>)。

## 10.发布RESTful API

详细参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_restful_api.html>)。