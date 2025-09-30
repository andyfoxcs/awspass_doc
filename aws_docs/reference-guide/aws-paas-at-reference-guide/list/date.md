# 日期 | AWS @公式参考指南

# 日期

  * date
  * datetime
  * time
  * hour
  * minute
  * second
  * dateAdd
  * date2Chinese
  * dayOfMonth
  * dayOfYear
  * nextDate
  * preDate
  * year
  * month
  * monthBegin
  * monthEnd
  * weekDay
  * weekOfYear
  * quarter
  * quarterBegin
  * quarterEnd
  * timestemp
  * GMTDate
  * UTCDate
  * isoDateFormat
  * timestamp2date
  * date2Timestamp
  * isLeapYear
  * dateDiff
  * hours
  * days

## date

**_语法_**

@date

  * 当前日期，格式为`yyyy-MM-dd`
  * 取自当前AWS服务器节点的时钟时间

**_参数_**

  * 无

**_例子_**
    
    
    @date
    

**_结果_**
    
    
    2014-07-18
    

## datetime

**_语法_**

@datetime

  * 当前日期时间，格式为`yyyy-MM-dd HH:mm:ss`
  * 取自当前AWS服务器节点的时钟时间

**_参数_**

  * 无

**_例子_**
    
    
    @datetime
    

**_结果_**
    
    
    2014-07-18 18:08:08
    

## time

**_语法_**

@time(_datetime_)

  * 当前时间，格式为`HH:mm:ss`
  * 取自当前AWS服务器节点的时钟时间

**_参数_**

  * _datetime_ （可选）从指定日期提取时间，格式为`yyyy-MM-dd HH:mm:ss`

**_例子_**
    
    
    @time 至 @time(2014-09-18 19:38:56)
    

**_结果_**
    
    
    18:08:08 至 19:38:56
    

## hour

**_语法_**

@hour(_datetime_)

  * 当前小时，范围是`0到23`
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _datetime_ （可选）从指定日期提取小时，格式为`yyyy-MM-dd HH:mm:ss`

**_例子_**
    
    
    @hour 至 @hour(2014-09-18 19:38:56)
    

**_结果_**
    
    
    18 至 19
    

## minute

**_语法_**

@minute(_datetime_)

  * 当前分钟，范围是`0到59`
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _datetime_ （可选）从指定日期提取分钟，格式为`yyyy-MM-dd HH:mm:ss`

**_例子_**
    
    
    @minute 至 @minute(2014-09-18 19:38:56)
    

**_结果_**
    
    
    15 至 38
    

## second

**_语法_**

@second(_datetime_)

  * 当前秒钟，范围是`0到59`
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _datetime_ （可选）从指定日期提取秒钟，格式为`yyyy-MM-dd HH:mm:ss`

**_例子_**
    
    
    @second 至 @second(2014-09-18 19:38:56)
    

**_结果_**
    
    
    22 至 56
    

## dateAdd

**_语法_**

@dateAdd(*datepart, *number, *date)

  * 日期计算
  * number参数支持负号（表示时间往前算起）

**_参数_**

  * _datepart_ （必选）可以是year、month、week、day
  * _number_ （必选）间隔，一个有符号整数
  * _date_ （必选）从该日期开始算起，格式为yyyy-MM-dd HH:mm:ss或yyyy-MM-dd

**_例子_**
    
    
    2014-07-14在100天前的日期是@dateAdd(day,-100,2014-07-14)
    

**_结果_**
    
    
    2014-07-14在100天前的日期是2014-04-05
    

## date2Chinese

**_语法_**

@date2Chinese(_*date_)

  * 将指定日期转换成中国大写名称

**_参数_**

  * _date_ （必选）指定该日期，格式为`yyyy-MM-dd`

**_例子_**
    
    
    2014-08-18的大写是@date2Chinese(2014-08-18)
    

**_结果_**
    
    
    2014-07-14的大写是二零一四年八月十八日
    

## dayOfMonth

**_语法_**

@dayOfMonth(date)

  * 当前月份中天数，在1到31范围内
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取天数，格式为yyyy-MM-dd HH:mm:ss或yyyy-MM-dd

**_例子_**
    
    
    2014-07-14是7月的第@dayOfMonth(2014-07-14)天
    

**_结果_**
    
    
    2014-07-14是7月的第14天
    

## dayOfYear

