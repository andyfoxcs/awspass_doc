# 文本 | AWS @公式参考指南

# 文本

  * concat
  * len
  * lower
  * upper
  * trim
  * rmb
  * left
  * mid
  * right
  * search
  * rightSearch
  * replace
  * substitute
  * phonetic
  * lpad
  * rpad
  * encode
  * decode
  * urlEncode
  * urlDecode
  * ascii
  * char
  * split
  * isMatch
  * match
  * matchAll
  * rept
  * clean
  * md5
  * sha256
  * loadFile

## concat

**_语法_**

@concat(str1,str2,...)

  * 将两个或多个文本字符串联接为一个字符串

**_参数_**

  * _str1_ （必选）字符串
  * _str2_ （必选）字符串
  * _..._ （可选）更多组数字符串

**_例子_**
    
    
    @concat(abcd,为英文字符)
    

**_结果_**
    
    
    abcd为英文字符
    

## len

**_语法_**

@len(_*str_)

  * 返回字符串长度
  * 每个阿拉伯数字、字母和中文字符都占1个字符长度

**_参数_**

  * _str_ （必选）字符串

**_例子_**
    
    
    @len(abcd中文字符)
    

**_结果_**
    
    
    8
    

## lower

**_语法_**

@lower(_*str_)

  * 字符串转换成小写

**_参数_**

  * _str_ （必选）字符串

**_例子_**
    
    
    @lower(abCD123中文字符)
    

**_结果_**
    
    
    abcd123中文字符
    

## upper

**_语法_**

@upper(_*str_)

  * 字符串转换成大写

**_参数_**

  * _str_ （必选）字符串

**_例子_**
    
    
    @upper(abCD123中文字符)
    

**_结果_**
    
    
    ABCD123中文字符
    

## trim

**_语法_**

@trim(_*str_)

  * 去除字符串前后多余空格

**_参数_**

  * _str_ （必选）字符串

**_例子_**
    
    
    @trim(  去掉前后空格    )
    

**_结果_**
    
    
    去掉前后空格
    

## rmb

**_语法_**

@rmb(_*str_)

  * 将数字转换成人民币大写

**_参数_**

  * _str_ （必选）一个数字字符串

**_例子_**
    
    
    @rmb(123456789.32 )
    

**_结果_**
    
    
    壹亿贰仟叁佰肆拾伍万陆仟柒佰捌拾玖元叁角贰分
    

## left

**_语法_**

@left(*str,*length)

  * 从文本字符串的第一个字符开始返回指定个数的字符
  * 如果length大于文本长度，则返回全部文本

**_参数_**
    
    
    str （必选）字符串
    length （必选）要截取的长度
    

**_例子_**
    
    
    @left(abcd中文字符,4)
    

**_结果_**
    
    
    abcd
    

## mid

**_语法_**

@mid(*str,startNum,numChars)

  * 返回字符串的中间字符。在字符串str中从startNum位置开始截取numChars个字符，且区分大小写

**_参数_**

  * _str_ （必选）字符串
  * _startNum_ （必选）起始位置。 字符串的第一个字符是位置 1
  * _numChars_ （可选）截取字符串个数，不填写截取至最后

**_例子_**
    
    
    @mid(20220801,5)
    

**_结果_**
    
    
    0801
    

## right

**_语法_**

@right(*str,*length)

  * 用法同@left，只是取数方向相反，从右侧开始取数
  * 如果length大于文本长度，则返回全部文本

**_参数_**

  * str （必选）字符串
  * length （必选）要截取的长度

**_例子_**
    
    
    @right(abcd中文字符,4)
    

**_结果_**
    
    
    中文字符
    

## search

**_语法_**

@search(str1,str2,startNum)

  * 匹配位置。获取str2在str1的起始位置，未匹配返回-1
  * 每个阿拉伯数字、字母和中文字符都占1个字符长度
  * 区分大小写

**_参数_**

  * _str1_ （必选）字符串
  * _str2_ （必选）关键词，字符串
  * _startNum_ （可选）开始查找位置，字符串的第一个字符是位置 1

**_例子_**
    
    
    在AWS PaaS字符串中PaaS的起始位置是,从第一个字符开始查找@search(AWS PaaS,PaaS)
    

**_结果_**
    
    
    在AWS PaaS字符串中PaaS的起始位置是5
    

## rightSearch

**_语法_**

@rightSearch(str1,str2,startNum)

  * 匹配位置。获取str2在str1中最右边出现处的索引，未匹配返回-1
  * 每个阿拉伯数字、字母和中文字符都占1个字符长度
  * 区分大小写

**_参数_**

  * _str1_ （必选）字符串
  * _str2_ （必选）关键词，字符串
  * _startNum_ （可选）开始查找位置，字符串的第一个字符是位置 1

**_例子_**
    
    
    在AWS PaaSPaaS字符串中S从最右边出现处的索引,从最后一个字符开始查找@rightSearch(AWS PaaSPaaS,S)
    

