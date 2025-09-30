# 上传文件 | AWS MVC框架参考指南

## 上传文件

AWS应用容器对每个应用各类资源提供了沙箱管理，对于文件读写提供了一套完善的`DC`(Doc Center)机制，文件必须通过DC处理器进行处理。AWS对文件上传封装了一个公用的组件，能够满足常用浏览器（IE8+, Firefox, Google Chrome, Safari、平板UC等）的文件上传功能。

### 服务端插件注册和声明

注册DCPluginProfile需要你声明`repositoryName`（存放文件的根目录名）和文件处理器（继承com.actionsoft.bpms.server.fs.AbstFileProcessor）。

>   * 有关`DC`开发详细内容，参见《AWS 插件扩展开发参考指南》
>   * 有关DC API操作（如读、写文件），参见**aws-api-doc** 提供的`DCAPI`
> 

### 客户端调用

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
    

> 上述客户端调用示例，也可从`AWS企业应用商店`安装`扩展插件概念验证`应用，所有源码在src目录下

![](https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/aws_mvc/plugin-app.png)

### 参数说明

  * 属性

Name | Type | Description | Default  
---|---|---|---  
sid(*-必须) | String | 会话ID  
appId(*-必须) | String | 应用ID  
repositoryName(*-必须) | String | DC插件定义  
groupValue(*-必须) | String | 文件大类  
fileValue(*-必须) | String | 文件小类  
filesToFilter | String | var filter = [["Images (_.jpg;_.jpeg; _.gif;_.png; _.bmp)","_.jpg; _.jpeg;_.gif; _.png;_.bmp"]]; | 不过滤，可上传所有文件  
sizeLimit | number | 文件大小限制 | 25*1024*1024(25M)  
numLimit | int | 上传个数限制 | 0(无限制)  
  
  * 事件

Name | Param | Description  
---|---|---  
add | e 事件;data(返回的数据) | 文件被添加到上传列表时触发，当返回false时，可阻止上传。  
例如： //data.files 为上传文件的数组   
add:function(e, data){   
//data.files 为上传文件的数组   
$.each(data.files, function(index, file) {   
// file.name 文件名称 file.size 文件大小 file.type 文件类型   
}) if(size==0){ //空文件不允许上传 return false;   
} }  
progress | e 事件;data(返回的数据) | 文件上传中触发  
done | e 事件;data(返回的数据) | 单个文件上传完毕后触发  
error | e 事件;data(返回的数据) | 单个文件上传失败后触发。  
可能是web服务器也可能是app服务器造成的失败  
complete | 文件成功上传结束后触发  
  
> 上面的`客户端调用`和`参数说明`适合6.4.GA之前的版本，6.4.GA及以后的版本用下面的

### 客户端调用

`awsui-upload-file`是AWSUI封装的通用文件上传组件，实现批量文件上传、文件类型过滤、文件大小控制和上传进度控制。

**上传组件引入AWSUI资源**
    
    
    import awsui from "../libraries/lib/awsui.es"; //注意awsui组件库根据情况指定路径
    import "../libraries/lib/awsui.css";
    

**在VUE中打开上传对话框**
    
    
    <awsui-upload-file
        :url="url"
        :files="uploadImgList"
        :fileCount="options.fileCount"
        :fileMaxSize="options.fileMaxSize"
        :fileTypeFormat="fileTypeFormat"
        :drag=true
        :accept="accept"
        @on-success="handleImgSuccess"
        @onExceed="handleExceed"
        @onError="handleError"
        @onProgress="handleProgress"
        :before-upload="beforeUpload"
    >
    <template #button>
      <awsui-button :class="{'up-file-btn': true, 'disabled': progressList.length > 0}">
        <i class="awsui-iconfont upload-icon">&#xf0f0;</i>{{$t("上传")}}
      </awsui-button>
    </template>
    </awsui-upload-file>
    

### 参数说明

  * URL属性格式 'uf?sid=&appId=&repositoryName=&groupValue=&fileValue='

  * URL属性具体说明

Name | Type | Description | Default  
---|---|---|---  
sid(*-必须) | String | 会话ID  
appId(*-必须) | String | 应用ID  
repositoryName(*-必须) | String | DC插件定义  
groupValue(*-必须) | String | 文件大类  
fileValue(*-必须) | String | 文件小类  
  
  * 其他属性

Name | Param | Description  
---|---|---  
url  | 上传文件的URL，参考上面`URL属性具体说明`  
files | 文件的列表  
fileCount | 文件个数限制  
fileMaxSize | 文件大小限制  
fileTypeFormat | 要支持上传的文件类型，文件扩展名，英文逗号分隔  
noFileTypeFormat | 不支持上传的文件类型，文件扩展名，英文逗号分隔  
drag | true | 是否支持拖拽上传  
accept | 要支持选择上传的文件类型，全部是 _._ ，或者使用英文逗号分隔扩展名  
disabled | 只读  
beforeUpload | file: any | 上传文件之前的钩子，参数为上传的文件， 若返回 false 或者返回 Promise 且被 reject，则停止上传。  
  
  * 事件

Name | Param | Description  
---|---|---  
on-success | response: any | 文件上传成功时的钩子  
on-exceed | files: File[], uploadList: any | 当超出限制时，执行的钩子函数  
on-error | response: any, uploadFile: any | 文件上传失败时的钩子  
on-progress | percentage: number, uploadFile: any | 文件上传中的钩子