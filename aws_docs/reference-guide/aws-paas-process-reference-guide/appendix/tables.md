# 流程引擎表结构 | AWS BPMN2 Process参考指南

# 流程引擎表结构

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/appendix/db.png)

### 流程控制数据(WFC_*)

##### 1\. WFC_PROCESS（流程实例）

字段 | 说明  
---|---  
ID | 流程实例ID  
BUSINESSKEY | 业务主键  
PROCESSDEFID | 流程定义ID  
PROCESSDEFVERID | 流程主版本ID  
CONTROLSTATE | 实例控制状态  
PROCESSGROUPID | 流程组ID  
PROCESSTITLE | 实例标题  
STARTACTIVITYID | 开始事件定义ID  
STARTTASKINSTID | 开始实例ID  
STARTTIME | 启动时间  
PROCESSPROFILEID | 子流程配置ID  
PROCESSINSTTYPE | 子流程实例类型  
PARENTPROCESSINSTID | 父流程实例ID  
PARENTTASKINSTID | 父任务实例ID  
SECURITYLAYER | 保密级别  
CREATEUSER | 创建者  
CREATETIME | 创建时间  
CREATEUSERORGID | 创建者所在组织ID  
CREATEUSERDEPTID | 创建者部门ID  
CREATEUSERROLEID | 创建者角色ID  
CREATEUSERLOCATION | 创建者部门全路径  
ENDACTIVITYID | 结束事件定义ID  
ENDTIME | 结束时间  
ISPROCESS | 是否流程实例  
ISSTART | 是否启动  
ISEND | 是否结束  
ISASYNC | 是否异步执行  
ISEXCEPTION | 是否异常  
ISOVERTIME | 是否超时  
ISEXISTSUBPROC | 是否存在子流程  
COSTTTIME | 执行耗时  
EXPIRETIME | 超时时间  
REMARK | 备注信息  
IOBD | 业务域ID，Instance Of Business Domain  
IOR | 组织区域ID，Instance Of Regional  
IOS | 系统ID，Instance Of System  
IOC | 自定义分类ID，Instance Of Customize  
EXT1 | 扩展参数1  
EXT2 | 扩展参数2  
EXT3 | 扩展参数3  
EXT4 | 扩展参数4  
EXT5 | 扩展参数5  
EXT6 | 扩展参数6  
EXT7 | 扩展参数7，整型  
EXT8 | 扩展参数8，浮点型  
REMINDTIMES | 流程总催办次数  
ISTRASH | 是否垃圾数据  
  
##### 2\. WFC_TASK（任务实例）

字段 | 说明  
---|---  
ID | 任务实例ID  
PARENTTASKINSTID | 父任务实例ID  
SCOPEID | 范围ID  
ACTIVITYTYPE | 活动类型  
ACTIVITYDEFID | 活动定义ID  
PROCESSINSTID | 流程实例ID  
PROCESSDEFID | 流程定义ID  
PROCESSDEFVERID | 流程主版本ID  
PROCESSGROUPID | 流程组ID  
DISPATCHID | 多例调度ID  
TASKTITLE | 任务标题  
TASKSTATE | 任务类型  
CONTROLSTATE | 实例控制状态  
PRIORITY | 优先级  
OWNER | 任务创建  
TARGET | 任务执行  
CLAIMTYPE | 任务认领类型  
CLAIMRESOURCEID | 任务认领资源ID  
DUETIME | 到期时间  
BEGINTIME | 开始时间  
BEGINENGINENODE | 任务创建在服务节点  
READTIME | 任务读取时间  
READSTATE | 任务是否已读  
OWNERDEPTID | 创建人所在部门ID  
TARGETDEPTID | 办理人所在部门ID  
TARGETCOMPANYID | 办理人所在单位ID  
TARGETROLEID | 办理人角色ID  
ISMONITOR | 是否监控  
ISASYNC | 是否异步执行  
EXCEPTIONERR | 异常信息  
IOBD | 业务域ID，Instance Of Business Domain  
IOR | 组织区域ID，Instance Of Regional  
IOS | 系统ID，Instance Of System  
IOC | 自定义分类ID，Instance Of Customize  
EXT1 | 扩展参数1，流程引擎使用该字段进行特殊操作，业务场景请勿使用该字段  
EXT2 | 扩展参数2  
EXT3 | 扩展参数3  
EXT4 | 扩展参数4  
EXT5 | 扩展参数5  
EXT6 | 扩展参数6  
EXT7 | 扩展参数7，整型  
EXT8 | 扩展参数8，浮点型  
DELAYTIMES | 任务延期时间  
REMINDTIMES | 任务总催办次数  
SECURITYLAYER | 密级级别  
ISTRASH | 是否垃圾数据  
  
