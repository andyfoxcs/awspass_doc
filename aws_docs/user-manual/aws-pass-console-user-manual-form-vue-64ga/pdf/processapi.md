# 流程相关的API · AWS PaaS文档中心

# 流程相关的API

**提供实例上下文相关方法**

获取流程审批记录数据
    
    
    this.task.getCommentDefInfo()// 返回审核菜单定义
    
    
    this.task.getComment()
    //返回：{
    //    "actionName":"",
    //    "msg":""
    //}
    this.task.setComment({
    "actionName":"",
    "msg":""
    })
    

**获取/设置当前审核菜单选项、留言内容**
    
    
    this.task.getCommentDefInfo()// 返回审核菜单定义
    
    
    this.task.getComment()
    //返回：{
    //    "actionName":"",
    //    "msg":""
    //}
    this.task.setComment({
    "actionName":"",
    "msg":""
    })
    

**获取流程对象信息（常用信息封装）**
    
    
    this.process.getInfo()
    

**获取任务对象信息（常用信息封装）**
    
    
    this.task.getInfo()
    

**获取节点信息（常用信息封装）**
    
    
    this.task.activityDefInfo()
    

**获取当前设备模式(pc/移动)、入口类型（企微、钉钉、移动门户。。。）**
    
    
    this.api.getDeviceInfo()
    //返回：
    {
    "device":"pc/mobile",
    "entry":"dingding/wxwork/awsmobileportal/feishu/蓝信(关键字待定)"
    }