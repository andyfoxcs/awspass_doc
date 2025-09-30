# MongoDB - 连接文档型数据库服务 · AWS PaaS文档中心

# MongoDB - 连接文档型数据库服务

MongoDB 是一个基于分布式文件存储的数据库（<https://www.mongodb.com/）> ，它的特点是高性能、易部署、易使用，存储数据非常方便。MongoDB 介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。

主要功能

  * 支持MongoDB 4.2版本的文档数据库服务
  * 提供CCAPI封装，方便开发者使用
  * 支持CC部署环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/mongodb.gif)](<mongodb.gif>)

## 基本信息

配置MongoDB适配器。

项 | 说明  
---|---  
名称 | MongoDB适配器的名称  
服务地址 | MongoDB服务地址，格式：`host1:port1,host1:port2`，<br/>支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
默认库 | 默认操作的mongo库  
验证库 | 验证认证信息的mongo库，空时使用默认库  
用户名 | 认证账户，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
密码 | 认证口令，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
复制集 | 复制集replSet的名称  
连接超时 | 连接超时时间  
请求超时 | 请求超时时间  
最大连接数 | 最大并发数  
SSL | 是否开启SSL安全通信  
描述 | 适配器描述信息  
  
## 2.调用

由开发者在Java代码中调用MongoDB服务。

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/mongouuid.png)](<mongouuid.png>)

### API代码示例

在访问前，我们假设已创建了一个CC MongoDB技术适配器，其分配的模型Id为`00000000`
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.MongoDBAPI;
    import org.bson.BsonDocument;
    import org.bson.Document;
    import org.bson.codecs.configuration.CodecRegistry;
    import org.bson.conversions.Bson;
    
    import java.util.Arrays;
    
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.MongoDB/lib目录下
     */
    public class MongoDBAPITest extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
    
            //获得一个MongoDB对象
            MongoDBAPI mongoDBAPI = SDK.getCCAPI().getMongoDBAPI("00000000");
    
            //记录数
            long n = mongoDBAPI.count("orgcompany");
    
            //创建Document
            Document doc = new Document("name", "MongoDB")
                     .append("type", "database")
                     .append("count", 1)
                     .append("versions", Arrays.asList("v3.2", "v3.0", "v2.6"))
                     .append("info", new Document("x", 203).append("y", 102));
    
            //插入一条
            mongoDBAPI.insertOne("conn", doc);
    
            //取出第一条
            Document myDoc = mongoDBAPI.find("conn").first();
            //......
        }
    }
    

> MongoDBAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/MongoDBAPI.html>
> 
> MongoDB Driver Quick Start: <http://mongodb.github.io/mongo-java-driver/3.5/driver/getting-started/quick-start/>

## 3.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用MongoDBAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc MongoDBAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/MongoDBAPI.html>)说明。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log0.png)](<log0.png>)

### 记录访问请求到审计日志

开启后，将访问请求记录到审计日志，该日志存储在AWS PaaS平台SYS_AUDIT_LOG表中，可在`日志`页进行查看。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log.png)](<log.png>)

### 记录返回结果到文件日志

开启后，将请求数据和返回结果记录到文件日志，该日志存储在AWS PaaS平台%AWS_HOME%/logs/目录下，默认每个文件日志最大为20M，最多存储20个文件，超出将自动清除最早日期文件。 log文件个数及单文件最大值可在%AWS_HOME%/bin/conf/aws-log4j.xml文件中配置。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log1.png)](<log1.png>)

## 4.监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`SLA服务质量监控`后，当调用RDSAPI时，将自动对`调用次数、出错次数、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/sla.png)](<sla.png>)

## 5.删除

在连接列表，光标移至需要删除的模型上，点击右侧删除按钮，按钮提示进行删除。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/mongod.png)](<mongod.png>)

## 6.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 7.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>