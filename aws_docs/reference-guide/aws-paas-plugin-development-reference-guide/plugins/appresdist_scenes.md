# 应用场景 · AWS PaaS文档中心

## 应用场景

**`应用A`关联`应用P`的文件资源**

关联`应用P`的资源信息会随`应用A`的分发保存到`应用A`的安装包中，以确保`应用A`分发给其他环境后`应用P`的资源信息不会丢失。  

配置`应用A`时，关联`应用P`要勾选`随应用分发`选项。  

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/appresdist1.png)](<appresdist1.png>)

**例如：**

邮件通知配置了应用A的邮件模板，对应的邮件模板数据信息存储在邮件通知应用中，如果分发应用A时邮件模板数据信息会在分发时存储到应用的安装包中，分发下载后的安装包安装在另一环境时也会安把邮件通知的数据安装到此环境的邮件通知的应用下。