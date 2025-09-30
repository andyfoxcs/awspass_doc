# PaaS内部Java调用示例 · AWS PaaS文档中心

## PaaS内部Java调用示例

该类调用方式仅限于同一PaaS内部的应用间。

  * SDK.getAppAPI().callASLP-同步调用
  * SDK.getAppAPI().asynCallASLP-异步调用

    
    
    // 调用方
    String sourceAppId = "com.actionsoft.apps.poc.plugin";
    // 服务地址
    String aslp = "aslp://com.actionsoft.apps.poc.plugin/myName";
    Map<String, Object> params = new HashMap<String, Object>();
    // 给定必填参数
    params.put("yourName", "Tom");
    ResponseObject ro = SDK.getAppAPI().callASLP(SDK.getAppAPI().getAppContext(sourceAppId), aslp, params);
    ...
    

#### 预期的返回结果
    
    
    {
    msg: "Hi Tom , My name is AWS!",
    id: ":responseobject;",
    result: "ok"
    }
    

#### 查看ASLP参数说明

ASLP通过注解生成元数据结构。在AWS CONSOLE的`应用管理 > 应用管理`打开服务提供者的应用窗口，在`资源`树中列出提供的ASLP服务地址，单击蓝色的`Meta`链接，可弹出调用该ASLP需要的参数及代码示范。