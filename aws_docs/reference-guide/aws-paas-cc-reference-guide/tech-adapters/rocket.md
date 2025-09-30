# RocketMQ - 连接RocketMQ服务 · AWS PaaS文档中心

# RocketMQ - 连接RocketMQ服务

RocketMQ是阿里巴巴贡献给Apache的开源分布式消息中间件（<http://rocketmq.apache.org/），RocketMQ> Connector为上层应用场景提供统一的RocketMQ服务访问和管理。

主要功能

  * 支持RocketMQ 4.7版本的消息队列服务
  * 提供CCAPI封装，方便开发者使用
  * 提供RocketMQ Producer(向RocketMQ发送消息)的流程编排服务(Service Task)
  * 支持CC环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rocket.gif)](<rocket.gif>)

配置RocketMQ适配器。

项 | 说明  
---|---  
名称 | RocketMQ适配器的名称  
注册中心地址 | 设置RockeMQ的nameserver地址，示例：127.0.0.1:9876，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
最小消费者线程数量 | 设置MQ的consumeThreadMin，范围[0,1000]  
最大消费者线程数量 | 设置MQ的consumeThreadMax，范围[0,1000]  
一次消费消息数量 | 设置MQ的consumeMessageBatchMaxSize，一次消费消息的条数，默认为1条  
描述 | 适配器描述信息  
  
## 2.调用

由开发在Java代码中调用RocketMQ服务。

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rocketuuid.png)](<rocketuuid.png>)

### API代码示例

在访问前，我们假设已创建了一个CC RocketMQ技术适配器，其分配的模型Id为`00000000`
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.bpms.cc.Consumer;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.RocketmqAPI;
    import org.apache.rocketmq.client.consumer.MQPushConsumer;
    import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyContext;
    import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyStatus;
    import org.apache.rocketmq.client.consumer.listener.MessageListenerConcurrently;
    import org.apache.rocketmq.client.producer.MQProducer;
    import org.apache.rocketmq.client.producer.SendResult;
    import org.apache.rocketmq.common.message.Message;
    import org.apache.rocketmq.common.message.MessageExt;
    import org.apache.rocketmq.remoting.common.RemotingHelper;
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.rocketmq/lib目录下
     */
    public class RocketMQAPITest extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
            RocketmqAPI rocket = SDK.getCCAPI().getRocketmqAPI(SDK.getAppAPI().getProperty(processExecutionContext.getProcessInstance().getAppId(),"rocketmq"));
    
            Consumer<MQProducer> producer = x -> {  //  生产者
                Message msg = new Message("TopicTest", "TagA", ("Hello RocketMQ").getBytes(RemotingHelper.DEFAULT_CHARSET));
                SendResult sendResult =  x.send(msg);
                System.out.println("sendResult = " + sendResult);
            };
    
            Consumer<MQPushConsumer> cosumer = t -> {  //  消费者
                t.registerMessageListener(new MessageListenerConcurrently() {
                    public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> msgs,
                                                                    ConsumeConcurrentlyContext context) {
                        System.out.printf(Thread.currentThread().getName() + "Receive New Messages :" + msgs + "%n");
                        return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
                    }
                });
            };
    
            try {
                rocket.doProduce("tt", producer);
            } catch (Exception e2) {
                e2.printStackTrace();
            }
    
            try {
                rocket.doConsume("tt", cosumer);
            } catch (Exception e2) {
                e2.printStackTrace();
            }
      //.......
        }
    
    }
    

> RocketMQ JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/RocketmqAPI.html>

## 3\. 流程编排服务

该应用提供RocketMQ Producer(向RocketMQ发送消息)的流程编排服务(Service Task)。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rocket2.png)](<rocket2.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rocket3.png)](<rocket3.png>)

### 调用

操作步骤：

  1. 创建一个流程模型
  2. 拖动一个系统任务至画布
  3. 配置系统任务，服务类型为`流程服务`，选择该流程服务，配置相关信息
  4. 完成流程模型的正确设计，创建流程实例，到任务到达系统任务时，即可发送消息

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rocket0.png)](<rocket0.png>)

## 4.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用RocketmqAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc RocketmqAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/RocketmqAPI.html>)说明。

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

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rocketd.png)](<rocketd.png>)

## 7.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 8.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>