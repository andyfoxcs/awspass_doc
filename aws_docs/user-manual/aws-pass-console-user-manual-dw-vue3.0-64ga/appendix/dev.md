# DW相关开发 · AWS PaaS文档中心

## DW相关开发

### DW视图高级选项侧边栏右下角URL外链增加自动查询条件

DW视图高级选项侧边栏右下角URL外链
    
    
    http://localhost:8088/portal/r/w?sid=053740bc-b231-44b0-932b-9d0b3288745a&cmd=CLIENT_DW_PORTAL&processGroupId=xxxxxx&appId=xxxx
    

如果实现自动查询，需要增加如下查询字符串
    
    
    //查询条件
    condition=[{tp:'文本',cp:'like',fd:'NAMEOBJ_FAF1569E1992444BA4B351C702E747CC',cv:'1'}]
    
    
    
    //完整URL
    http://localhost:8088/portal/r/w?sid=053740bc-b231-44b0-932b-9d0b3288745a&cmd=CLIENT_DW_PORTAL&processGroupId=xxxxxx&appId=xxxx&condition=[{tp:'文本',cp:'like',fd:'NAMEOBJ_FAF1569E1992444BA4B351C702E747CC',cv:'1'}]
    

参数 | 描述 | 说明  
---|---|---  
tp | 数据类型，选填 | 可填写 文本、数值、日期或者str、num、date；不填写默认为文本类型  
cp | 比较运算符，必填 | 可填写 =、!=、<、>、<=、>=、like、not like  
fd | 字段名称，必填 | 要求大写，支持2种格式：   
1.大写字段名。  
2.大写字段名+查询器条件查询组件标识ID。  
第2种格式时，如果页面上有此条件查询器项，将会回填此值到元素上。  
cv | 值，必填 | 字段的值  
  
更多详细介绍参见[URL外链地址](<../new_dw/table.html#url>)