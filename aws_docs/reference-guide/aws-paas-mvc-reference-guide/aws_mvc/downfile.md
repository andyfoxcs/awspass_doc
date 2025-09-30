# 下载文件 · AWS PaaS文档中心

## 下载文件

下载`DC`仓库内文件的url必须由`DCContext`的`getDownloadURL()`获取。

  * 以下是获取文件下载链接的Java示例
        
        // 构造下载附件的url链接
        UserContext me = getContext();
        String appId = "xxxxxx";                //该App Id名
        String repositoryName = "orderFile";    //该App的DC仓库根目录
        String groupValue = yearMonth;          //一级目录为年月，201402
        String fileValue = orderId;             //订单Id
        String fileName = "order.jpg";          //文件名
        DCContext context = new DCContext(me, SDK.getDCAPI().getDCProfile(appId, repositoryName), appId, groupValue, fileValue, fileName);
        result.put("url", context.getDownloadURL());
        

  * JavaScript示例
        
        window.open(url);
        // or
        window.location.href = url;