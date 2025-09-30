# 流程安全 · AWS PaaS文档中心

# 流程安全

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/common_set16.png)](<common_set16.png>)

项 | 说明  
---|---  
保密级别  | 开启后，为工作流提供`普通、秘密、机密、绝密`安全等级及手动选择 ，只有具备该类保密级别的人才可以查看此流程产生的任务。  
1\. 流程创建节点时，工具条出现保密级别选项：[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/mj1.png)](<mj1.png>)  
2\. 执行阶段保密级别不允许修改，工具条出现安全提示：[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/mj2.png)](<mj2.png>)  
3\. 若下一任务办理者在保密级别中未获得该安全级别，办理时将提示：[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/mj3.png)](<mj3.png>)  
表单安全 | ．`常规`通过合法的URL即可访问任务、表单数据  
．`参与者可访问`仅允许该流程的参与者（执行、通知、传阅）访问，非流程的参与者访问表单时，表单内容显示：[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/data1.png)](<data1.png>)