**_结果_**
    
    
    在AWS PaaSPaaS字符串中S从最右边出现处的索引位置是12
    

## replace

**_语法_**

@replace(*str,*oldStr,*newStr)

  * 值替换。将str中oldStr的值替换成newStr
  * 每个阿拉伯数字、字母和中文字符都占1个字符长度
  * 区分大小写

**_参数_**

  * _str_ （必选）字符串
  * _oldStr_ （必选）要替换的老关键词，字符串
  * _newStr_ （必选）替换成新的关键词，字符串

**_例子_**
    
    
    将AWS PaaS字符串处理成@replace(AWS PaaS,PaaS,PaaS 6)
    

**_结果_**
    
    
    将AWS PaaS字符串处理成AWS PaaS 6
    

## substitute

**_语法_**

@substitute(_str,_ oldStr,*newStr)

  * 值替换。将str中oldStr的值替换成newStr
  * 每个阿拉伯数字、字母和中文字符都占1个字符长度
  * 区分大小写

**_参数_**

  * _str_ （必选）字符串
  * _oldStr_ （必选）要替换的老关键词，字符串
  * _newStr_ （必选）替换成新的关键词，字符串

**_例子_**
    
    
    将AWS PaaS字符串处理成@substitute(AWS PaaS,PaaS,PaaS 6)
    

**_结果_**
    
    
    将AWS PaaS字符串处理成AWS PaaS 6
    

## phonetic

**_语法_**

@phonetic(_*str_)

  * 取汉语拼音首字母
  * 支持GB2312字符集内的汉语，不支持的汉字不提供拼音缩写。如囧

**_参数_**

  * _str_ （必选）字符串

**_例子_**
    
    
    商学院的汉语拼音首字母是@phonetic(商学院)
    

**_结果_**
    
    
    商学院的汉语拼音首字母是SXY
    

## lpad

**_语法_**

@lpad(*str,*len,padStr)

  * 字符串左填充。返回str字符串的len数量，如果长度不足从左侧补充padStr值
  * 每个阿拉伯数字、字母和中文字符都占1个字符长度
  * 如果str已超出定长值，直接返回该值

**_参数_**

  * _str_ （必选）字符串
  * _len_ （必选）定长值，整数
  * _padStr_ （可选）不足长度时以该值补充，默认0

**_例子_**
    
    
    我是@lpad(7,3)，一个7位定长串@lpad(99,7,*)
    

**_结果_**
    
    
    我是007，一个7位定长串*****99
    

## rpad

**_语法_**

@rpad(*str,*len,padStr)

  * 字符串右填充。返回str字符串的len数量，如果长度不足从右侧补充padStr值
  * 每个阿拉伯数字、字母和中文字符都占1个字符长度
  * 如果str已超出定长值，直接返回该值

**_参数_**

  * _str_ （必选）字符串
  * _len_ （必选）定长值，整数
  * _padStr_ （可选）不足长度时以该值补充，默认0

**_例子_**
    
    
    我是@rpad(7,3)，一个7位定长串@rpad(99,7,*)
    

**_结果_**
    
    
    我是700，一个7位定长串99*****
    

## encode

**_语法_**

@encode(_*str_)

  * 编码成Base64
  * 字符串编码格式为utf-8，如编码失败返回原始字符串值

**_参数_**

  * _str_ （必选）字符串

**_例子_**
    
    
    BPM业务流程管理的Base64值是@encode(BPM业务流程管理)
    

**_结果_**
    
    
    BPM业务流程管理的Base64值是QlBN5Lia5Yqh5rWB56iL566h55CG
    

## decode

**_语法_**

@decode(_*str_)

  * 解码Base64
  * 字符串编码格式为utf-8，如解码失败返回原始字符串值

**_参数_**

  * _str_ （必选）Base64编码字符串

**_例子_**
    
    
    QlBN5Lia5Yqh5rWB56iL566h55CG解码后是@decode(QlBN5Lia5Yqh5rWB56iL566h55CG)
    

**_结果_**
    
    
    QlBN5Lia5Yqh5rWB56iL566h55CG解码后是BPM业务流程管理
    

## urlEncode

**_语法_**

@UrlEncode(_*str,charset_)

  * 将字符串以Url编码

**_参数_**

  * _str_ （必选）字符串
  * _charset_ （可选）编码成指定字符集的串，如果未指定默认为utf-8

**_例子_**
    
    
    BPM业务流程管理的UrlEncode值是@UrlEncode(BPM业务流程管理)
    

**_结果_**
    
    
    BPM%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B%E7%AE%A1%E7%90%86
    

## urlDecode

**_语法_**

@urlDecode(_*str_)

  * 解码URL编码成字符串

**_参数_**

  * _str_ （必选）Url编码字符串

**_例子_**
    
    
    BPM%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B%E7%AE%A1%E7%90%86
    解码后是:@UrlDecode(BPM%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B%E7%AE%A1%E7%90%86)
    

