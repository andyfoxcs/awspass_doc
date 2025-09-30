# 应用场景 · AWS PaaS文档中心

## 应用场景

这是一个AWS PaaS的ADD-ONS（工具附加）应用，能够通过插件注册为AWS PaaS的上层应用创建独立的索引库，提供内容（文件/数据记录）全文索引和搜寻服务。

> 如果启用该项服务，可从`AWS企业应用商店`安装`全文检索引擎`应用。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/fullsearch-1.png)](<fullsearch-1.png>)

### ASLP服务接口

可以通过调用该应用提供的ASLP服务接口，让你的程序支持全文检索能力。包括入库、检索及各种Lucene高级语法支持。下图是该App的资源清单：

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/fullsearch-2.png)](<fullsearch-2.png>)

> 每个服务接口的参数说明和示例，可点击`Meta`查看

### 工具附加扩展

作为PaaS管理员，安装`全文检索引擎`应用后，可在`AWS CONSOLE > 工具附加`访问全部索引库的存储信息

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/fullsearch-3.png)](<fullsearch-3.png>)

> 当前`全文检索引擎`v1.0.1版本不支持AWS集群模式，很快将会得到支持