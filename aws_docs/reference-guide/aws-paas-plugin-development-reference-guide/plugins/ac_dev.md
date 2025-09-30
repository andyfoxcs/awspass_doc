# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 用`ACPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  2. 编写客户端JavaScript，弹出授权对话框
  3. 使用`SDK`的`PermAPI`进行鉴权判断
  4. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### 注册语法

由`ACPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册AC
    list.add(new ACPluginProfile(resourceType, resourceName,
    assignmentTypes, accessModes, isolationCompany , orgAdminSecurity));
    

  * `resourceType`-资源类别，全局唯一。建议英文字母并区分大小写
  * `resourceName`-资源名称，授权对话框的窗口标题
  * `assignmentTypes`-资源可分配的范围，如果给入空支持全部类型
  * `accessModes`-对该资源提供的访问控制模式，必须定义，最大定义99种
  * `isolationCompany`-分配的范围是否组织间隔离。如果为真不提供单位选择，如支持role或team的tree，过滤非本单位的账户
  * `orgAdminSecurity`-分配的范围是否应用已设定的ORG管理权限，设置为true：可以访问单位、部门；设置为false，控制访问的范围，即应用二级管理员的单位、部门权限

### 判断权限

判断是否拥有资源resourceId的accessMode类型访问权限
    
    
    SDK.getPermAPI().havingACPermission(uid, resourceType, resourceId, accessMode);