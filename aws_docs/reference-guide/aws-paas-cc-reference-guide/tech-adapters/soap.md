# SOAP - 连接Web Service服务 · AWS PaaS文档中心

# SOAP - 连接Web Service服务

SOAP（Simple Object Access Protocol，简单对象访问协议） Adapter是一种可让开发者在程序和建模时直接访问PaaS外部Web Service服务的技术适配器。

主要功能

  * 支持符合SOAP 1.1/1.2规范的Web Service服务调用
  * 提供CCAPI封装，方便开发者使用
  * 支持秘钥身份和CC环境变量，发布的API服务支持流控策略、访控策略
  * 支持SLA服务质量监控和告警通知，提供全局requestId
  * 提供访问日志开关
  * 提供结果日志开关

特别说明

  * 使用该应用要求AWS PaaS平台许可支持CC服务
  * 使用该应用要求AWS PaaS平台版本不低于6.4.1

> 适用于企业内传统ERP、CRM等SOA架构的服务接口访问

## 1.配置

### 主要配置

项 | 说明  
---|---  
WSDL地址 | Web Service的WSDL地址  
服务 | WSDL中定义的服务  
端口 | WSDL中定义的端口  
操作 | WSDL中定义的服务方法。可根据操作生成消息模板，发起基于消息的服务调用  
服务接口（SEI） | 服务接口，可用于api中基于代理的服务调用。格式：`类全路径`+`Soap`  
访问策略 | 设置调用时需要的身份信息，该身份信息来源于用于连接器类型的[访控策略](<../service-center/access.html#adpter>)  
服务地址 | 服务调用的地址，该参数默认来自WSDL中对应的服务，需要点“保存”  
启用MTOM | 需要和服务器端设置保持一致，在某些带附件的服务调用时优化服务执行效率  
  
### 按钮

项 | 说明  
---|---  
生成服务客户端 | 根据WSDL生成对应的客户端jar，该jar引入工程后，可使用SDK SOAP API调用服务。如果jar文件生成失败，很可能是WSDL不符合规范，可以将WSDL下载到本地参考日志修复不合理部分，然后修改WSDL参数指向修复后的WSDL生成jar，该jar一般放到模型所在APP的lib中  
  
## 2.调用

### 获取模型ID

在CC连接列表中可获取适配器模型ID。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/soapuuid.png)](<soapuuid.png>)

### API代码示例

在访问前，我们假设已创建了一个CC SOAP技术适配器，其分配的模型Id为00000000
    
    
    package com.actionsoft.cc.CCAPI;
    
    import cn.com.webxml.TraditionalSimplifiedWebServiceSoap;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    import com.actionsoft.cc.webapi.AppPermWebDemo;
    import com.actionsoft.sdk.local.SDK;
    import com.actionsoft.sdk.local.api.cc.SOAPAPI;
    
    
    public class SOAPAPITest extends ExecuteListener {
        @Override
        public void execute(ProcessExecutionContext processExecutionContext) throws Exception {
    
            //soap
            SOAPAPI soapAPI = SDK.getCCAPI().getSOAPAPI("00000000");
            soapAPI.connectTimeout(8000);
    
            //本地服务
            AppPermWebDemo port1 = soapAPI.getPort(AppPermWebDemo.class);
            port1.getProperty("appid", "b");
            port1.getPropertyErr("appid", "a");
            port1.getPropertyException("appid", "b");
    
            // 公共转大小写服务
            TraditionalSimplifiedWebServiceSoap port = soapAPI.getPort(TraditionalSimplifiedWebServiceSoap.class);
            String str1 = port.toSimplifiedChinese("炎黄盈动");
            String str2 = port.toTraditionalChinese("炎黄盈动");
    
            //......
    
            soapAPI.close();
    
        }
    }
    

  * **SEI如何获得**

上述代码中xxx为该服务的SEI（serviceEndpointInterface），该接口类可以在“生成服务客户端”生成的jar中得到，该接口包含WSDL中定义的操作列表，用于客户端代理方式调用。开发时需要将该jar引入工程。

  * **SAP的SOAP服务如何设置策略**

SAP的安全认证用http basic验证的比较常见，在服务策略的验证策略中选择“HTTP验证”，在调用身份中选择根据SAP提供的账户密码对应建立的秘钥身份。

SAP服务如果调用不成功，在“端口”列表中选择soap12的协议。

> SOAPAPI JavaDOC <https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/SOAPAPI.html>

## 3.平台使用场景

  1. 流程人工任务的参与者，路由方案使用服务API/用户来自SOAP服务，从WebService结果指定执行人

## 4.日志

当连接器开启`记录访问请求到审计日志`和`记录返回结果到文件日志`开关后，调用SOAPAPI相关方法时，可记录日志，具体哪些方法会记录日志，请参见[javadoc SOAPAPI](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/sdk/local/api/cc/SOAPAPI.html>)说明。

### 记录访问请求到审计日志

开启后，将访问请求记录到审计日志，该日志存储在AWS PaaS平台SYS_AUDIT_LOG表中，可在`日志`页进行查看。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/eslog.png)](<eslog.png>)

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

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/soap4.png)](<soap4.png>)

## 7.应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## 8.DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>

## 9.发布SOAP API

详细参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/appendix/publish_soap_api.html>)。