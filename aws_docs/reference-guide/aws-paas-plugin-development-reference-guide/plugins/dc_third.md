# 第三方云存储 · AWS PaaS文档中心

# DC第三方对象存储服务

**注：该章节内容仅适用于6.3.2及以前版本。如果您的AWS PaaS平台已升级至后续版本，请直接阅读下一章节。**

对于文件存储密集的应用场景，用户可能会产生大量的附件文件，积累的文件达数百甚至T级规模。第三方对象存储服务是为运行在PaaS上的各种应用，提供更灵活的文件读写服务，允许将某个应用场景或全部DC（文档存储中心）直接转移到第三方云存储服务。

# 开发步骤

  1. 继承`AbstFileProcessor`抽象类，实现对该DC事件的处理器
  2. 用`CloudDCPluginProfile`描述这个DC插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

    
    
    package com.actionsoft.apps.addons.dc.qiniu.plugins;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.CloudDCPluginProfile;
    
    public class Plugins implements PluginListener {
        @Override
        public List<AWSPluginProfile> register(AppContext appContext) {
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            list.add(new CloudDCPluginProfile("唯一标识", "XXX对象存储", "参数如果留空，则表示接管所有DC；如果指定AppId，则表示接管指定App的DC", CloudFile.class.getName(), "存储描述信息", true/*是否支持推送到三方存储*/, false/*是否支持拉取三方存储的文件列表，上传直接读取三方存储的列表*/));
            return list;
        }
    }
    

# 抽象类、接口介绍

## com.actionsoft.bpms.server.fs.dc.cloud.CloudFileProcessorInterface接口
    
    
    package com.actionsoft.bpms.server.fs.dc.cloud;
    
    import java.io.InputStream;
    import java.util.Map;
    
    public interface CloudFileProcessorInterface {
        /**
         * 将本地上传的文件推送至云端
         *
         * @param param DC相关参数
         * @return 返回推送的结果
         */
        public String pushCloudFile(Map<String, Object> param);
    
        /**
         * 拉取云端文件
         *
         * @param param DC相关参数
         * @return 通常返回拉取云端的附件列表的JSON结构
         */
        public String pullCloudFile(Map<String, Object> param);
    
        /**
         * 如果有需要，解析pullCloudFile方法获取的内容生成一个Html页面展示
         *
         * @param param DC相关参数
         * @return 解析pullCloudFile方法获取的内容生成一个Html页面展示
         */
        public String getCloudFileHtml(Map<String, Object> param);
    
        /**
         * 下载一个云文件
         *
         * @param param DC相关参数
         * @return 返回云附件的InputStream
         */
        public InputStream downloadCloudFile(Map<String, Object> param);
    
        /**
         * 获取云文件下载地址
         *
         * @param param DC相关参数
         * @return 返回云附件的下载地址
         */
        public String getDownloadURL(Map<String, Object> param);
    }
    

