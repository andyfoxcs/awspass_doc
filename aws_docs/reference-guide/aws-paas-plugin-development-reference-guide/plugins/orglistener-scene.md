# 应用场景 · AWS PaaS文档中心

## 应用场景

组织改变监听事件在组织、角色、权限发生变化时被触发，包括改变发生前事件和改变发生后事件，利用该机制可以

  * 在改变发生前事件中可以阻止该改变
  * 在改变发生后事件中获取改变后的数据做进一步处理，比如同步到三方系统中

**事件类型**

事件类型 | 说明  
---|---  
ACTION_ADD | 增加  
ACTION_MODIFY | 修改  
ACTION_REMOVE | 删除  
ACTION_DISABLE_USER_ACCOUNT | 注销用户  
ACTION_ENABLE_USER_ACCOUNT | 激活用户  
ACTION_USER_SET_PASSWORD | 用户修改密码  
ACTION_USER_INIT_PASSWORD | 用户初始化密码