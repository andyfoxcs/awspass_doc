# 如何使用CC？ | AWS CC连接中心参考指南

# 如何使用CC？

## 1\. 从应用商店安装CC应用

目前在[AWS应用商店](<http://www.awsappstore.com>)已提供的CC应用有如下：

应用名称与ID | 描述  
---|---  
[RDS Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.rds>)   
com.actionsoft.apps.cc.connector.rds | 连接关系型数据库服务  
[LDAP Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.ldap>)   
com.actionsoft.apps.cc.connector.ldap | 连接LDAP服务，并提供LDAP组织同步服务  
[Elasticsearch Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.elasticsearch>)   
(com.actionsoft.apps.cc.connector.elasticsearch) | 连接Elasticsearch服务  
[Redis Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.redis>)   
com.actionsoft.apps.cc.connector.redis | 连接Redis服务  
[MongoDB Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.mongodb>)  
com.actionsoft.apps.cc.connector.mongodb | 连接MongoDB服务  
[FTP Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.ftp>)  
(com.actionsoft.apps.cc.connector.ftp) | 连接FTP服务  
[HTTP Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.http>)  
(com.actionsoft.apps.cc.connector.http) | 连接HTTP服务，并提供HTTP API 和 RestFUL API发布服务  
[SOAP Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.soap>)   
com.actionsoft.apps.cc.connector.soap | 连接Web Service服务，并提供Web Service API发布服务  
[ActiveMQ Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.activemq>)   
(com.actionsoft.apps.cc.connector.activemq) | 连接ActiveMQ服务  
[RabbitMQ Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.rabbitmq>)  
com.actionsoft.apps.cc.connector.rabbitmq | 连接RabbitMQ服务  
[RocketMQ Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.rocketmq>)   
com.actionsoft.apps.cc.connector.rocketmq | 连接RocketMQ服务  
[Kafka Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.kafka>)  
com.actionsoft.apps.cc.connector.kafka | 连接Kafka服务  
[ZooKeeper Connector](<https://www.awsappstore.com/apps/detail/com.actionsoft.apps.cc.connector.zookeeper>)   
com.actionsoft.apps.cc.connector.zookeeper | 连接ZooKeeper服务  
  
> AWS PaaS如何安装应用，参见《快速上手//安装应用商店的标准应用》<https://docs.awspaas.com/reference-guide/aws-appstore-reference-guide/install-apps/install.html>

**特别说明**

  1. **CC应用安装到AWS PaaS平台后，不提供重启操作**
  2. **从应用商店升级CC应用后，需要重启AWS PaaS平台，方可正常使用**

## 2\. 在AWS PaaS控制台进行连接器创建或服务发布

以admin用户登录AWS PaaS控制台，进入`连接服务`，在`连接`中创建相关连接服务。 具体操作请参见本文档后续章节。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/introduction/1.gif)

## 3\. 通过CC API操作连接器

通过如下代码获取连接器对象，具体操作请参见本文档后续章节。
    
    
    SDK.getCCAPI().getXXXAPI("连接模型UUID")
    

> 使用CC服务要求AWS PaaS平台许可支持CC连接服务。