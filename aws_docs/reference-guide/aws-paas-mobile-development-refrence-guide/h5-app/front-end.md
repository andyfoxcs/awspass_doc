# 前端开发 | AWS 移动开发参考指南

# 前端开发

  1. 新建Web工程
  2. 页面开发
  3. 在HBuilder Web浏览器中测试

## 1\. 新建Web工程

这里使用HBuilder作为前端开发工具，演示前端开发的过程。

1、HBuilder菜单中选择 「文件>新建>移动App」。

  * `应用名称`与创建web应用的ID保持一致， 如 com.actionsoft.apps.poc.h5
  * `位置`固定在AWS Web服务器app资源目录，具体路径为: {AWS PaaS安装目录}\webserver\webapps\portal\apps, 如`E:\release\webserver\webapps\portal\apps`
  * 模板选择`mui项目`

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/h5-app/hbuilder_newprj.png)

2、打开index.html，右上角选择`边改边看模式`。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/h5-app/hbuilder_mode.png)

3、将本机AWS PaaS的访问地址配置为HBuilder的Web服务器。详细的配置步骤请看[这里](<../appendix/hbuilder-webserver.html>)。

4、HBuilder web浏览器锁定网址。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/h5-app/hbuilder_lockweb.png)

## 2\. 页面开发

因访问首页时会传递sid参数，可以通过js获取sid参数。
    
    
    sid = getParam("sid");
    
    function getParam(name){
        var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
        var r = window.location.search.substr(1).match(reg);
        if(r!=null)return  unescape(r[2]); return null;
    }
    

页面跳转时，可以将sid作为参数传递到下一个页面， 或者提前保存到cookie中，下个页面中通过cookie获取。
    
    
        $("#history").off("tap").on("tap", function(){
            location.href = "history.html?sid="+sid;
        });
    
        function setCookie(c_name,value,expiredays){
            var exdate=new Date()
            exdate.setDate(exdate.getDate()+expiredays)
            document.cookie=c_name+ "=" +escape(value)+
            ((expiredays==null) ? "" : ";expires="+exdate.toGMTString())
        }
    
        function getCookie(c_name){
            if (document.cookie.length>0) {
                c_start=document.cookie.indexOf(c_name + "=")
                if (c_start!=-1) {
                    c_start=c_start + c_name.length+1
                    c_end=document.cookie.indexOf(";",c_start)
                    if (c_end==-1)
                        c_end=document.cookie.length
                    return unescape(document.cookie.substring(c_start,c_end))
                }
            }
            return ""
        }
    

index.html
    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
        <title></title>
    
        <link rel="stylesheet" type="text/css" href="css/mui.min.css">
        <style>
    
                .from-username {
                    color: #8f8f94;
                    font-size: 13px;
                    font-weight: 400;
                }
    
                .time {
                       float: right;
                    color: #8f8f94;
                    font-size: 13px;
                    font-weight: 400;
                }
    
            </style>
    
    </head>
    <body>
    
        <div class="mui-content">
                <ul class="mui-table-view mui-table-view-striped mui-table-view-condensed" id="taskList">
    
                </ul>
            </div>
    
        <nav class="mui-bar mui-bar-tab" >
                <a id="todo" class="mui-tab-item mui-active">
                    <span class="mui-icon mui-icon-list"></span>
                    <span class="mui-tab-label">待办任务</span>
                </a>
                <a id="history" class="mui-tab-item">
                    <span class="mui-icon mui-icon-checkmarkempty"></span>
                    <span class="mui-tab-label">已办任务</span>
                </a>
    
            </nav>
    
    
    </body>
    <script src="js/mui.min.js"></script>
    <script src="js/jquery.min.js"></script>
    <script src="js/app.js"></script>
    <script>
        var sid;
        $(function(){
    
            if(getParam("sid") != null){
                sid = getParam("sid");
            }
            buildTaskList();
        });
    
        function buildTaskList(){
            var url = "../../r/jd?cmd=com.actionsoft.apps.poc.h5_todo&sid="+sid;
            $.getJSON(url, {}, function(json){
                if(json.result == "ok"){
                    var taskListUL = $("#taskList");
                    taskListUL.html("");
                    var taskList = json.data.taskList;
    
                    taskList.forEach(function(value, index, array){
                        taskListUL.append(getTaskLi(value.taskTitle, value.taskOwner, value.taskTime));
                    });
    
                }else{
                    processError(json);
                }
            });
        }
    
        function getTaskLi(taskTitle, taskOwner, taskTime){
    
            var li = '\
            <li class="mui-table-view-cell">\
                <div class="mui-table">\
                    <div class="mui-table-cell">\
                         <div class="mui-media-body">\
                                <span class="mui-ellipsis">'+taskTitle+'</span>\
                                <span class="time">'+taskTime+'</span>\
                            </div>\
                            <span class="from-username">来自: '+taskOwner+'</span>\
                    </div>\
                </div>\
            </li>\
            ';
            return li;
        }
    
    </script>
    </html>
    

app.js
    
    
    $(function(){
        $("#todo").off("tap").on("tap", function(){
            location.href = "index.html?sid="+sid;
        });
        $("#history").off("tap").on("tap", function(){
            location.href = "history.html?sid="+sid;
        });
    
    
    });
    
    function processError(json){
        if(json.errorCode == "401" || json.errorCode == "403"){
            window.location = 'http://sessiontimeout';
        }else{
            alert(json.msg);
        }
    }
    
    function getParam(name){
        var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
        var r = window.location.search.substr(1).match(reg);
        if(r!=null)return  unescape(r[2]); return null;
    }
    

## 3\. 在HBuilder Web浏览器中测试

初次打开html文件时，可能会提示如下错误，这是因为HBuilder的Web浏览器请求页面时，不会传递sid参数， 所以需要手动添加sid参数。 ![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/h5-app/hbuilder_err.png)

1、生成测试sid， 可在服务端调用API生成：
    
    
    String sid = SDK.getPortalAPI().createClientSessionByDevice("admin", "pwd", LoginConst.DEFAULT_LANG, "", LoginConst.DEVICE_MOBILE);
    

2、在HBuilder Web浏览器地址栏尾部添加上面生成的sid参数值， 如`?sid=512292d0-2eb8-438f-b496-aa58dfcf1d19`，按回车键可刷新页面。

![](https://docs.awspaas.com/reference-guide/aws-paas-mobile-development-refrence-guide/h5-app/hbuilder_sid.png)