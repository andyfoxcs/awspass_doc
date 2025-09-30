# Elasticsearch - 连接Elasticsearch服务 | AWS CC连接中心参考指南

# Elasticsearch - 连接Elasticsearch服务

Elasticsearch是一个分布式、RESTful 风格的搜索和数据分析引擎（<https://www.elastic.co/cn/elasticsearch/），Elasticsearch> Connector为上层应用场景提供统一的ES服务访问和管理。

主要功能

  * 支持Elasticsearch 7.8版本的搜索引擎服务
  * 提供CCAPI封装，方便开发者使用
  * 支持CC环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/es.gif)

## 基本信息

配置Elasticsearch适配器。

项 | 说明  
---|---  
名称 | Elasticsearch适配器的名称  
服务器地址 | Elasticsearch服务地址，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
用户名 | 登录用户名，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
密码 | 登录密码，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
连接超时 | 连接超时时间  
请求超时 | 请求超时时间  
最大连接数 | 最大连接数，默认100  
描述 | 适配器描述信息，可在列表中显示  
  
## 2.调用

由开发者在Java代码中调用Elasticsearch服务，如创建删除索引。

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/es1.png)

### API代码示例

在访问前，我们假设已创建了一个CC Elasticsearch技术适配器，其分配的模型Id为`00000000`
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.EsAPI;
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.elasticsearch/lib目录下
     */
    public class ESAPITest extends ExecuteListener {
    
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
            EsAPI esAPI = SDK.getCCAPI().getESAPI("00000000");
    
            //判断索引库是否存在
            boolean exist =  esAPI.exist("aws_process");
    
            String json = "";
            //创建一条索引记录
            esAPI.create("aws_process","df718ac4-7095-4146-bb58-1111111111111",json);
            //删除索引记录
            esAPI.delete("aws_process","60cfd5df-221d-4d32-a766-77791463a3f7");
            //......
        }
    }
    

> ESAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/EsAPI.html>

## 3.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用EsAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc EsAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/EsAPI.html>)说明。 ![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log0.png)

### 记录访问请求到审计日志

开启后，将访问请求记录到审计日志，该日志存储在AWS PaaS平台SYS_AUDIT_LOG表中，可在`日志`页进行查看。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/eslog.png)

### 记录返回结果到文件日志

开启后，将请求数据和返回结果记录到文件日志，该日志存储在AWS PaaS平台%AWS_HOME%/logs/目录下，默认每个文件日志最大为20M，最多存储20个文件，超出将自动清除最早日期文件。 log文件个数及单文件最大值可在%AWS_HOME%/bin/conf/aws-log4j.xml文件中配置。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log1.png)

## 4.监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`SLA服务质量监控`后，当调用RDSAPI时，将自动对`调用次数、出错次数、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/sla.png)

## 5.删除

在连接列表，光标移至需要删除的模型上，点击右侧删除按钮，按钮提示进行删除。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/es4.png)

## 6.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 7.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>