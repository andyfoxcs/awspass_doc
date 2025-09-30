# 表格 · AWS PaaS文档中心

# 表格

`表格`、`列表`、`卡片`、`时间轴`的配置详情，参见[交互模式-pc端](<pc.html>)、[交互模式-移动端](<mobile.html>)

## 多级表头

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18-4.png)](<18-4.png>)

  * `表头`，当列表选择表头时，会自动增加一行用于配置当前表头对应的字段
  * `字段`，配置显示字段，未出现在该配置中的字段在运行时将自动追加到列后面显示

**运行效果**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18-3.png)](<18-3.png>)

## 条件样式

灵活配置字段显示值、图标及外观的提示语：

  1. 同一个字段被作为条件配置多次，仅最下面的配置有效  

  2. 只有虚拟字段能显示其他字段的值  

  3. 条件可以编写JavaScript脚本，需要返回boolean类型的值  

  4. 结果字段可以显示原值及配置外观

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/rule1.png)](<rule1.png>)

展示效果图

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/rule2.png)](<rule2.png>)

>   * `多级表头`、`条件样式`只支持交互风格是表格的，其他的不支持  
> 
>   * 条件样式优先级高于列表字段样式
> 

### 地图条件样式配置入口

[![](https://helpcdn.awspaas.com/picture/picture/202404/0032a212df1848cd8505bca6e30bde1a.png)](<https://helpcdn.awspaas.com/picture/picture/202404/0032a212df1848cd8505bca6e30bde1a.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18-3.1.png)](<18-3.1.png>)

PC端展示效果

[![点位显示运行效果](https://helpcdn.awspaas.com/picture/picture/202404/760bfbfff77145f2b0751a3408df104b.png)](<https://helpcdn.awspaas.com/picture/picture/202404/760bfbfff77145f2b0751a3408df104b.png>)

移动端端展示效果

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18-3.2.png)](<18-3.2.png>)

## URL外链

为当前DW视图快速生成独立部署的URL地址。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/3-3-4.png)](<3-3-4.png>)

  * `隐藏查询条件区`，URL地址页面是否显示视图查询条件区域
  * `隐藏工具条`，URL地址页面是否显示工具条区域
  * `隐藏标题栏`，，URL地址页面是否显示标题栏
  * `参数condition`，URL地址支持`condition`参数，自动执行查询条件，详细配置参见页面说明

> 如果确认URL地址没写错，但打开URL报`HTTP Status 400 – Bad Request`错，这说明`condition`参数值需要转义