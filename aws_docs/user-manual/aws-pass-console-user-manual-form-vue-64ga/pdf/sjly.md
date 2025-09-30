# 数据来源 · AWS PaaS文档中心

# 数据来源

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/sjly.png)](<sjly.png>)  
---  
  
`关联表单` `关联存储` `SQL数据` `数据服务` `数据流`的具体配置 参见单行[辅助录入](<../zj/text.html#source>)

**SQL数据中的查询语句需要注意的：**

● 查询结果必须包含ID字段，且不支持AS结果为 ID的字段  
● 支持@公式  
● 多表查询语句需转换成视图  
● 语句支持$getForm(字段名),该变量可替换客户端表单域中的值，该变量可获取主表中的数据 例如【… where orderType=’$getForm(ORDERTYPE)’  
● 语句支持$getGrid(字段名)变量，该变量可替换客户端普通子表、Ajax子表模式下当前行列值 例如【… where id='$getGrid(ID)'】  
● 支持直接写$[字段名]

**$[字段名] $getform(字段名)的使用场景  
** 1.字典在主表里，用$[字段名] $getform(字段名)，级联其他主表的字段，不支持级联子表的字段  
2.字典在子表里，级联其他主表的字段，可以使用$[字段名]和getform，级联字典当前所在行里其他子表字段，使用getgrid  
3.字段子表里，字典取当前字段子表其他字段，使用getgrid，取当前字段子表父级子表的字段使用getform，字段子表不支持取爷爷级别的主表字段

> 关联选择字典在移动端数据展示 下拉加载更多数据，且至少设置1屏以上的数据，才能下拉加载更多