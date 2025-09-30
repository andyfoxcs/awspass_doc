# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现`HumanPerformerInterface`接口
  2. 继承`HumanPerformerAbst`抽象类，该类提供了一些公共方法
  3. 用`HumanPerformerPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  4. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### HumanPerformerInterface接口

> com.actionsoft.bpms.bpmn.engine.performer.HumanPerformerInterface
> 
> 关于方法中参数UIContext的说明，请参考以**aws-api-doc**
    
    
    public interface HumanPerformerInterface {
    
        /**
         * 该路由方案为实施人员提供的特定属性编辑页面。一个符合嵌入人工任务“参与者”属性页的HTML代码段，如果没有参数可设置，返回空串
         *
         * @param user 建模人员
         * @param params 路由方案自定义参数
         */
        public String getSetting(UserContext user, Map<String, Object> params);
    
        /**
         * 获得路由结果确认页面，该界面是一个人工交互的Dialog内容
         *
         * @param user 操作者
         * @param isBranch 是否在complete任务时，自动向下执行分支
         * @param processInst 流程实例
         * @param taskInst 任务实例，如果是流程启动节点无任何任务可能为空，否则必须提供即将产生下一任务的当前任务实例
         * @param userTaskDefModel 目标节点的定义
         * @param params 路由方案自定义参数
         * @return
         */
        public String getPage(UserContext user, boolean isBranch, ProcessInstance processInst, TaskInstance taskInst, UserTaskModel userTaskDefModel, Map<String, Object> params);
    
        /**
         * 这是getHumanPerformer的钩子函数，平台在执行getHumanPerformer前的注入操作
         *
         * @param user 操作者
         * @param processInst 流程实例
         * @param taskInst 任务实例，如果是流程启动节点无任何任务可能为空，否则必须提供即将产生下一任务的当前任务实例
         * @param userTaskDefModel 目标节点的定义
         * @param params 路由方案自定义参数
         * @return 执行人账户列表
         */
        public String getHumanPerformerByHook(UserContext user, ProcessInstance processInst, TaskInstance taskInst, UserTaskModel userTaskDefModel, Map<String, Object> params);
    
        /**
         * 获得目标节点的任务执行人账户列表，多个用空格隔开，该方法返回原始的UID即可，被引擎API或getPage()方法回调。
         * 这是路由接口的主要实现的方法， 当前办理者可能是兼任身份，涉及到部门相对关系的算法，
         * 使用getCurrentContextDepartmentId或者getCurrentContextRoleId方法可获取当前办理者的真实身份
         *
         * @param user 操作者
         * @param processInst 流程实例
         * @param taskInst 任务实例，如果是流程启动节点无任何任务可能为空，否则必须提供即将产生下一任务的当前任务实例
         * @param userTaskDefModel 目标节点的定义
         * @param params 路由方案自定义参数
         * @return 执行人账户列表
         */
        public String getHumanPerformer(UserContext user, ProcessInstance processInst, TaskInstance taskInst, UserTaskModel userTaskDefModel, Map<String, Object> params);
    
    }
    

### 注册语法

由`HumanPerformerPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册路由
    
    /**
     * @param group 分类
     * @param title 路由方案名称
     * @param clazz 类名称，该类必须继承HumanPerformerAbst
     * @param desc 详细说明
     */
    list.add(new HumanPerformerPluginProfile(HumanPerformerGroup.ROLE, "共享任务", ClaimRole.class.getName(), "该任务共享给一个特定的角色，该角色的用户可以通过认领完成该任务"));
    

`HumanPerformerGroup`根据路由的分组方式，分为以下几类：

  * 账户
  * 角色
  * 部门
  * 单位
  * 团队小组
  * 复杂找主管
  * 服务API
  * 其他

通常新开发的路由方案放到`其他`中，第一个参数应设置为`HumanPerformerGroup.OTHER`

### 设计时刻界面

注册好之后，将应用部署好，`人工任务属性`->`参与者`->`方案库`中，就会展示相应的路由方案

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/performer-1.png)](<performer-1.png>)

实现类中配置好的界面效果如图：  
示例中仅使用简单的文本框，还是参考AWSUI使用更复杂的界面来满足要求。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/performer-2.png)](<performer-2.png>)

### 代码运行时调试

自定义的配置参数将会写入`params`参数中，可以根据具体业务逻辑使用

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/performer-3.png)](<performer-3.png>)

### 相关资源

  * [ AWS SDK API](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)
  * [《AWS MVC框架参考指南》](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/index.html>)