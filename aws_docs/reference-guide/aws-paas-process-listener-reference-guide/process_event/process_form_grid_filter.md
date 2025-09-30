# PROCESS_FORM_GRID_FILTER | AWS 流程事件开发参考指南

## PROCESS_FORM_GRID_FILTER

### 该流程全局的FORM_GRID_FILTER事件

项 | 说明  
---|---  
抽象类 | FormGridFilterListener  
接口 | ValueListenerInterface  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
**注意** 原子表过滤事件设置行样式，链接机制，VUE表单引擎不支持，请使用表单事件实现

如果该流程某个节点注册了FORM_GRID_FILTER事件，则对该节点来说，该PROCESS_FORM_GRID_FILTER事件失效。

### 常见触发场景

### 场景1：刷新有子表的表单时

  * 过滤子表行记录
  * 禁止子表行删除

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/process_event/13.png)

#### 开发示例
    
    
    @Override
    public FormGridRowLookAndFeel acceptRowData(ProcessExecutionContext context, List<BOItemModel> boItemList, BO boData) {
        String tableName = context.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
        if (tableName.equals("BO_ACT_PUTONGSUB1")) {
            //创建一个对象
            FormGridRowLookAndFeel diyLookAndFeel = new FormGridRowLookAndFeel();
            String s3 = boData.getString("S3");
            String s4 = boData.getString("S4");
            if (s3 != null && s3.equals("50")) {
                diyLookAndFeel.setRemove(false);// 设置这行数据不允许删除
            }
            if (s3 != null && s3.equals("55")) {
                diyLookAndFeel.setDisplay(false);//不显示这条数据
            }
            //特别说明：
            //如果控制字段子表的`编辑`和`明细`链接的文字的显示隐藏
            //可判断字段名是否是`字段子表`UI组件，然后进行赋值
            //赋值规则：`编辑|明细`
            //如果不显示`编辑`，将该部分留空，如果不显示`明细`，将该部分留空
            //如：`|明细`，`编辑|`，`|`
            boData.set("字段子表字段名", "编辑|明细");
    
            //处理好之后，将该对象返回
            return diyLookAndFeel;
        }
        return null;//返回null按照原始数据展示子表
    }
    

### 场景2：指定子表排序

#### 开发示例
    
    
    @Override
    public String orderByStatement(ProcessExecutionContext context) {
        return "field1 asc,field2 desc";//两种字段组合的排序
        //return "field2 desc";//单个字段排序
    }