# Redis - 连接分布式K/V缓存服务 · AWS PaaS文档中心

# Redis - 连接分布式K/V缓存服务

Redis 是一个高性能的key-value缓存/存储系统，由Pivotal旗下的SpringSource维护（<https://redis.io/）。>

主要功能

  * 支持Redis 6.0.6版本的缓存服务
  * 提供CCAPI封装，方便开发者使用
  * 支持CC环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/redis1.gif)](<redis1.gif>)

配置Redis适配器。

项 | 说明  
---|---  
名称 | Redis适配器的名称  
服务模式 | 常规(单机模式)/Sentinel(哨兵)/Cluster(集群)，redis不同的部署模式  
默认DB(dbindex) | 访问的db索引  
密码 | 认证密码，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
SSL | 使用ssl协议  
\--- 常规 --- | \--- 常规 ---  
服务器IP  
端口 | Redis服务器端口，Redis服务默认端口为6379  
\--- Sentinel(哨兵) --- | \--- Sentinel(哨兵) ---  
主服务名 | 主服务名  
节点 | 格式:`IP1:PORT1,IP2:PORT2`。支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
\--- Cluster(集群) --- | \--- Cluster(集群) ---  
节点 | redis集群节点列表，格式:`IP1:PORT1,IP2:PORT2`。支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
最大出错转发次数 | 集群模式失败转发次数  
\------ | \------  
最小空闲数 | 连接池维持的最小空闲连接  
最大空闲数 | 连接池维持的最大空闲连接  
最大连接数 | 连接池维持的最大并发连接  
描述 | 适配器描述信息  
  
## 2.调用

由开发者在Java代码中调用Redis服务。

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/redisuuid.png)](<redisuuid.png>)

### API代码示例

在访问前，我们假设已创建了一个CC Redis技术适配器，其分配的模型Id为`00000000`
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.RedisAPI;
    import com.actionsoft.sdk.local.api.cc.jedis.*;
    import com.actionsoft.sdk.local.api.cc.jedis.serializer.Serializer;
    import com.actionsoft.sdk.local.api.cc.jedis.serializer.StringSerializer;
    
    import java.util.Date;
    import java.util.Set;
    
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.redis/lib目录下
     */
    public class RedisAPITest extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
            //获得一个操作redis服务的RedisAPI对象
            RedisAPI<String,String> api = SDK.getCCAPI().getRedisAPI('00000000');
            api.serializer(new StringSerializer());
    
            //opsList()，这是定义key.   rightPush（）,在右边放值,每push一次，size就会加1
            api.opsList( "A1").rightPush("这是A1的值");
    
            //rightPop() 删除，pop一次，就会删除一个，list siZe就会减1
            api.opsList("A1").rightPop();
    
            //显示所有的List
            api.opsList("A1").range(0, redisAPI.opsList("A1").size());
    
            //关闭释放资源
            api.close();
    
            //...
        }
    }
    

> RedisAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/RedisAPI.html>

## 3.平台SESSION缓存放到Redis

把新建的Redis适配器ID配置到bin/conf/server.xml的redis.cc.id属性中，配置好后不需要重启平台服务

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/redis4.1.png)](<redis4.1.png>)

然后从`工具附加-Redis Connector`进入操作列表，找到`AWS PaaS实例控制台`应用中的缓存是 `com.actionsoft.bpms.commons.session.cache.SessionCache`，点击 `切换到Redis`将对应的操作切换到Redis,完成SESSION缓存放到Redis操作

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/redis4.2.png)](<redis4.2.png>)

> 缓存放到Redis,必须先实现RedisAdapter接口，否则无法切换到Redis，实现RedisAdapter接口示例详细参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/rediscache.html>)

## 4.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用RedisAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc RedisAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/RedisAPI.html>)说明。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log0.png)](<log0.png>)

### 记录访问请求到审计日志

开启后，将访问请求记录到审计日志，该日志存储在AWS PaaS平台SYS_AUDIT_LOG表中，可在`日志`页进行查看。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log.png)](<log.png>)

### 记录返回结果到文件日志

开启后，将请求数据和返回结果记录到文件日志，该日志存储在AWS PaaS平台%AWS_HOME%/logs/目录下，默认每个文件日志最大为20M，最多存储20个文件，超出将自动清除最早日期文件。 log文件个数及单文件最大值可在%AWS_HOME%/bin/conf/aws-log4j.xml文件中配置。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log1.png)](<log1.png>)

  * 存储在logs目录中的文件日志，无字符数限制，可将全部的result结果或错误日志全部记录下来

## 5.监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`SLA服务质量监控`后，当调用RDSAPI时，将自动对`调用次数、出错次数、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/sla.png)](<sla.png>)

## 6.删除

在连接列表，光标移至需要删除的模型上，点击右侧删除按钮，按钮提示进行删除。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/redisd.png)](<redisd.png>)

## 7.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 8.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>