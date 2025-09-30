# 环境 · AWS PaaS文档中心

# 环境

实现连接服务CC模块中各适配器、策略配置中服务器地址、URL、端口、用户名、密码等参数值的统一配置管理。 方便开发、测试、生成环境相关参数的快速切换。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/hj/env.gif)](<env.gif>)

> 环境列表无分页。

## 配置

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/hj/1.png)](<1.png>)

项 | 说明  
---|---  
变量名 | 全局唯一，不允许重复。@env将传入该变量名获取变量值 建议仅包含字母和数字。  
类型 | Text，文本   
Password，密码，该类型会采用加密方式存储到数据库   
Dockfile Env，当AWS部署到Docker容器中时，可获取Dockerfile文件中Env的值   
etcd Key，获取etcd数据库相应key值  
变量值 | 变量值。   
当类型为Dockfile Env 时，此处填写Dockerfile文件中Env的Key   
当类型为etcd key时，此处填写etcd库中存在的的Key  
分类 | 分类名  
描述 | 描述信息，不允许超过200个字符  
扩展1 | 当类型为 etcd Key时，此处填写etcd库的连接信息。  
格式：`{endpoints:["http://192.168.0.100:2379"],user:"",password:""}`  
扩展2 | 扩展2，备用  
扩展3 | 扩展3，备用  
  
## 修改

点击需要修改变量所在行右侧编辑按钮，打开修改窗口进行修改，其中变量名不允许修改。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/hj/2.png)](<2.png>)

## 删除

勾选要删除的记录，点击删除按钮，按照提示进行删除。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/hj/3.png)](<3.png>)

## 导入

点击工具条导入按钮，下载模板后，填写信息，上传，进行导入。

  * 导入模板中变量名如果有重复，导入后值为第一条记录的值
  * 导入模板中变量名如果与已有变量名重复，则修改原变量值为模板中变量值

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/hj/4.png)](<4.png>)

## 导出

勾选需要导出的记录，点击工具栏导出按钮，进行导出。导出后可直接作为导入模板，进行导入。例如：从测试环境中导出后导入到生产环境。

## 获取变量值

在相关CC模型支持@公式的属性中使用@env(变量名)进行获取。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/hj/5.png)](<5.png>)

**_语法_**

@env(*varName,valueOf)

  * 取CC环境变量值，如果参数不存在返回空串

**_参数_**

  * _varName_ （必选）CC环境参数名称

  * _valueOf_ （可选）可设置常量ext1、ext2、ext3取扩展值

**_例子_**
    
    
    @env(crmServerUrl)/api/abc