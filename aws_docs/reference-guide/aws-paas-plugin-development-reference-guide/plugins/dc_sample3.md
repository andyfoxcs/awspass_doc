# 下载生成的临时文件示例 · AWS PaaS文档中心

# 下载生成的临时文件示例

  * 开发`tmp`DC处理器，为该应用存放临时文件（如上节你已完成，不再重复）
  * 用程序生成一个文件并下载，下载完毕后删除这个临时文件

源码见`扩展插件概念验证`应用
    
    
    //本示例的文件存储目录
    %AWS-HOME%/doccenter/com.actionsoft.apps.poc.plugin/tmp/
    

### TmpFileProcessor

> com.actionsoft.apps.poc.plugin.dc.TmpFileProcessor
    
    
    package com.actionsoft.apps.poc.plugin.dc;
    
    import java.util.Map;
    
    import com.actionsoft.bpms.server.fs.AbstFileProcessor;
    import com.actionsoft.bpms.server.fs.DCContext;
    import com.actionsoft.bpms.server.fs.FileProcessorListener;
    import com.actionsoft.bpms.server.fs.dc.DCMessage;
    import com.actionsoft.bpms.util.UtilFile;
    
    public class TmpFileProcessor extends AbstFileProcessor implements FileProcessorListener {
    
        public void downloadComplete(Map<String, Object> param) {
            DCContext context = (DCContext) param.get("DCContext");
            if (context.getGroupValue().equals("crm") && context.getFileValue().equals("auto-report")) {
                // 删除这个临时文件
                new UtilFile(context.getFilePath()).delete();
            }
        }
    }
    

### 生成临时文件

> com.actionsoft.apps.poc.plugin.web.SampleWeb#getDCSample3Home
    
    
    public String getDCSample3Home() {
        long time = System.currentTimeMillis();
        // 生成一个临时文件，供用户下载
        String appId = "com.actionsoft.apps.poc.plugin";
        String repositoryName = "tmp";
        String groupValue = "crm";
        String fileValue = "auto-report";
        String fileName = time + ".txt";
        DCPluginProfile dcProfile = SDK.getDCAPI().getDCProfile(appId, repositoryName);
        DCContext dcContext = new DCContext(getContext(), dcProfile, appId, groupValue, fileValue, fileName);
        File dirFile = new File(dcContext.getPath());
        File tmpFile = new File(dcContext.getFilePath());
        // 模拟处理，返回一段文字
        String data = "Hello AWS PaaS! currentTimeMillis:" + time;
        InputStream in = null;
        try {
            if (tmpFile.exists()) {
                tmpFile.delete();
                tmpFile.createNewFile();
            } else {
                if (!dirFile.exists()) {
                    dirFile.mkdirs();
                }
                tmpFile.createNewFile();
            }
            in = new ByteArrayInputStream(data.getBytes());
            boolean isWrited = SDK.getDCAPI().write(in, dcContext);
            if (!isWrited) {
                throw new AWSException("Write Error!");
            }
        } catch (Exception e) {
            throw new AWSException(e);
        } finally {
            try {
                if (in != null)
                    in.close();
            } catch (Exception e) {
            }
        }
        Map<String, Object> macroLibraries = new LinkedHashMap<String, Object>();
        macroLibraries.put("sid", getContext().getSessionId());
        macroLibraries.put("tip", time);
        macroLibraries.put("url", dcContext.getDownloadURL());
        return HtmlPageTemplate.merge("com.actionsoft.apps.poc.plugin", "dc-sample3.htm", macroLibraries);
    }
    

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`DCSample3`，点击下载按钮得到如下相似内容的.txt文件
    
    
    Hello AWS PaaS! currentTimeMillis:1416735361470