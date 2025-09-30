# LDAP组织同步 · AWS PaaS文档中心

# LDAP组织同步

将LDAP的目录同步至当前平台。适用于企业内AD、LDAP接口。

## 概述

当前有企业用户使用LDAP作为基础信息平台，通过该平台集中为各子系统提供统一基准的部门人员信息。组织机构是AWS BPM系统运行的基础，需要用到LDAP的组织定义。

**选择同步技术方案的原因在于**

  * AWS组织模型和LDAP存在差异，直接使用不够灵活，复杂度高
  * 基于本地cache的元数据访问能获得性能上的优势

**特性**

  * 支持同步增加部门/人员到AWS组织
  * 支持同步变更部门/人员到AWS组织
  * 支持LDAP部门/人员删除后，AWS同步删除

### LDAP术语

LDAP常见述语 | 说明  
---|---  
DN | 上下文唯一名称，如：ou=研发部,ou=炎黄测试公司,dc=awstest,dc=com  
RDN | 上下文相对唯一名称，如：ou=研发部  
DC | Domain Component，域组件  
OU | Organizational Unit，组织单元  
CN | Common Name, 通用名  
  
## 配置

  1. 进入`工具附加 > LDAP Connector`页面
  2. 配置页面信息
  3. 点击`执行同步`按钮，开始同步

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady1.png)](<ady1.png>)

项 | 说明  
---|---  
LDAP适配器 | 选择已经配置的LDAP Connector  
同步线程数 | 不允许大于AWS数据库连接中maxActive值  
部门搜索上下文 | 相对CC LDAP适配器的子目录名称，用于配置搜索部门的目录，为空时搜索【服务提供者URL】所在的目录。  
例如，【服务提供者URL】为ldap://ip:port/DC=actionsoft,DC=com,DC=cn待同步的Active Directory部门为：OU=actionsoft,DC=actionsoft,DC=com,DC=cn  
那么该属性可配置为: OU=actionsoft或者【服务提供者URL】为ldap://ip:port/OU=actionsoft,DC=actionsoft,DC=com,DC=cn，该项为空  
人员搜索上下文 | 相对CC LDAP适配器的子目录名称，用于设置搜索人员的目录，  
为空时搜索【服务提供者URL】所在的目录，如：cn=users  
根部门//搜索条件 | 在`部门搜索上下文`目录下搜索根部门时使用的过滤条件，如：(OrgID=107876543290)  
根部门//搜索范围 | 根部门搜索方式  
Object：默认。当前目录  
One Level：`部门搜索上下文`的所有子目录  
Subtree：`部门搜索上下文`和所有子孙目录  
部门 | 部门搜索条件，例如(objectClass=organizationalUnit)  
人员 | 人员搜索条件，例如(&(objectclass=user)(!(objectclass=computer)))  
部门变更 | 新增或者部门变化的搜索条件，例如(&(objectClass=organizationalUnit)(|(whenCreated>=$st(yyyyMMddHHmmss.0'Z'))(whenChanged>=$st(yyyyMMddHHmmss.0'Z'))))。这里支持`$st`变量，配合`LDAP组织增量同步`定时任务使用  
人员变更 | 新增或者人员属性变化的搜索条件，例如(&(&(objectclass=user)(!(objectclass=computer)))(|(whenCreated>=$st(yyyyMMddHHmmss.0'Z'))(whenChanged>=$st(yyyyMMddHHmmss.0'Z'))))。这里支持`$st`变量，配合`LDAP组织增量同步`定时任务使用  
删除搜索上下文 | 相对CC LDAP适配器的子目录名称，用于配置删除部门的搜索目录，例如CN=Deleted Objects  
被删部门 | 被删除部门的搜索条件，例如(&(objectClass=organizationalUnit)(|(whenCreated>=$st(yyyyMMddHHmmss.0'Z'))(whenChanged>=$st(yyyyMMddHHmmss.0'Z'))))。这里支持`$st`变量，配合`LDAP组织增量同步`定时任务使用  
被删人员 | 被删除人员的搜索条件，例如(&(&(objectclass=user)(!(objectclass=computer)))(|(whenCreated>=$st(yyyyMMddHHmmss.0'Z'))(whenChanged>=$st(yyyyMMddHHmmss.0'Z'))))。这里支持`$st`变量，配合`LDAP组织增量同步`定时任务使用  
关联定义//用户ID | LDAP中用于存放登录账号的属性。  
关联定义//用户部门 | LDAP中用于表示用户所在部门的属性，其中**DN，Parent DN为特殊属性。**  
DN即Distinguished Name，是LDAP对象的唯一名称，例如：OU=actionsoft,DC=actionsoft,DC=com,DC=cn  
Parent DN是LDAP对象的父DN，例如：对象是部门，DN为OU=actionsoft,DC=actionsoft,DC=com,DC=cn，那么Parent DN为：DC=actionsoft,DC=com,DC=cn；如果对象是人员，DN为CN=levle1,OU=level1,DC=actionsoft,DC=com,DC=cn，那么Parent DN为OU=level1,DC=actionsoft,DC=com,DC=cn  
关联定义//部门ID | LDAP中用于存放部门ID的属性  
关联定义//父部门 | LDAP中用于表示父部门的属性  
关联定义//用户的部门属性值  
与部门的何属性值相同 | 用户部门属性值和部门的那个属性值相等。用于确定人员和部门的父子关系  
同步到//根部门 | LDAP组织同步到AWS单位  
同步到//其它部门 | LDAP组织同步到AWS部门  
默认角色 | LDAP组织账户同步到AWS后用户角色  
同步删除 | 全量同步时，当AWS中对象是来自于LDAP时，且该对象已在LDAP服务器删除，则同步从AWS系统中删除  
扩展接口 | 继承com.actionsoft.apps.addons.ldapsync.LdapAdapter的类，可自定义映射关系，例如Ldap上多个属性值映射到一个扩展字段中。如果返回null，则不同步当前执行对象。  
部门属性配置  | 设置LDAP属性与AWS部门属性字段对应关系，其中`CLOSED(部门注销)`这个字段实际不存在，程序会自动判断当LDAP来源字段值为0时，且该部门下没有子部门和账户时，会自动在AWS系统执行删除动作，当LDAP服务器上表示部门注销字段值不符合此逻辑时， 用户可通过`扩展接口`开发实现;支持扩展ORG结构应用中扩展的部门字段的映射  
人员属性配置 | 设置LDAP属性与AWS用户字段对关系，其中`CLOSED(账户注销)`程序会自动识别当LDAP来源字段值为0时，自动映射到orguser表closed字段为注消状态,当LDAP服务器上表示用户注销字段值不符合此逻辑时，用户可通过`扩展接口`开发实现。如果LDAP服务器是AD域可将userAccountControl映射为cloese字段，且程序已默认将514,546,66050,66082,262658,262690,328194,328226值自动映射为orguser表closed字段为注销状态; 支持扩展ORG结构应用中扩展的用户字段的映射  
  
