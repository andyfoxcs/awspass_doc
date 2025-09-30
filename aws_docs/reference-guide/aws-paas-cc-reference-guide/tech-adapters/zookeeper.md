# ZooKeeper - 连接分布式调度服务 · AWS PaaS文档中心

# ZooKeeper - 连接分布式调度服务

ZooKeeper 是一个高可用的分布式数据管理与系统协调软件，它可以为分布式应用提供状态同步、配置管理、名称服务、群组服务、分布式锁及队列、以及 Leader 选举等服务。

主要功能

  * 支持Zookeeper 3.6.1版本的分布式调度服务
  * 提供CCAPI封装，方便开发者使用
  * 支持CC部署环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/zookeeper.gif)](<zookeeper.gif>)

配置ZooKeeper适配器。

项 | 说明  
---|---  
名称 | ZooKeeper适配器的名称  
连接信息 | ZooKeeper服务IP和PORT列表，格式：IP1:PORT1,IP2:PORT2，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
认证 | 支持用户:密码格式的认证信息  
描述 | 适配器描述信息  
  
## 2.调用

由开发者在Java代码中调用ZooKeeper服务。

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/zookeeperuuid.png)](<zookeeperuuid.png>)

### API代码示例

在访问前，我们假设已创建了一个CC ZooKeeper技术适配器，其分配的模型Id为`00000000`
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.ZooKeeperAPI;
    import com.actionsoft.sdk.local.api.cc.zookeeper.ChildListener;
    import com.actionsoft.sdk.local.api.cc.zookeeper.StateListener;
    
    import java.util.List;
    
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.ZooKeeper/lib目录下
     */
    public class ZookeeperAPITest extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
            //获得一个ZooKeeper对象
            ZooKeeperAPI zookeeperAPI = SDK.getCCAPI().getZooKeeperAPI("00000000");
    
            //增加连接状态监听器
             zookeeperAPI.addStateListener(new StateListener(){
                @Override
                public void stateChanged(int arg0) {
                    // TODO Auto-generated method stub
                    System.out.println(arg0);
                }});
             Thread.sleep(60000);
    
             //检测是否处于连接状态
             boolean is =   zookeeperAPI.isConnected();
             //创建一个zk Node
             zookeeperAPI.create("/step7/abc", true);
             //创建一个监听
             ChildListener childListener = new ChildListener(){
                 @Override
                 public void childChanged(String s, EventType eventType, List<String> list) {
                     System.out.println(s);
                     System.out.println(list.size());
                 }};
                 //addChildListener添加节点
             zookeeperAPI.addChildListener("/step5/abc", childListener );
    
            //创建一个zk Node
            zookeeperAPI.create("/p2", true);
            //        zookeeperAPI.create("/p1/s1", true);
            //获得子节点列表
            List l =  zookeeperAPI.getChildren("/step5/abc");
            //判断zk节点是否存在
            boolean falgzk = zookeeperAPI.checkExists("/step5/abc");
            System.out.println("===节点是否存在=="+falgzk);
            //删除一个zk Node
            zookeeperAPI.delete("/step5/abc");
            //判断zk节点是否存在
            boolean zk1 = zookeeperAPI.checkExists("/step5/abc");
            System.out.println("====zk节点是否存在===="+zk1);
    
             byte[] b = {1,1,1,1,1,1,4};
             //设置节点数据
            zookeeperAPI.setData("/p2", b);
            System.out.println("====节点数据====="+zookeeperAPI.getData("/p2").toString());
    
             //关闭zk资源
             zookeeperAPI.close();
            //......
        }
    }
    

> ZooKeeperAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/ZooKeeperAPI.html>

## 3.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用ZooKeeperAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc ZooKeeperAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/ZooKeeperAPI.html>)说明。

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

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/zookeeperd.png)](<zookeeperd.png>)

## 6.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 7.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>