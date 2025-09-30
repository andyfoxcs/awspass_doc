# 关联任务 · AWS PaaS文档中心

# 关联任务

将与当前操作者相关的已办任务关联到当前表单，为领导决策提供与表单信息相关联的其他流程数据，这是一个私有封装。该组件在运行时为用户提供一个任务关联界面，实施该组件的字段类型应为文本型，将在数据库中存储关联任务的ID值

> 1.关联任务UI组件仅支持主表单，不支持子表  
>  2.当一个流程实例当前用户有多个已办任务时，只显示最后一个已办任务  
>  3.支持按流程分类、任务标题模糊查询

## 运行

PC端  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/gltask1_pc.png)](<gltask1_pc.png>)  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/gltask2_pc.png)](<gltask2_pc.png>)  
移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/gltask_mobile.png)](<gltask_mobile.png>)  
  
> 回填表单上的任务标题可查看原任务表单

## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/gltask1.png)](<gltask1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**个数**

参见流程字典[个数](<text.html#length>)

**限定范围**

可以选择多个流程 ，不选择时，默认显示当前用户有权限查看的所有关联任务

**显示传阅任务**

开启后显示已阅的传阅任务

**SAD支持**

安装[SAD流程实例分库分表服务](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.sad/index.html>)应用后，才显示该属性，没安装不显示。开启`SAD支持`,在表单运行中会显示按归档期间进行搜索

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/gltask2.png)](<gltask2.png>)  
运行  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/gltask2.1.png)](<gltask2.1.png>)  
  
**控制属性**

参见单行[控制属性](<text.html#control>)

**宽度**

参见单行[宽度](<text.html#wigth>)

**字段规则**

参见单行[字段规则](<text.html#zdgz>)