# 表单 | AWS @公式参考指南

# 表单

  * form
  * parentForm
  * gridFirst
  * gridLast
  * gridCount
  * gridSum
  * gridAvg
  * gridMax
  * gridMin
  * gridSet

## form

**_语法_**

@form(*boName,*fieldName,processInstId)

  * 表单主表数据

**_参数_**

  * _boName_ （必选）BO表名称

  * _fieldName_ （必选）字段名称

  * _processInstId_ （可选）指定流程实例的表单数据

**_例子_**
    
    
    当前流程表单字段F1的值是@form(BO_ABC,F1)
    
    流程实例是999的表单字段F1的值是@form(BO_ABC,F1,999)
    

## parentForm

**_语法_**

@parentForm(*boName,*parentBoName,*parentFieldName)

  * 字段子表中父级子表指定字段的值，仅支持字段子表网格数据字典查询语句使用（只适用于普通子表的新增场景）

**_参数_**

  * _boName_ （必选）BO表名称

  * _parentBoName_ （必选）父级子表BO表名称

  * _parentFieldName_ （必选）父级子表BO表字段名称

**_例子_**
    
    
    当前流程字段子表SHI的值是【… WHERE SHENG='@parentForm(BO_ACT_SHI,BO_ACT_SHENG,SHENG)'】
    

## gridFirst

**_语法_**

@gridFirst(*boName,*fieldName,sqlClause,processInstId)

  * 表单子表首记录字段值

**_参数_**

  * _boName_ （必选）BO表名称

  * _fieldName_ （必选）字段名称

  * _sqlClause_ （可选）过滤业务字段条件的补充sql。如VIP=1 AND L=3

  * _processInstId_ （可选）指定流程实例的表单数据

**_例子_**
    
    
    当前流程表单子表BO_ABC字段F1的首值是@gridFirst(BO_ABC,F1)
    

## gridLast

**_语法_**

@gridLast(*boName,*fieldName,sqlClause,processInstId)

  * 表单子表末记录字段值

**_参数_**

  * _boName_ （必选）BO表名称

  * _fieldName_ （必选）字段名称

  * _sqlClause_ （可选）过滤业务字段条件的补充sql。如VIP=1 AND L=3

  * _processInstId_ （可选）指定流程实例的表单数据

**_例子_**
    
    
    当前流程表单子表BO_ABC字段F1的最后一条记录值是@gridLast(BO_ABC,F1)
    

## gridCount

**_语法_**

@gridCount(_*boName,sqlClause,processInstId_)

  * 表单子表记录数

**_参数_**

  * _boName_ （必选）BO表名称

  * _sqlClause_ （可选）过滤业务字段条件的补充sql。如VIP=1 AND L=3

  * _processInstId_ （可选）指定流程实例的表单数据

**_例子_**
    
    
    当前流程表单子表BO_ABC的记录数是@gridCount(BO_ABC)
    

## gridSum

**_语法_**

@gridSum(*boName,*fieldName,sqlClause,processInstId)

  * 表单子表字段求和

**_参数_**

  * _boName_ （必选）BO表名称

  * _fieldName_ （必选）字段名称

  * _sqlClause_ （可选）过滤业务字段条件的补充sql。如VIP=1 AND L=3

  * _processInstId_ （可选）指定流程实例的表单数据

**_例子_**
    
    
    当前流程表单子表BO_ABC字段F1的合计值是@gridSum(BO_ABC,F1)
    
    人民币大写是@rmb(@gridSum(BO_ABC,F1))
    

## gridAvg

**_语法_**

@gridAvg(*boName,*fieldName,sqlClause,processInstId)

  * 表单子表字段求平均

**_参数_**

  * _boName_ （必选）BO表名称

  * _fieldName_ （必选）字段名称

  * _sqlClause_ （可选）过滤业务字段条件的补充sql。如VIP=1 AND L=3

  * _processInstId_ （可选）指定流程实例的表单数据

**_例子_**
    
    
    当前流程表单子表BO_ABC字段F1的平均值是@gridAvg(BO_ABC,F1)
    

## gridMax

**_语法_**

@gridMax(*boName,*fieldName,sqlClause,processInstId)

  * 表单子表字段最大值

**_参数_**

  * _boName_ （必选）BO表名称

  * _fieldName_ （必选）字段名称

  * _sqlClause_ （可选）过滤业务字段条件的补充sql。如VIP=1 AND L=3

  * _processInstId_ （可选）指定流程实例的表单数据

**_例子_**
    
    
    当前流程表单子表BO_ABC字段F1的最大值是@gridMax(BO_ABC,F1)
    

## gridMin

**_语法_**

@gridMin(*boName,*fieldName,sqlClause,processInstId)

  * 表单子表字段最小值

**_参数_**

  * _boName_ （必选）BO表名称

  * _fieldName_ （必选）字段名称

  * _sqlClause_ （可选）过滤业务字段条件的补充sql。如VIP=1 AND L=3

  * _processInstId_ （可选）指定流程实例的表单数据

**_例子_**
    
    
    当前流程表单子表BO_ABC字段F1的最小值是@gridMin(BO_ABC,F1)
    

## gridSet

**_语法_**

@gridSet(_boName,_ fieldName,sqlClause,processInstId)

  * 聚合表单子表字段值

**_参数_**

  * _boName_ （必选）BO表名称
  * *fieldName （必选）子表BO字段名。支持|或>分隔符多个字段，聚合值亦按该分割合并值
  * _sqlClause_ （可选）过滤业务字段条件的补充sql。如VIP=1 AND L=3
  * _processInstId_ （可选）指定流程实例的表单数据(不填取当前实例)

**_例子_**
    
    
    @gridSet(BO_XXX,F1>F2>F3)
    

**_结果_**
    
    
    张三>社保>1800,张三>五险>1200