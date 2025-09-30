# 列数据 · AWS PaaS文档中心

# 列数据

**添加列数据**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/ldate.png)](<ldate.png>)  
---  
项 | 说明  
---|---  
来源字段 | 在数据来源中合法的字段名  
显示名称 | 在数据来源中合法的字段名对应的显示名称，默认显示对应字段名的标题名，可以自定义  
显示 | 默认开启，当关闭时，值可以回填到表单，但在字典表格中隐藏，设置关闭在列数据中置灰显示  
回填字段 | 回填场景选择的数据源BO表中合法的字段名，当来源字段与回填字段名称相同时选择来源字段会自动把回填字段带出  
条件查询 | 默认关闭，开启后，`文本` `日期` `日期时间` `时间` `列表`等组件支持条件查询  
模糊查询 | 默认关闭，开启后，只允许`文本`类型的字段支持模糊查询  
  
>   * 关联选择字典仅支持回填的字段UI类型为单行、多行、数值、货币、列表、单选组、复选组、日期、时间、日期时间、滑杆、开关、网格数据字典、地址簿、附件  
> 
>   * 支持附件回填，清空时附件不做删除操作，只追加
>   * 配置附件回填，列数据中需要配置唯一标识列数据
>   * 移动端不支持条件查询
>   * 列数据中未开启模糊查询时，条件查询最多配置3个，这3个是AND关系
>   * 列数据中已配置3个条件查询时，不能开启模糊查询
>   * 列数据中开启模糊查询，条件查询最多配置2个，模糊查询与条件查询没有关系，两者是分开查的
> 

**条件查询**

**文本**

**_配置_**

  * 无

**_运行示例_**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/text.png)](<text.png>)  
---  
  
**日期**

**_配置_**

  * 无

**_运行示例_**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/data.png)](<data.png>)  
---  
  
**日期时间**

**_配置_**

  * 无

**_运行示例_**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/datatime.png)](<datatime.png>)  
---  
  
**时间**

**_配置_**

  * 无

**_运行示例_**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/time.png)](<time.png>)  
---  
  
**列表**

**_配置_**

数据源配置参见[组件-常规-单行辅助录入](<../zj/text.html#source>)

> 条件查询列表中支持单选

**_运行示例_**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/selectR.png)](<selectR.png>)  
---  
  
**列数据编辑/删除/拖动**

  * 列数据配置后，还可以点击编辑按钮，打开进行编辑
  * 删除列数据后，设计区和运行端不在显示该列数据
  * 鼠标放在列数据拖动图标，拖动列数据，调整顺序，展示区和运行端会与调整后的顺序同步，展示区也能拖动顺序同步到列数据

**展示区操作**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/ldate1.png)](<ldate1.png>)  
---  
  
  * 支持修改标题名称
  * 支持拖动列宽
  * 支持拖动字段调整顺序，同步列数据
  * 开启修改每页行数，不是控制分页不分页
  * 内容换行显示，默认关闭，显示不全的，鼠标放上去会提示全部内容；开启后，内容换行显示
  * 支持预览，预览中不支持查询操作