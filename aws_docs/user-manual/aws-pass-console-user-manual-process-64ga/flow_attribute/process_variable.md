# 流程变量 · AWS PaaS文档中心

## 流程变量

流程变量在流程实例周期内全局共享。可用于连线条件判断。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/bianliang1.png)](<bianliang1.png>)

项 | 说明  
---|---  
变量名称 | 变量的名称  
变量类型 | 支持`字符串、整数值、浮点数、附件`  
默认值 | 变量类型为`字符串、整数值、浮点数`时可设置默认值，支持@公式(仅支持常量类和流程实例相关@公式)  
  
### 用于连线条件判断

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/bianliang2.png)](<bianliang2.png>)

### 用API设置流程变量值
    
    
    //读取指定的流程变量
    ProcessExecutionContext.getVariable(varName);
    //读取全部流程变量
    ProcessExecutionContext.getVariables();
    //设置流程变量
    ProcessExecutionContext.setVariable(varName, varValue)
    //批量设置流程变量
    ProcessExecutionContext.setVariables(vars)