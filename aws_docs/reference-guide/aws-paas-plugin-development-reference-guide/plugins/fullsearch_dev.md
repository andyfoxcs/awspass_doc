# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 确认AWS PaaS已安装`全文检索引擎`应用
  2. 用`FullSearchPluginProfile`申请全文检索引擎服务，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 在你的应用manifest.xml配置文件中声明requires，如

> <requires>
>           <require appId="com.actionsoft.apps.fullsearch" notActiveHandler="warning"/>
>          </requires>
>          

4.在你的应用中调用相关ASLP服务接口，实现自己的全文检索服务

5.场景模拟，调试

> 对于全文检索相关知识（如搜索语法、参数），可翻阅[Apache Lucene](<http://lucene.apache.org/>)相关技术文档

### 注册语法

由`FullSearchPluginProfile`类申请全文检索引擎服务。
    
    
    // 注册全文检索引擎服务
    list.add(new FullSearchPluginProfile(repositoryName, isSupportHTTP, desc));
    

  * `repositoryName`-索引库名，建议使用英文字母和数字命名(区分大小写)，不建议使用中文、怪字符和空格等
  * `isSupportHTTP`-该库是否开放HTTP API
  * `desc`-说明

> 入库的索引文件将自动存储在以下位置
>     
>     
>     %AWS-HOME%/doccenter/%appId%/_fullsearch/%repositoryName%
>     //AWS-HOME指安装目录
>     //appId指你的应用Id
>     //repositoryName指注册申请的索引库名称
>     

### 提供的ASLP服务接口

可以使用`SDK.getAppAPI.callASLP`和HTTP两种方式调用

  * /createIndexByContent - 入库操作，通过给定的内存创建索引
  * /createIndexByFile - 入库操作，通过给定的文件路径创建索引
  * /deleteIndex - 删除索引
  * /updateIndex - 更新索引
  * /search - 简单查询
  * /advancedSearch - 高级查询
  * /searchTotalNum - 检索结果总数
  * /parseDoc - 工具服务，抽取文档内容

#### /createIndexByContent

入库操作，创建内容索引。如果提供了`documentPath`且该文件类型支持正文抽取，将该正文入库。如果你需要自定义索引字段，丰富条件查询，可以使用`otherFields`定义扩展字段的结构。

项 | 说明  
---|---  
地址 | aslp://com.actionsoft.apps.fullsearch/createIndexByContent  
参数 | -`repositoryName`：索引库名（必须）  
-`documentId`：索引ID（必须）  
-`content`：内容（必须）  
-`abstract`：摘要  
-`documentPath`：要入库的文件全路径  
-`title`：标题  
-`createTime`：创建时间，格式为“yyyy-MM-ddHH:mm:ss”，不填则默认为当前时间  
-`otherFields`：扩展的索引字段域结构描述，JSONArray串。  
返回值 | \- 成功返回状态为`ok`的提示  
\- 其他见`result`状态值和`msg`项  
  
> `otherFields` 扩展的索引字段域结构描述，是一个JSONArray串，每一个JSONObject中应该包括：

属性名 | 说明  
---|---  
fieldName | 索引域名（必须）  
fieldType | 索引类型，支持“int”、“text”、“String”。“int”和“String”类型索引不分词，“text”类型索引内容会进行分词，默认为“text”  
fieldContent | 索引内容（必须）  
fieldBoost | 影响查询结果打分，float类型。索引域的boost值越大，查询结果得分越多，排名越靠前，默认为1.0  
fieldStore | 是否保存。如果保存，查询结果返回该字段，否则不返回到查询结果。“true”表示保存  
  
#### /createIndexByFile

入库操作，通过给定的文件路径创建索引

项 | 说明  
---|---  
地址 | aslp://com.actionsoft.apps.fullsearch/createIndexByFile  
参数 | -`repositoryName`：索引库名（必须）  
-`documentPath`：要入库的文件全路径（必须）  
返回值 | \- 成功返回状态为`ok`的提示  
\- 其他见`result`状态值和`msg`项  
  
#### /deleteIndex

删除索引。如果要删除的索引由`createIndexByFile`入库，可给定`documentId`和`documentPath`值为文件路径名

项 | 说明  
---|---  
地址 | aslp://com.actionsoft.apps.fullsearch/deleteIndex  
参数 | -`repositoryName`：索引库名（必须）  
-`documentId`：索引ID，入库时给定的ID（必须）  
-`documentPath`：入库的文件全路径  
返回值 | \- 成功返回状态为`ok`的提示  
\- 其他见`result`状态值和`msg`项  
  
#### /updateIndex

更新索引，接口参数参见`/createIndexByContent`

#### /search

简单查询

项 | 说明  
---|---  
地址 | aslp://com.actionsoft.apps.fullsearch/search  
参数 | -`repositoryName`：索引库名（必须）  
-`searchText`：搜索内容（必须）  
-`highlight`：是否高亮显示，“true”高亮显示，默认为“false”  
\- `maxResult`：最大结果数，默认为“1000”  
`pageNo`：页数，分页查询需要提供  
`pageSize`：每页结果数，分页查询需要提供  
`sortFields`：排序字段，JSONObject字符串格式，key为要排序的字段，value为“true”或“false”。“true”表示降序排序；“false”表示升序排序  
返回值 | \- 成功返回类型为`List<Map<String, String>>`的JSON串  
\- 其他见`result`状态值和`msg`项  
  
> 如该索引库定义了扩展字段（ `otherFields`），那些设置`fieldStore`为`false`的字段值可以参与查询但不提供至查询结果中

#### /advancedSearch

高级查询，接口参数参见`/search`。与简单查询不同的是，`searchText`参数必须是一个查询表达式，具体用法如下：

  * **多域查询**  
title:\"a b c\" AND content:d，表示查询title中包含“a b c”，并且content中包含“d”的索引。Option可以为“AND（+）”、“OR（空格）”或“NOT（-）”。注意：不能单独使用NOT；查询多个词时要用引号引起来。
  * **模糊查询**  
① 通配符：支持正则表达式。例如，匹配单一字符，用“？”，匹配多个字符用“ _”。注意：“？”和“_ ”不能放在第一个字符  
② 模糊查询：查询与某个词类似的词，在要查询的词语后面加“~”。例如：查询“roam~”，也会查到包含“roams”、“foam”等词语的索引  
③ 范围查询：查询某个范围内的索引，用“[XX TO XX]”。例如：“createTime:[2014-1-01-01 00:00:00 TO 2014-01-31 23:59:59]”
  * **查询优先级**  
可以给不同的查询词设置不同的权重，例如“fulll^4 search”表示查询时，“full”更重要。权重因子越大，表示越重要，默认为“1”
  * **分组查询**  
可以用圆括号将查询表达式分组。例如：”(a OR b) AND c“表示必须包含”c”,并且包含”a“或”b“中的一个

> 以上查询可以组合使用，可翻阅[Apache Lucene](<http://lucene.apache.org/>)相关技术文档

* * *

> 通常需要对查询结果做权限过滤。如果权限简单（如基于业务类型），可以在入库时通过创建扩展字段，在查询时增加匹配条件；如果权限复杂（如基于用户组织身份、业务数据权限），可以在你的程序中对搜索结果做二次权限过滤

#### /searchTotalNum

检索结果总数，接口参数参见`/search`。

#### /parseDoc

工具服务，抽取文档内容。支持的文档后缀类型如下

  * txt
  * doc
  * docx
  * xls
  * xlsx
  * ppt
  * pptx
  * pdf
  * htm
  * html
  * xml
  * wps

> 如支持更多后缀类型的文件，可修改该App的`PARSEDOC-TYPE`参数