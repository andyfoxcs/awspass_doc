# 添加数据方案 · AWS PaaS文档中心

## 添加数据方案

**步骤**

  1. 打开数据方案管理器
  2. 点击左侧"添加"按钮，弹出数据方案窗口
  3. 输入数据方案属性，点击"确定"按钮
  4. 系统将自动在数据方案管理器左侧方案列表增加对应数据方案
  5. 在左侧方案列表选中该数据方案，点击右侧"表单库"按钮，为该数据 方案绑定需要的表单模型

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/manager_data/39.png)](<39.png>)

属性项 | 说明  
---|---  
数据方案名称 | 数据方案标识名，必填  
表达式内容 | 一个返回Boolean值的表达式，支持@公式，通常为多个@公式组合使用   
如`@if(@equals(@uid,admin),true,false)，表示当admin访问该用户视图时，将使用此数据方案表单`。  
如果不填默认为true  
  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/manager_data/40.png)](<40.png>)

> 一个数据应用视图可以增加多个数据方案，且支持上下拖动排序，当有多个数据方案都满足当前业务场景时，将应用第一个满足当前业务场景的数据方案。