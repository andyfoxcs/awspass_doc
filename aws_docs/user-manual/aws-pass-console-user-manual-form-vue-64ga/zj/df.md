# 打分 · AWS PaaS文档中心

# 打分

动态显示一个星级图片，这是一个私有封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态，数据库的值为从0-2N，N为星星颗数（仅考虑整数），该UI组件在一个表单仅允许了出现一次。

## 运行

PC端 | 移动端  
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textsc_pc.png)](<textsc_pc.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textsc_mobile.png)](<textsc_mobile.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textsc1.png)](<textsc1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**星星颗数**

表单页面总共显示星星的数量，默认为5（4,5,6,7,8,9,10上下箭头选择）

**整颗星分值**

1或2（上下箭头选择），如果选择2，则每半颗星单位为1

**是否显示分数**

默认右侧显示分数数字

**控制属性**

参见单行[控制属性](<text.html#control>)

> `打分`只支持只读

**宽度**

参见单行[宽度](<text.html#wigth>)

**帮助说明**

参见单行[帮助说明](<text.html#help>)

**字段规则**

参见单行[字段规则](<text.html#zdgz>)