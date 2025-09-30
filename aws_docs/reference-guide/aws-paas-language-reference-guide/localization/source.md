# 元数据多语言 | AWS PaaS多语言开发参考指南

# 元数据多语言

AWS PaaS平台各模型名称均可统称为元数据。如下场景已提供元数据在线翻译。

  * 单位名称
  * 部门名称
  * 人员姓名
  * 角色名称
  * BO名称/BO字段名称
  * DD/DR字典标题名称
  * 表单名称
  * 流程组/流程名称/节点名称/审核菜单名称
  * DW名称/DW视图名称/DW报表名称
  * 导航菜单子系统/功能/目录名称
  * 应用名称

![](https://docs.awspaas.com/reference-guide/aws-paas-language-reference-guide/localization/1.png)

>   1. 元数据在线翻译功能要求AWS PaaS平台版本不低于6.2.GA
>   2. 组织相关类元数据多语言资源自动存放在`%AWS_HOME%/apps/install/_bpm.platform/i18n/`目录下
>   3. 业务建模相关类元数据多语言资源自动存放在相应应用`%AWS_HOME%/apps/install/%APPID%/i18n/`目录下
>   4. 如果一个导航菜单被应用引用，则多语言资源部署到`%AWS_HOME%/apps/install/%APPID%/i18n`目录中，如果导航菜单是孤立的，不属于任何应用，则多语言资源自动部署到`%AWS_HOME%/apps/install/_bpm.platform/i18n`中
>