**_结果_**
    
    
    BPM%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B%E7%AE%A1%E7%90%86
    解码后是:BPM业务流程管理
    

## ascii

**_语法_**

@ascii(_*str_)

  * 字符转换为ASCII码。返回与指定字符对应的十进制ASCII码，多个ASCII码空格隔开

**_参数_**

  * _str_ （必选）字符串

**_例子_**
    
    
    BPM业务流程管理的ASCII码是@ascii(BPM业务流程管理)
    

**_结果_**
    
    
    BPM业务流程管理的ASCII码是66 80 77 19994 21153 27969 31243 31649 29702
    

## char

**_语法_**

@char(_*ascii_)

  * ASCII码转换成字符

**_参数_**

  * _ascii_ （必选）ASCII码，多个码用空格隔开

**_例子_**
    
    
    66 80 77 19994 21153 27969 31243 31649 29702是
    @char(66 80 77 19994 21153 27969 31243 31649 29702)
    

**_结果_**
    
    
    66 80 77 19994 21153 27969 31243 31649 29702是BPM业务流程管理
    

## split

**_语法_**

@split(_str,_ separator)

  * 将文本字符串str拆分成子字符串数组

**_参数_**

  * _str_ （必选）字符串
  * _separator_ （必选) 拆分字符串时要使用的分隔符。 可以是零个、一个或多个字符

**_例子_**
    
    
    例1：@split(北京/海淀区,/);例2：@split(北京海淀区,)
    

**_结果_**
    
    
    结果1：北京,海淀区;结果2：北,京,海,淀,区
    

## isMatch

**_语法_**

@isMatch(_str,_ pattern)

  * 测试文本字符串是否与包含普通字符、预定义模式或正则表达式的某种模式相符

**_参数_**

  * _str_ （必选）字符串
  * _pattern_ （必选) 正则表达式,\需要转义

**_例子_**
    
    
    @isMatch(986,\\d+) 匹配大于零的整数
    

**_结果_**
    
    
    true
    

## match

**_语法_**

@match(_str,_ pattern)

  * 提取与模式匹配的第一个文本字符串

**_参数_**

  * _str_ （必选）字符串
  * _pattern_ （必选) 正则表达式\需要转义

**_例子_**
    
    
    @match(actionsoft炎黄盈动665中文,[\\u4e00-\\u9fa5]+)
    

**_结果_**
    
    
    炎黄盈动
    

## matchAll

**_语法_** @matchAll(_str,_ pattern)

  * 提取与模式匹配的全部文本字符串

**_参数_**

  * _str_ （必选）字符串
  * _pattern_ （必选) 正则表达式\需要转义

**_例子_**
    
    
    @matchAll(actionsoft炎黄盈动665中文,[\\u4e00-\\u9fa5]+)
    

**_结果_**
    
    
    炎黄盈动,中文
    

## rept

**_语法_**

@rept(_str,_ times)

  * 重复生成一段字符串。如将用户录入的实际300个文字报告内容替换成300个*

**_参数_**

  * _str_ （必选）一个或多个字符串
  * _pattern_ （必选) 次数

**_例子_**
    
    
    @rept(*,10)
    

**_结果_**
    
    
    **********
    

## clean

**_语法_**

@clean(*str)

  * 删除字符串中所有空格,如果字符串中有逗号需要转义

**_参数_**

  * _str_ （必选）文本字符串

**_例子_**
    
    
    @clean(张三 李四 王五\,赵 六)
    

**_结果_**
    
    
    张三李四王五,赵六
    

## md5

**_语法_**

@md5(_*str_)

  * 获得字符串的MD5哈希摘要（十六进制编码）

**_参数_**

  * _str_ （必选）字符串

**_例子_**
    
    
    BPM业务流程管理的MD5是@md5(BPM业务流程管理)
    

**_结果_**
    
    
    BPM业务流程管理的MD5是QlBN5Lia5Yqh5rWB56iL566h55CG
    

## sha256

**_语法_**

@sha256(*str,*password)

  * 获得字符串的SHA256的哈希摘要（十六进制编码）

**_参数_**

  * _str_ （必选）字符串
  * _password_ （必选）摘要密钥

**_例子_**
    
    
    BPM业务流程管理的SHA256是@sha256(BPM业务流程管理,aaaaabbbbb)
    

**_结果_**
    
    
    BPM业务流程管理的SHA256是
    39B74F0F1398784C410BDD76A0A5CD1AE1D9359F4DB90A747A1FAE698EFA6D5B
    

## loadFile

**_语法_**

@loadFile(*appId,*fileName)

  * 读取指定App下的文件正文，并将这一文件按照字符串的格式返回，同时解析文件中包含的@公式

**_参数_**

  * _appId_ （必选）应用Id
  * _fileName_ （必选）该应用文件夹下的文件路径

**_例子_**
    
    
    @loadFile(com.actionsoft.apps.poc.api,/script/rule1.txt)
    

**_结果_**
    
    
    这是AWS BPM PaaS 6测试脚本