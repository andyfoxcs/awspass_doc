# RDS - 连接关系型数据库服务 · AWS PaaS文档中心

# RDS - 连接关系型数据库服务

RDS是AWS CC的官方连接适配器，为上层应用场景提供统一的关系型数据库服务访问和管理。

主要功能

  * 支持符合JDBC 2.0规范的SQL调用
  * 提供常见开源和商业数据库驱动，内置数据库连接池
  * 提供CCAPI封装，方便开发者使用
  * 支持CC环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

以admin用户登录AWS PaaS控制台进入`连接服务 > 连接`，新建：数据源选择 `RDS`，弹出侧边栏填写相关属性，保存，点击`测试一下`，可进行试。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rds.gif)](<rds.gif>)

### 基本信息

项 | 说明  
---|---  
名称 | RDS适配器的名称  
用户名 | 数据库用户名 ，支持@公式，如@env(rdsXX)可获取[环境](<../hj>)中相应变量值  
密码 | 数据库用户名对应口令，支持@公式，如@env(rdsXX)可获取[环境](<../hj>)中相应变量值  
驱动 | 选择需要连接数据库的驱动类型，该列表可在应用参数中进行配置  
URL地址 | 数据库URL地址，支持@公式，如@env(rdsXX)可获[环境](<../hj>)中相应变量值  
连接池 > 初始化连接数 | 连接池默认初始化的连接数  
连接池 > 最大连接数 | 连接池提供的最大连接数  
描述 | RDS描述信息，可在列表显示  
  
>   1. 相关JDBC驱动程序包存放在`%AWS-HOME%/bin/jdbc`目录下
>   2. 不支持同一种数据库多JDBC版本情况
>   3. 目前AWS PaaS平台支持的数据库类型请参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/runtime/server.html> 如需求修改驱动列表，请保存列表范围为AWS PaaS平台支持的数据库类型
> 

### 扩展属性

数据库链接的扩展属性，属性名可在应用参数中进行配置，各属性含义自行参考数据库JDBC属性说明。

  * `maxAge` 连接存活时间，单位毫秒，默认值为1小时。设置该值用于防止部分数据库例如mysql默认8小时过期时间
  * `maxIdle` 最大空闲数，数据库连接的最大空闲时间。超过空闲时间，数据库连 接将被标记为不可用，然后被释放。设为0表示无限制
  * `minIdle` 最小空闲连接,连接池中容许保持空闲状态的最小连接数量， 低于这个数量将创建新的连接， 如果设置为0 则不创建
  * `testWhileIdle` 空闲时做连接可用性检查，可选值：true、false，默认true。该参数对数据库稳定性要求高的场景可以设为true
  * `timeBetweenEvictionRunsMillis`在空闲连接回收器线程运行期间休眠的时间值， 以毫秒为单位。 如果设置为非正数， 则不运行空闲连接回收器线程 这个值不应该小于1秒，它决定线程多久验证连接或丢弃连接
  * `testOnBorrow` 连接使用前做可用性检查，可选值：true、false，默认false。该参数设置为true会消耗一定资源，但对数据库稳定性要求高的场景可以设为true。
  * `validationInterval` (long) 避免过度验证，保证验证不超过这个频率——以毫秒为单位。如果一个连接应该被验证，但上次验证未达到指定间隔，将不再次验证
  * `maxWait` 单位毫秒，默认30秒。等待maxWait时间没能从连接池获得连接，抛出异常，避免线程因为等待连接阻塞

有关Tomcat jdbc属性官方说明参见：<http://tomcat.apache.org/tomcat-8.5-doc/jdbc-pool.html>

## 2.调用

通过AWS PaaS平台提供的CCAPI，操作连接器。

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rdsuuid.png)](<rdsuuid.png>)

### API代码示例

Java代码中执行外部数据库操作，如select、insert、update。在访问前，我们假设已创建了一个CC RDS技术适配器，其分配的模型Id为00000000
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.bpms.commons.database.DBUtils.SUPPLY;
    import com.actionsoft.bpms.commons.database.RowMap;
    import com.actionsoft.bpms.commons.database.tomcat.PoolTrackModel;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.RDSAPI;
    
    import java.sql.Connection;
    import java.util.List;
    
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.rds/lib目录下
     */
    public class RDSAPITest  extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
            //获得一个操作外部数据库的RDSAPI对象
            RDSAPI rdsapi = SDK.getCCAPI().getRDSAPI("00000000");
            Connection conn = rdsapi.open();
            RowMap rowMap =  rdsapi.getMap("select * from orguser where userid = ?","admin");
            String username = rowMap.getString("username");
            String password = rowMap.getString("password");
    
            //查询sql取第一条数据集的第一列String值，如果没有满足要求的数据，返回空串
            String getstring = rdsapi.getString("select * from orguser", "admin");
    
            //查询sql取第一条数据集的第一列int值，如果没有满足要求的数据，返回0
            int getint = rdsapi.getInt("select * from orguser", "admin");
    
            //设置resultSet每次向数据库取的行数
            rdsapi.setFetchSize(-1);
    
            //设置resultSet最多返回的行数
            rdsapi.setMaxRows(-1);
    
            //获得当前数据库类型
            SUPPLY getsupply = rdsapi.getSupply();
    
            //获得当前CC RDS活动连接对象的跟踪信息，详细堆栈需日志参数开启
            List<PoolTrackModel> gettrace = rdsapi.getTrace();
    
            // 自定义查询
            rdsapi.query.....
    
            //基于回调接口
            rdsapi.execute......
    
            //......
    
            conn.close();
        }
    }
    

> RDSAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/RDSAPI.html>

## 3.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用RDSAPI中update、execute、等方法时，可记录相关日志，具体哪些方法会记录日志，请参见javadoc RDSAPI说明。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rdslog.png)](<rdslog.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rdsapi.png)](<rdsapi.png>)

### 审计日志

审计日志存储在SYS_AUDIT_LOG表中，日志信息最多显示1000个字符，可在`日志`页签查看。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rdslog1.png)](<rdslog1.png>)

### 文件日志

文件日志存储在AWS PaaS平台%AWS_HOME%/logs/目录下，默认每个文件日志最大为20M，最多存储20个文件，超出将自动清除最早日期文件。 log文件个数及单文件最大值可在%AWS_HOME%/bin/conf/aws-log4j.xml文件中配置。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log1.png)](<log1.png>)

## 4.监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`SLA服务质量监控`后，当调用RDSAPI时，将自动对`调用次数、出错次数、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rds1.png)](<rds1.png>)

## 5.平台使用RDS适配器场景

  1. 创建BO表选择CC数据源
  2. UI组件列表、数据字典、单选、复选、树形字典选择CC数据源
  3. DW视图选择CC数据源

相关场景使用RDS连接后，可在关联页签进行查看。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rds4.png)](<rds4.png>)

## 7.删除

在连接列表，光标移至需要删除的模型上，点击右侧删除按钮，按钮提示进行删除。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rdsd.png)](<rdsd.png>)