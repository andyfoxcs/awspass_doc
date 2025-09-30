# 第三方云存储(6.3.3及以上版本) · AWS PaaS文档中心

# DC第三方对象存储服务(6.3.3+)

自6.3.3版本开始，系统重构了附件三方存储的实现机制，应用商店提供的S3 app通过该机制支持部分业务使用兼容S3协议的对象存储。相比前版本，三方存储机制主要改变如下：

  1. 注册DCPluginProfile时，设置storeAdapte参数为true指示该processor支持存储接管。S3 app默认只接管storeAdapte为true的附件。

  2. 支持存储接管的processor，开发人员需检查程序中附件读写的处理方法，需要调用父类（AbstFileProcessor）的read/write。

# 开发步骤

  1. 继承`AbstDCStore`抽象类，实现文件存储操作
  2. 用`DCStorePluginProfile`描述这个DC插件，注册到该应用的`PluginListener`类(见本文档[插件应用 > PluginListener](<../app_plugin/pluginlistener.html>)章节)
  3. 场景模拟，调试

    
    
    package com.actionsoft.apps.addons.dc.qiniu.plugins;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.DCStorePluginProfile;
    
    public class Plugins implements PluginListener {
        @Override
        public List<AWSPluginProfile> register(AppContext appContext) {
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            list.add(new DCStorePluginProfile("唯一标识", "XXX对象存储", "参数如果留空，则表示接管所有DC；如果指定AppId，则表示接管指定App的DC", S3Store.class.getName(), "存储描述信息", true/*是否支持推送到三方存储*/, false/*是否支持拉取三方存储的文件列表，上传直接读取三方存储的列表*/));
            return list;
        }
    }
    

# 抽象类、接口介绍

## com.actionsoft.bpms.server.fs.dc.cloud.DCStoreInterface接口
    
    
    package com.actionsoft.bpms.server.fs.dc.cloud;
    
    import java.io.InputStream;
    import java.util.Map;
    
    /**
     * 使用DCStore
     */
    public interface DCStoreInterface {
    
        /**
         * 将附件上传DC Store，需要关闭输入流
         *
         * @param is 输入流
         * @return 字节数
         */
        void write(InputStream is) throws Exception;
    
        /**
         * 获得附件输入流，需要关闭输入流
         *
         * @return 返回附件的InputStream
         */
        InputStream read() throws Exception;
    
        /**
         * 获取文件下载地址
         *
         * @param param DC相关参数
         * @return 返回云附件的下载地址
         */
        String getDownloadURL();
    
        /**
         * 拉取附件列表，支持pull时使用。额外参数通过getContext().get(XX)获取
         *
         * @return 通常返回拉取云端的附件列表的JSON结构
         */
        String pullStoreFile();
    
        /**
         * 如果有需要，解析pullStoreFile方法获取的内容生成一个Html页面展示。额外参数通过getContext().get(XX)获取
         *
         * @return 解析pullStoreFile方法获取的内容生成一个Html页面展示
         */
        String getStoreFileHtml();
    
        /**
         * 获取父目录下文件列表，返回json格式字符串，key为名称；value为对象，例如文件。push子类需要重载
         *
         * @return 通常返回附件列表的JSON结构
         */
        Map<String, Object> list();
    
        /**
         * 删除当前DC附件。push子类需要重载
         *
         * @return 是否删除附件标志
         */
        boolean delete();
    
        /**
         * 删除list的value对象。push子类需要重载
         *
         * @param o
         * @return
         */
        boolean delete(Object o);
    
        /**
         * 删除父目录下附件。push子类需要重载
         *
         */
        void deleteParent();
    }
    

