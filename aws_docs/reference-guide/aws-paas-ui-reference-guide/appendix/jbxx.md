# 基本信息 | AWS UI组件参考指南

## 基本信息

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/appendix/dictJbxx1.png)

项 | 说明  
---|---  
字典标题 | 字典在运行时，弹出窗口的标题名称，例如【客户列表】  
数据源  | ● **当前BPM数据源** 数据来自当前AWS连接的本地数据库  
● **CC DB数据源** 数据来自AWS CC的[RDS适配器](<https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/rds.html>)  
● **CC http数据源** 数据来自AWS CC的[HTTP - 连接Web服务](<https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/tech-adapters/http.html>)，示例参见[附录](<../appendix/eg.html>)章节  
  
查询语句  | 标准的SELECT查询语句  
● 查询结果必须包含`ID`字段，且不支持AS结果为 `ID`的字段  
● 支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)   
● 多表查询语句需转换成视图    
● 语句支持$getForm(字段名),该变量可替换客户端表单域中的值，该变量可获取主表中的数据  
例如【… where orderType=’$getForm(ORDERTYPE)’  
● 语句支持$getGrid(字段名)变量，该变量可替换客户端普通子表、Ajax子表模式下当前行列值  
例如【… where id='$getGrid(ID)'】  
  
其它 |  ● **换行显示** 当列数据超过列宽度后，换行显示  
● **多选时是否显示已选中项** 网格数据字典勾选`允许行多选`后，修改时是否默认选中已选记录 _(仅在数据字典模型可用)_  
● **插入前是否提示保存表单** 当主表单数据有更新未保存时是否给出提示 _(仅在参考录入模型可用)_   
● **插入前是否校验字段必填** 当参考录入的子表必填字段,在选择的参考录入行记录中为空时是否给出提示 _(仅在参考录入模型可用)_  
● **插入后是否提示非空信息** 当参考录入的子表必填字段为空时是否给出提示 _(仅在参考录入模型可用)_  
● **每页行数** 每页显示记录行数，若设置0为不分页  
插入前JS脚本  | JavaScript片段，例如`parent.$('#BTN_SAVE').click();` 表示插入前执行表单保存  
插入后JS脚本 | JavaScript片段，例如`var datenumber = $('input:radio:checked').val();`表示数据字典单选时获取用户选择行值  
  
> 网格数据字典在移动端数据展示 下拉加载更多数据，且至少设置1屏以上的数据，才能下拉加载更多