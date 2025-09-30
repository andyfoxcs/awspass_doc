# 附录3-开发工具 · AWS PaaS文档中心

# 附录3-开发工具

AWS MVC的开发者可以根据自己的编程习惯选择开发工具。

## Eclipse

对于熟悉AWS PaaS和App应用资源配置结构的开发者，也可以直接使用Eclipse完成所有的任务目标。

  1. 新建`Java普通工程`
  2. 在`Java Build Path>Libraries`下创建`aws_lib`库，增加以下资源
         
         %AWS-HOME%/bin/lib/*.jar(含子目录）
         %AWS-HOME%/bin/jdbc/*.jar
         

  3. 启动`aws-infrastructure-common.jar`的`StartUp`
         
         com.actionsoft.bpms.server.AWSServer.StartUp
         

  4. 指定启动选项中`Working directory`目录
         
         %AWS-HOME%/bin
         

开发环境搭建详细步骤参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-dev-env-guide/index.html>)。

## developer.csr

在你的团队正式开发应用前，应获得应用开发者证书(ISV)。证书文件路径如下
    
    
    %AWS-HOME%/apps/developer.csr