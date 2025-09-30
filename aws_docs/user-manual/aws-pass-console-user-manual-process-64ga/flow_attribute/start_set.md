# 流程启动 · AWS PaaS文档中心

## 流程启动

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/start1.png)](<start1.png>)

项 | 说明  
---|---  
启动权限  | 流程必须指定启动权限范围才能够在客户端或通过API创建流程实例  
启动权限 > 授权组织 | 通过组织机构方式授权流程启动权限  
任务标题  | 开启此项后，流程启动时自动显示标题，支持@公式，默认未开启   
任务摘要  | 开启此项后， 提取表单字段，参与任务查询和通知，默认未开启   
移动端启动  | 开启此项后，在启动权限范围内的用户可在[移动端](https://docs.awspaas.com/solution-package/aws-paas-app-solution-package-oa/workbench/README.html)发起该流程，默认不开启  
启动流程选身份 | 开启此项后，流程启动者如果存在兼任身份，则提供身份选择页面[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/start3.png)](<start3.png>)  
办理任务选身份 | 开启时，如果办理者有兼任身份，则提供身份选择页面[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/jianren1.png)](<jianren1.png>)  
  
启动权限没有设置时，在设计器上给初学者友好提示

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/start1.1.png)](<start1.1.png>)

**任务摘要**

  * 提取表单字段仅支持主表单字段及流程变量，表单字段支持的UI组件：单行、多行、货币、数值、列表、单选组、复选组、日期、时间、日期时间
  * 任务摘要支持任务模糊搜索、也支持入全文检索和查询

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/start1.2.png)](<start1.2.png>)

> 1.任务摘要在第一个节点不能搜索，在待办任务中下一节点搜索的摘要内容是上一节点字段的值  
>  2.入全文检索要安装[ES全文检索服务](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.es/index.html>)搜索

  * `PC`、`批量办理`显示摘要信息，优化用户体验

PC通知  
---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/pcnotice.png)](<pcnotice.png>)  
批量办理  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/flow_attribute/plbl.png)](<plbl.png>)  
  * [`企业微信`](<https://docs.awspaas.com/reference-guide/aws-paas-wechat-reference-guide/index.html>)、[`钉钉`](<https://docs.awspaas.com/apps/com.actionsoft.apps.dingding/index.html>)、[`飞书`](<https://docs.awspaas.com/apps/com.actionsoft.apps.feishu.open/index.html>)、[`移动门户`](<https://docs.awspaas.com/emm/aws-pass-portal-user-manual-emm/news/README.html>)通知以摘要形式展示消息内容

飞书 | 企业微信  
---|---  
![](./feishu-zy.png) | ![](./weixin-zy.png)  
阿里钉钉 | 移动门户  
![](./dingding-zy.png) | ![](./mobile-zy.png)