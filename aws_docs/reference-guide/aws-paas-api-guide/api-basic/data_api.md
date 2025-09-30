# 数据 · AWS PaaS文档中心

# 数据

AWS PaaS为开发者提供的BO/DC等数据操作接口。

  * BO操作
  * DC操作

> 以下给出该类API的常用部分，但不完整，请以相关文档为准

## BO操作（Business Object）

  * CRUD操作
    * 增加记录
    * 删除记录
    * 修改记录
    * 查询记录
  * 其他
    * 对附件字段的CRUD操作

## DC操作（Doc Center）

  * 读文件
  * 写文件
  * 复制文件
  * 加密文件
  * 解密文件

## API索引

API类型 | 说明  
---|---  
[HTTP(s)](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/http/>) | cmd=bo.xxx(如`bo.create`)   
cmd=dc.xxx(如`dc.downfile`)  
[SOAP](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/soap/>) | service=`boApi`  
service=`dcApi`  
[Java SDK](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/>) | SDK.getBOAPI()  
SDK.getTDCAPI()