**AD(Active Directory)应用实例配置示例图**

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady5.png)](<ady5.png>)

**其它LDAP应用实例配置示例图**

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady4.png)](<ady4.png>)

## 同步日志

LDAP组织同步时，可查看同步日志

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady3.1.1.png)](<ady3.1.1.png>)

## 结构参考

LDAP组织同步，提供了LDAP服务器部门和人员属性值参考信息，方便使用者了解LDAP组织信息结构。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady3.2.1.png)](<ady3.2.1.png>)

## 定时同步

### 全量定时同步

组织同步功能封装已在如下实现类中，该类继承了Runnable和Job接口，可以配置为定时任务或者作为线程执行（定时器需要配置在`com.actionsoft.apps.cc.connector.ldap`应用中或者配置依赖该应用）
    
    
    com.actionsoft.apps.addons.ldapsync.FullSyncJob
    

#### 延伸阅读

  * [AWS 定时器开发参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-job-reference-guide/index.html>)

### 增量定时同步

出厂预置定时任务。根据配置的`部门变更`、 `人员变更`、`被删部门`、`被删人员`属性值，从startTime参数时间开始到当前时间段内发生变化的对象执行增量同步。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady4.3.1.png)](<ady4.3.1.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady4.3.2.png)](<ady4.3.2.png>)

>   1. 第一次执行该定时器时需要配置自定义参数startTime。后续在执行时程序会自动读取上次执行的时间为本次执行时startTime参数值。
>   2. 定义器自琮义参数还可以写成`{startTime:"",useStartTime:"true"}`格式，`useStartTime`用于指示是否使用startTime属性。增量同步需要确定第一次同步的时间（非第一次使用上一次同步时间），比如第一次同步发生时间为2021.3.20日，但希望同步2021.1.1开始的组织变更，则将`useStartTime`参数放开即可，同理，如果同步中间出错，则设置最近一次时间用于矫正；
> 

