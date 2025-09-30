# 开发示例 · AWS PaaS文档中心

# 开发步骤及代码示例

## 开发步骤

  1. 实现`LoginAdapterInterface`接口
  2. 在`bin/conf/aws-portal.xml`文件中,配置`loginAdapter`参数，完成注册
  3. 场景模拟，调试

### LoginAdapterInterface
    
    
    package com.actionsoft.bpms.commons.login;
    
    import com.actionsoft.bpms.commons.login.control.LoginContext;
    import com.actionsoft.bpms.commons.login.control.LoginResult;
    
    /**
     * 登录适配器接口
     *
     */
    public interface LoginAdapterInterface {
    
        /**
         * 依据Context获取登录信息，进行登录检验
         *
         * @return 返回校验结果
         */
        public LoginResult validate(LoginContext context);
    
    }
    

### LoginContext context参数说明

参数 | 说明 | 备注  
---|---|---  
context.getIp(); | 当前IP | \--  
context.getMD5Pwd(); | 加密后密码 | \--  
context.getPwd(); | 明文密码 | \--  
context.getUid(); | 登录账户 | \--  
context.getDeviceType(); | 登录设备类型 | \--  
context.getSDK(); | 是否sdk创建 | \--  
context.getParams(); | 各类的扩展参数，可通过前端传递 | 若设置参数params.put("changeUserPWD", true);表示通过修改密码登录  
context.getLang(); | 登录语言 | \--  
  
### 代码示例
    
    
    package com.actionsoft.apps.zhanghf.adapter;
    
    import com.actionsoft.bpms.commons.login.LoginAdapterInterface;
    import com.actionsoft.bpms.commons.login.constant.LoginConst;
    import com.actionsoft.bpms.commons.login.control.LoginContext;
    import com.actionsoft.bpms.commons.login.control.LoginResult;
    
    /**
     * 默认本地用户名+口令验证
     *
     */
    public class LoginAdapter implements LoginAdapterInterface {
    
        /**
         * 依据Context获取登录信息，进行登录检验
         *
         * @return 返回校验结果
         */
        public LoginResult validate(LoginContext context) {
            //首先构造一个登录结果对象
            LoginResult lr = new LoginResult();
            //针对具体业务要求，实现相关代码
            //...
    
            //最后设置登录UID，
            lr.setLocalUID(context.getUid());
            //设置登录的结果
            lr.setStatus(LoginConst.LOGIN_STATUS_OK);
            //如果登录失败，可将自定义的消息写入下面的方法，前端界面会展示该信息
            lr.setMsg("消息内容");
            return lr;
        }
    
    }
    

### 注册

在`bin/conf/aws-portal.xml`文件中,配置`loginAdapter`参数，完成注册
    
    
    //平台登录适配器注册方式
    <security loginAdapter="com.actionsoft.bpms.commons.login.DefaultLoginAdapter" failLockedTimes="5" unlockTime="600000" pwdDefault="1" minPwdLength="0" maxPwdLength="32" pwdCycle="0" pwdComplexity="false" pwdChange="true" code="AH{%C1%F5%BD%F0%D6%F9}" requiredUserInfo=""/>
    

如果登录适配器实现类在应用中，`loginAdapter`参数值格式："AppId:登录适配器类全路径"

推荐部署到应用中，无需重启平台服务。

### 登录页面传入参数

可以修改登录页面传入扩展参数

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/loginadapter-sample-1.png)](<loginadapter-sample-1.png>)

### 登录适配器接收扩展参数

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/loginadapter-sample-2.png)](<loginadapter-sample-2.png>)