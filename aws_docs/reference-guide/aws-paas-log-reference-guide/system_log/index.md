# 系统日志 · AWS PaaS文档中心

# 系统日志

系统日志是排除出错故障和调试信息打印的运行记录。日志数据存放在独立的文件中，有关保留期限请[查看这里](<../appendix/record_cycle.html>)。

AWS服务的日志文件(WARN/ERR)存放在`%AWS-HOME%/logs`目录下，Web服务日志(INFO/WARN/ERR)存放在`%AWS-HOME%/logs`目录下。

环境 | 文件名命名  
---|---  
单一环境 | logs/aws.log  
集群环境 | logs/AWS实例名.log  
单一环境 | logs/web.log  
集群环境 | logs/Web实例名.log  
  
> 注意集群环境下，配置的Web实例名和AWS实例名避免冲突

集群多节点时，实例名由启动脚本`-Daws.inst`参数指定。 请参阅：<https://docs.awspaas.com/reference-guide/aws-paas-cluster-reference-guide/architecture/script.html>

**_附加1：LDAP组织同步日志_**

如果启用了[LDAP组织同步](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.ldapsync/index.html>)应用，同步日志被记录在以下位置
    
    
    %AWS-HOME%/webserver/logs/ldapsync.log
    

## 日志API

参见[日志编程接口](<../appendix/api.html>)

## 系统审计选项

### 1\. 记录cmd请求

配置见`%AWS-HOME%/bin/conf/server.xml`，默认关闭。
    
    
        <debug sql="false" //是否记录SLA质量监控中数据库连接track跟踪
        cmd="false" //是否记录cmd请求
        templatePage="false" //是否开启调试Web页面开发模版
        cache="false" //是否开启集群下Cache广播调试信息
        />
    

### 记录SLA质量监控中数据库连接track跟踪L对平台性能的损耗

当开启`%AWS-HOME%/bin/conf/server.xml#debug/sql`时，平台会监控每次SQL的代码调用堆栈。这是一种比较耗费性能的处理，尤其在高并发的`PRD`生产环境，更是不能够轻易开启。

经过我们模拟200并发用户，持续80分钟压测对比分析，**开启SQL调试模式，会增大10倍以上的性能开销。**

A用例，开启SQL调试 | B用例，关闭SQL调试  
---|---  
登录-Min(13毫秒)/Avg(617毫秒)/Max(1.69秒) | 登录-Min(6毫秒)/Avg(185毫秒)/Max(1.09秒)  
创建流程-Min(135毫秒)/Avg(57.8秒)/Max(107.6秒) | 创建流程-Min(16毫秒)/Avg(81毫秒)/Max(3.14秒)  
累计创建15,264个流程和15,264个任务 | 累计创建188,855个流程和188,855个任务  
  
### 2\. 记录sql操作

配置见`%AWS-HOME%/bin/conf/aws-log4j.xml`，默认关闭。
    
    
    //level值为OFF时不输出sql操作，为ALL时输出sql操作
    <Logger name="com.actionsoft.sql" additivity="false" level="OFF">
                <appender-ref ref="asyncAppender" />
    </Logger>
    

### 3\. 记录慢sql操作

配置见`%AWS-HOME%/bin/conf/db_pool.properties`，默认开启。
    
    
    // 默认输出执行时间超过2s (threshold=2000) 的sql语句
    #拦截器
    jdbcInterceptors=StatementFinalizer;ResetAbandonedTimer;SlowQueryReport(notifyPool=false,maxQueries=1000,threshold=2000)
    

### 4\. AWS平台引擎类debug

如调试流程引擎的执行过程。配置见`%AWS-HOME%/apps/install/_bpm.platform/manifest.xml`，默认关闭。
    
    
        ...
        <debug>false</debug>
        ...
    

### 5\. App类debug

配置见`%AWS-HOME%/apps/install/%appId%/manifest.xml`，新建应用时默认开启，安装的新应用默认关闭。
    
    
        ...
        <debug>true</debug>
        ...
    

该开关对应如下API
    
    
    LogAPI.getLogger(this.getClass()).debug(msg);
    

## 日志访问

  1. 登录您的AWS PaaS实例控制台
  2. 访问“运维管理>日志审计查询”页面
  3. 在左侧，点击相关日志文件类型链接

[![](https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/system_log/1.png)](<1.png>)

**您可以：**

  * 在线浏览
  * 打包下载