# Flow Control - 流控策略 | AWS CC连接中心参考指南

# Flow Control - 流控策略

流控策略（流量控制）可限制单位时间内API的被调用次数，对绑定策略的API进行流量控制，保护后端服务。流控策略和发布的API是相互独立的，只有将API绑定流控策略后，流量控制策略才对该API生效。如果暂停流控策略，随之相关的API也将暂停流量控制。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/fk.gif)

## 配置

项 | 说明  
---|---  
名称 | 服务名称，用于开发人员区分服务  
范围 | 独享，每个API服务（每个API Class）独立控制  
共享，多个API服务（多个API Class间）共用控制  
  
## 流量控制

设置一段时间内，同一IP允许调用的最大次数；或一段时间内不区分IP情况下允许调用的最大次数。

## API断路

断路器是一种当服务发生异常，防止跨多个系统的这种灾难性级联故障，断路器允许构建容错和弹性的系统，当关键服务不可用或具有高延迟时，系统仍然可以正常运行。当调用API服务时，程序连续出错或连续抛出异常时，达到设置的连续出错次数后，API服务将进行跳闸不可用，此时设用API服务，会提示【410:由于流控策略未通过，该请求被限制访问】。

## API绑定列表

当该策略被已发布的HTTP或SOAP服务绑定后，此处可展示相应API列表。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/3.png)

## 应用信息

显示当前模型所属应用信息及受管状态。在不同环境中，支持AWS PaaS的模型受管(Managed)控制。有关模型受管详细参见<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>

## DevOps

显示当前模型的开发维护权限，可查看到具体人员信息。有关权限的设置参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html#a>

## 上线下线

在策略列表，可以切换流控策略的状态。处于上线状态的策略，在HTTP和SOAP服务中引擎可以正常应用该策略限制，处于下线状态的策略，引擎将自动不执行该策略。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/14.png)

## 删除

在策略列表，光标移至需要删除的模型上，点击右侧删除按钮，按照提示进行删除。

![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/service-center/ld.png)