##### 3\. WFC_TRANSITION（状态转移控制）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
PROCESSDEFID | 流程定义ID  
SOURCEDEFID | 源活动定ID  
SOURCETYPE | 源活动类型  
SEQUENCEFLOWDEFID | 转移定义ID  
TARGETDEFID | 目标活动定义ID  
TARGETTYPE | 目标活动类型  
ISACTIVE | 是否活动  
CREATETIME | 创建时间  
  
##### 4\. WFC_VAR（流程变量）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
VARSCOPE | 有效范围  
VARNAME | 变量名  
VALUETYPE | 值类型  
TEXTVALUE | 变量值  
LONGVALUE | 变量值  
DOUBLEVALUE | 变量值  
CREATETIME | 创建时间  
UPDATETIME | 更新时间  
  
##### 5\. WFC_TASKMID（多例任务调度）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
PROCESSDEFID | 流程定义ID  
PROCESSDEFVERID | 流程主版本ID  
ACTIVITYDEFID | 活动定义ID  
OWNER | 任务创建  
OWNERDEPTID | 创建人所在部门ID  
TARGET | 任务执行  
TARGETDEPTID | 执行人所在部门ID  
TARGETCOMPANYID | 执行人所在单位ID  
TARGETROLEID | 执行人角色ID  
DISPATCHSTATE | 调度状态  
PRIORITY | 优先级  
DUETIME | 到期时间  
ORDERINDEX | 调度顺序  
  
##### 6\. WFC_COMMENTTEMP（用户暂存的审批信息）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
ACTIONNAME | 审核菜单名  
MSG | 留言信息  
FILES | 留言附件  
DIGITALSIGNATURE | 数字签名  
SIGNKEY | 签名证书  
  
##### 7\. WFC_COMMENT（任务审批记录）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
CREATEDATE | 记录日期  
CREATEUSER | 创建人  
DEPTNAME | 部门名称  
POSITIONNAME | 岗位名称  
ACTIONNAME | 审核菜单名  
ACTIVITYNAME | 节点名称  
MSG | 留言信息  
FILES | 留言附件  
DIGITALSIGNATURE | 数字签名  
SIGNKEY | 签名证书  
  
##### 8\. WFC_FORMFILES（流程表单附件）

字段 | 说明  
---|---  
ID | 主键唯一索引  
APPID | 应用ID  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
BOID | BO表ID  
BONAME | BO模型名称  
BOFIELDNAME | 字段名  
CREATEDATE | 记录日期  
CREATEUSER | 创建人  
FILENAME | 文件名  
FILESIZE | 文件大小  
REMARK | 文件注释  
EXT1 | 扩展数据1  
SECURITYLEVEL | 密级级别  
CLOUDINFO | 云信息  
ORDERINDEX | 排序  
GROUPNAME | 分组  
  
##### 9\. WFC_URLTOKEN（授权外部系统执行表单）

字段 | 说明  
---|---  
TOKENID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
AWSUID | 账户名  
TOKENSTATE | 状态  
ACCESSTIME | 访问时间  
MEMO | 备注  
  
### 流程历史数据(WFH_*)

##### 1\. WFH_TASK（历史任务实例）

