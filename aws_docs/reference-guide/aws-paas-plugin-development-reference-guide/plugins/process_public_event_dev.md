# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 继承`ProcessPubicListener`抽象类，实现call方法的处理逻辑
  2. 用`ProcessPublicEventPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### ProcessPubicListener抽象类

开发者可继承这个类完成全局事件监听器的开发。

> com.actionsoft.bpms.bpmn.engine.listener.ProcessPubicListener
    
    
    public abstract class ProcessPubicListener extends BizBeanImpl implements ExecuteListenerInterface {
    
        public ProcessPubicListener() {
        }
    
        /**
         * 所有人工任务相关行为发生时被触发(见PublicEventConst常量)
         *
         * @param eventName 事件名称，见PublicEventConst常量
         * @param taskInst 任务实例对象
         * @param ctx 流程引擎提供给监听器的上下文对象
         * @see PublicEventConst
         */
        public abstract void call(String eventName, TaskInstance taskInst, ProcessExecutionContext ctx);
    
    }
    

> call方法是该事件的回调接口。应尽量避免复杂的业务处理或I/O、JDBC操作，降低流程引擎的整体处理性能。如果性能影响明显存在，一种优化方案是可以将程序逻辑处理通过线程完成。

### 注册语法

由`ProcessPublicEventPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册流程全局事件监听器
    list.add(new ProcessPublicEventPluginProfile(clazz,  desc));
    

  * `clazz`-类名称，该类必须继承ProcessPubicListener
  * `desc`-说明