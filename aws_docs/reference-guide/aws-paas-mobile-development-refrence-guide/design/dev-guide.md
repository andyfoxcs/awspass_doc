# 开发规范 | AWS 移动开发参考指南

# 开发规范

### 1.常规要求

项 | 遵循度 | 说明  
---|---|---  
AppId | *必须 | 该 App 的唯一标识名，前缀与开发证书相同  
  
**要求:**  
-最小 6 个字符,最大 64 个字符长度  
-前缀必须以下划线、英文字母、阿拉伯数字开头  
-全部小写,至少包含一个.  
-建议参考 Java Package 命名规范  
  
**示例:**  
com.haier.apps.globalorder   
com.abc.apps.notepad  
App Name | 建议 | 简短、易识别、易区别的名称  
  
**示例:**  
海尔全球订单系统  
金山记事本  
App Version | 建议 | -一位小数  
-第一次发布从 1.0 开始  
-Bug 修复和功能改善增加小版本号，如 1.1  
增加新模块或较大提升，增加大版本号，如2.0  
应用参数配置 | 建议 | 非业务字典类简单开关配置，  
建议定义到App的 manifest.xml(可在控制台的应用管理模块中维护)，  
程序中使用 SDK.getAPPAPI().getProperty()读取  
数据库物理表前缀 | *必须 | manifest.xml文件 tablePrefix项。  
您的App将可能与其他厂商的App 组合部署在同一个PaaS平台，  
这项规范要求为创建的BO 表和自定义的  
物理表约定前缀关 键词。前缀由申请的开发证书约定  
  
**要求：**  
-最小 2 个字符,最大 4 个字符长度  
-前缀必须以英文字母、阿拉伯数字开头  
-不区分大小写  
  
**示例:**  
-如果是BO存储,前缀规则为 BO`_`前缀关键词`_`XXX  
-如果SQL建表,前缀规则为APP`_`前缀关键词`_`XXX  
App依赖 | *必须 | 每个App应用必须依赖一个父 App。  
若规划的应用是一个全新的独立系统，可指定依赖平台的 AppId；  
若该应用是某个应用的扩展时必须指定正确的依赖AppId。  
此项在 manifest.xml(可在控制台的应用开发模块中设置)   
  
**要求:**  
-给定一个依赖的AppId  
-给定适用于该 AppId 的版本号,多个逗号隔开  
根App | 建议 | 补充上述规范。如果要规划的是一个全新独立应用，  
建议按如下规则选择父appId  
  
-业务应用类App,选择`_bpm.portal`  
-CoE类 App，选择`_bpm.coe`  
-系统技术类App，选择`_bpm.platform`  
  
### 2.MVC编程

项目 | 遵循度 | 说明  
---|---|---  
Java程序包路径命名 | *必须 | 前缀与appId相同   
  
**示例:**  
package `com.haier.apps.globalorder`  
package `com.abc.apps.notepad`  
cmd命名 | *必须 | 前缀与appId相同  
  
**示例:**  
`com.haier.apps.globalorder`_home_dashboard  
`com.abc.apps.notepad`_saveContent  
Java编程风格与注释 | 建议 | -遵循Java标准  
-类、方法、变量提供简洁、有效的注释  
文件读写限制 | *必须 | **限制如下:**  
-只允许读写该 app安装目录下的资源  
-通过声明DC，读写doccenter下的 DC资源  
  
超出该限制的，应在申请发布时给予原因说明  
变量命名 | 建议 | 与AWS PaaS相关的Java变量命名参考  
-流程实例 ID(processInstId、processInstanceId)  
-流程实例对象(processInstModel、processInstanceModel)  
-任务实例ID(taskInstId、taskInstanceId)  
-任务实例对象(taskInstModel、taskInstanceModel)  
-BO表ID(boId)  
-BO表与流程实例关联Id(bindId)  
HTML 模版等外部文件资源 | *必须 | UTF-8无BOM编码格式  
数据库设计 | 建议 | -使用平台提供的UUIDGener获得定长的UUID 值(36位长度)  
-不推荐使用数据库自增长字段或数值类Id字段  
-不推荐使用存储过程  
  
JDBC编程 | *必须 | -使用Preparedstatement  
-Connection资源被确保释放  
-循环之内，不允许超过10次循环的创建Connection  
Web层禁止数据库操作 | *必须 | 避免不统一的连接配置和集群失效风险，降低故障排查成本。建议采用AWS MVC编程框架或调用AWS的OPEN API，将逻辑封装到服务端  
  
### 3.Java工程资源结构

假设应用Id为`com.abc.apps.xyz`

项 | 遵循度 | 说明  
---|---|---  
注册类 | 建议 | 示例：`com.abc.apps.xyz`.Plugin  
控制类 | 建议 | 示例：`com.abc.apps.xyz`.XYZController  
常量类 | 建议 | 示例：`com.abc.apps.xyz`.XYZConst  
web包 | 建议 | 示例：`com.abc.apps.xyz`.web.*  
工具包 | 建议 | 示例：`com.abc.apps.xyz`.util.*  
事件包 | 建议 | 示例：`com.abc.apps.xyz`.event.*  
调度包 | 建议 | 示例：`com.abc.apps.xyz`.job.*  
通知包 | 建议 | 示例：`com.abc.apps.xyz`.notification.*  
接口包 | 建议 | 示例：`com.abc.apps.xyz`.aslp.*  
规则包 | 建议 | 示例：`com.abc.apps.xyz`.at.*  
UI包 | 建议 | 示例：`com.abc.apps.xyz`.ui.*  
  
### 4.其它

如果开发中用到了`BO建模配置`、`公共基础字典`、`DW建模配置`等，可参考[这里](<https://docs.awspaas.com/reference-guide/aws-paas-app-design-guide/develop/dev.html>)。