# 接管输入输出流示例 · AWS PaaS文档中心

# 接管输入输出流示例

使用`!`命名的`repositoryName`可以接管上传或下载的流操作

  * uploadReady - 读来自客户上传的输入流(InputStream)
  * downloadContent - 返回一个输入流作为客户下载的内容

> 此时`repositoryName`是个虚拟不存在的目录

源码见`扩展插件概念验证`应用

### StreamFileProcessor

> com.actionsoft.apps.poc.plugin.dc.StreamFileProcessor
    
    
    package com.actionsoft.apps.poc.plugin.dc;
    
    import java.io.ByteArrayInputStream;
    import java.io.ByteArrayOutputStream;
    import java.io.InputStream;
    import java.util.Map;
    
    import com.actionsoft.bpms.server.fs.AbstFileProcessor;
    import com.actionsoft.bpms.server.fs.DCContext;
    import com.actionsoft.bpms.server.fs.FileProcessorListener;
    import com.actionsoft.bpms.server.fs.dc.DCMessage;
    import com.actionsoft.bpms.util.UtilIO;
    
    public class StreamFileProcessor extends AbstFileProcessor implements FileProcessorListener {
    
        public boolean uploadReady(Map<String, Object> param) {
            DCContext context = (DCContext) param.get("DCContext");
            InputStream in = (InputStream) param.get("data");
            // 如果你的应用需要多类自定义处理的场景，可通过groupValue/fileValue变量做识别
            if (context.getGroupValue().equals("hr") && context.getFileValue().equals("action1")) {
                try {
                    // 模拟处理，读来自用户上传的文件，什么都不做
                    ByteArrayOutputStream bytes = new ByteArrayOutputStream();
                    UtilIO.copy(in, bytes);
                    context.setDCMessage(DCMessage.OK, "fileName:" + context.getFileName() + ",byte size:" + bytes.size());
                    return true;
                } catch (Exception e) {
                    context.setDCMessage(DCMessage.ERROR, e.toString());
                    return false;
                }
            } else {
                context.setDCMessage(DCMessage.WARNING, "处理器无法识别的类型。groupValue:" + context.getGroupValue() + ",fileValue:" + context.getFileValue());
                return false;
            }
        }
    
        public InputStream downloadContent(Map<String, Object> param) throws Exception {
            DCContext context = (DCContext) param.get("DCContext");
            // 如果你的应用需要多类自定义处理的场景，可通过groupValue/fileValue变量做识别
            if (context.getGroupValue().equals("hr") && context.getFileValue().equals("action1")) {
                // 模拟读文件，将流返回给客户端
                ByteArrayInputStream bytes = new ByteArrayInputStream("hi, AWS PaaS!".getBytes());
                return bytes;
            } else {
                context.setDCMessage(DCMessage.WARNING, "处理器无法识别的类型。groupValue:" + context.getGroupValue() + ",fileValue:" + context.getFileValue());
                return null;
            }
        }
    }
    

### 将!myStream注册至PluginListener监听器

  * 声明根目录为`!myStream`的文件处理器是StreamFileProcessor
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
            list.add(new DCPluginProfile("!myStream", StreamFileProcessor.class.getName(), "由程序接管写文件流和读文件流，模拟处理过程", false));
    
            return list;
        }
    }
    

### 前端JavaScript示例

调用AWS UI的upfile组件，完成文件的上传。有关该组件参数的详细用法参见《AWS MVC框架参考指南》相关章节。

> com.actionsoft.apps.poc.plugin/template/page/dc-sample4.htm

**上传组件的资源引用**
    
    
    <link rel="stylesheet" type="text/css" href="../commons/css/awsui.css"/>
    <script type="text/javascript" src="../commons/js/jquery/scripts/jquery.js"></script>
    <script type="text/javascript" src="../commons/js/awsui.js"></script>
    

**用JavaScript打开上传对话框**
    
    
    <script type="text/javascript">
    $(function(){
        //myUpfile对象绑定upfile组件
        $("#myStreamUpfile").upfile({
            sid: "<#sid>", // 会话ID
            appId: "com.actionsoft.apps.poc.plugin", // 应用ID
            groupValue: "hr", // DC使用!前缀时，可以根据自己程序需要提供变量
            fileValue: "action1", // DC使用!前缀时，可以根据自己程序需要提供变量
            numLimit: "1", //最多一次允许上传几个，0(无限制)
            repositoryName: "!myStream", // 该应用申请的DC名
            extParam: "", //自定义业务参数，可以不定义，默认为空字符串
            done: function(e, data){
                //事件回调函数
                if (data['result']['data']['result'] == 'ok') {
                    $.simpleAlert(data['result']['data']['msg']);
                } else {
                    // 上传失败，打印出错误信息
                    $.simpleAlert(data['result']['data']['msg'], data['result']['data']['result']);
                }
            }
        });
    
    });
    </script>
    

**上传按钮的定义**
    
    
    <span id="myStreamUpfile" class="button green" onclick="return false;">上传</span>
    

**用JavaScript下载文件**
    
    
        window.location="./df?sid=<#sid>&repositoryName=!myStream&groupValue=hr&fileValue=action1&appId=com.actionsoft.apps.poc.plugin&fileName=abc.txt";
    

### 验证

  1. 进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`!myStream`的DC配置，说明注册成功。
  2. 进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`DCSample4`，测试上传操作，你会看到处理器返回的类似信息
         
         fileName:xxx,byte size:xxx
         

  3. 测试下载操作，得到一个名为`abc.txt`的附件，内容如下
         
         hi, AWS PaaS!