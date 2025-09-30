# 按钮 · AWS PaaS文档中心

# 按钮

有关按钮属性的详细介绍参见[数据窗口-自定义按钮](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/event.html>)章节

禁用规则、显示规则、样式规则、校验规则中的规则条件与[数据窗口-自定义按钮](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/event.html>)不同，这的规则条件根据下面三种条件来判断：

  * 根据`主表单` `可编辑` `只读`这两种状态作为条件
  * 根据`流程状态`等于`流程结束后`作为条件
  * 根据`任务状态`等于`普通待办`、`抄送`、`沟通`、`通知`、`已办`、`全部状态`、`共享状态`等状态作为条件

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/zjbutton.png)](<zjbutton.png>)  
---  
  
> 任务状态是`通知`的场景比较特殊，只有在未读状态打开表单时生效，已读打开表单规则失效