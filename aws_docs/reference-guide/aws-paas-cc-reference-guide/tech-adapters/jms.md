# ActiveMQ - 连接消息服务 | AWS CC连接中心参考指南

# ActiveMQ - 连接消息服务

ActiveMQ是Apache下的开源消息中间件（<https://activemq.apache.org/），ActiveMQ> Connector为上层应用场景提供统一的ActiveMQ服务访问和管理。

主要功能

  * 支持ActiveMQ 5.16.0版的消息队列服务
  * 提供CCAPI封装，方便开发者使用
  * 提供ActiveMQ Producer(向ActiveMQ发送消息)的流程编排服务(Service Task)
  * 支持CC环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/activemq.gif)

项 | 说明  
---|---  
名称 | ActiveMQ适配器的名称  
代理URL | 格式：tcp://39.106.193.36:61616，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
用户名 | 用户名，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
密码 | 密码，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
描述 | 适配器描述信息  
  
## 2.调用

由开发者在Java代码中调用ActiveMQ服务。

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/activemquuid.png)

### API代码示例

在访问前，我们假设已创建了一个CC ActiveMQ技术适配器，其分配的模型Id为`00000000`
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.JmsAPI;
    import com.actionsoft.sdk.local.api.cc.jms.MessageCreator;
    
    import javax.jms.JMSException;
    import javax.jms.Message;
    import javax.jms.Session;
    import javax.jms.TextMessage;
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.activemq/lib目录下
     */
    public class JMSAPITest  extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
           //获得一个ActiveMQ对象
            JmsAPI jmsAPI =  SDK.getCCAPI().getJMSAPI("00000000");
    
            // mytest1
            jmsAPI.sDefaultDestination("mytest1");
            jmsAPI.send(new MessageCreator() {  //发送
    
                @Override
                public Message createMessage(Session session) throws JMSException {
                    TextMessage txt = session.createTextMessage();
                    txt.setText("hello");
                    return txt;
                }
    
            });
    
            jmsAPI.receive("mytest1");  //接收，先有发送，才能有接收
    
    
    
            //mytest2
            jmsAPI.send("mytest2", new MessageCreator() {
                @Override
                public Message createMessage(Session arg0) throws JMSException {
                    TextMessage ms=arg0.createTextMessage();
                    ms.setText("hello  test2");
                    return ms;
                }
            });
    
            TextMessage msg=(TextMessage)jmsAPI.receive("mytest2");
            System.out.println("##############"+msg.getText());
    
    
            //test3
            jmsAPI.sendAndReceive("这是默认",new MessageCreator() {
                @Override
                public Message createMessage(Session arg0) throws JMSException {
                    Message ms = arg0.createMessage();
                    ms.setJMSMessageID("这是一条消息");
                    return ms;
                }
            });
    
            //....
        }
    }
    

> ActiveMQAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/JmsAPI.html>

## 3.流程编排服务

该应用提供ActiveMQ Producer(向ActiveMQ发送消息)的[流程服务(Service Task)](<../fb/process.html>)。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/activemq2.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/activemq3.png)

### 配置

操作步骤：

  1. 创建一个流程模型
  2. 拖动一个系统任务至画布
  3. 配置系统任务，服务类型为`流程服务`，选择该流程服务，配置相关信息
  4. 完成流程模型的正确设计，创建流程实例，到任务到达系统任务时，即可发送消息

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/activemq5.png)

## 4.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用JmsAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc JmsAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/JmsAPI.html>)说明。

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

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/activemqd.png)

## 7.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 8.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>