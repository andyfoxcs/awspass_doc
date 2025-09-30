# LDAP - 连接目录服务 | AWS CC连接中心参考指南

# LDAP - 连接目录服务

LDAP（Lightweight Directory Access Protocol） 是AWS CC的官方连接适配器，为上层应用场景提供统一的LDAP服务访问和管理。

主要功能

  * 支持符合JAVA JNDI API规范的LDAP服务调用
  * 提供CCAPI封装，方便开发者使用
  * 支持CC环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ldap1.gif)

### 基本信息

项 | 说明  
---|---  
名称 | LDAP适配器的名称  
上下文工厂 | 设置JNDI的`javax.naming.direcotry`属性值，不填默认为`com.sun.jndi.ldap.LdapCtxFactory`  
服务提供者URL | 设置JNDI的`java.naming.provider.url`属性值，例如：`ldap://39.106.201.113:389/ou=测试公司,dc=actionsoft,dc=com` ，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
协议 | 支持 `LDAP LDAPS TLS`  
身份 | simple验证用的账户，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
密码 | simple验证用的密码 ，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
引用 | 如果不设置，默认由服务端决定  
有效性 | 是否使用缓存或副本，默认为false  
描述 | 当前适配器描述信息  
  
### 扩展属性

和工厂有关的其它属性配置，详见[官方文档](<https://docs.oracle.com/javase/7/docs/technotes/guides/jndi/jndi-ldap.html>)。

  * com.sun.jndi.ldap.connect.timeout：默认1200毫秒
  * java.naming.security.authentication：默认simple

## 2.调用

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ldap1.png)

### API代码示例

在访问前，我们假设已创建了一个CC LDAP技术适配器，其分配的模型Id为00000000
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.LDAPAPI;
    
    import javax.naming.ldap.LdapName;
    
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.LDAP/lib目录下
     */
    
    public class LdapAPITest extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
    
            //获得一个操作LDAP的LDAPAPI对象
            LDAPAPI api = SDK.getCCAPI().getLDAPAPI('00000000');
    
            //示例代码
            boolean y =  LDAPAPI.authenticate("","(sAMAccountName=aws)","123QWEasd");
            String name = "cn=aws";
            LdapName dn = new LdapName(name);
            java.util.List<java.lang.String> list  = LDAPAPI.list(dn);
    
            // 注意，open产生的context对象需要关闭
            api.search/list/listBindings/lookup/authenticate...
    
    
            //...
        }
    }
    

> LDAPAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/LDAPAPI.html>

## 3.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用LDAPAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc LDAPAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/LDAPAPI.html>)说明。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ldaplog.png)

### 审计日志

审计日志存储在SYS_AUDIT_LOG表中，日志信息最多显示1000个字符，可在`日志`页签查看。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ldaplog1.png)

### 文件日志

文件日志存储在AWS PaaS平台%AWS_HOME%/logs/目录下，默认每个文件日志最大为20M，最多存储20个文件，超出将自动清除最早日期文件。 log文件个数及单文件最大值可在%AWS_HOME%/bin/conf/aws-log4j.xml文件中配置。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log1.png)

## 4.监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`SLA服务质量监控`后，当调用RDSAPI时，将自动对`调用次数、出错次数、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ldapsla.png)

## 5.删除

在连接列表，光标移至需要删除的模型上，点击右侧删除按钮，按钮提示进行删除。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ldapd.png)

## 6.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 7.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>