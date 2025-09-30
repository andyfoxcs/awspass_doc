# 使用Postman工具 · AWS PaaS文档中心

# 使用Postman工具

## 环境准备

  * [Postman工具](<https://www.postman.com/>)

## 场景

测试由开发者自扩展的API，[参见附录示例](<../appendix/publish_restful_api.html>) 中如下方法：
    
    
    @Path("/param/{name}")
    @GET
    public String sayHelloparam(@PathParam("name") String name) {
        return "hello,world!-param  " + name;
    }
    

## 步骤

### **1.在Postman创建Collections**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/postman2.png)](<postman2.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/postman3.png)](<postman3.png>)

### **2.在AWS PaaS平台获取RESTful API访问地址及相关参数信息**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/1.png)](<1.png>)

### **3.配置WEB API访问地址及相关参数**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/4.png)](<4.png>)

### **4.配置认证方式及用户名 密码**

用户名密码为发布RESTful时绑定身份策略信息。

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/postman5.png)](<postman5.png>)

### **5.运行查看结果**

[![](https://docs.awspaas.com/reference-guide/aws-paas-api-guide/restful/5.png)](<5.png>)