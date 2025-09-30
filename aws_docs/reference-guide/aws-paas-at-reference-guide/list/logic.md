# 逻辑 | AWS @公式参考指南

# 逻辑

  * equals
  * lessThan
  * max
  * min
  * and
  * or
  * if
  * ifthen
  * in
  * nullValue
  * execJavaBean
  * execJXPath
  * xor
  * not
  * isEmpty

## equals

**_语法_**

@equals(*str1,*str2)

  * 字符串比较。比较两个字符串是否相等，相等返回TRUE，否则返回FALSE
  * 匹配时，区分大小写

**_参数_**

  * _str1_ （必选）字符串
  * _str2_ （必选）字符串

**_例子_**
    
    
    A等于a吗=@equals(A,a)
    

**_结果_**
    
    
    A等于a吗=FALSE
    

## lessThan

**_语法_**

@lessThan(*num1,*num2)

  * 数值比较。比较两个数值，如果num1小于num2返回TRUE，否则返回FALSE

**_参数_**

  * _num1_ （必选）数值字符串
  * _num2_ （必选）数值字符串

**_例子_**
    
    
    100小于99吗=@lessThan(100,99)
    

**_结果_**
    
    
    100小于99吗=FALSE
    

## max

**_语法_**

@max(*num1,*num2,num3,num4,num5)

  * 最大值。从一组数字中取最大值

**_参数_**

  * _num1_ （必选）数值字符串
  * _num2_ （必选）数值字符串
  * _num3_ （可选）数值字符串
  * _num4_ （可选）数值字符串
  * _num5_ （可选）数值字符串

**_例子_**
    
    
    1,2,3,4,5的最大值是@max(1,2,3,4,5)
    

**_结果_**
    
    
    1,2,3,4,5的最大值是5
    

## min

**_语法_**

@min(*num1,*num2,num3,num4,num5)

  * 最小值。从一组数字中取最小值

**_参数_**

  * _num1_ （必选）数值字符串
  * _num2_ （必选）数值字符串
  * _num3_ （可选）数值字符串
  * _num4_ （可选）数值字符串
  * _num5_ （可选）数值字符串

**_例子_**
    
    
    1,2,-3,4,5的最小值是@min(1,2,-3,4,5)
    

**_结果_**
    
    
    1,2,-3,4,5的最小值是-3
    

## and

**_语法_**

@and(*logical,*logical2,logical3,logical4,logical5)

  * 并判断。给定参数值为真时，返回 TRUE，只要一个参数的逻辑值为假，即返回 FALSE
  * 表示真值的串支持自然语言：TRUE、ON、1、YES、是
  * 表示假值的串支持自然语言：FALSE、OFF、0、NO、否

**_参数_**

  * _logical_ （必选）真假值
  * _logical2_ （必选）真假值
  * _logical3_ （可选）真假值
  * _logical4_ （可选）真假值
  * _logical5_ （可选）真假值

**_例子_**
    
    
    你是满18岁并且在校的学生吗？@and(@equals(18,18),@equals(在校,在校))
    

**_结果_**
    
    
    你是满18岁并且在校的学生吗？TRUE
    

## or

**_语法_**

@or(*logical,*logical2,logical3,logical4,logical5)

  * 或判断。给定参数只要有一个为真时，返回 TRUE，否则返回FALSE
  * 表示真值的串支持自然语言：TRUE、ON、1、YES、是
  * 表示假值的串支持自然语言：FALSE、OFF、0、NO、否

**_参数_**

  * _logical_ （必选）真假值
  * _logical2_ （必选）真假值
  * _logical3_ （可选）真假值
  * _logical4_ （可选）真假值
  * _logical5_ （可选）真假值

**_例子_**
    
    
    你是满18岁或在校的学生吗？@or(@equals(18,16),@equals(在校,在校))
    

**_结果_**
    
    
    你是满18岁或在校的学生吗？TRUE
    

## if

**_语法_**

@if(_*logical,valueTrue,valueFalse_)

  * 逻辑取值。判断logical，取对应的真值或假值
  * 表示真值的串支持自然语言：TRUE、ON、1、YES、是
  * 表示假值的串支持自然语言：FALSE、OFF、0、NO、否

