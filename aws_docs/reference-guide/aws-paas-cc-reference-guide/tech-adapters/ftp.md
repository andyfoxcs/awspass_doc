# FTP - 连接文件传输服务 | AWS CC连接中心参考指南

# FTP - 连接文件传输服务

FTP（File Transfer Protocol，文件传输协议） Adapter是一种实现远程文件传输的技术适配器。

主要功能

  * 支持符合RFC 959规范的FTP服务调用
  * 提供CCAPI封装，方便开发者使用
  * 支持CC部署环境变量
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

## 1.配置

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ftp.gif)

配置FTP适配器。

项 | 说明  
---|---  
名称 | FTP适配器的名称  
验证身份 | 是否匿名访问，开启后将显示用户和口令属性  
用户 | 登录账户，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
口令 | 登录口令，支持@公式，如@env(xxx)可获取[环境](<../hj>)中相应变量值  
服务器IP | FTP服务IP地址  
端口 | FTP服务器端口，一般FTP服务器默认端口为21  
文件路径 | 工作路径  
文件名编码 | 远程编码  
传输模式 | 文件类型，ASCII或二进制文件  
SSL安全 | 是否开启FTPS加密通讯  
被动模式 | 开启则为被动（FTP Passive）模式，关闭则为主动（FTP Port）模式  
连接超时 | 连接超时时间  
请求超时 | 请求超时时间  
描述 | 适配器描述信息  
  
## 2.调用

由开发在Java代码中调用FTP服务，如进行远程文件的读写。

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ftpuuid.png)

### API代码示例

在访问前，我们假设已创建了一个CC FTP技术适配器，其分配的模型Id为`00000000`
    
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.FtpAPI;
    
    import java.io.File;
    import java.io.FileInputStream;
    import java.io.FileOutputStream;
    import java.io.InputStream;
    
    /**
     * 需要在开发环境中引入AWS PaaS平台以下目录下所有jar包：
     * bin/lib目录下
     * bin/jdbc目录下
     * apps/install/com.actionsoft.apps.cc.connector.ftp/lib目录下
     */
    public class FTPAPITest extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
            FtpAPI ftpAPI = SDK.getCCAPI().getFtpAPI("00000000");
    
            //由引擎自动转换编码，如果您不了解FTP服务器及AWS PaaS平台服务器编码，建意设为true
            ftpAPI.setConvertName(true);
    
            //重命名
            ftpAPI.rename("1.xls", "2.xls");
    
            File file = new File("/Users/aws/awspaas.htm");
            InputStream inputStream= new FileInputStream(file);
            //上传文件
            ftpAPI.upload("/","awspaas.htm",inputStream);
    
            //list
            String[] n = ftpAPI.list("/");
    
            //删除
            ftpAPI.delete("/","manifest.xml");
    
            FileOutputStream fs=new FileOutputStream(new File("/Users/aws/awspaas.htm"));
            //下载
            ftpAPI.download("/","awspaas", fs);
    
            //......
        }
    }
    

> FTPAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/FtpAPI.html>

## 3.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用FtpAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc FtpAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/FtpAPI.html>)说明。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log0.png)

### 记录访问请求到审计日志

开启后，将访问请求记录到审计日志，该日志存储在AWS PaaS平台SYS_AUDIT_LOG表中，可在`日志`页进行查看。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log.png)

### 记录返回结果到文件日志

开启后，将请求数据和返回结果记录到文件日志，该日志存储在AWS PaaS平台%AWS_HOME%/logs/目录下，默认每个文件日志最大为20M，最多存储20个文件，超出将自动清除最早日期文件。 log文件个数及单文件最大值可在%AWS_HOME%/bin/conf/aws-log4j.xml文件中配置。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/log1.png)

  * 存储在logs目录中的文件日志，无字符数限制，可将全部的result结果或错误日志全部记录下来

## 4.监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`SLA服务质量监控`后，当调用RDSAPI时，将自动对`调用次数、出错次数、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/sla.png)

## 5.删除

在连接列表，光标移至需要删除的模型上，点击右侧删除按钮，按钮提示进行删除。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ftp4.png)

## 6.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 7.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>