**_语法_**

@dayOfYear(date)

  * 当前年份中天数，在1到366范围内
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取天数，格式为yyyy-MM-dd HH:mm:ss或yyyy-MM-dd

**_例子_**
    
    
    2014-07-14是2014年的第@dayOfYear(2014-07-14)天
    

**_结果_**
    
    
    2014-07-14是2014年的第195天
    

## nextDate

**_语法_**

@nextDate(_date_)

  * 明日。当前日期的下一天日期
  * 取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期计算下一天，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    @date 至 @nextDate 。2015-12-31日的下一日是@nextDate(2015-12-31)
    

**_结果_**
    
    
    2014-07-18 至 2014-07-19 。 2015-12-31日的下一日是2016-01-01
    

## preDate

**_语法_**

@preDate(_date_)

  * 昨日。当前日期的前一天日期
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期计算前一天，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    2015-12-31日的前一日是@preDate(2015-12-31)
    

**_结果_**
    
    
    2015-12-31日的前一日是2015-12-30
    

## year

**_语法_**

@year(_date_)

  * 当前年份
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取年份，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    今年是@year年
    

**_结果_**
    
    
    今年是2015年
    

## month

**_语法_**

@month(_date_)

  * 当前月份
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取月份，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    今年是@year年@month月
    

**_结果_**
    
    
    今年是2015年10月
    

## monthBegin

**_语法_**

@monthBegin(_date_)

  * 当前月份第一天日期
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取月份第一天的日期，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    2015-10-12日的月份第1日是@monthBegin(2015-10-12)
    

**_结果_**
    
    
    2015-10-12日的月份第1日是2015-10-01
    

## monthEnd

**_语法_**

@monthEnd(_date_)

  * 当前月份最后一天日期
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取月份最后一天的日期，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    2015-10-12日的月份最后一日是@monthEnd(2015-10-12)
    

**_结果_**
    
    
    2015-10-12日的月份最后一日是2015-10-30
    

## weekDay

**_语法_**

@weekDay(_date_)

  * 当前星期数(1=星期天，2=星期一, ……7=星期六)
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取星期数，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    2014-07-14的星期数是@weekDay(2014-07-14)
    

**_结果_**
    
    
    2014-07-14的星期数是2
    

## weekOfYear

**_语法_**

@weekOfYear(_date_)

  * 当年第几周，将1月1日所在的周视为一年中的第一周
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取周数，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    2014-07-14是这一年的第@weekOfYear(2014-07-14)周
    

**_结果_**
    
    
    2014-07-14是这一年的第29周
    

## quarter

**_语法_**

@quarter(_date_)

  * 当前季度，在1到4范围内
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取季度，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    2014-07-14是2014年的第@quarter(2014-07-14)季度
    

**_结果_**
    
    
    2014-07-14是2014年的第3季
    

## quarterBegin

**_语法_**

@quarterBegin(_date_)

  * 当前季度第一天日期
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取季度第一天日期，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    2014-07-14的季度第1天是@quarterBegin(2014-07-14)
    

**_结果_**
    
    
    2014-07-14的季度第1天是2014-07-01
    

## quarterEnd

**_语法_**

@quarterEnd(_date_)

  * 当前季度最后一天日期
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期中提取季度最后一天日期，格式为`yyyy-MM-dd HH:mm:ss或yyyy-MM-dd`