字段 | 说明  
---|---  
ID | 任务实例ID  
PARENTTASKINSTID | 父任务实例ID  
SCOPEID | 范围ID  
ACTIVITYTYPE | 活动类型  
ACTIVITYDEFID | 活动定义ID  
PROCESSINSTID | 流程实例ID  
PROCESSDEFID | 流程定义ID  
PROCESSDEFVERID | 流程主版本ID  
PROCESSGROUPID | 流程组ID  
DISPATCHID | 多例调度ID  
TASKTITLE | 任务标题  
TASKSTATE | 任务类型  
CONTROLSTATE | 实例控制状态  
PRIORITY | 优先级  
OWNER | 任务创建  
TARGET | 任务执行  
CLAIMTYPE | 任务认领类型  
CLAIMRESOURCEID | 任务认领资源ID  
DUETIME | 到期时间  
BEGINTIME | 开始时间  
BEGINENGINENODE | 任务创建在服务节点  
ENDTIME | 结束时间  
ENDENGINENODE | 任务结束在服务节点  
READTIME | 任务读取时间  
READSTATE | 任务是否已读  
OWNERDEPTID | 创建人所在部门ID  
TARGETDEPTID | 办理人所在部门ID  
TARGETCOMPANYID | 办理人所在单位ID  
TARGETROLEID | 办理人角色ID  
ISMONITOR | 是否监控  
ISASYNC | 是否异步执行  
EXCEPTIONERR | 异常信息  
IOBD | 业务域ID，Instance Of Business Domain  
IOR | 组织区域ID，Instance Of Regional  
IOS | 系统ID，Instance Of System  
IOC | 自定义分类ID，Instance Of Customize  
EXT1 | 扩展参数1  
EXT2 | 扩展参数2  
EXT3 | 扩展参数3  
EXT4 | 扩展参数4  
EXT5 | 扩展参数5  
EXT6 | 扩展参数6  
EXT7 | 扩展参数7  
EXT8 | 扩展参数8  
ISUNDO | 是否可收回  
COSTTTIME | 执行耗时  
EXPIRETIME | 超时时间  
DELAYTIMES | 任务延期时间  
REMINDTIMES | 任务总催办次数  
ISTRASH | 是否垃圾数据  
SECURITYLEVEL | 密级级别  
  
##### 2\. WFH_TRANSITION（历史状态转移控制数据）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
PROCESSDEFID | 流程定义ID  
SOURCEDEFID | 源活动定ID  
SOURCETYPE | 源活动类型  
SEQUENCEFLOWDEFID | 转移定义ID  
TARGETDEFID | 目标活动定义ID  
TARGETTYPE | 目标活动类型  
ISACTIVE | 是否活动  
CREATETIME | 创建时间  
ENDTIME | 结束时间  
  
##### 3\. WFH_VAR（历史流程变量）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
VARSCOPE | 有效范围  
VARNAME | 变量名  
VALUETYPE | 值类型  
TEXTVALUE | 变量值  
LONGVALUE | 变量值  
DOUBLEVALUE | 变量值  
CREATETIME | 创建时间  
UPDATETIME | 更新时间  
  
##### 4\. WFH_COMMENT（任务审批历史记录）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
CREATEDATE | 记录日期  
CREATEUSER | 创建人  
DEPTNAME | 部门名称  
POSITIONNAME | 岗位名称  
ACTIONNAME | 审核菜单名  
ACTIVITYNAME | 节点名称  
MSG | 留言信息  
DIGITALSIGNATURE | 数字签名  
SIGNKEY | 签名证书  
  
##### 5\. WFH_FORMSNAPSHOT（表单数据版本快照）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
PROCESSDEFID | 流程定义ID  
ACTIVITYDEFID | 活动定义ID  
AUTHORUID | 表单操作人  
AUTHORNAME | 操作人姓名  
RECORDTIME | 记录日期  
FORMID | 表单模型ID  
VNAME | 表单名称或其他简称  
  
##### 6\. WFH_FORMPRINT（表单打印历史）

字段 | 说明  
---|---  
ID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
PRINTTIME | 打印时间  
USERID | 操作人  
USERNAME | 操作人姓名  
IPADD | IP 地址  
  
##### 7\. WFH_URLTOKEN（历史授权外部系统执行表单）

字段 | 说明  
---|---  
TOKENID | 主键唯一索引  
PROCESSINSTID | 流程实例ID  
TASKINSTID | 任务实例ID  
AWSUID | 账户名  
TOKENSTATE | 状态  
MEMO | 备注  
  
### 流程归档数据(WFA_*)

由归档方案定制。