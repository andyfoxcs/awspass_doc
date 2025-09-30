# 组织 | AWS @公式参考指南

## 组织

  * userName
  * uid
  * userUniqueId
  * userNo
  * userPositionName
  * userPositionNo
  * userPositionLayer
  * userMobile
  * userTel
  * userEmail
  * userPhoto
  * userExt1
  * userExt2
  * userExt3
  * userExt4
  * userExt5
  * userBOExt
  * userManager
  * user
  * companyName
  * companyId
  * companyNo
  * companyType
  * companyExt1
  * companyExt2
  * companyExt3
  * companyExt4
  * companyExt5
  * companyBOExt
  * departmentName
  * departmentPathName
  * departmentId
  * departmentPathId
  * departmentNo
  * departmentType
  * departmentZone
  * departmentManager
  * isDepartmentManager
  * departmentExt1
  * departmentExt2
  * departmentExt3
  * departmentExt4
  * departmentExt5
  * departmentBOExt
  * roleId
  * roleName
  * roleExt1
  * roleExt2
  * roleExt3
  * roleExt4
  * roleExt5
  * roleNameKey
  * roleUsers
  * roleNoUsers
  * roleBOExt
  * positionBOExt
  * teamUsers
  * departmentIsManager

### userName

**_语法_**

@userName(_uidAliasName,delimiter_)

  * 用户姓名
  * 如果不指定uidAliasName，上下文依赖UserContext

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    你好@userName,他们也刚刚访问过@userName(cc<曹操> lb<刘备> sq<孙权>)
    

**_结果_**
    
    
    你好系统管理员,他们也刚刚访问过曹操 刘备 孙权
    

### uid

**_语法_**

@uid(_uidAliasName,delimiter_)

  * 用户登录账户名，全局不重复
  * 如果不指定uidAliasName，上下文依赖UserContext

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式。通常实施人员可以使用该参数将值中包含的别名处理掉
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是他们三个的登录账户@uid(cc<曹操> lb<刘备> sq<孙权>)
    

**_结果_**
    
    
    这是他们三个的登录账户cc lb sq
    

### userUniqueId

**_语法_**

@userUniqueId(_uidAliasName,delimiter_)

  * 用户注册Id，由系统自动分配的全局不重复Id
  * 如果不指定uidAliasName，上下文依赖UserContext

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是他们三个的注册Id@userUniqueId(cc<曹操> lb<刘备> sq<孙权>)
    

**_结果_**
    
    
    这是他们三个的注册Id610ce679-47af-4411-ab92-75424bca2acc 01f3eae8-2c4d-4585-93e8-12483c5b676c 31f5eae7-2c4d-4ade-93e8-12485h5b676c
    

### userNo

**_语法_**

@userNo(_uidAliasName,delimiter_)

  * 员工编号
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 员工编号不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是他们三个的员工编号@userNo(cc<曹操> lb<刘备> sq<孙权>)
    

**_结果_**
    
    
    这是他们三个的员工编号001 002 003
    

### userPositionName

**_语法_**

@userPositionName(_uidAliasName,delimiter_)

  * 职位名称
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 职位名称不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是他们三个的职位名称@userPositionName(cc<曹操> lb<刘备> sq<孙权>)
    

**_结果_**
    
    
    这是他们三个的职位名称兖州太守 徐州牧 都督
    

### userPositionNo

**_语法_**

@userPositionNo(_uidAliasName,delimiter_)

  * 职位编码
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 职位编码不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是他们三个的职位编码@userPositionNo(cc<曹操> lb<刘备> sq<孙权>)
    

**_结果_**
    
    
    这是他们三个的职位编码001 002 003
    

### userPositionLayer

**_语法_**