## com.actionsoft.bpms.server.fs.dc.cloud.AbstDCStore抽象类
    
    
    public abstract class AbstDCStore implements DCStoreInterface {
    
        protected DCContext context;
    
        protected long getLastModified() {
            return System.currentTimeMillis();
        }
    
        public void readTo(OutputStream out) throws Exception {
            InputStream in = read();
            UtilIO.copyAndCloseInput(in, out);
            out.flush();
        }
    
        /**
         * 获取父目录下文件列表，返回json格式字符串，key为名称；value为对象，例如文件
         *
         * @return 通常返回附件列表的JSON结构
         */
        public Map<String, Object> list() {
            throw new UnsupportedOperationException();
        }
    
        /**
         * 删除当前DC附件
         *
         * @return 是否删除附件标志
         */
        public boolean delete() {
            throw new UnsupportedOperationException();
        }
    
        /**
         * 删除list的value对象
         *
         * @param o
         * @return
         */
        public boolean delete(Object o) {
            throw new UnsupportedOperationException();
        }
    
        /**
         * 删除父目录下附件
         *
         */
        public void deleteParent() {
            throw new UnsupportedOperationException();
        }
    
        /**
         * 探测是否附件存在
         *
         * @return 存在标志
         */
        public boolean exists() {
            return false;
        }
    
    public String getDownloadURL() {
            DCContext dc = getContext();
            StringBuilder sb = new StringBuilder();
            if (UtilString.isEmpty(dc.getContentTokenId())) {
            sb.append("./df?groupValue=");
                sb.append(UtilURL.URLEncode(dc.getGroupValue()));
                sb.append("&fileValue=");
                sb.append(UtilURL.URLEncode(dc.getFileValue()));
                sb.append("&sid=");
                if (dc.getSession() != null) {
                    sb.append(dc.getSession().getSessionId());
                }
                sb.append("&repositoryName=");
                sb.append(UtilURL.URLEncode(dc.getRepositoryName()));
                sb.append("&appId=");
                sb.append(UtilURL.URLEncode(dc.getAppId()));
                sb.append("&attachment=true");
                if (dc.getFileNameShow() != null && !"".equals(dc.getFileNameShow())) {
                    sb.append("&fileNameShow=" + UtilURL.URLEncode(dc.getFileNameShow()));
                }
                sb.append("&fileName=");
                sb.append(UtilURL.URLEncode(dc.getFileName()));
                sb.append("&lastModified=");
                sb.append(getLastModified());
            } else {
                sb.append("./df?contentTokenId=");
                sb.append(UtilURL.URLEncode(dc.getContentTokenId()));
                sb.append("&repositoryName=");
                sb.append(UtilURL.URLEncode(dc.getRepositoryName()));
                sb.append("&appId=");
                sb.append(UtilURL.URLEncode(dc.getAppId()));
                sb.append("&attachment=true");
                if (dc.getFileNameShow() != null && !"".equals(dc.getFileNameShow())) {
                    sb.append("&fileNameShow=" + UtilURL.URLEncode(dc.getFileNameShow()));
                }
                sb.append("&fileName=");
                sb.append(UtilURL.URLEncode(dc.getFileName()));
                sb.append("&lastModified=");
                sb.append(getLastModified());
            }
            return sb.toString();
        }
    
        /**
         * 默认空实现，有需要可重写
         *
         * @param param DC相关参数
         * @return
         */
        @Override
        public String pullStoreFile() {
            return "";
        }
    
        /**
         * 默认空实现，有需要可重写
         *
         * @param param DC相关参数
         * @return
         */
        @Override
        public String getStoreFileHtml() {
            return "";
        }
    
        /**
         * 设置DC上下文
         */
        public void setContext(DCContext dcContext) {
            this.context = dcContext;
        }
    
        public DCContext getContext() {
            return context;
        }
    
    }
    

