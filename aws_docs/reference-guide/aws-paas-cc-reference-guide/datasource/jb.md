# 脚本模式 · AWS PaaS文档中心

# 脚本模式

脚本模式是为高级开发人员提供的在线编辑映射关联的窗口。使用该功能要求您对 JAVA、JSON、JavaScripte等相关技术有一定的基础，如果您不完全了解，建意不要随意修改。

[![](http-input32.png)](<http-input32.png>)

示例：

## 输入转换（输入JavaScript脚本）

> 假设场景：数据服务（DS）上文的分页页码是从1开始的，但是服务端要求从0开始，可以利用脚本实现该差异转换
    
    
       //原脚本（自动生成的脚本）
       var $result = {
           "header": {},
    
           "pathParameters": {},
    
           "queryParameters": {
               "accesstoken": parameters.access_token
           },
    
           "bodyParameters": {
               "pageNum": page.index,
               "pageSize": page.size,
               "orderBy": {
                   "field": parameters.orderBy.field,
                   "sort": parameters.orderBy.sort
               },
               "queryParameter": {
                   "goodsStatus": parameters.queryParameter.goodsStatus,
                   "goodsClassifyId": parameters.queryParameter.goodsClassifyId,
                   "search": parameters.queryParameter.search
               }
           }
       }
    
    
    
       //修改后的脚本
       var $result = {
           "header": {},
    
           "pathParameters": {},
    
           "queryParameters": {
               "accesstoken": parameters.access_token
           },
    
           "bodyParameters": {
               "pageNum": page.index - 1,//将页码减去1，以适配服务端接口
               "pageSize": page.size,
               "orderBy": {
                   "field": parameters.orderBy.field,
                   "sort": parameters.orderBy.sort
               },
               "queryParameter": {
                   "goodsStatus": parameters.queryParameter.goodsStatus,
                   "goodsClassifyId": parameters.queryParameter.goodsClassifyId,
                   "search": parameters.queryParameter.search
               }
           }
       }
    

## 输出转换（输出JavaScript脚本）

> 假设场景：需要将服务端返回的英文状态转换为中文
    
    
       //原脚本（自动生成的脚本）
       var $result = {
           "result": {
               "title": result.title,
               "createDate": result.createDate,
               "status": result.status
           },
           "sla": {
               "inTimes": sla.inTimes,
               "outTimes": sla.outTimes,
               "totalTimes": sla.totalTimes
           }
       }
    
    
    
       //自定义脚本
       var $result = {
           "result": {
               "title": result.title,
               "createDate": result.createDate,
               "status": convert(result.status) //调用自定义的转换函数
           },
           "sla": {
               "inTimes": sla.inTimes,
               "outTimes": sla.outTimes,
               "totalTimes": sla.totalTimes
           }
       }
    
       //转换status为具有可读性的中文
       function convert(status) {
           var result;
           if ("READY" === status) {
               result = '就绪';
           } else if ("STARTING" === status) {
               result = '启动中';
           } else if ("ACTIVE" === status) {
               result = '活动';
           } else if ("STOPPED" === status) {
               result = '已停止';
           } else {
               result = '不可识别的状态';
           }
           return result;
       }