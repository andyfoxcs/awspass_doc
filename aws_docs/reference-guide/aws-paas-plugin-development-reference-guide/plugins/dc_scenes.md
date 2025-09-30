# 应用场景 · AWS PaaS文档中心

# 应用场景

DC是Doc Center的缩写，AWS平台通过DC为每个应用存取和管理非结构文件。AWS DC是一个有着严格规范的结构化存储体系，能够根据`DC根目录`的命名规则确定深度和安全性，并为每个App分配私有的存储空间。

[![DC文件仓库结构](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/dc-1.png)](<dc-1.png>)

### 读/写文件

  * 为你的应用申请DC根目录，并编写私有的文件处理器
  * 使用AWS MVC编程框架封装的upfile组件，实现文件上传

下图显示`Metro主题风格`应用，通过开发`DC文件处理器`与AWS MVC编程框架的upfile组件，实现头像文件的上传。

[![DC文件处理器与upfile组件配合](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/dc-2.png)](<dc-2.png>)