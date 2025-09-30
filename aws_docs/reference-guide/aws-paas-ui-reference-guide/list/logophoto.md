# 图片标识 | AWS UI组件参考指南

## 图片标识

动态显示一个图片，这是一个私有封装。可支持数字、英文字母下划线和@公式。 运行时，保存数据后数据库中字段存储的是设计时图片标识名称和图片格式的组合。

> 目前该UI组件移动端仅支持只读展示图片，不支持上传修改图片

### 运行

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/logophotoR1.png)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/logophotoD1.png)

**基本属性**

  * **_查询列宽_**

不支持

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

不支持

**扩展属性**

  * **_图片标识_**

支持0~9数字，英文字符，@公式和_ -等

> 同一个图片标识，在同一应用内，图片唯一