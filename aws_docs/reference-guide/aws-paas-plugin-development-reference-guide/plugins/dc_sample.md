# 文件上传下载示例 · AWS PaaS文档中心

# 文件上传、下载示例

这是常规的文件上传、下载处理过程，文件从客户端上传并存储至DC下。源码见`扩展插件概念验证`应用
    
    
    //本示例的文件存储目录
    %AWS-HOME%/doccenter/com.actionsoft.apps.poc.plugin/myfile/
    

### MyFileProcessor

> com.actionsoft.apps.poc.plugin.dc.MyFileProcessor

debug文件处理的每个事件，空跑方法
    
    
    package com.actionsoft.apps.poc.plugin.dc;
    
    import java.util.Map;
    
    import com.actionsoft.bpms.server.fs.AbstFileProcessor;
    import com.actionsoft.bpms.server.fs.DCContext;
    import com.actionsoft.bpms.server.fs.FileProcessorListener;
    import com.actionsoft.bpms.server.fs.dc.DCMessage;
    
    public class MyFileProcessor extends AbstFileProcessor implements FileProcessorListener {
    
        public boolean uploadReady(Map<String, Object> param) {
            DCContext context = (DCContext) param.get("DCContext");
            System.out.println("准备上传文件--" + context.getPath() + context.getFileName());
            return true;
        }
    
        public void uploadError(Map<String, Object> param) {
            DCContext context = (DCContext) param.get("DCContext");
            System.out.println("上传失败--" + context.getPath() + context.getFileName());
        }
    
        public void uploadBeforeEncrypt(Map<String, Object> param) {
            DCContext context = (DCContext) param.get("DCContext");
            System.out.println("已上传明文，准备加密前--" + context.getPath() + context.getFileName());
        }
    
        public void uploadSuccess(Map<String, Object> param) {
            DCContext context = (DCContext) param.get("DCContext");
            context.setDCMessage(DCMessage.OK, "");
            context.getDCMessage().addAttr("fileName", context.getFileName());
            context.getDCMessage().addAttr("url", context.getDownloadURL());
            System.out.println("上传成功--" + context.getPath() + context.getFileName());
        }
    
        public boolean downloadValidate(Map<String, Object> param) {
            DCContext context = (DCContext) param.get("DCContext");
            System.out.println("下载校验--" + context.getPath() + context.getFileName());
            return true;
        }
    
        public void downloadComplete(Map<String, Object> param) {
            DCContext context = (DCContext) param.get("DCContext");
            System.out.println("下载结束--" + context.getPath() + context.getFileName());
        }
    }
    

### 将myfile注册至PluginListener监听器

  * 声明根目录为`myfile`的文件处理器是MyFileProcessor
  * `isCommon`为false，即不共享给其他App（无特别场景，应设置为false）

    
    
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
            list.add(new DCPluginProfile("myfile", MyFileProcessor.class.getName(), "文件存放到该应用的myfile根目录下", false));
            return list;
        }
    }
    

### 前端JavaScript示例

调用AWS UI的upfile组件，完成文件的上传。有关该组件参数的详细用法参见《AWS MVC框架参考指南》相关章节。

> com.actionsoft.apps.poc.plugin/template/page/dc-sample1.htm

**上传组件的资源引用**
    
    
    <link rel="stylesheet" type="text/css" href="../commons/css/awsui.css"/>
    <script type="text/javascript" src="../commons/js/jquery/scripts/jquery.js"></script>
    <script type="text/javascript" src="../commons/js/awsui.js"></script>
    

**用JavaScript打开上传对话框**
    
    
    <script type="text/javascript">
    $(function(){
        //myUpfile对象绑定upfile组件
        $("#myUpfile").upfile({
            sid: "<#sid>", // 会话ID
            appId: "com.actionsoft.apps.poc.plugin", // 应用ID
            groupValue: "dir1", // DC大类，建议变量规则
            fileValue: "dir2", // DC小类，建议变量规则
            numLimit: "2", //最多一次允许上传几个，0(无限制)
            filesToFilter : [["Images (*.jpg; *.jpeg; *.gif; *.png; *.bmp)","*.jpg; *.jpeg; *.gif; *.png; *.bmp"]],
            repositoryName: "myfile", // 该应用申请的DC名
            extParam: "", //自定义业务参数，可以不定义，默认为空字符串
            done: function(e, data){
                //事件回调函数
                if (data['result']['data']['result'] == 'ok') {
                    $.simpleAlert('文件上传成功!');
                    // downloadURL
                    var url = data['result']['data']['data']['attrs']['url'];
                } else {
                    // 上传失败，打印出错误信息
                    $.simpleAlert(data['result']['data']['msg'], data['result']['data']['result']);
                }
            }
        });
    
    });
    </script>
    

**上传按钮的定义**
    
    
    <span id="myUpfile" class="button green" onclick="return false;">上传</span>
    

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`myfile`的DC配置，说明注册成功。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/dc-4.png)](<dc-4.png>)

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`DCSample1`，测试上传和下载功能。在AWS CONSOLE命令行，你会看到MyFileProcessor处理器debug的如下信息
    
    
    准备上传文件--../doccenter/com.actionsoft.apps.poc.plugin/myfile/dir1/dir2/xxx
    上传成功--../doccenter/com.actionsoft.apps.poc.plugin/myfile/dir1/dir2/xxx
    下载校验--../doccenter/com.actionsoft.apps.poc.plugin/myfile/dir1/dir2/xxx