@userPositionLayer(_uidAliasName,delimiter_)

  * 职位等级
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 职位等级不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是他们三个的职位等级@userPositionLayer(cc<曹操> lb<刘备> sq<孙权>
    

**_结果_**
    
    
    这是他们三个的职位等级18 18 18
    

### userMobile

**_语法_**

@userMobile(_uidAliasName,delimiter_)

  * 用户手机号
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 手机号不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是他们三个的手机号@userMobile(cc<曹操> lb<刘备> sq<孙权>)
    

**_结果_**
    
    
    这是他们三个的联系电话138XXXXXXXX 189XXXXXXXX 158XXXXXXXX
    

### userTel

**_语法_**

@userTel(_uidAliasName,delimiter_)

  * 用户联系电话
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 联系电话不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是他们三个的联系电话@userTel(cc<曹操> lb<刘备> sq<孙权>)
    

**_结果_**
    
    
    这是他们三个的联系电话110 120 119
    

### userEmail

**_语法_**

@userEmail(_uidAliasName,delimiter_)

  * 用户外部邮件
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 外部邮件不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是他们三个的电子邮箱@userEmail(cc<曹操> lb<刘备> sq<孙权>)
    

**_结果_**
    
    
    这是他们三个的电子邮箱cc@sg.org lb@sg.org sq@sg.org
    

### userPhoto

**_语法_**

@userPhoto(_uidAliasName_)

  * 返回当前登录账户的头像URL地址

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当账户不存在时返回空串，兼容友好格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    这是刘备的头像URL地址@userPhoto(lb<刘备>)
    

**_结果_**
    
    
    这是刘备的头像URL地址
    ../df?groupValue=lb&fileValue=560ba8a2-b47c-4d90-a8e0-a672c8f443ac&sid=a3fa194b-4e9f-45b3
    -9ff1-3608b9ce5bdb&repositoryName=%21photo-&appId=_bpm.platform&attachment=true&fileName
    =lb.png
    

### userExt1

**_语法_**

@userExt1(_uidAliasName,delimiter_)

  * 用户扩展字段1配置的值
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 扩展字段1不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

### userExt2

**_语法_**

@userExt2(_uidAliasName,delimiter_)

  * 用户扩展字段2配置的值
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 扩展字段2不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

### userExt3

**_语法_**

@userExt3(_uidAliasName,delimiter_)

  * 用户扩展字段3配置的值
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 扩展字段3不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

### userExt4

**_语法_**

@userExt4(_uidAliasName,delimiter_)

  * 用户扩展字段4配置的值
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 扩展字段4不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

### userExt5

**_语法_**

@userExt5(_uidAliasName,delimiter_)

  * 用户扩展字段5配置的值
  * 如果不指定uidAliasName，上下文依赖UserContext
  * 扩展字段5不是AWS账户的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _uidAliasName_ （可选）解析一组指定账户，当某一账户非法或不存在时从列表中剔除，兼容友好地址别名格式
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

### userBOExt

**_语法_**

@userBOExt(_fieldName,userId_)

  * 获取实施顾问扩展的用户BO结构值

**_参数_**

  * _fieldName_ （必填）表示自定义的字段名
  * _userId_ （可选）获取指定这个账户的扩展属性

**_例子_**
    
    
    当前用户的工作年限是@userBOExt(EXT_YEAR)
    

**_结果_**
    
    
    当前用户的工作年限是10年
    

### userManager

**_语法_**

@userManager(uidAliasName,type,delimiter,includeSelf)

  * 返回当前账户的管理者

**_参数_**

  * uidAliasName（可选），如果指定此参数，返回指定账户的管理者
  * type(可选)，有2种可选值：all/one;指定all时，向上找所有的管理者（包括本部门及兼职），指定one向上找到管理者立即退出（包括本部门及兼职）
  * delimiter（可选），如果指定delimiter分隔符，返回的多个值用delimiter分割，不指定用空格分割
  * includeSelf（可选），表示当前账户是管理者时是否返回，参数有2种选项：1：包括自已（默认）；0：不包括自已

**_例子_**
    
    
    指定账户张三的管理者的账户为@userManager(zhangsan,all,,1)
    

**_结果_**
    
    
    指定账户张三的管理者的账户为zhangsan liubei sunquan
    

### user

**_语法_**

@user(key,uidAliasName,delimiter)

  * 根据用户指定的信息类型，返回用户相应的信息

**_参数_**

  * key（可选），key参数包括UID;cacheLoginFailTimes;cachePauseTime;closed;departmentId;email;ext1;ext2;ext3;ext4;ext5;manager;mobile;officeFax;officeTel;orderIndex;outerId;password;photoLastModified;positionLayer;positionName;positionNo;preSpell;reportTo;roleId;sessionTime;singleLogin;uniqueId;userIp;userName;userNameAlias;userNo;workStatus;workcanlendar，如果使用多个可用半角分号分隔，返回的信息使用半角分号分隔，如果未指定key信息，返回该账户的所有的信息并使用半角分号分隔
  * uidAliasName（可选），如果指定uidAliasName参数，返回指定账户的相应信息
  * delimiter（可选），如果指定delimiter分隔符，返回的多个值用delimiter分割，不指定用空格分割

**_例子_**
    
    
    指定账户张三的手机号为@user(mobile,zhangsan)
    

**_结果_**
    
    
    指定账户张三的手机号为13344556677
    

### companyName

**_语法_**

@companyName(_contextType,contextId_)

  * 单位名称
  * contextType不区分大小写
  * 如果读取的值未找到,返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）常量：org、process、taskOwner和taskTarget
        
        - 如果值为org或未提供时，从操作者所在组织结构中读取
                  - 如果值为process时，从流程实例的创建者信息中读取
                  - 如果值为taskOwner时，从任务实例的发起人信息中读取
                  - 如果值为taskTarget时，从任务实例的执行人信息中读取
        

  * _contextId_ （可选）对应contextType，如不提供该参数，默认取当前上下文
        
        - 如果contextType为org或未提供时，该值为指定的部门Id
                  - 如果contextType为process，该值为指定的流程实例Id
                  - 如果contextType为taskOwne，该值为指定的任务实例Id
                  - 如果contextType为taskTarget，该值为指定的任务实例Id
        

**_例子_**
    
    
    这是我注册的单位名称@companyName,也可以这样写@companyName(org)
    
    这是当前流程实例创建人所在的单位名称@companyName(process)
    
    指定获取Id为ABC的流程实例创建人所在单位名称@companyName(process,ABC)
    
    这是当前任务实例发起人所在的单位名称@companyName(taskOwner)
    
    这是当前任务实例执行人所在的单位名称@companyName(taskTarget)
    
    指定获取Id为ABC的任务实例执行人所在单位名称@companyName(taskTarget,ABC)
    

### companyId

**_语法_**

@companyId(_contextType,contextId_)

  * 单位Id
  * contextType不区分大小写
  * 如果读取的值未找到,返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### companyNo

**_语法_**

@companyNo(_contextType,contextId_)

  * 单位编号
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 单位编号不是AWS单位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### companyExt1

**_语法_**

@companyExt1(_contextType,contextId_)

  * 单位扩展字段1配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS单位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### companyExt2

**_语法_**

@companyExt2(_contextType,contextId_)

  * 单位扩展字段2配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS单位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### companyExt3

**_语法_**

@companyExt3(_contextType,contextId_)

  * 单位扩展字段3配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS单位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### companyExt4

**_语法_**

@companyExt4(_contextType,contextId_)

  * 单位扩展字段4配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS单位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### companyExt5

**_语法_**

@companyExt5(_contextType,contextId_)

  * 单位扩展字段5配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS单位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### companyBOExt

**_语法_**

@companyBOExt(_*fieldName,contextType,contextId_)

  * 获取实施顾问扩展的单位BO结构值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _fieldName_ （必填）自定义的字段名

  * _contextType_ （可选）常量：org、process、taskOwner和taskTarget
        
        - 如果值为org或未提供时，从操作者所在组织结构中读取
                  - 如果值为process时，从流程实例的创建者信息中读取
                  - 如果值为taskOwner时，从任务实例的发起人信息中读取
                  - 如果值为taskTarget时，从任务实例的执行人信息中读取
        

  * _contextId_ （可选）是个增强参数。对应contextType，如不提供该参数，默认取当前上下文
        
        - 如果contextType为org或未提供时，该值为指定的部门Id
                  - 如果contextType为process，该值为指定的流程实例Id
                  - 如果contextType为taskOwne，该值为指定的任务实例Id
                  - 如果contextType为taskTarget，该值为指定的任务实例Id
        

**_例子_**
    
    
    李四所在单位传真号码是：@companyBOExt(COM_FAX,org,8911e732-b42a-4556-853f-ad32761bcbee)
    

**_结果_**
    
    
    李四所在单位传真号码是010-6545021
    

### companyType

**_语法_**

@companyType(_contextType,contextId_)

  * 单位类型配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS单位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentName

**_语法_**

@departmentName(_contextType,contextId_)

  * 部门名称
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentPathName

**_语法_**

@departmentPathName(_contextType,contextId_)

  * 部门名称路径。格式：部门a/部门b...
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentId

**_语法_**

@departmentId(_contextType,contextId_)

  * 部门Id
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentPathId

**_语法_**

@departmentPathId(_contextType,contextId_)

  * 部门Id路径。格式：部门a/部门b...
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentNo

**_语法_**

@departmentNo(_contextType,contextId_)

  * 部门编号
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 部门编号不是AWS部门的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentZone

**_语法_**

@departmentZone(_contextType,contextId_)

  * 部门区域名称（本部门无区域划分时继承上级部门）
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 部门区域不是AWS部门的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentManager

**_语法_**

@departmentManager(_isIgnoreMe，contextType,contextId_)

  * 部门有管理者身份的账户，多个用空格隔开
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 支持兼职，当本部门找不到时，会逐级向上寻找，直到找到为止

**_参数_**

  * _isIgnoreMe_ （可选）是否忽略自己，默认为false

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### isDepartmentManager

**_语法_**

@isDepartmentManager(_contextType,contextId_)

  * 是否为部门管理者
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentExt1

**_语法_**

@departmentExt1(_contextType,contextId_)

  * 部门扩展字段1配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS部门的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentExt2

**_语法_**

@departmentExt2(_contextType,contextId_)

  * 部门扩展字段2配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS部门的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentExt3

**_语法_**

@departmentExt3(_contextType,contextId_)

  * 部门扩展字段3配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS部门的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentExt4

**_语法_**

@departmentExt4(_contextType,contextId_)

  * 部门扩展字段4配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS部门的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentExt5

**_语法_**

@departmentExt5(_contextType,contextId_)

  * 部门扩展字段5配置的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS部门的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentType

**_语法_**

@departmentType(_contextType,contextId_)

  * 获取部门类型
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段不是AWS部门的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### departmentBOExt

**_语法_**

@departmentBOExt(_*fieldName,contextType,contextId_)

  * 获取实施顾问扩展的部门BO结构值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _fieldName_ （必填）自定义的字段名

  * _contextType_ （可选）常量：org、process、taskOwner和taskTarget
        
        - 如果值为org或未提供时，从操作者所在组织结构中读取
                  - 如果值为process时，从流程实例的创建者信息中读取
                  - 如果值为taskOwner时，从任务实例的发起人信息中读取
                  - 如果值为taskTarget时，从任务实例的执行人信息中读取
        

  * _contextId_ （可选）是个增强参数。对应contextType，如不提供该参数，默认取当前上下文
        
        - 如果contextType为org或未提供时，该值为指定的部门Id
                  - 如果contextType为process，该值为指定的流程实例Id
                  - 如果contextType为taskOwne，该值为指定的任务实例Id
                  - 如果contextType为taskTarget，该值为指定的任务实例Id
        

**_例子_**
    
    
    研发部门的电话号码是：@departmentBOExt(DEP_TEL,org,5d5d90a3-e21c-4b36-8fd3-e3f3cd743c5f)
    

**_结果_**
    
    
    研发部门的电话号码是010-6335148
    

### roleId

**_语法_**

@roleId(contextType,contextId)

  * 角色/岗位Id
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）参见companyName参数参数说明
  * _contextId_ （可选）参见companyName参数参数说明

**_例子_**

参见@companyName示例

### roleName

**_语法_**

@roleName(_contextType,contextId_)

  * 角色/岗位名称
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 不同角色/岗位分类下的角色/岗位名称允许被重复定义，做规则匹配时注意

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### roleExt1

**_语法_**

@roleExt1(_contextType,contextId_)

  * 获取角色/岗位扩展字段1的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段1不是角色/岗位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### roleExt2

**_语法_**

@roleExt2(_contextType,contextId_)

  * 获取角色/岗位扩展字段2的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段2不是角色/岗位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### roleExt3

**_语法_**

@roleExt3(_contextType,contextId_)

  * 获取角色/岗位扩展字段3的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段3不是角色/岗位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### roleExt4

**_语法_**

@roleExt4(_contextType,contextId_)

  * 获取角色/岗位扩展字段4的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段4不是角色/岗位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### roleExt5

**_语法_**

@roleExt5(_contextType,contextId_)

  * 获取角色/岗位扩展字段5的值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志
  * 扩展字段5不是角色/岗位的必填项，若启用需要实施顾问设置该值

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### roleNameKey

**_语法_**

@roleNameKey(_contextType,contextId_)

  * 不重复的名称组合。格式为：角色/岗位分类名.角色/岗位名称
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）参见companyName参数说明

  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    参见@companyName示例
    

### roleUsers

**_语法_**

@roleUsers(_*roleId,delimiter_)

  * 获取指定角色/岗位的用户账户

**_参数_**

  * _roleId_ 角色/岗位的Id
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    普通用户角色/岗位对应的账户是@roleUsers(28ee65b1-7219-4aef-9a14-021cc98a07d6)
    

**_结果_**
    
    
    普通用户角色/岗位对应的账户是lixue gaoli
    

### roleNoUsers

**_语法_**

@roleNoUsers(_*No,delimiter_)

  * 获取指定角色/岗位代码的用户账户，包含兼职

**_参数_**

  * _No_ 角色/岗位代码
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    角色/岗位代码为001的账户是@roleUsers(001)
    

**_结果_**
    
    
    角色/岗位代码为001的账户是lixue gaoli
    

### roleBOExt

**_语法_**

@roleBOExt(_*fieldName,contextType,contextId_)

  * 获取实施顾问扩展的部门BO结构值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _fieldName_ （必填）自定义的字段名

  * _contextType_ （可选）常量：org、process、taskOwner和taskTarget

    * 如果值为org或未提供时，从操作者所在组织结构中读取
    * 如果值为process时，从流程实例的创建者信息中读取
    * 如果值为taskOwner时，从任务实例的发起人信息中读取
    * 如果值为taskTarget时，从任务实例的执行人信息中读取
  * _contextId_ （可选）是个增强参数。对应contextType，如不提供该参数，默认取当前上下文

    * 如果contextType为org或未提供时，该值为指定的部门Id
    * 如果contextType为process，该值为指定的流程实例Id
    * 如果contextType为taskOwne，该值为指定的任务实例Id
    * 如果contextType为taskTarget，该值为指定的任务实例Id

**_例子_**
    
    
    项目管理角色描述是：@roleBOExt(ROLE_INTRODUCT,org,28ee65b1-7219-4aef-9a14-021cc98a07d6)
    

**_结果_**
    
    
    项目管理角色描述是：负责项目的部署、实施及运维
    

### positionBOExt

**_语法_**

@positionBOExt(_*fieldName,contextType,contextId_)

  * 获取实施顾问扩展的岗位BO结构值
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _fieldName_ （必填）自定义的字段名
  * _contextType-_ （可选）常量：org、process、taskOwner和taskTarget

    * 如果值为org或未提供时，从操作者所在组织结构中读取
    * 如果值为process时，从流程实例的创建者信息中读取
    * 如果值为taskOwner时，从任务实例的发起人信息中读取
    * 如果值为taskTarget时，从任务实例的执行人信息中读取
  * contextId （可选）是个增强参数。对应contextType，如不提供该参数，默认取当前上下文

    * 如果contextType为org或未提供时，该值为指定的部门Id
    * 如果contextType为process，该值为指定的流程实例Id
    * 如果contextType为taskOwne，该值为指定的任务实例Id
    * 如果contextType为taskTarget，该值为指定的任务实例Id

**_例子_**
    
    
    项目管理岗位描述是：@positionBOExt(POSITION_INTRODUCT,org,28ee65b1-7219-4aef-9a14-021cc98a07d6)
    

**_结果_**
    
    
    项目管理岗位描述是：负责项目的部署、实施及运维
    

### teamUsers

**_语法_**

@teamUsers(_*teamId,delimiter_)

  * 获取指定小组的用户账户

**_参数_**

  * _teamId_ 团队的Id
  * _delimiter_ （可选）返回的多个值用delimiter分割，默认使用空格分隔

**_例子_**
    
    
    测试团队对应的账户是@teamUsers(153dcca3-7210-43b9-8a82-c7a57aa2b00e)
    

**_结果_**
    
    
    测试团队对应的账户是gaoli handong
    

### departmentIsManager

**_语法_**

@departmentIsManager(contextType,contextId)

  * 是否为部门管理者
  * contextType不区分大小写
  * 如果读取的值未找到返回空串，并留下异常日志

**_参数_**

  * _contextType_ （可选）参见companyName参数说明
  * _contextId_ （可选）参见companyName参数说明

**_例子_**
    
    
    @departmentIsManager()
    

**_结果_**
    
    
    true