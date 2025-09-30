# 开发步骤 · AWS PaaS文档中心

# 开发步骤

  1. 继承`AbstExpression`抽象类，实现公式的处理逻辑
  2. 用`AtFormulaPluginProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

## AbstExpression抽象类

开发者可继承这个类完成AT公式的开发。

> com.actionsoft.bpms.commons.at.AbstExpression
    
    
    public abstract class AbstExpression implements ExpressionInterface{
    
        /**
         * 公式解析，需要开发者实现的接口
         *
         * @param expression 待解析的AT公式
         * @return 解析后的结果
         * @throws AWSExpressionException UnCheck类异常
         */
        public abstract String execute(String expression) throws AWSExpressionException;
    
        /**
         * AT公式上下文对象，如获取UserContext、ProcessInstance、TaskInstance等。对于性能提升，
         * 开发者应优先判断上下文中是否已提供足够多的对象线索，避免从内存或数据库中二次构建
         *
         * @return AT公式引擎提供的上下文信息
         * @see ExpressionContext AT公式上下文
         */
        public ExpressionContext getExpressionContext();
    
        /**
         * 工具方法。如果该公式可以接受实施人员给定的参数，该方法用于获得指定顺序的参数值。如果该参数还包含嵌套的AT公式，返回最终的参数值
         *
         * @param str 待解析的AT公式
         * @param index 取参顺序，从1开始
         * @return 参数值，如果未找到或未定义返回空串
         */
        public String getParameter(String str, int index);
    
        /**
         * 工具方法。判断某个等价语义的字符串是否为假
         *
         * @param str 假值的语义等价字符串
         * @return 如果给定的值等于(忽略大小写)false、off、0、no、否，返回true
         */
        public boolean isFalse(String str);
    }
    

## 注册语法

由`AtFormulaPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册AT公式
    list.add(new AtFormulaPluginProfile(groupName, syntax,
    clazz, title, desc));
    

  * `groupName`-分类，首先检查当前AT公式库的分类是否符合你的公式，如果不符合可以给定一个合理的新分类
  * `syntax`-语法，例如`@hour(datetime)`。如某参数必填可加*前缀，例如`@dateAdd(*datepart,*number,*date)`
  * `clazz`-实现类路径，如`com.actionsoft.apps.poc.plugin.at.MyLenExpression`
  * `title`-简要说明，简明扼要
  * `desc`-详细说明