**_参数_**

  * _logical_ （必选）真假值
  * _valueTrue_ （必选）如果逻辑为真，返回的字符串
  * _valueFalse_ （必选）如果逻辑为假，返回的字符串

**_例子_**
    
    
    如果你是在校学生出示身份证否则出示毕业证？@if(true,身份证,毕业证)
    

**_结果_**
    
    
    如果你是在校学生出示身份证否则出示毕业证？身份证
    

## ifthen

**_语法_**

@ifthen(*value,*if1,*then1,if2,then2......else)

  * 条件取值。如果value等于if1时
  * ifThen公式的结果返回then1 ...
  * 如果不等于任何一个if值，则返回else

**_参数_**

  * value （必选）值
  * if1 （必选）与参数value进行判断
  * then1 （必选）如果逻辑为真，返回的字符串

**_例子_**
    
    
    你的会员等级是@ifThen(3,1,普通会员,2,VIP会员,3,粉丝会员,匿名)
    

**_结果_**
    
    
    你的会员等级是粉丝会员
    

## in

**_语法_**

@in(*str1,*str2,str3,str4,str5)

  * 包含判断。判断str1是否与str2或str3..相等，命中一个返回TRUE
  * 判断区分大小写

**_参数_**

  * _str1_ （必选）字符串
  * _str2_ （必选）字符串
  * _str3_ （可选）字符串
  * _str4_ （可选）字符串
  * _str5_ （可选）字符串

**_例子_**
    
    
    Tom这个词包含吗？@in(Tom,smith,jack,tom)
    

**_结果_**
    
    
    Tom这个词包含吗？FALSE
    

## nullValue

**_语法_**

@nullValue(*str1,*str2)

  * 空值转换。如果str1为null或空串，返回str2，否则返回str1
  * 判断区分大小写

**_参数_**

  * _str1_ （必选）字符串
  * _str2_ （必选）字符串

**_例子_**
    
    
    @nullValue(,转换空值)
    

**_结果_**
    
    
    转换空值
    

## execJavaBean

**_语法_**

@execJavaBean(*appId,*className,param)

  * 执行Java类。执行Java类exec方法，该方法要求返回String值，方法体定义参考：public String exec(String param,ExpressionContext atContext){}
  * 要调用的class必须存在于指定的app中
  * 该类必须存在一个名为exec的约定方法

**_参数_**

  * _appId_ （必选）应用Id
  * _className_ （必选）类名称
  * _param_ （可选）由公式提供给exec方法的扩展参数

**_例子_**
    
    
    @execJavaBean(com.actionsoft.apps.poc.api,com.actionsoft.apps.poc.api.local.app.at.AtAPITest,
    处理Id=99的业务)
    

**_结果_**
    
    
    处理Id=99的业务-ok
    

## execJXPath

**_语法_**

@execJXPath(_*jxpath_)

  * 解析基于对象的xpath值
  * 目前该公式特定应用于BPMN ServiceTask参数处理场景

**_参数_**

  * _jxpath_ （必选）XPATH表达式

**_例子_**
    
    
    @execJXPath(company/name)
    

**_结果_**
    
    
    东山矿石加工厂
    

## xor

**_语法_**

@xor(*logical1,*logical2...)

  * 对所有参数逻辑值求异或值

**_参数_**

  * _logical1_ （必选）真假值
  * _logical2_ （必选）真假值
  * _..._ （可选）更多组参数

**_例子_**
    
    
    @xor(true,true)
    

**_结果_**
    
    
    false
    

## not

**_语法_**

@not(*logical)

  * 对参数逻辑值求反

**_参数_**

  * _logical_ （必选）真假值

**_例子_**
    
    
    @not(true)
    

**_结果_**
    
    
    false
    

## isEmpty

**_语法_**

@isEmpty(*value)

  * 去除前/后缀空格，判断值是否为空

**_参数_**

  * _value_ （必选）文本值

**_例子_**
    
    
    @isEmpty(ABC)
    

**_结果_**
    
    
    false