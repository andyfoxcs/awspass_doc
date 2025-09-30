# 调试流程 · AWS PaaS文档中心

## 调试流程

在流程未正式部署使用前，流程设计者对各项流程设置进行运行调试。该过程与未来部署使用的实际环境相同，会产生流程实例、任务实例数据。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/run_manager/run1.png)](<run1.png>)

>   1. 在流程调试、测试期间，建议启动项仅开放给测试人员。
>   2. 流程调试、测试期间产生的垃圾数据可使用[实例数据批量清除](<https://docs.awspaas.com/apps/com.actionsoft.apps.prm.remove/>)工具删除
> 

### 流程自动化测试

为提高对审批类流程的测试效率和测试质量。炎黄盈动为AWS PaaS平台提供了一个ADDONS扩展应用`流程自动化测试`。

项 | 说明  
---|---  
AppID | com.actionsoft.apps.addons.pat  
版本 | 1.0  
开发者 | 炎黄盈动  
移动版 | 无  
依赖应用 | 无  
  
可以完全免除测试人员频繁切换测试账号模拟申请以及审批过程，缩短审批类流程的上线时间，提高用户满意度。该应用为流程配置人员测试审批路由提供完整工具和方法支持，包括测试用例编写（自动生成）、分配测试用例、测试计划、执行测试计划、自动生成测试报告等。

基于测试结果，系统会根据未通过项自动生成问题列表，提高配置人员和测试人员的协作效率，并方便进行回归测试。为保持开发与测试进度同步进行，允许测试人员提前编写测试用例，即每个测试用例可以被一个独立的Excel文件定义、分发（用例编写人员将测试文件发送给实际测试人员）。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/run_manager/run1.gif)](<run1.gif>)

#### 延伸阅读

  * [流程自动化测试发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.pat/index.html>)