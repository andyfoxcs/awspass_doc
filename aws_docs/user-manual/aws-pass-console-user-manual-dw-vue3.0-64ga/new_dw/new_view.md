# 新建、复制、删除视图类型 · AWS PaaS文档中心

# 新建、复制、删除视图类型

## 新建视图

  1. 打开视图模型配置界面
  2. 点击左上角"加号"图标
  3. 弹出"填写类型、名称"框，选择类型并输入名称点击"确定"按钮，完成操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/11.png)](<11.png>)

属性项 | 说明  
---|---  
类型 | 任务分组显示方式，详细分类说明参见[视图](<../base_def/view.html>)章节，`数据视图`没有类型这个属性  
名称 | 客户端视图列表的显示名称，必填  
  
## 菜单选项卡

  1. 打开视图模型配置界面
  2. 打开一个视图，鼠标移动到视图名称就能显示`菜单选项卡`，没打开的视图，是不能显示的

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/menu.png)](<menu.png>)

### 修改视图名称

  1. 打开视图模型配置界面
  2. 打开一个视图的`菜单选项卡`
  3. 点击`菜单选择卡上的视图名称`，进行修改，通过回车或点击[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/dg.png)](<dg.png>)图标，完成修改操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/modify_name.png)](<modify_name.png>)

### 访问权限

设置当前视图允许访问的范围，如不设置，默认所有用户均可访问

  1. 打开视图模型配置界面
  2. 鼠标移动视图名称上，点击"访问权限"  

  3. 弹出"授权"框，添加可访问权限，完成操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/3-3-3.png)](<3-3-3.png>)

### 复制

  1. 打开视图模型配置界面
  2. 鼠标移动视图名称上，点击"复制"，出现新的带`复制`名称的视图，完成复制

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/copy.png)](<copy.png>)

>   * 视图的相关权限不会被复制
>   * `我的待办视图`、`我的已办视图`、`发起跟踪视图`不支持复制
>   * 一个视图被复制多次，复制视图的名称有数字标记
> 

### 删除

  1. 打开视图模型配置界面
  2. 鼠标移动视图名称上，点击"删除"
  3. 弹出提示信息，点击"确定"按钮，完成操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/delete.png)](<delete.png>)

> 最后一个视图不能删除，不显示删除菜单

### 排序

  1. 打开视图模型配置界面
  2. 点击视图并拖动视图到另一视图的位置
  3. 放开鼠标，位置交换成功

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/px.gif)](<px.gif>)

> 多个视图交换位置后，客户端运行效果视图展示顺序与交换位置后的顺序一致,排在第一个的视图作为默认视图

## 预览

  1. 打开视图模型配置界面
  2. 点击左上角的`预览`按钮
  3. 弹出视图运行效果页面，完成操作。该操作适用于设计阶段模拟运行

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/9-1.png)](<9-1.png>)