### 定时同步日志

通过定时器进行组织全量、增量同步时 ，默认不会输出同步日志信息，用户可通过在bin/conf/aws-log4j.xml文件增中如下信息开启日志，开启后，在进行定时同步时，日志将会输出到logs目录下。
    
    
    <Logger name="com.actionsoft.apps.cc.connector.ldap" additivity="false" level="ALL">
                <appender-ref ref="asyncAppender" />
    </Logger>
    

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/adylog.png)](<adylog.png>)

## 同步修改LDAP密码

当AWS账户修改密码时，支持同步修改LDAP服务器相应账户密码。AWS平台使用默认登录适配器时，如果本地密码验证不通过，会支持LDAP服务器的登录验证。

**准备**

因LDAP用户的密码修改要求必须使用ldaps协议，因此

  1. LDAP服务器必须安装证书服务
  2. LDAP服务器证书必须能被AWS平台JDK识别 (建议将LDAP服务器证书导入到AWS平台使用的JDK所在 jre/lib/security/cacerts秘钥库)

> 关于LDAP服务器如何安装证书服务和导出证书，导入证书。可参考 <https://confluence.atlassian.com/display/CROWD/Configuring+an+SSL+Certificate+for+Microsoft+Active+Directory>   
>  <http://social.technet.microsoft.com/wiki/contents/articles/2980.ldap-over-ssl-ldaps-certificate.aspx>   
>  <https://yq.aliyun.com/articles/118657?t=t1>

**配置步骤**

  1. 注册LDAP适配器，其中URL应为ldaps格式，示例：【ldaps://192.168.0.30:636/ou=炎黄测试公司,dc=awstest,dc=com】。详细请参见上一章节
  2. 获得注册的LDAP适配器模型ID值，并配置到%AWS_HOME%/bin/conf/aws-portal.xml文件property name="org.ad.pwd.sync.cc" 属性值  
[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady3.4.1.png)](<ady3.4.1.png>)  
[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady3.4.2.png)](<ady3.4.2.png>)  

  3. 验证同步修改LDAP密码功能

> 该功能仅适用于AWS账户来自LDAP服务时

## 登录适配器

该应用默认提供了一个登录适配器，用于当LDAP服务可用时，登录信息直接从LDAP服务器上校验，如果验证不成功则不允许登录，当LDAP服务不可用时，采用AWS默认的登录适配器验证机制进行验证。

### 步骤

  1. 修改%AWS_HOME%/bin/conf/aws-portal.xml文件中`security #loginAdapter="com.actionsoft.bpms.commons.login.LDAPLoginAdapter"`
  2. 配置%AWS_HOME%/bin/conf/aws-portal.xml文件中`<property name="login.ldap.cc">LDAP适配器UUID值</property>`  
[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady3.4.1.png)](<ady3.4.1.png>)  

  3. 配置%AWS_HOME%/bin/conf/aws-portal.xml文件中`<property name="login.ldap.user.filter">(sAMAccountName=???)</property>`。 login.ldap.user.filter用于指定用户的匹配规则，除AD外必须填，???为占位符，例如AD的默认为：(sAMAccountName=???)

## AD用户属性userAccountControl

userAccountControl记录了用户的AD账号的很多属性信息，是一组16进制数。 该属性标志是累积性的。若要禁用用户的帐户，请将 UserAccountControl 属性设置为 0x0202 (0x002 + 0x0200)。在十进制中，它是 514 (2 + 512)。

**例如**  

  * 514=512+2=账号存在且关闭  

  * 66045=65536+512=密码永不过期+账号正常

属性标志 | 十六进制值 | 十进制值  
---|---|---  
SCRIPT | 0x0001 | 1  
ACCOUNTDISABLE | 0x0002 | 1:3  
HOMEDIR_REQUIRED | 0x0008 | 8  
LOCKOUT | 0x0010 | 16  
PASSWD_NOTREQD | 0x0020 | 32  
PASSWD_CANT_CHANGE | 0x0040 | 64  
ENCRYPTED_TEXT_PWD_ALLOWED | 0x0080 | 128  
TEMP_DUPLICATE_ACCOUNT | 0x0100 | 256  
NORMAL_ACCOUNT | 0x0200 | 512  
INTERDOMAIN_TRUST_ACCOUNT | 0x0800 | 20481  
WORKSTATION_TRUST_ACCOUNT | 0x1000 | 4096  
SERVER_TRUST_ACCOUNT | 0x2000 | 8192  
DONT_EXPIRE_PASSWORD | 0x10000 | 65536  
MNS_LOGON_ACCOUNT | 0x20000 | 131072  
SMARTCARD_REQUIRED | 0x40000 | 262144  
TRUSTED_FOR_DELEGATION | 0x80000 | 524288  
NOT_DELEGATED | 0x100000 | 1048576  
USE_DES_KEY_ONLY | 0x200000 | 2097152  
DONT_REQ_PREAUTH | 0x400000 | 4194304  
PASSWORD_EXPIRED | 0x800000 | 8388608  
TRUSTED_TO_AUTH_FOR_DELEGATION | 0x1000000 | 16777216  
  
