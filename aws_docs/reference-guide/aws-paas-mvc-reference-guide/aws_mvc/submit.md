# 提交请求 · AWS PaaS文档中心

## 提交请求

AWS MVC基于Command命令请求驱动，对Web开发者约定了5类常见`url`请求地址，这些请求可以通过`GET`/`POST`提交。

url | 类型 | 说明  
---|---|---  
./w | text/html | (web)-请求结果一定是普通Web页面数据时  
./jd | application/json | (json data)-请求结果一定是`ResponseObject` Json  
./xd | application/xml | (xml data)-请求结果一定是`ResponseObject` XML  
./df | application/octet-stream(成功)  
application/json(失败) | (download file)-文件下载流，如下载失败或权限校验不通过，返回Json处理结果  
./uf | application/json | (upload file)-文件上传流，返回Json处理结果  
  
启动完你的本地AWS服务，试着在浏览器输入以下URL请求
    
    
    http://localhost:8088/portal/r/w?cmd=API_BENCHMARK_TEST&p=Hello AWS
    

**说明**

  * `8088`是安装AWS开发服务的默认Web端口号
  * /`portal`/是默认的Web App根名
  * 看到预期的返回结果了吗？“**Hello AWS** ”

### Web可靠性编程习惯

任何请求在极端环境或服务故障时都会发生错误，这是你的编程信条。如果你期望在浏览器背后(如一个Ajax请求)发送的HTTP返回一个特定数据结构或操作状态值，那么AWS MVC会要求你在Java代码使用`ResponseObject`对象进行封装，并在前端对`result`进行检查，只有当`result`为`ok`时从`data`中读取结果，否则应该检查`errorCode`及`msg`项，并处理该异常（如提醒操作者或其他操作）

模拟一个停机故障。现在关闭你的AWS服务，但保持Web服务的正常运行，在浏览器中输入以下URL请求
    
    
    http://localhost:8088/portal/r/jd?cmd=API_BENCHMARK_TEST&p=Hello AWS
    

**说明**

  * 使用`./jd`请求一个json数据结果，模拟加载ajax数据
  * 你获得了非预期的“**Hello AWS** ”

    
    
    {
    result: "error",
    msg: "AWS Instance Server连接失败！(590)"
    }
    

> **result值类型**
> 
>   * `ok`（操作成功）
>   * `error`（服务端发生错误，错误描述在`msg`项）
>   * `warning`（服务端发生警告，警告描述在`msg`项）
> 

### 默认编码字符集

`utf-8`

### 常规请求必须参数

  * `sid`（用户会话）
  * `cmd`（请求指令。命名规范：**前缀为该应用的Id，后面是动作名，中间以下划线分割，区分大小写** ）

### Web层配置文件

每个AWS App的Web资源被独立的定义在webapp根目录apps/`%AppId%`下。如果该应用需要cmd处理，至少应定义一个接参配置文件，并建议命名为`action.xml`

配置文件以UTF-8 NO BOM编码存储，格式为一个或多个符合Schema规范、以action（不区分大小写）开头、后缀为xml的文件。一个`action.xml`示例如下
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <aws-actions>
        <cmd-bean name="%AppId%_xxx1">
            <param name="p1" />
        </cmd-bean>
        <cmd-bean name="%AppId%_xxx2">
            <param name="p1" />
        </cmd-bean>
        <cmd-bean name="%AppId%_xxx3">
            <param name="p1" type="body"/>
        </cmd-bean>
    </aws-actions
    

cmd-bean的type属性：

  * `type`不配置时，该参数的值来自请求中查询参数或者application/x-www-form-urlencoded类型内容中请求参数
  * `type=body`时，该参数的值来自请求内容application/xml、application/json等类型的值，Controller将接收到请求内容的字符串值
  * `type=cookie`时，该参数的值来自请求内容的cookie，Controller将接收到对应`name`的`cookie`值
  * `type=header`时，该参数的值来自请求内容的header，Controller将接收到对应`name`的`header`值