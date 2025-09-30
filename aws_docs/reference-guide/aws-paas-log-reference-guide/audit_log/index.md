# 审计日志 · AWS PaaS文档中心

# 审计日志

AWS的审计日志数据涵盖了应用开发、部署、运行和维护全周期，并对安全、风险等特定场景提供专项记录。所有这些日志的收集默认开启。

审计日志数据存放在数据库中，有关保留期限请[查看这里](<../appendix/record_cycle.html>)。

## 日志分类

  * 专项审计
  * 控制台
  * 客户端

分类 | 项 | 说明  
---|---|---  
专项审计 | 平台升级 | 当前AWS平台补丁升级日志  
专项审计 | 账户冻结 | 客户端登录时因口令错误被暂时冻结记录  
专项审计 | 越权访问 | 用户试图访问权限外操作  
专项审计 | 用户会话 | 创建的用户会话  
控制台 | 组织服务 | 单位、部门、账户、角色的增/删/改操作  
控制台 | 业务建模 | 流程、表单、存储等业务模型的增/删/改操作  
控制台 | 调度服务 | 定时器Job的增/删/改操作和调度日志  
控制台 | 连接服务 | CC各类服务资源的增/删/改操作和调用日志  
控制台 | 运行管理 | 对流程实例、任务实例执行的运维操作，如跳转、删除  
控制台 | 应用管理 | 应用的安装、升级、卸载日志  
控制台 | 导航服务 | 导航菜单增/删/改操作  
控制台 | 工具附加 | 工具附加应用的访问日志  
客户端 | 用户操作 | 客户端特定操作日志  
  
## 日志访问

  1. 登录您的AWS PaaS实例控制台
  2. 访问“运维管理>日志审计查询”页面

[![](https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/audit_log/1.png)](<1.png>)

**日志信息**

项 | 说明  
---|---  
级别 | 日志级别  
主体 | 访问主体，如一个用户账号  
操作时间 | 日志记录时间，取服务器端时间  
地点 | 通常是访问主体的IP地址  
日志类型 | 操作场景，见上表  
客体 | 主体操作的对象标识，如一个流程模型Id  
操作 | 主体对客体的操作类型  
信息 | 信息描述线索，通常是对日志操作的补充  
  
**日志级别**

  * 普通级别
  * 警告级别
  * 错误级别

**客体操作**

对访问主体或操作的客体，可能会记录以下操作类型

  * access 访问
  * create 创建
  * update 更新
  * delete 删除
  * reset 重置
  * disable 注销
  * active 激活
  * memo 记录
  * exec 执行
  * call 调用
  * install 安装
  * upgrade 升级
  * uninstall 卸载

应用开发者可以使用LogAPI记录客户端审计操作
    
    
    /**
     * 记录一条客户端审计日志
     *
     * @param auditSubject 审计主体标识，如登录账户名
     * @param op 操作（可选操作类型：access、create、update、delete、exec、call）
     * @param auditObject 审计客体标识，自定义
     * @param detail 描述信息
     * @param ip 主体IP，通常可以从UserContext上下文中获取
     * @param level 日志级别
     *
     * @see Level
     */
    SDK.getLogAPI().audit(auditSubject, op, auditObject, detail, ip, level);