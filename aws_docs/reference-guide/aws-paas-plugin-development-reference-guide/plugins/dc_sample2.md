# 处理上传的临时文件示例 · AWS PaaS文档中心

# 处理上传的临时文件示例

  * 开发`tmp`DC处理器，为该应用存放临时文件
  * 处理用户上传的文件，操作完毕后删除这个临时文件

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
    
        public void uploadSuccess(Map<String, Object> param) {
            DCContext context = (DCContext) param.get("DCContext");
            UtilFile tmpFile = new UtilFile(context.getFilePath());
            // 模拟处理过程，比如用POI处理Excel文件
            byte[] data = tmpFile.readBytes();
            context.setDCMessage(DCMessage.OK, "This file size : " + data.length + " bytes.");
            // 删除
            tmpFile.delete();
        }
    }
    

### 将tmp注册至PluginListener监听器

  * 声明根目录为`tmp`的文件处理器是TmpFileProcessor
  * `isCommon`为false，即不共享给其他App（尤其各种tmp类DC，应设置为false）

    
    
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
            list.add(new DCPluginProfile("tmp", TmpFileProcessor.class.getName(), "存放用户上传的临时文件，模拟处理过程", false));
            return list;
        }
    }
    

### 前端JavaScript示例

调用AWS UI的upfile组件，完成文件的上传。有关该组件参数的详细用法参见《AWS MVC框架参考指南》相关章节。

> com.actionsoft.apps.poc.plugin/template/page/dc-sample2.htm

**上传组件的资源引用**
    
    
    <link rel="stylesheet" type="text/css" href="../commons/css/awsui.css"/>
    <script type="text/javascript" src="../commons/js/jquery/scripts/jquery.js"></script>
    <script type="text/javascript" src="../commons/js/awsui.js"></script>
    

**用JavaScript打开上传对话框**
    
    
    <script type="text/javascript">
    $(function(){
        //tmpUpfile对象绑定upfile组件
        $("#tmpUpfile").upfile({
            sid: "<#sid>", // 会话ID
            appId: "com.actionsoft.apps.poc.plugin", // 应用ID
            groupValue: "crm", // DC大类，建议变量规则
            fileValue: "customer", // DC小类，建议变量规则
            numLimit: "1", //最多一次允许上传几个，0(无限制)
            repositoryName: "tmp", // 该应用申请的DC名
            extParam: "", //自定义业务参数，可以不定义，默认为空字符串
            done: function(e, data){
                //事件回调函数
                if (data['result']['data']['result'] == 'ok') {
                     // 检查处理的消息结果
                    var msg = data['result']['data']['msg'];
                     $.simpleAlert(msg);
                } else {
                    // 上传失败，打印出错误信息
                    $.simpleAlert(data['result']['data']['msg'], data['result']['data']['result']);
                }
            }
        });
    
    });
    </script>
    

**上传按钮的定义**
    
    
    <span id="tmpUpfile" class="button green" onclick="return false;">上传</span>
    

### 验证

  1. 进入`AWS CONSOLE > 应用管理`并打开你的应用，在`资源`中如出现`tmp`的DC配置，说明注册成功。
  2. 进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`DCSample2`，测试上传操作，你会看到处理器返回的类似信息
         
         This file size : 12345 bytes.