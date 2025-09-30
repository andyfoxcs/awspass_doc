# 开发步骤 · AWS PaaS文档中心

## 开发步骤

  1. 实现`AbstractSecurityProcessor`抽象类
  2. 用`SecurityProcessorProfile`描述这个插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 修改`AWS PaaS平台 > 安全处理机制(SecurityProcessorId)`参数值为步骤2中注册名
  4. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

**插件中使用JSON组件是FastJSON，开发中注意包的引用**

### AbstractSecurityProcessor抽象类

开发者可实现这个抽象类完成安全处理机制开发。

> com.actionsoft.bpms.commons.security.processor.AbstractSecurityProcessor
    
    
    public abstract class AbstractSecurityProcessor {
    
        /**
         * 判断安全处理器是否可用
         *
         * @param params
         * @return
         */
        public boolean isAvailable(Map<String, Object> params);
    
    
        /**
         * 加密文本
         *
         * @param params content 需要加密的文本，password 平台默认加密方式的秘钥
         * @return 加密后的文本
         */
        public String encryptContent(Map<String, Object> params);
    
        /**
         * 解密文本
         *
         * @param params content 需要解密的文本，password 平台默认加密方式的秘钥
         * @return 解密后的文本
         */
        public String decryptContent(Map<String, Object> params);
    
    //---------------------这是分隔线以下两个方法为6.3.GA及以后版本请使用------------------------------
    
        /**
         * 返回解密包装流
         *
         * @param is 要解密的文件流
         * @param password 取自文件路经的一段信息
         * @return 解密后的文件流
         * @throws Exception
         * @since 6.3.GA及以后使用该接口
         */
        public InputStream decrypt(InputStream is, String password, Map<String, Object> params) throws Exception;
    
        /**
         * 返回加密包装流
         *
         * @param is 待加密的文件流
         * @param password 取自文件路经的一段信息
         * @return 加密后的文件流
         * @throws Exception
         * @since 6.3.GA及以后使用该接口
         */
        public InputStream encrypt(InputStream is, String password, Map<String, Object> params) throws Exception;
    
    //----------------这是分隔线以下两个方法为6.3.3、 6.3.2、 6.3.1版本请使用-----------------------
        /**
         * 加密文件
         * <p>6.3.GA以前的版本使用该方法</p>
         *
         * @param params path 文件路径  password 平台默认加密方式的秘钥
         * @return 文件大小
         */
        public Integer encryptFile(Map<String, Object> params);
    
        /**
         * 解密文件
         * <p>6.3.GA以前的版本使用该方法</p>
         *
         * @param params path 文件路径 context 文件的DCContext对象  password 平台默认加密方式的秘钥
         * @return 解密后的文件流
         */
        public InputStream decryptFile(Map<String, Object> params);
    
    
    }
    

上述列出的是接口方法，必须实现的

另外，如果有实际需求，需要重写两个方法：

  * public String calculateHashcode(Map params);//用于计算BO的字段防篡改的摘要信息
  * public String getPassword(String userId, String pwd);//用于调整登录密码的摘要算法调整

### 注册语法

由`SecurityProcessorProfile`类完成向AWS PaaS的注册。
    
    
    //注册安全处理机制
    
    /**
     * @param securityId 全局唯一名称
     * @param name 中文名称
     * @param clazz 实现类
     * @param desc 描述
     */
    list.add(new SecurityProcessorProfile("SM-SECURITY", "My安全处理机制", SMSecurityProcess.class.getName(), ""));
    

  * `clazz`-实现类路径，如`com.actionsoft.apps.formui.sample.FormUISampleImpl`