# 代码示例 · AWS PaaS文档中心

## 代码示例

### 分发时资源ASLP方法
    
    
        public ResponseObject call(Map<String, Object> params) {
            ResponseObject ro = ResponseObject.newOkResponse();
            try {
                String resAppId = (String)params.get("resAppId"); //获取安装的appId
                JSONObject data = new JSONObject(); //jo中存放资源数据
                data.put("test","ok"+resAppId);
                //TODO data可以是任意字符串的数据（格式可根据需要定制，此处为JSON字符串）
                ro.put("res",data); //把需要处理的资源数据放到data中，注意约定res关键字
            } catch (AWSException e) {
                return ro.err(e.getMessage());
            }
            return ro;
        }
    

### 安装时资源ASLP方法
    
    
        public ResponseObject call(Map<String, Object> params) {
            ResponseObject ro = ResponseObject.newOkResponse();
            try {
                String resAppId = (String)params.get("resAppId"); //获取安装的appId
                //params.get("res")里是获取的资源数据，需要处理一些相关操作。
                System.out.println("安装时成功获取" + resAppId + "一个值："+ params.get("res").toString());
                //TODO 需要根据业务处理分发资源
            } catch (AWSException e) {
                return ro.err(e.getMessage());
            }
            return ro;
        }
    

### 升级时资源ASLP方法
    
    
        public ResponseObject call(Map<String, Object> params) {
            ResponseObject ro = ResponseObject.newOkResponse();
            try {
                String resAppId = (String)params.get("resAppId"); //获取安装的appId
                //params.get("res")里是获取的资源数据，需要处理一些相关操作。
                System.out.println("更新时成功获取" + resAppId + "一个值："+ params.get("res").toString());
                //TODO 需要根据业务处理分发资源
            } catch (AWSException e) {
                return ro.err(e.getMessage());
            }
            return ro;
        }