# 常见错误搭配 | AWS BPMN2 Gateway参考指南

## 常见错误搭配

错误的 | 正确的  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/appendix/1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/appendix/2.png)  
Service1和Service2都会执行，应该使用“并行网关”进行合并。**该场景会导致“排他网关”及之后的分支路径被实例化2次。** | 并行拆分、并行合并  
错误的 | 正确的  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/appendix/3.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/appendix/4.png)  
Service1和Service2只能执行其中的一条分支，应该使用“排他网关”进行合并。**该场景中“并行网关”永远也等不到Service1和Service2都能到达，导致流程被永久的中断在该网关。** | 排他拆分、排他合并  
错误的 | 正确的  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/appendix/5.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/appendix/6.png)  
Service1和Service2可能同时执行也可能只执行其中的一条分支，建议使用“包容网关”或“复杂网关”进行合并。**该场景会导致“排他网关”及之后的分支路径可能被实例化2次。** | 包容拆分、包容合并