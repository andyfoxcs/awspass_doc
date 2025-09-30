# 上传文件 | AWS 移动开发参考指南

### 上传文件

AWS平台通过[DC（Doc Center）](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/dc.html>)为每个应用存取和管理非结构文件。AWS DC是一个有着严格规范的结构化存储体系，能够根据DC根目录的命名规则确定深度和安全性，并为每个App分配私有的存储空间。 AWS对文件上传封装了一个公用的组件，能够满足移动端浏览器的文件上传功能。

`upfile`是AWS UI封装的通用文件上传组件，采用双核技术（IE8/IE9提供Flash模式，对支持HTML5的浏览器采用无插件模式）实现批量文件上传、文件类型过滤、文件大小控制和上传进度控制，对各类浏览器提供了较好的体验支持。

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
            done: function(e, data){
                //事件回调函数
                //上传完成后，开始调用导入代码
                if (awsui.ajax.ok(data.result.data)) {//判断请求是否执行成功
                    //可以调用公共方法处理提示信息
                    awsui.ajax.alert(data.result.data);
                    //或者自行处理提示信息
                    //$.simpleAlert('文件上传成功!');
                    // downloadURL
                    var url = data.result.data.data.attrs.url;
                    //如果定义了其他返回的属性，也需要使用data.result.data.data.attrs调用
                } else {
                    // 上传失败，提示出错误信息
                    awsui.ajax.alert(data.result.data);
                }
            }
        });
    
    });
    </script>
    

**上传按钮的定义**
    
    
    <span id="myUpfile" class="button green" onclick="return false;">上传</span>
    

有关文件上传的后端处理， 参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/aws_mvc/upfile.html>)