# 数据库 | AWS @公式参考指南

# 数据库

  * sqlValue
  * sqlSet
  * sqlClauseOfManager

## sqlValue

**_语法_**

@sqlValue(_*sql,cc_)

  * sql第1条记录中第一个字段值
  * 如果sql错误或数据库连接错误，记入异常日志并返回一个空串

**_参数_**

  * _sql_ （必选）一个数据库查询语句且必须以SELECT为前缀

  * _cc_ （可选）从指定的CC数据源执行

**_例子_**
    
    
    BO_ABC表ORDERID为9的F1值是@sqlValue(SELECT F1 FROM BO_ABC WHERE ORDERID=9)
    

## sqlSet

**_语法_**

@sqlSet(_*sql,separator,cc_)

  * sql全部记录中第一个字段值
  * 如果sql错误或数据库连接错误，记入异常日志并返回一个空串

**_参数_**

  * _sql_ （必选）一个数据库查询语句且必须以SELECT为前缀

  * _separator_ （可选）多个值用指定的符号隔开，默认半角逗号

  * _cc_ （可选）从指定的CC数据源执行

**_例子_**
    
    
    BO_ABC表的F1值是@sqlSet(SELECT F1 FROM BO_ABC WHERE ORDERID=9)
    

**_结果_**
    
    
    BO_ABC表的F1值是香蕉,桔子,苹果
    

## sqlClauseOfManager

**_语法_**

@sqlClauseOfManager(_*fieldName,isSubDepartment_)

  * 所管部门的sql片断
  * 如果该操作者没有管辖范围，返回空串
  * 管辖范围与该账户在组织结构是否为部门管理者相关（含兼任）

**_参数_**

  * _fieldName_ （必选）指定业务表存储部门Id的字段名，根据这个字段拼凑出业务场景需要的过滤条件，多值OR判断

  * _isSubDepartment_ （可选）是否包含子部门，默认不包含

**_例子_**
    
    
    操作者王经理能够查询的销售订单业务记录与他管辖的部门范围相关，这个SQL片段是
    @sqlClauseOfManager(DEPTID,true)
    

**_结果_**
    
    
    BO_ABC操作者王经理能够查询的销售订单业务记录与他管辖的部门范围相关，这个SQL片段是
    (DEPTID='1111' OR DEPTID='222')