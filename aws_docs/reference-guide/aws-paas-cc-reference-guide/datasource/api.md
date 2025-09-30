# DS提供的API · AWS PaaS文档中心

# DS提供的API

CC DS为开发者提供了执行API：`SDK.getCCAPI().getDataServiceAPI(java.lang.String dataServiceDefId).execDataService(java.util.Map inParams)`
    
    
    
    // CC DataService参数结构
    Map<String, Object> params = new HashMap<>();{
        Map<String,Object> page=new HashMap<>();{
            // 参数类型：java.lang.Integer
            page.put("size", size);
            // 参数类型：java.lang.Integer
            page.put("index", index);
        }
        params.put("page",page);
    }
    
    {
        Map<String,Object> parameters=new HashMap<>();{
        // 参数类型：java.lang.String
        parameters.put("keyword_abc", keyword_abc);
        }
        params.put("parameters",parameters);
    }
    /**
    * 执行状态:ro.result，ok表示成功，error表示失败
    * 结果数据:ro.data.result
    * SLA数据:ro.data.sla
    */
    ResponseObject ro = SDK.getCCAPI().getDataServiceAPI(dataServiceDefId).execDataService(java.util.Map params);
    

### 参数来源及是否必填时API调用规则

[![](httpapi1.png)](<httpapi1.png>)

  * 参数来源为系统给定时，此时API调用无需传入该参数，即使传入后，引擎也不会使用传入值，始终读取配置的默认值
  * 参数来源为调用方给定时，当API调用时可传入参数，也可不传，当未传入参数时，引擎读取配置的默认值，如果未配置默认值，则系统自动传入空串继续后续动作
  * 当参数勾选必填时，API调用时会解析传入的值或默认值，如果传入的值或默认值计算结果为null或空字符串，则直接返回XX参数不允许为空