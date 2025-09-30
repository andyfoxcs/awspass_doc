# 简单查询示例 · AWS PaaS文档中心

## 简单查询示例

### search

> com.actionsoft.apps.poc.plugin.web.SampleWeb#searchFS
    
    
    // 调用方
    String sourceAppId = "com.actionsoft.apps.poc.plugin";
    // 服务地址
    String aslp = "aslp://com.actionsoft.apps.fullsearch/search";
    Map<String, Object> params = new HashMap<String, Object>();
    // 给定必填参数
    params.put("repositoryName", "db1");
    params.put("searchText", searchText);
    ResponseObject ro = SDK.getAppAPI().callASLP(SDK.getAppAPI().getAppContext(sourceAppId), aslp, params);
    return ro.toString();
    }
    

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`FullSearchSample`，在查询录入框输入`订单`，点击`简单查询`按钮，返回JSON搜索结果的结构如下
    
    
    {"data":{"result":[{"customerName":"环球科技","content":"订单确认","customerId":"CUST00009","documentId":"38799b80-eb92-45c3-9300-e354d321a487"}]},"msg":"","id":":responseobject;","result":"ok"}