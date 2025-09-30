# 表单相关的API · AWS PaaS文档中心

# 表单相关的API

**校验方法**
    
    
    1 this.ui("字段名").validate() //校验字段方法
    2 this.api.validate() //校验表单方法
    3 this.validateMsg("字段名","msg");
    

**保存方法**
    
    
    1 this.api.saveData({"isValidate":true/false,//是否校验表单数据
    2 "isShowMsg":true/false,// 是否提示保存成功的信息
    3 "isTransact":true/false,// 是否继续执行流程办理动作
    4 "callback":function(){} // 成功后回调函数
    5 }) //保存表单数据，提供是否校验，是否弹出提示，是否执行流程办理
    

**切换表单**
    
    
    this.api.changeForm("formDefId")//切换指定表单，多表单时支持
    

**字段子表关闭刷新子表表格**
    
    
    1 formApi.userExtend.formGridDialogClose = (closeContext)=>{
    2 //F_UC0WNS4J为字段子表的字段
    3 if(closeContext.isFieldGrid && closeContext.fieldTableOptions && closeContext.fieldTableOptions.fieldName ==='F_UC0WNS4J'){
    4     //BO_EU_1682647039054为子表表名
    5      formApi.grids["BO_EU_1682647039054"].refreshData()
    6   }
    7 }