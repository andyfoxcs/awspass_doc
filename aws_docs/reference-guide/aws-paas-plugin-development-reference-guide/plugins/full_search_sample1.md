# 入库内容示例 · AWS PaaS文档中心

## 入库内容示例

### createIndexByContent

> com.actionsoft.apps.poc.plugin.web.SampleWeb#createFSIndex
    
    
    public String createFSIndex(String myContent, String myCustomerName, String myCustomerId) {
        // 调用方
        String sourceAppId = "com.actionsoft.apps.poc.plugin";
        // 服务地址
        String aslp = "aslp://com.actionsoft.apps.fullsearch/createIndexByContent";
        Map<String, Object> params = new HashMap<String, Object>();
        // 给定必填参数
        params.put("repositoryName", "db1");
        params.put("documentId", UUIDGener.getUUID());
        params.put("content", myContent);
        JSONArray extendFields = new JSONArray();
        // 扩展客户名称字段
        JSONObject customerNameField = new JSONObject();
        customerNameField.put("fieldName", "customerName");
        customerNameField.put("fieldType", "text");
        customerNameField.put("fieldContent", myCustomerName);
        customerNameField.put("fieldBoost", 1);
        customerNameField.put("fieldStore", true);// 可以返回到查询结果
        // 扩展客户ID字段
        JSONObject customerIdField = new JSONObject();
        customerIdField.put("fieldName", "customerId");
        customerIdField.put("fieldType", "text");
        customerIdField.put("fieldContent", myCustomerId);
        customerIdField.put("fieldBoost", 1);
        customerIdField.put("fieldStore", true);// 可以返回到查询结果
    
        extendFields.add(customerNameField);
        extendFields.add(customerIdField);
        params.put("otherFields", extendFields.toString());
        ResponseObject ro = SDK.getAppAPI().callASLP(SDK.getAppAPI().getAppContext(sourceAppId), aslp, params);
        return ro.toString();
    }
    

### 验证

进入`AWS CONSOLE > 应用管理`并打开你的应用，在`部署`中点击`FullSearchSample`，在弹出的对话框中输入信息后点击`入库操作`按钮

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/fullsearch-4.png)](<fullsearch-4.png>)