# 脚本任务（Script Task） | AWS BPMN2 Activity参考指南

# 脚本任务（Script Task）

脚本任务（Script Task）是一个自动化任务。当流程到达脚本任务时，自动执行编写的脚本，完毕后继续执行后继路线。

### 图形符号

符号 | 说明  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/activities/3.png) | 脚本任务能够执行指定的程序脚本  
  
### 支持的脚本语言

  * [Groovy](<groovy.html>)
  * [JavaScript](<javascript.html>)
  * [BeanShell](<beanshell.html>)

> 正常调试脚本任务，建议开发者在Eclipse启动AWS的选项中，设置`-XX:PermSize=64M -XX:MaxPermSize=256m`JVM参数