## com.actionsoft.bpms.server.fs.dc.cloud.AbstractCloudFileProcessor抽象类
    
    
    package com.actionsoft.bpms.server.fs.dc.cloud;
    
    import java.io.InputStream;
    import java.util.Map;
    
    /**
     * 第三方云存储抽象类处理类
     * <p>
     * @author zhanghf
     */
    public abstract class AbstractCloudFileProcessor implements CloudFileProcessorInterface {
    
        /**
         * 默认空实现，有需要可重写
         *
         * @param param DC相关参数
         * @return
         */
        @Override
        public String pullCloudFile(Map<String, Object> param) {
            return "";
        }
    
        /**
         * 默认空实现，有需要可重写
         * @param param DC相关参数
         * @return
         */
        @Override
        public String getCloudFileHtml(Map<String, Object> param) {
            return "";
        }
    
        /*
         * <p>以下方法说明参考<a href='https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/dc_dev.html'>AbstFileProcessor抽象类</a></p>
         * <b>注意返回值会有所不同</b>
         */
    
        /**
         * <p>为了避免过于复杂的处理，影响平台现有DC的机制，可以有选择性的处理平台的DC根目录中前缀是<b>!</b>的DC</p>
         *
         * @param param DC相关参数
         * @return 如果干预某类DC，则处理完返回，按照业务逻辑返回true/false；如果不干预，则返回null，这样则使用平台自身的处理机制
         * @see FileProcessorListener#uploadReady
         */
        public Boolean uploadReady(Map<String, Object> param) {
            //默认情况返回null，这样默认其他的自定义DC，则使用平台自身的处理机制
            return null;
        }
    
        /**
         * <p>为了避免过于复杂的处理，影响平台现有DC的机制，可以有选择性的处理平台的DC根目录中前缀是<b>!</b>的DC</p>
         *
         * @param param DC相关参数
         * @return 如果干预某类DC，则处理完返回，按照业务逻辑返回true；如果不干预，则返回false，这样则使用平台自身的处理机制
         * @see FileProcessorListener#uploadBeforeEncrypt
         */
        public boolean uploadBeforeEncrypt(Map<String, Object> param) {
            return false;
        }
    
        /**
         * 为了避免过于复杂的处理，影响平台现有DC的机制，可以有选择性的处理平台的DC根目录中前缀是<b>!</b>的DC
         *
         * @param param DC相关参数
         * @return 如果干预某类DC，则处理完返回，按照业务逻辑返回true；如果不干预，则返回false，这样则使用平台自身的处理机制
         * @see FileProcessorListener#uploadSuccess
         */
        public boolean uploadSuccess(Map<String, Object> param) {
            return false;
        }
    
        /**
         * 为了避免过于复杂的处理，影响平台现有DC的机制，可以有选择性的处理平台的DC根目录中前缀是<b>!</b>的DC
         *
         * @param param DC相关参数
         * @return 如果干预某类DC，则处理完返回，按照业务逻辑返回true；如果不干预，则返回false，这样则使用平台自身的处理机制
         * @see FileProcessorListener#uploadError
         */
        public boolean uploadError(Map<String, Object> param) {
            return false;
        }
    
        /**
         * 为了避免过于复杂的处理，影响平台现有DC的机制，可以有选择性的处理平台的DC根目录中前缀是<b>!</b>的DC
         *
         * @param param DC相关参数
         * @return 如果干预某类DC，则处理完返回，按照业务逻辑返回true/false；如果不干预，则返回null，这样则使用平台自身的处理机制
         * @see FileProcessorListener#downloadValidate
         */
        public Boolean downloadValidate(Map<String, Object> param) {
            return null;
        }
    
        /**
         * 为了避免过于复杂的处理，影响平台现有DC的机制，可以有选择性的处理平台的DC根目录中前缀是<b>!</b>的DC
         *
         * @param param DC相关参数
         * @return 如果干预某类DC，则处理完返回，按照业务逻辑返回InputStream；如果不干预，则返回null，这样则使用平台自身的处理机制
         * @see FileProcessorListener#downloadContent
         */
        public InputStream downloadContent(Map<String, Object> param) {
            return null;
        }
    
        /**
         * 为了避免过于复杂的处理，影响平台现有DC的机制，可以有选择性的处理平台的DC根目录中前缀是<b>!</b>的DC
         *
         * @param param
         * @return 如果干预某类DC，则处理完返回，按照业务逻辑返回true；如果不干预，则返回false，这样则使用平台自身的处理机制
         * @see FileProcessorListener#downloadComplete
         */
        public boolean downloadComplete(Map<String, Object> param) {
            return false;
        }
    }
    

# 具体示例
    
    
    package com.actionsoft.apps.addons.dc.qiniu.plugins;
    
    import java.io.InputStream;
    import java.util.Map;
    
    import com.actionsoft.apps.addons.dc.qiniu.constant.QNConstant;
    import com.actionsoft.apps.addons.dc.qiniu.model.CloudFilePutRet;
    import com.actionsoft.bpms.server.fs.dc.cloud.AbstractCloudFileProcessor;
    import com.actionsoft.sdk.local.SDK;
    import com.alibaba.fastjson.JSONObject;
    import com.google.gson.Gson;
    import com.qiniu.common.QiniuException;
    import com.qiniu.common.Zone;
    import com.qiniu.http.Response;
    import com.qiniu.storage.Configuration;
    import com.qiniu.storage.UploadManager;
    import com.qiniu.util.Auth;
    import com.qiniu.util.StringMap;
    
    public class CloudFile extends AbstractCloudFileProcessor {
        @Override
        public String pushCloudFile(Map<String, Object> param) {
            ResponseObject result = ResponseObject.newOkResponse();
            // 文件全路径的MD5摘要，开发者可使用该路径作为云存储的一个路径
            String pathMD5 = (String) param.get("PathMD5");
            // 文件的输入流
            InputStream in = (InputStream) param.get("data");
            // 存储后的结果，一个标准的ResponseObject对象封装，处理成功封装为OK的状态
            return result.toString();
        }
    
        @Override
        public InputStream downloadCloudFile(Map<String, Object> param) {
            return null;
        }
    
        @Override
        public String getDownloadURL(Map<String, Object> param) {
            // 返回文件的访问地址
            String finalUrl = "";
            return finalUrl;
        }
    
        /**
         * 为了避免过于复杂的处理，影响平台现有DC的机制，可以有选择性的处理平台的DC根目录中前缀是<b>!</b>的DC
         *
         * @param param
         * @return 如果干预某类DC，则处理完返回，按照业务逻辑返回true/false；如果不干预，则返回null，这样则使用平台自身的处理机制
         */
        public Boolean uploadReady(Map<String, Object> param) {
            DCContext dcContext = (DCContext) param.get("DCContext");
            if (DCConst.REPOSITORY_UI_FILE.equals(dcContext.getRepositoryName())) {
                // 举例如果需要接管平台的UI组件中“附件”的文件
                // ...
                // 自行处理后需要返回true
                return true;
            }
            //默认情况返回null，这样默认其他的自定义DC，则使用平台自身的处理机制
            return null;
        }
    
    }