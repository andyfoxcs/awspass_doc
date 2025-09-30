# 群组 | AWS UI组件参考指南

## 群组

创建一个群组控件，这是一个私有封装。用于显示和修改组织服务下团队群组的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。

### 运行

PC端  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/group1.png)  
移动端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/group1_m.png)  
  
**公共群组**

由管理员用户在Console控制台创建的[公共群组](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-org/organization/public_team.html>)，所有用户均可查看使用。

**私人群组**

由普通用户自己创建的群组，可通过共享，供其他人使用。

  * **_新建私人群组_**

**步骤：**  

    1. 点击右上角"管理"进入我的群组队管理页面  

    2. 点击"新建"按钮，弹出"新增群组"对话框  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/group8.png)  

    3. 填写群组名称和父群组，点击"确定"按钮，完成创建

  * **_删除私人群组_**

**步骤：**  

    1. 选择数据点击"删除"按钮  

    2. 弹出删除提示  

    3. 点击"确定"完成删除  

  * **_修改、管理、共享私人群组_**

    * `管理` 为私人群组填加成员
    * `共享` 将当前私人群组共享给他人使用

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/group9.png)

**预置校验**

无

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/group2.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

不支持

**扩展属性**

  * **_选择模式_**

包括单选和多选

  * **_分隔符_**

多选时，分隔符包括空格和逗号