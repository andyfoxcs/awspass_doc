# 创建SOAP Job | AWS 定时器开发参考指南

## 创建SOAP Job

**此章节内容仅在6.4.3版本前提供，后续版本由[DataService Job](<dataservice_job.html>)替代。**

在指定的触发条件执行一次或周期重复执行指定的SOAP服务，该服务指向一个AWS CC的SOAP适配器。

### 步骤1：在CC，注册SOAP连接器

  1. 登录您的AWS PaaS实例控制台
  2. 访问“连接服务 > 连接”页面
  3. 点击“新建”按钮
  4. 选择“访问SOAP Web服务”
  5. 点击“确定”按钮，完成新建

> 如果您的CC中已完成相关SOAP注册，此步骤可忽略，有关SOAP连接器的创建详细参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/soap.html>)。

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/5.png)

本示例使用一个公共服务
    
    
    http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl
    

**选择调用方法**

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/6.png)

保存后点击`服务调用`，配置服务参数。

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/7.png)

### 步骤2：新建Job

  1. 访问“调度服务”页面
  2. 点击“新建”按钮
  3. 选择“SOAP Job // 定时访问SOAP Web服务”
  4. 点击“确定”按钮，完成新建

> 任务的配置信息将创建在选择的应用

![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/9.png)

### 步骤3：完成配置

**如下图所示** ![](https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/scheduler_management/10.png)

项 | 说明  
---|---  
任务名称 | 易于运维人员了解的Job名，如`定时批量更新ERP付款状态`  
CC SOAP | 访问列表，由AWS CC提供的SOAP技术适配器  
调用条件 | true/false值，当值为false时不执行（可选）。支持基本的@公式  
请求参数 | 一个JSON串（可选），key/value对应该SOAP服务的方法参数和值。支持基本的@公式，如`{"param1":"来自SOAP Job的调度请求 - @date"}`  
触发规则 | 执行该Job的循环策略  
通知规则 | 执行该Job的通知规则，支持邮件通知、企业微信、钉钉通知，详见[邮件通知](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.mail/appendix/scenes.html#a>)