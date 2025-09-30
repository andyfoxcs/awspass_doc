# 批量打印二维码 · AWS PaaS文档中心

# 批量打印二维码

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/link1.gif)](<link1.gif>)

添加`批量打印二维码`按钮后，需进一步设置表单。 扫码时将根据所选表单中配置的表单二维码权限进行判断或者是字段二维码来展示内容。

## SQL数据源配置

当DW为SQL数据源时，需要手动配置流程实例字段对应关系。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/linksql.png)](<linksql.png>)

## 运行说明

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/link2.png)](<link2.png>)

### 类型

**表单二维码**

表单二维码和字段二维码、字段条形码

**自定义二维码**

可以输入任意内容，使用公式编辑器可以获取字段的引用

### 打印

**打印勾选数据**

仅支持当前页的勾选

**打印全部数据**

一次最多可支持10000条

### 排版布局（A4纸）

支持用户选择排版布局

### 二维码下方内容

**自定义标题**

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/link3.png)](<link3.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/link4.png)](<link4.png>)  
  
  * 可以输入任意内容，使用公式编辑器可以获取字段的引用

**表格**

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/link5.png)](<link5.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/link6.png)](<link6.png>)  
  
  * 设置标题列、值内容宽度
  * 可以添加多行，设置对应的标题及值内容，支持@公式

## 常见说明

如果扫码提示`表单【XXX】未配置表单二维码`，则您需要在相应表单配置表单二维码，详细参见 <https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue/zj/bdewm.html>

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/link9.png)](<link9.png>)