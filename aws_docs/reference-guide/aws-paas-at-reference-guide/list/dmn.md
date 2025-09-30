# 决策 | AWS @公式参考指南

# 决策

  * dmn
  * parseDmn

## dmn

**_语法_**

@dmn(_dmnDefId,_ decisionKey,_isFilterVal,_ paramKey1,_paramVal1,_ paramKey2,*paramVal2)

  * 通过传入的参数执行决策模型，返回相应结果

**_参数_**

  * _dmnDefId_ （必须）决策模型ID
  * _decisionKey_ （必须）决策表ID
  * _isFilterVal_ （必须）是否过滤返回值，true返回用空格分隔符的字符串val1 val2 val3，false返回Map类型字符串[{'key1','val1'},{'key2','val2'}] paramKey1（必须）输入参数1 paramVal1（必须）输入参数1的值 paramKey2（必须）输入参数2 paramVal2（必须）输入参数2的值 ...如果有其他继续追加

**_例子_**
    
    
    @dmn(obj_38817fa98d4e4372b7c7996cb4835435,obj_253cb4352371524e9128142252d8c738,true,a,2)
    

**_结果_**
    
    
    执行决策模型id为obj_38817fa98d4e4372b7c7996cb4835435中决策id为obj_253cb4352371524e9128142252d8c738的决策，输入变量名称a值为2。执行结果为空格分隔符的字符串
    

## dparseDmnmn

**_语法_**

@parseDmn(_dmnAtStr,_ outputVariableName1,*outputVariableName2)

  * 通过传入的参数，解析@dmn公式结果，返回固定输出列值

**_参数_**

  * _dmnAtStr_ （必须）@dmn公式字符串
  * _outputVariableName1_ （必须）决策输出列变量名称1
  * _outputVariableName2_ （必须）决策输出列变量名称2 ...如果有其他继续追加

**_注意_**

  * 参数dmnAtStr必须为@dmn公式字符串

**_例子_**
    
    
    @parseDmn(@dmn(obj_38817fa98d4e4372b7c7996cb4835435,obj_253cb4352371524e9128142252d8c738,true,a,2),output1,output2)
    

**_结果_**
    
    
    返回@dmn(obj_38817fa98d4e4372b7c7996cb4835435,obj_253cb4352371524e9128142252d8c738,true,a,2)执行结果中的output1列和output2列值。@dmn公式执行结果其他输出列会被过滤