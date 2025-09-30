# 星级打分 | AWS UI组件参考指南

## 星级打分

动态显示一个星级图片，这是一个私有封装。可以显示和修改被表单数据源绑定后的数据，自动通过平台各种权限配置控制其读、写、隐藏状态，数据库的值为从0-2N，N为星星颗数（仅考虑整数），该UI组件在一个表单仅允许了出现一次。

### 运行

PC端 | 移动端  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/ratingR1.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/ratingR1_m.png)  
  
### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/ratingD1.png)

**基本属性**

  * **_查询列宽_**

不支持

  * **_帮助说明_**

不支持

  * **_扩展代码_**

不支持

**扩展属性**

  * **_星星颗数_**

表单页面总共显示星星的数量，默认为5（4,5,6,7,8,9,10下拉框）

  * **_整颗星的分值_**

1或2（下拉框），如果选择2，则每半颗星单位为1

  * **_是否显示分数_**

默认右侧显示分数数字