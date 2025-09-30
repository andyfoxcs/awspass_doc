# 配置查询条件 · AWS PaaS文档中心

# 配置查询条件

DW运行时查询区域的维护，分为：

  * [条件查询](<query.html>)
  * [范围查询](<navigation.html>)

**步骤**

  1. 打开用户视图配置界面
  2. 鼠标划动到"配置查询条件"区域并点击"配置查询条件"，显示成可编辑状态
  3. 点击"添加"按钮，弹出"查询字段配置选项卡"
  4. "查询字段配置选项卡"的相关操作配置完成后，点"保存"，完成操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/quickstart/select.gif)](<../quickstart/select.gif>)

**高级选项**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/28.png)](<28.png>)

属性项 | 说明  
---|---  
自动查询 | 运行时打开DW列表自动执行查询条件，显示相应数据，如果不开启，则打开DW时，默认无数据展示，需手动点查询按钮进行查询后展示，默认开启  
交互方式 | 查询条件区交互方式，仅适用于条件查询  
● 弹出列表  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/28-1.png)](<28-1.png>)  
● 平铺（展开）   
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/28-2.png)](<28-2.png>)  
● 平铺（收起）  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/28-3.png)](<28-3.png>)  
布局 | ● 上下布局  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/28-3.png)](<28-3.png>)   
● 左右布局  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/28-4.png)](<28-4.png>)  
  
### 移动端查询条件展示效果

配置查询条件后在移动端视图列表右下角点击([![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/27.png)](<27.png>))将自动显示([![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/27-1.png)](<27-1.png>)) 图标，点击打开查询侧边栏进行查询。

[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/27-2.png)](<27-2.png>)

>   * 列表配置显示规则后，查询结果是按取值来进行查询的，即数据库中存的值。如字段值是`admin`,配置显示规则后显示成`管理员`,用`admin`查询，查询结果是列表中显示成`管理员`的数据  
> 
>   * 地址簿在移动端显示的是文本，不是地址簿组件
>