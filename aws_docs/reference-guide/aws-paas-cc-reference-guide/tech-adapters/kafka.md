# Kafka - 连接分布式消息服务 · AWS PaaS文档中心

# Kafka - 连接分布式消息服务

Kafka是LinkedIn贡献给Apache的开源时时流处理平台（<http://kafka.apache.org/）。>

主要功能

  * 支持Kafka 2.5版本的流消息服务
  * 提供CCAPI封装，方便开发者使用
  * 提供Kafka Producer(向Kafka发送消息)的流程可编排服务(Service Task)
  * 支持CC部署环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/kafka.gif)](<kafka.gif>)

## 基本信息

配置Kafka适配器。

项 | 说明  
---|---  
名称 | Kafka适配器的名称  
服务地址 | 设置bootstrap.server，格式：host1:port1,host2:port2支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
描述 | 适配器描述信息  
  
## 扩展属性

配置Kafka发送、接收消息的类型。仅支持配置一种类型，如需处理多种类型消息，请创建多个Kafka连接器。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/kafka4.png)](<kafka4.png>)

## 2.调用

由开发在Java代码中调用Kafka服务。

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/kafkauuid.png)](<kafkauuid.png>)

### API代码示例

在访问前，我们假设已创建了一个CC Kafka技术适配器，其分配的模型Id为`00000000`
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.KafkaAPI;
    
    import org.apache.kafka.clients.consumer.Consumer;
    import org.apache.kafka.common.PartitionInfo;
    import org.apache.kafka.common.TopicPartition;
    
    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.List;
    import java.util.Map;
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.kafka/lib目录下
     */
    public class KafkaAPITest extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
             //获得一个操作KafkaAPI服务的getKafkaAPI对象
            KafkaAPI<String,String> kafkaAPI = SDK.getCCAPI().getKafkaAPI("00000000");
    
            // 刷新相关(需在send之前设置，否则不生效)
            kafkaAPI.autoFlush(true);//设为true，每次发送后刷新
    
            //发送消息到指定topic
            kafkaAPI.sendTopic("test","heelo");
            //消息接收
            kafkaAPI.execute(new KafkaAPI.ConsumerCallback<String, String>() {
    
                @Override
                public void doInKafka(Consumer<String, String> consumer) {
                    List<PartitionInfo> list = consumer.partitionsFor("test");
                    List<TopicPartition> tps = new ArrayList<TopicPartition>();
                    for (PartitionInfo pi : list) {
                        TopicPartition tp = new TopicPartition(pi.topic(), pi.partition());
                        tps.add(tp);
                        consumer.assign(Collections.singletonList(tp));
                        long l = consumer.position(tp);
                        System.out.println("position:" + tp + "," + l);
                    }
                    Map<TopicPartition, Long> boff = consumer.beginningOffsets(tps);
                    Map<TopicPartition, Long> eoff = consumer.endOffsets(tps);
                    System.out.println("Offsets:" + boff + "," + eoff);
                }
            });
    
            //........
    
            //关闭释放资源
            kafkaAPI.close();
    
        }
    }
    

> KafkaAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/KafkaAPI.html>

## 3\. 流程编排服务

该应用提供Kafka Producer(向Kafka发送消息)的流程编排服务(Service Task)。进行连接服务`发布`页签可进行查看。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/kafka2.png)](<kafka2.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/kafka3.png)](<kafka3.png>)

### 调用

操作步骤：

  1. 创建一个流程模型
  2. 拖动一个系统任务至画布
  3. 配置系统任务，服务类型为`流程服务`，选择该流程服务，配置相关信息
  4. 完成流程模型的正确设计，创建流程实例，到任务到达系统任务时，即可发送消息

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/kafka0.png)](<kafka0.png>)

## 4.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用KafkaAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc KafkaAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/KafkaAPI.html>)说明。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log0.png)](<log0.png>)

### 记录访问请求到审计日志

开启后，将访问请求记录到审计日志，该日志存储在AWS PaaS平台SYS_AUDIT_LOG表中，可在`日志`页进行查看。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log.png)](<log.png>)

### 记录返回结果到文件日志

开启后，将请求数据和返回结果记录到文件日志，该日志存储在AWS PaaS平台%AWS_HOME%/logs/目录下，默认每个文件日志最大为20M，最多存储20个文件，超出将自动清除最早日期文件。 log文件个数及单文件最大值可在%AWS_HOME%/bin/conf/aws-log4j.xml文件中配置。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log1.png)](<log1.png>)

## 5.监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`SLA服务质量监控`后，当调用RDSAPI时，将自动对`调用次数、出错次数、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/sla.png)](<sla.png>)

## 6.删除

在连接列表，光标移至需要删除的模型上，点击右侧删除按钮，按钮提示进行删除。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/kafkad.png)](<kafkad.png>)

## 7.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 8.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>