# 具体示例
    
    
    package com.actionsoft.apps.addons.dc.s3.impl;
    
    import java.io.ByteArrayInputStream;
    import java.io.FileInputStream;
    import java.io.InputStream;
    import java.net.URISyntaxException;
    import java.util.ArrayList;
    import java.util.Calendar;
    import java.util.HashSet;
    import java.util.List;
    import java.util.Map;
    import java.util.Set;
    
    import org.apache.commons.beanutils.BeanUtils;
    
    import com.actionsoft.apps.addons.dc.s3.constant.S3Constant;
    import com.actionsoft.apps.resource.plugin.profile.DCPluginProfile;
    import com.actionsoft.bpms.commons.formfile.model.delegate.FormFile;
    import com.actionsoft.bpms.commons.security.processor.SecurityProcessorHelper;
    import com.actionsoft.bpms.server.fs.DCContext;
    import com.actionsoft.bpms.server.fs.dc.DCConst;
    import com.actionsoft.bpms.server.fs.dc.DCUtil;
    import com.actionsoft.bpms.server.fs.dc.cloud.AbstDCStore;
    import com.actionsoft.bpms.util.DBSql;
    import com.actionsoft.bpms.util.UtilString;
    import com.actionsoft.exception.AWSException;
    import com.actionsoft.sdk.local.SDK;
    import com.alibaba.fastjson.JSONObject;
    import com.amazonaws.ClientConfiguration;
    import com.amazonaws.auth.AWSStaticCredentialsProvider;
    import com.amazonaws.auth.BasicAWSCredentials;
    import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;
    import com.amazonaws.services.s3.AmazonS3;
    import com.amazonaws.services.s3.AmazonS3ClientBuilder;
    import com.amazonaws.services.s3.model.DeleteObjectsRequest;
    import com.amazonaws.services.s3.model.ListObjectsV2Result;
    import com.amazonaws.services.s3.model.ObjectMetadata;
    import com.amazonaws.services.s3.model.S3Object;
    import com.amazonaws.services.s3.model.S3ObjectSummary;
    
    public class S3Store extends AbstDCStore {
    
        public InputStream read() throws Exception {
            String[] ifo = getBucketAndKey();
            AmazonS3 s3 = getClient();
            S3Object o = s3.getObject(ifo[0], ifo[1]);
            InputStream is = o.getObjectContent();
            if (isEncrypt()) {
                is = SecurityProcessorHelper.decrypt(is, getPwd());
            }
            return is;
        }
    
        public void write(InputStream is) throws Exception {
            ObjectMetadata mt = new ObjectMetadata();
            String strlen = getContext().getFileLength();
            if (!UtilString.isEmpty(strlen) && (!isEncrypt() || !doEncrypt)) {
                mt.setContentLength(Integer.parseInt(strlen));
            } else if ((is instanceof ByteArrayInputStream) || (is instanceof FileInputStream)) {
                mt.setContentLength(is.available());
            }
    
            String[] ifo = getBucketAndKey();
            InputStream tp = is;
            if (isEncrypt()) {
                tp = SecurityProcessorHelper.encrypt(is, getPwd());
            }
            AmazonS3 s3 = getClient();
            s3.putObject(ifo[0], ifo[1], tp, mt);
        }
    
        public void deleteParent() {
            String[] tt = getBucketAndKeyParent();
            String[] xx = listKeys(tt);
            if (xx != null && xx.length > 0) {
                DeleteObjectsRequest dor = new DeleteObjectsRequest(tt[0]);
                dor.withKeys(xx);
                AmazonS3 s3 = getClient();
                s3.deleteObjects(dor);
            }
        }
    
        public boolean delete(Object key) {
            AmazonS3 s3 = getClient();
            String[] ifo = getBucketAndKey();
            s3.deleteObject(ifo[0], ifo[1]);
            return true;
        }
    
        private String[] listKeys(String[] tt) {
            AmazonS3 s3 = getClient();
            ListObjectsV2Result lr = s3.listObjectsV2(tt[0], tt[1]);
            List<String> ff = new ArrayList<String>();
            for (S3ObjectSummary objectSummary : lr.getObjectSummaries()) {
                ff.add(objectSummary.getKey());
            }
            return ff.toArray(new String[0]);
        }
    
        public Map<String, Object> list() {
            String[] tt = getBucketAndKeyParent();
            AmazonS3 s3 = getClient();
            ListObjectsV2Result lr = s3.listObjectsV2(tt[0], tt[1]);
            JSONObject jo = new JSONObject();
            for (S3ObjectSummary objectSummary : lr.getObjectSummaries()) {
                String[] split = objectSummary.getKey().split("\\/");
                String fileName = split[split.length - 1];
                jo.put(fileName, objectSummary.getKey());
            }
            return jo;
        }
    
        public boolean exists() {
            String[] ifo = getBucketAndKey();
            if (ifo == null) {
                return false;
            }
            AmazonS3 s3 = getClient();
            return s3.doesObjectExist(ifo[0], ifo[1]);
        }
    
        public boolean delete() {
            String[] ifo = getBucketAndKey();
            AmazonS3 s3 = getClient();
            try {
                s3.deleteObject(ifo[0], ifo[1]);
                return true;
            } catch (Exception ex) {
                System.err.println(ex);
            }
            return false;
        }
    
        public String getDownloadURL() {
            if (downloadS3URL && !DCConst.REPOSITORY_PHOTO.equals(getContext().getRepositoryName())) {
                String[] ifo = getBucketAndKey();
                Calendar c = Calendar.getInstance();
                c.add(Calendar.MINUTE, expireMinutes);
                AmazonS3 s3 = getClient();
                String url = s3.generatePresignedUrl(ifo[0], ifo[1], c.getTime()).toExternalForm();
                return url;
            }
    
            return super.getDownloadURL();
        }
    
        public boolean isIgnore() {
            DCContext context = getContext();
            Boolean b = isRuleIgnore(context.getRepositoryName());
            if (b != null) {
                return b;
            }
            if (buildinSupport(context.getRepositoryName())) {
                return false;
            }
            DCPluginProfile pf = context.getDCProfile();
            if (pf != null && pf.getStoreAdapte() != null && pf.getStoreAdapte()) {
                return false;
            }
            return true;
        }
    
    }