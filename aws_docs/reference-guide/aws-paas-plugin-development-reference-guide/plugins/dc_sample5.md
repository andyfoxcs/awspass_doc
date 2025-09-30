# 自定义contentTokenId实现URL匿名下载 · AWS PaaS文档中心

# 自定义contentTokenId实现URL匿名下载

使用`!`命名的`repositoryName`可以接管上传或下载的流操作。默认必须提供有效的sid（会话），如果开发者希望实现匿名（非登录AWS系统）下载DC文件，可以在下载url中提供`contentTokenId`（自定义的安全令牌），自定义实现安全的文件流的处理。

> 适合匿名互联网用户通过URL直接获取该应用的文件资源。如网盘分享、外部网站的图片/文件资源动态获取场景

  * uploadReady - 读来自客户上传的输入流(InputStream)
  * downloadContent - 返回一个输入流作为客户下载的内容

> 此时`repositoryName`是个虚拟不存在的目录

源码见`扩展插件概念验证`应用

### TokenFileProcessor

> com.actionsoft.apps.poc.plugin.dc.TokenFileProcessor
    
    
    package com.actionsoft.apps.poc.plugin.dc;
    
    import java.io.ByteArrayInputStream;
    import java.io.InputStream;
    import java.util.Map;
    
    import com.actionsoft.bpms.server.fs.AbstFileProcessor;
    import com.actionsoft.bpms.server.fs.DCContext;
    import com.actionsoft.bpms.server.fs.FileProcessorListener;
    import com.actionsoft.bpms.server.fs.dc.DCMessage;
    import com.actionsoft.bpms.util.UtilString;
    import com.actionsoft.exception.AWSIllegalArgumentException;
    
    public class TokenFileProcessor extends AbstFileProcessor implements FileProcessorListener {
    
        public InputStream downloadContent(Map<String, Object> param) throws Exception {
            DCContext context = (DCContext) param.get("DCContext");
            String contentTokenId = context.getContentTokenId();
            if (UtilString.isEmpty(contentTokenId)) {
                throw new AWSIllegalArgumentException("contentTokenId", AWSIllegalArgumentException.EMPT);
            }
            // 根据contentTokenId做逻辑处理，此处为该应用的实现。
            // 如检查contentTokenId的有效性、反向查到对应的groupValue、fileValue，完成文件流的读取
            if (contentTokenId.equals("1234567890")) {
                System.out.println(context.getDownloadURL());
                // 模拟读文件，将流返回给客户端
                ByteArrayInputStream bytes = new ByteArrayInputStream(contentTokenId.getBytes());
                return bytes;
            } else {
                context.setDCMessage(DCMessage.WARNING, "无效的contentTokenId=" + contentTokenId);
                return null;
            }
        }
    }
    

### 将!myStream2注册至PluginListener监听器

  * 声明根目录为`!myStream2`的文件处理器是TokenFileProcessor
  * `isCommon`为false，即不共享给其他App

    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.at.MyLenExpression;
    import com.actionsoft.apps.poc.plugin.dc.MyFileProcessor;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.AtFormulaPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.DCPluginProfile;
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            // 注册DC
            list.add(new DCPluginProfile("!myStream2", TokenFileProcessor.class.getName(), "通过contentTokenId处理下载内容", false));
    
            return list;
        }
    }
    

### 前端JavaScript示例

> com.actionsoft.apps.poc.plugin/template/page/dc-sample5.htm

**用JavaScript下载文件**
    
    
        window.location="./df?repositoryName=!myStream2&contentTokenId=1234567890&appId=com.actionsoft.apps.poc.plugin&fileName=abcde.txt";
    

### 验证

  1. 进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`!myStream2`的DC配置，说明注册成功。
  2. 进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`DCSample5`，测试下载操作，得到一个名为`abcde.txt`的附件，内容如下
         
         1234567890