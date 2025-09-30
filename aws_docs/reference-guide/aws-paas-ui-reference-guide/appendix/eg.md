# 附录 | AWS UI组件参考指南

# 附录

**网格数据字典为CC http数据源示例步骤：**

1.在HTTP连接服务进行相关配置，URL中支持@公式，只支持[@env](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/list/system.html#env>) ![](http1.png)

2.字典模型中两个参数的设置

![](http2.png)

3.字典模型中几个参数可以在自定义cmd中获得对应的值

![](http3.png)

代码示例
    
    
    package com.awspaas.user.apps.meizu641.test;
    
    import com.actionsoft.bpms.server.UserContext;
    import com.actionsoft.bpms.server.bind.annotation.Controller;
    import com.actionsoft.bpms.server.bind.annotation.Mapping;
    import com.alibaba.fastjson.JSONArray;
    import com.alibaba.fastjson.JSONObject;
    import org.apache.cxf.wsdl11.SOAPBindingUtil;
    
    //value = "com.awspaas.user.apps.db_home",session = false,noSessionEvaluate = "无安全隐患",noSessionReason = "用于MVC框架稳定性测试"
    @Controller
    public class Mycontroller {
        @Mapping(value = "com.awspaas.user.apps.meizu641_getstr",session = false,noSessionEvaluate = "无安全隐患",noSessionReason = "用于MVC框架稳定性测试")
        public String getStr(int nb1, int nb2,String pagecurrent){
    //        System.out.println(me.toString());
            System.out.println("进来方法");
    
    
    //        JSONArray jsonarray = new JSONArray();
    
            JSONObject json = new JSONObject();
            JSONArray array = new JSONArray();
    
            JSONObject jo1 = new JSONObject();
            jo1.put("A","111111");
            jo1.put("B","222222");
            jo1.put("pagecurrent","1");
            JSONObject jo2 = new JSONObject();
            jo2.put("A","333333");
            jo2.put("B","444444");
            jo2.put("pagecurrent","1");
            JSONObject jo3 = new JSONObject();
            jo3.put("A","555555");
            jo3.put("B","666666");
            jo3.put("pagecurrent","2");
            JSONObject jo4 = new JSONObject();
            jo4.put("A","777777");
            jo4.put("B","888888");
            jo4.put("pagecurrent","2");
            JSONObject jo5 = new JSONObject();
            jo5.put("A","99999");
            jo5.put("B","9");
            jo5.put("pagecurrent","3");
    
    
            if("1".equals(pagecurrent)){
                array.add(jo1);array.add(jo2);
            }else if("2".equals(pagecurrent)){
                array.add(jo3);array.add(jo4);
            }else if("3".equals(pagecurrent)){
                array.add(jo5);
            }
    //        json.put("pageeach",2);//每页行数
    
            json.put("data",array);//数据
            json.put("pagecount",5);//总条数
    
            System.out.println("结果:" + json.toString());
    
            return json.toString();
        }
    }
    

**运行效果**

![](http4.png)

>   * 参数condition表示查询框的条件，对于查询框的条件需要自定义处理，此参数参考步骤4中的截图的请求地址  
> 
>   * 每次翻页会重新请求你的cmd,所以需要根据当前页这个字段来过滤返回的JSON中的数据
>