### 属性标志说明

  * `SCRIPT` \- 将运行登录脚本。
  * `ACCOUNTDISABLE` \- 禁用用户帐户。
  * `HOMEDIR_REQUIRED` \- 需要主文件夹。
  * `PASSWD_NOTREQD` \- 不需要密码。
  * `PASSWD_CANT_CHANGE` \- 用户不能更改密码。可以读取此标志，但不能直接设置它。
  * `ENCRYPTED_TEXT_PASSWORD_ALLOWED` \- 用户可以发送加密的密码。
  * `TEMP_DUPLICATE_ACCOUNT` \- 此帐户属于其主帐户位于另一个域中的用户。此帐户为用户提供访问该域的权限，但不提供访问信任该域的任何域的权限。有时将这种帐户称为“本地用户帐户”。
  * `NORMAL_ACCOUNT` \- 这是表示典型用户的默认帐户类型。
  * `INTERDOMAIN_TRUST_ACCOUNT` \- 对于信任其他域的系统域，此属性允许信任该系统域的帐户。
  * `WORKSTATION_TRUST_ACCOUNT` \- 这是运行 Microsoft Windows NT 4.0 Workstation、Microsoft Windows NT 4.0 Server、Microsoft Windows 2000 Professional 或 Windows 2000 Server 并且属于该域的计算机的计算机帐户。
  * `SERVER_TRUST_ACCOUNT` \- 这是属于该域的域控制器的计算机帐户。
  * `DONT_EXPIRE_PASSWD` \- 表示在该帐户上永远不会过期的密码。
  * `MNS_LOGON_ACCOUNT` \- 这是 MNS 登录帐户。
  * `SMARTCARD_REQUIRED` \- 设置此标志后，将强制用户使用智能卡登录。
  * `TRUSTED_FOR_DELEGATION` \- 设置此标志后，将信任运行服务的服务帐户（用户或计算机帐户）进行 Kerberos 委派。任何此类服务都可模拟请求该服务的客户端。若要允许服务进行 Kerberos 委派，必须在服务帐户的userAccountControl 属性上设置此标志。
  * `NOT_DELEGATED` \- 设置此标志后，即使将服务帐户设置为信任其进行 Kerberos 委派，也不会将用户的安全上下文委派给该服务。
  * `USE_DES_KEY_ONLY` \- (Windows 2000/Windows Server 2003) 将此用户限制为仅使用数据加密标准 (DES) 加密类型的密钥。
  * `DONT_REQUIRE_PREAUTH` \- (Windows 2000/Windows Server 2003) 此帐户在登录时不需要进行 Kerberos 预先验证。
  * `PASSWORD_EXPIRED` \- (Windows 2000/Windows Server 2003) 用户的密码已过期。
  * `TRUSTED_TO_AUTH_FOR_DELEGATION`\- (Windows 2000/Windows Server 2003) 允许该帐户进行委派。这是一个与安全相关的设置。应严格控制启用此选项的帐户。此设置允许该帐户运行的服务冒充客户端的身份，并作为该用户接受网络上其他远程服务器的身份验证。

## 突破AD查询1000条限制

Active Directory 中 LDAP策略 MaxTempTableSize 默认最大1000条记录，因此在同步用户时，如果发现只能同步到1000个用户时，可考虑该限制影响。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/ady1000.png)](<ady1000.png>)

具体配置更改请参见：

<http://blog.csdn.net/mooncarp/article/details/51119126>

<https://support.microsoft.com/zh-cn/help/315071/how-to-view-and-set-ldap-policy-in-active-directory-by-using-ntdsutil>

## 延伸阅读

  * [扩展ORG结构产品发行文档](<https://docs.awspaas.com/apps/com.actionsoft.apps.extendorg/index.html>)