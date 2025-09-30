# 开发步骤 · AWS PaaS文档中心

# 开发步骤

  1. 继承`AbstFileProcessor`抽象类，实现对该DC事件的处理器
  2. 用`DCPluginProfile`描述这个DC插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

> 注意：本章节提供的相关接口说明，请以**aws-api-doc** 为主。

### AbstFileProcessor抽象类

开发者可继承这个类完成DC文件处理器的开发。由于抽象类`AbstFileProcessor`提供了默认实现，通常不需要做出任何处理。开发者可以根据业务需要重载相关事件。
    
    
    //DC文件处理事件空实现(父类)，开发者可以根据需要覆盖特定方法。如果不干预这些事件，开发者的实现类可以什么都不做
    public abstract class AbstFileProcessor implements FileProcessorListener{
        /**
         * 上传文件执行前准备事件，通常在这里先将文件名更新至业务表，或根据需要对文件名进行重命名
         *
         * @param param 取key=DCContext，value=DCContext的对象，获取操作DC上下文对象
         * @return 返回false阻止文件上传
         */
        public boolean uploadReady(Map<String, Object> param);
    
        /**
         * 上传的原始文件已保存到DC，如果该文件正文是需要加密的，在加密前触发，如果不需加密，该事件不触发。通常在这里可以读取文件原文，
         * 做全文检索的入库或其他操作
         *
         * @param param 取key=DCContext，value=DCContext的对象，获取操作DC上下文对象
         */
        public void uploadBeforeEncrypt(Map<String, Object> param);
    
        /**
         * 上传文件成功后补偿事件
         *
         * @param param 取key=DCContext，value=DCContext的对象，获取操作DC上下文对象
         * @return
         */
        public void uploadSuccess(Map<String, Object> param);
    
        /**
         * 上传文件失败后补偿事件。对应ready()，如在这里将附件名从业务表中移走
         *
         * @param param 取key=DCContext，value=DCContext的对象，获取操作DC上下文对象
         * @return
         */
        public void uploadError(Map<String, Object> param);
    
        /**
         * 下载文件前校验事件，通常可在这里做权限或其他校验，将校验不通过信息放入DCMessage
         *
         * @param param 取key=DCContext，value=DCContext的对象，获取操作DC上下文对象
         * @return 返回false阻止文件下载
         */
        public boolean downloadValidate(Map<String, Object> param);
    
        /**
         * repositoryName名前缀为!时触发，由Java代码提供的输入流，提供给下载请求
         *
         * @param param 取key=DCContext，value=DCContext的对象，获取操作DC上下文对象
         */
        public InputStream downloadContent(Map<String, Object> param) throws Exception;
    
        /**
         * 附件下载结束触发
         */
        public void downloadComplete(Map<String, Object> param);
    }
    

### 注册语法

由`DCPluginProfile`类完成向AWS PaaS的注册。
    
    
    //注册DC
    list.add(new DCPluginProfile(repositoryName, clazz, desc, isCommon));
    

  * `repositoryName`-`DC根目录`(文件仓库根目录名)，建议使用英文字母和数字命名(区分大小写)，不建议使用中文、怪字符和空格等
  * `clazz`-实现类路径，如`com.abc.crm.dc.MyFileProcessor`
  * `desc`-说明
  * `isCommon`-是否允许被其他应用访问(全局DC)。除非必要，建议为false。如果设置为true，`repositoryName`命名不允许与另外一个全局DC名称相同

**DC根目录命名规范**

  * 前缀是-，标准DC：DC会自动加/解密文件，对开发人员是透明的
  * 前缀是!，接管文件读/写流的DC：DC本身不再提供写文件或读文件操作。此时`repositoryName`是一个不存在的虚拟目录
  * 后缀是-，4级存储，`%gDeep%/%groupValue%/%fDeep%/%fileValue%/`

**开发建议**

  * 如改变上传的文件名可在文件处理器的`uploadReady()`，调用`DCContext.setFileName()`
  * 如上传后要继续处理，比如上传模版文件然后解析，那么可以在处理器的`uploadSuccess()`里直接进行，这是个回调设计
  * 对于临时文件处理，如上传、下载模版，建议使用`tmp`这个全局DC
  * 如果存储的文件可能会含有重要隐私信息，用-前缀声明DC根目录名
  * groupValue和fileValue命名设计很关键。如果存储规模较大groupValue和fileValue应用变量进行合理规划（如使用某对象Id、操作者账户）
  * 如果groupValue或fileValue可能超过数万个，必须用-后缀来四级存储，否则会超出文件系统的单一目录文件最大数

> `DC根目录`名一旦被生产环境使用，将不允许再修改

### 相关资源

  * com.actionsoft.sdk.local.api.DCAPI
  * com.actionsoft.bpms.server.fs.DCContext
  * com.actionsoft.bpms.util.UtilFile
  * com.actionsoft.bpms.util.UtilIO
  * com.actionsoft.sdk.local.api.BOAPI