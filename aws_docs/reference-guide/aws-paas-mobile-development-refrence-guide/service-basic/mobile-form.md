# 移动表单 | AWS 移动开发参考指南

## 移动表单

  1. 表单设计
  2. 表单调试
  3. 表单部署

### 1\. 表单设计

移动表单部署为H5应用时，需在表单建模时选择生成移动端表单。表单设计器中可移动、拖拽元素:

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/service-basic/form_design.png)

为元素指定UI组件:

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/service-basic/form_component.png)

可查看修改源码:

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/service-basic/form_source.png)

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/service-basic/form_source2.png)

### 2\. 表单调试

调试表单时需要先将表单绑定流程并发起该流程，在表单页面可以看到一个二维码。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/service-basic/form_barcode.png)

点击该二维码可查看移动端表单，此时可通过PC上的Chrome或者Safari调试页面。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/service-basic/form_debug.png)

### 3\. 将表单部署为H5应用

移动端可以通过cmd`com.actionsoft.apps.workbench_mobile_process_start`来发起流程。下面是发起某个流程的完整地址示例：
    
    
    http://demo.awspaas.com/portal/r/w?cmd=com.actionsoft.apps.workbench_mobile_process_start&groupId=xxxx&processDefId=xxxx&sid=xxxx
    

  * groupId是待发起流程所在流程组ID
  * processDefId是待发起流程ID

如何获取流程组ID和流程定义ID参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/appendix/get-processid.html>)。

在AWS PaaS控制台移动应用列表中添加H5应用时， 基于AWS MVC编程框架的URL地址支持简写，URL中可以不包含服务器地址和sid参数， 比如发起流程的地址可以简写为:
    
    
    cmd=com.actionsoft.apps.workbench_mobile_process_start&groupId=xxxx&processDefId=xxxx
    

将表单部署为H5应用的详细步骤请参考[这里](<../appendix/add-h5.html>)。