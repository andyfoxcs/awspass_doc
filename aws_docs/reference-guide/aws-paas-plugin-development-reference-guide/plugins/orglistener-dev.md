# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现`OrgListener`接口，实现处理逻辑
  2. 用`OrgSyncPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### OrgListener接口

开发者可实现这个接口完成组织改变监听事件的开发。

> com.actionsoft.bpms.org.event.OrgListener
    
    
    package com.actionsoft.bpms.org.event;
    
    
    /**
     * 组织改变监听事件
     */
    public interface OrgListener {
        /**
         * 增加
         */
        public static final int ACTION_ADD = 1;
    
        /**
         * 修改
         */
        public static final int ACTION_MODIFY = 2;
    
        /**
         * 删除
         */
        public static final int ACTION_REMOVE = 3;
    
        /**
         * 注销账户
         */
        public static final int ACTION_DISABLE_USER_ACCOUNT = 4;
    
        /**
         * 激活账户
         */
        public static final int ACTION_ENABLE_USER_ACCOUNT = 5;
    
        /**
         * 修改密码
         */
        public static final int ACTION_USER_SET_PASSWORD = 6;
    
        /**
         * 初始化密码
         */
        public static final int ACTION_USER_INIT_PASSWORD = 7;
        /**
         * 操作单位模型前事件
         *
         * @param oldModel 原模型
         * @param newModel 新模型
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除
         */
        public boolean beforeCompanyChanged(CompanyModel oldModel, CompanyModel newModel, int action);
    
        /**
         * 操作部门模型前事件
         *
         * @param oldModel 原模型
         * @param newModel 新模型
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除
         */
        public boolean beforeDepartmentChanged(DepartmentModel oldModel, DepartmentModel newModel, int action);
    
        /**
         * 操作角色模型前事件
         *
         * @param oldModel 原模型
         * @param newModel 新模型
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除
         */
        public boolean beforeRoleChanged(RoleModel oldModel, RoleModel newModel, int action);
    
        /**
         * 操作团队模型前事件
         *
         * @param oldModel 原模型
         * @param newModel 新模型
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除
         */
        public boolean beforeTeamChanged(TeamModel oldModel, TeamModel newModel, int action);
    
        /**
         * 操作人员模型前事件
         *
         * @param oldModel 原模型
         * @param newModel 新模型
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除<br/>
         * OrgListener.ACTION_DISABLE_USER_ACCOUNT 表示注销用户<br/>
         * OrgListener.ACTION_ENABLE_USER_ACCOUNT 表示激活用户<br/>
         * OrgListener.ACTION_USER_SET_PASSWORD 表示设置用户密码<br/>
         * OrgListener.ACTION_USER_INIT_PASSWORD 表示初始化用户密码<br/>
         */
        public boolean beforeUserChanged(UserModel oldModel, UserModel newModel, int action);
    
    
    
        /**
        * 操作兼职人员模型前
        * @param oldModel 原模型
        * @param newModel 新模型
        * @param action 操作动作<br/>
        * OrgListener.ACTION_ADD 表示增加<br/>
        * OrgListener.ACTION_MODIFY 表示修改<br/>
        * OrgListener.ACTION_REMOVE 表示删除
        *
        */
        @Override
        public boolean beforeUserMapChanged(UserMapModel oldModel, UserMapModel newModel, int action) {
            return false;
        }
    
    
        /**
        * 操作兼职人员模型后
        * @param oldModel 原模型
        * @param newModel 新模型
        * @param action 操作动作<br/>
        * OrgListener.ACTION_ADD 表示增加<br/>
        * OrgListener.ACTION_MODIFY 表示修改<br/>
        * OrgListener.ACTION_REMOVE 表示删除
        */
         @Override
        public void afterUserMapChanged(UserMapModel oldModel, UserMapModel newModel, int action) {
    
        }
    
        /**
         * 操作单位模型后事件
         *
         * @param oldModel 修改前对象
         * @param newModel 修改后对象
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除
         */
        public void afterCompanyChanged(CompanyModel oldModel, CompanyModel newModel, int action);
    
        /**
         * 操作部门模型后事件
         *
         * @param oldModel 修改前对象
         * @param newModel 修改后对象
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除
         */
        public void afterDepartmentChanged(DepartmentModel oldModel, DepartmentModel newModel, int action);
    
        /**
         * 操作角色模型后事件
         *
         * @param oldModel 修改前对象
         * @param newModel 修改后对象
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除
         */
        public void afterRoleChanged(RoleModel oldModel, RoleModel newModel, int action);
    
        /**
         * 操作团队模型后事件
         *
         * @param oldModel 修改前对象
         * @param newModel 修改后对象
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除<br/>
         */
        public void afterTeamChanged(TeamModel oldModel, TeamModel newModel, int action);
    
        /**
         * 操作人员模型后事件
         *
         * @param oldModel 修改前对象
         * @param newModel 修改后对象
         * @param action 操作动作<br/>
         * OrgListener.ACTION_ADD 表示增加<br/>
         * OrgListener.ACTION_MODIFY 表示修改<br/>
         * OrgListener.ACTION_REMOVE 表示删除<br/>
         * OrgListener.ACTION_DISABLE_USER_ACCOUNT 表示注销用户<br/>
         * OrgListener.ACTION_ENABLE_USER_ACCOUNT 表示激活用户<br/>
         * OrgListener.ACTION_USER_SET_PASSWORD 表示设置用户密码<br/>
         * OrgListener.ACTION_USER_INIT_PASSWORD 表示初始化用户密码<br/>
         */
        public void afterUserChanged(UserModel oldModel, UserModel newModel, int action);
    

### 注册语法

由`OrgSyncPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册
    list.add(new OrgSyncPluginProfile(WeixinOrgSync.class.getName()),"描述说明");
    

  * `clazz` 实现类路径