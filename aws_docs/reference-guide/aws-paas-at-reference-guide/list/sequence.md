# 序列值 | AWS @公式参考指南

# 序列值

  * uuid
  * sequence
  * sequenceYear
  * sequenceMonth
  * sequenceDay

## uuid

**_语法_**

@uuid

  * 一个36位长度的不重复字符串

**_参数_**

无

**_例子_**
    
    
    这个Id值是@uuid
    

**_结果_**
    
    
    这个Id值是c6fb644c-b731-40ff-95eb-b3b446d0b9f8
    

## sequence

**_语法_**

@sequence(_varName,padLen,padStr_)

  * 下个序列值

**_参数_**

  * _varName_ （可选）任意指定一个全局不重复的序列变量名，如CRM_CUSTOMER。如果未给定，默认当前上下文的流程组Id

  * _padLen_ （可选）如果需要定长格式化输出，padLen用于指定定长长度

  * _padStr_ （可选）配合padLen定长参数，用来补充缺位字符串。如值是18，padLen设置为6，padStr设置为*，那么格式化后的值是****18。如未给出默认为0

**_例子_**
    
    
    CRM_CUSTOMER的序列值是@sequence(CRM_CUSTOMER)，定长8位后的值是：
    @sequence(CRM_CUSTOMER,8)，定长8位不足补*的值是@sequence(CRM_CUSTOMER,8,*)
    

**_结果_**
    
    
    CRM_CUSTOMER的序列值是18，定长8位后的值是00000018，定长8位不足补*的值是******18
    

## sequenceYear

**_语法_**

@sequenceYear(_varName,padLen,padStr_)

  * 下个年度的序列值，序列值隔年归零
  * 如果序列值已超出定长值，直接返回该值
  * 前4位用来表示YYYY

**_参数_**

  * _varName_ （可选）参见@sequence参数说明

  * _padLen_ （可选）参见@sequence参数说明

  * _padStr_ （可选）参见@sequence参数说明

**_例子_**
    
    
    CRM_CUSTOMER的年度序列值是@sequenceYear(CRM_CUSTOMER)，定长8位后的值是
    @sequenceYear(CRM_CUSTOMER,8)
    

**_结果_**
    
    
    CRM_CUSTOMER的年度序列值是201418，定长8位后的值是201400000018
    

## sequenceMonth

**_语法_**

@sequenceMonth(_varName,padLen,padStr_)

  * 下个月份的序列值，序列值隔月归零
  * 如果序列值已超出定长值，直接返回该值
  * 前6位用来表示YYYYMM

**_参数_**

  * _varName_ （可选）参见@sequence参数说明

  * _padLen_ （可选）参见@sequence参数说明

  * _padStr_ （可选）参见@sequence参数说明

  * _padStart_ （可选）参见@sequence参数说明

**_例子_**
    
    
    CRM_ORDER的月份序列值是@sequenceMonth(CRM_ORDER)，定长8位后的值是@sequenceMonth(CRM_ORDER,8)
    

**_结果_**
    
    
    CRM_ORDER的月份序列值是20140718，定长8位后的值是20140700000018
    

## sequenceDay

**_语法_**

@sequenceDay(varName,padLen,padStr,padStart)

  * 下一日的序列值，序列值隔天归零
  * 如果序列值已超出定长值，直接返回该值
  * 前6位用来表示YYYYMM

**_参数_**

  * _varName_ （可选）参见@sequence参数说明
  * _padLen_ （可选）参见@sequence参数说明
  * _padStr_ （可选）参见@sequence参数说明
  * _padStart_ （可选）参见@sequence参数说明

**_例子_**
    
    
    CRM_ORDER的日序列值是@sequenceDay(CRM_ORDER)，定长8位后的值是@sequenceDay(CRM_ORDER,8)
    

**_结果_**
    
    
    CRM_ORDER的日份序列值是20140718，定长8位后的值是2014071800000018