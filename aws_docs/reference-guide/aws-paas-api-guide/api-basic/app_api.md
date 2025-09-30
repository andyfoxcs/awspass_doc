# 应用 · AWS PaaS文档中心

# 应用

AWS PaaS为开发者提供的应用资源和状态的查询操作接口。

> 以下给出该类API的常用部分，但不完整，请以相关文档为准

  * 查询类
    * 根据appId，获得app在当前AWS节点实例的上下文对象
    * 获得当前App的用户会话对象
    * 判断指定的应用是否已安装
    * 判断指定appId的应用是否已启动
  * 参数类
    * 获得应用自定义的系统参数值
    * 保存应用自定义的系统参数值
  * 日志类
    * 向指定App发送一条调试信息日志(info)
    * 向指定App发送一条错误信息日志，并输出至命令行屏幕(err)
    * 向指定App发送一条警告信息日志，并输出至命令行屏幕(warn)
  * 多语言类
    * 取界面语言对应在i18n资源里的配置项
  * 应用间互操作类
    * 同步调用一个ASLP服务地址
    * 异步调用一个ASLP服务地址

## API索引

API类型 | 说明  
---|---  
[HTTP(s)](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/http/>) | cmd=app.xxx(如`app.get`)  
[SOAP](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/>) | service=`appApi`  
[Java SDK](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/>) | SDK.getAppAPI()