**_例子_**
    
    
    2014-07-14的季度区间是@quarterBegin(2014-07-14)至@quarterEnd(2014-07-14）
    

**_结果_**
    
    
    2014-07-14的季度区间是2014-07-01至2014-09-30
    

## timestemp

**_语法_**

@timestemp

  * 从世界时1970年1月1日0时0分0秒起至现在的毫秒数
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

无

**_例子_**
    
    
    从1970年1月1日到现在，消费了@timestemp秒
    

**_结果_**
    
    
    从1970年1月1日到现在，消费了1405322673793秒
    

## isLeapYear

**_语法_**

@isLeapYear(_date_)

  * 当前日期是否为闰年
  * 默认取自当前AWS服务器节点的时钟时间

**_参数_**

  * _date_ （可选）从指定日期计算是否为闰年，格式为`yyyy-MM-dd或yyyy-MM-dd HH:mm:ss`

**_例子_**
    
    
    2014-08-18这一年@if(@isLeapYear(2014-08-18),是闰年,不是闰年)
    

**_结果_**
    
    
    2014-07-14这一年不是闰年
    

## GMTDate

**_语法_**

@GMTDate

  * 获取en-US地区的GMT格式的时间，格式：Fri, 10 Dec 2021 06:17:34 GMT

**_参数_**

无

## UTCDate

**_语法_**

@UTCDate

  * 获取en-US地区的UTC格式的时间，格式：YYYYMMDD T HHMMSS Z

**_参数_**

无

## isoDateFormat

**_语法_**

@isoDateFormat(*isoDate,format)

  * 将ISO-8601格式日期（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'）按照目标格式进行转换

**_参数_**

  * _isoDate_ (必选) ISO-8601格式日期（如2017-07-10T10:13:47.861Z）
  * _format_ (必选) 日期表达式：如yyyy-MM-dd 或yyyy-MM-dd HH:mm:ss，支持"timestamp"转换为时间戳 -

**_例子_**
    
    
    @isoDateFormat(2022-03-03T18:11:00.211Z,yyyy-MM-dd HH:mm:ss)，@isoDateFormat(2022-03-03T18:11:00.211Z,timestamp)
    

## timestamp2date

**_语法_**

@timestamp2date(*timestamp)

  * 将时间戳转换成日期

**_参数_**

  * _timestamp_ （必填），格式为时间戳

**_例子_**
    
    
    @timestamp2date(1659846856)
    

**_结果_**
    
    
    2022-8-7 12:34:16
    

## timestamp2date

**_语法_**

@date2Timestamp(*datetime)

  * 将日期时间转时间戳

**_参数_**

  * _datetime_ （必填），格式为yyyy-MM-dd HH:mm:ss

**_例子_**
    
    
    @date2timestamp(2022-8-7 12:34:16)
    

**_结果_**
    
    
    1659846856
    

## dateDiff

**_语法_**

@dateDiff(_beginDate,_ endDate,*units)

  * 计算两个日期/时间值的差值

**_参数_**

  * _beginDate_ （必填）开始日期或日期时间，格式为yyyy-MM-dd HH:mm:ss或yyyy-MM-dd
  * _endDate_ （必填）结束日期或日期时间，格式为yyyy-MM-dd HH:mm:ss或yyyy-MM-dd
  * _units_ （必填）差值单位，包括：year、month、week、day、hour、minute、second

**_例子_**
    
    
    @dateDiff(2022-08-01,2022-08-02,day)
    

**_结果_**
    
    
    1
    

## hours

**_语法_**

@hours(_beginDate,_ endDate,holidays)

  * 计算开始日期到结束日期的小时数,精确到2位小数

**_参数_**

  * _beginDate_ （必填）开始日期或日期时间，格式为yyyy-MM-dd HH:mm:ss或yyyy-MM-dd
  * _endDate_ （必填）结束日期或日期时间，格式为yyyy-MM-dd HH:mm:ss或yyyy-MM-dd
  * _holidays_ （可选）节假日规则，不提供该参数时不排除节假日。格式为常量def或字符串数组：- def 固定常量， 使用平台公共节假日日历 ； - 字符串数组，格式为YYYY-MM-DD的节假日日期，多个空格分开

**_例子_**
    
    
    @hours(2022-08-01 8:30,2022-08-02 9:30,@sqlSet(xxx))//客户自定义在一个假期表里
    

**_结果_**
    
    
    9.5 //如果8月1日是节假日，有效小时数据是8月2日的0-9:30
    

## days

**_语法_**

@days(_beginDate,_ endDate,holidays)

  * 计算开始日期到结束日期的天数

**_参数_**

  * _beginDate_ （必填）开始日期或日期时间，格式为yyyy-MM-dd HH:mm:ss或yyyy-MM-dd
  * _endDate_ （必填）结束日期或日期时间，格式为yyyy-MM-dd HH:mm:ss或yyyy-MM-dd
  * _holidays_ （可选）节假日规则，不提供该参数时不排除节假日。格式为常量def或字符串数组：- def 固定常量， 使用平台公共节假日日历 ； - 字符串数组，格式为YYYY-MM-DD的节假日日期，多个空格分开

**_例子_**
    
    
    @days(2022-08-01,2022-08-18,@sqlSet(xxx)) //客户自定义在一个假期表里
    

**_结果_**
    
    
    7