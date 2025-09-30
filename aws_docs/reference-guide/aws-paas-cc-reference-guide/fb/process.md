# Process Service - 流程服务 | AWS CC连接中心参考指南

# Process Service - 流程服务

一类拥有特定接口定义服务组件，用于BPMN2系统任务的“流程服务”，例如，一个公共的发邮件服务。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/fb/service.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/fb/service1.png)

## 延伸阅读

  * [系统任务>调用公共流程服务](<https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/service_task/process_service.html>)

## 主要配置

项 | 说明  
---|---  
名称 | 服务名称，用于开发人员区分服务  
类路径 | 该组件的实现类全路径，必须存在于当前APP、父APP或者当前APP的依赖APP中  
  
## 示例代码
    
    
    package com.actionsoft.apps.addons.mail.service;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import javax.annotation.Resource;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.servicetask.HelperService;
    import com.actionsoft.bpms.bpmn.engine.servicetask.MappingField;
    import com.actionsoft.bpms.util.UtilString;
    import com.actionsoft.exception.AWSIllegalArgumentException;
    
    /**
     * @author AWS
     */
    public class SendMailService extends HelperService {
        public SendMailService() {
            setDescription("邮件发送服务");
        }
    
        @Resource
        private ProcessExecutionContext pec;
    
        public void sendMail(@MappingField(title = "收件人email账户", desc = "一个或多个合法的email地址，多个用分号分割，支持@公式", notNull = true) String to, @MappingField(title = "抄送人email账户", desc = "一个或多个合法的email地址，多个用分号分割，支持@公式") String cc, @MappingField(title = "邮件标题", desc = "邮件标题，支持@公式", notNull = true) String subject, @MappingField(title = "邮件正文", desc = "邮件正文，支持@公式和特定变量（办理URL）", notNull = true) String content
        ) throws Exception {
            try {
                MailService mailService = new MailService();
                to = pec.execAtScript(to);
                cc = pec.execAtScript(cc);
                subject = pec.execAtScript(subject);
                content = pec.execAtScript(content);
                List<String> toList = new ArrayList<String>();
                String[] toArr = to.split(";");
                for (int i = 0; i < toArr.length; i++) {
                    if (!UtilString.isEmpty(toArr[i])) {
                        toList.add(toArr[i]);
                    }
                }
                List<String> ccList = new ArrayList<String>();
                String[] ccArr = null;
                if (!UtilString.isEmpty(cc)) {
                    ccArr = cc.split(";");
                    for (int i = 0; i < ccArr.length; i++) {
                        if (!UtilString.isEmpty(ccArr[i])) {
                            ccList.add(ccArr[i]);
                        }
                    }
                }
                // 检查参数
                if (toList.size() == 0) {
                    throw new AWSIllegalArgumentException("收件人不能为空");
                }
                if (UtilString.isEmpty(subject)) {
                    throw new AWSIllegalArgumentException("邮件标题不能为空");
                }
                if (UtilString.isEmpty(content)) {
                    throw new AWSIllegalArgumentException("邮件正文不能为空");
                }
    
                mailService.sendMail("", toList.toArray(new String[toList.size()]), ccList.toArray(new String[ccList.size()]), subject, content, null);
            } catch (Exception e) {
                e.printStackTrace();
                throw e;
            }
        }
    
    }
    

## 日志

打开`记录访问请求到审计日志`开关后，调用流程服务，会记录日志，该日志存储在SYS_AUDIT_LOG表中，可在`日志`页签查看。日志信息最多显示1000个字符。

## 监控

> 使用该功能要求AWS PaaS平台许可支持SLA服务质量监控。

开启`开启SLA服务质量监控`后，当调用发布的SOAP API时，将自动对`调用次数、出错次数、限流次数、访控次数、熔断次数、流出流量、执行耗时`进行[监控](<../jk>)。 并可通过[`SLA告警监控策略`](<../service-center/sla.html>)对监控数据进行告警。

当配置了告警监控且触发后，可快速查看告警信息列表。

## 应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>