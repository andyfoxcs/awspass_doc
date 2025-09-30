# 代码示例 · AWS PaaS文档中心

## 代码示例

### SecurityProcessorDemo
    
    
    package com.actionsoft.apps.poc.plugin.security;
    
    import java.io.FileInputStream;
    import java.io.InputStream;
    import java.util.Map;
    
    import com.actionsoft.bpms.commons.security.processor.AESSecurityProcessor;
    import com.actionsoft.bpms.commons.security.processor.AbstractSecurityProcessor;
    import com.actionsoft.bpms.server.fs.DCContext;
    
    public class SecurityProcessorDemo extends AbstractSecurityProcessor {
        /**
         * 加密文本
         *
         * @return 加密后的文本
         * @params params
         */
        public String encryptContent(Map<String, Object> params) {
            // 需要加密的内容
            String content = (String) params.get("content");
            // 平台传入的密码，根据需要使用
            String password = (String) params.get("password");
            //加密具体代码
            //TODO
            String encryptedContent = content;
            // return encryptedContent;
            // 如果该方法不需要处理，则需要调用平台自身的处理机制，代码如下：
            return AESSecurityProcessor.getInstance().encryptContent(params);
        }
    
        /**
         * 解密文本
         *
         * @return 解密后的文本
         * @params params
         */
        public String decryptContent(Map<String, Object> params) {
            // 需要解密的内容
            String content = (String) params.get("content");
            // 平台传入的密码，根据需要使用
            String password = (String) params.get("password");
            // 解密具体代码
            //TODO
            String originContent = content;
            // return originContent;
            // 如果该方法不需要处理，则需要调用平台自身的处理机制，代码如下：
            return AESSecurityProcessor.getInstance().decryptContent(params);
        }
    //----------------这是分隔线以下两个方法为6.3.GA及以后版本请使用----------------------
    
       /**
         * 返回解密包装流
         *
         * @param is 要解密的文件流
         * @param password 取自文件路经的一段信息
         * @return 解密后的文件流
         * @throws Exception
         * @since 6.3.GA及以后使用该接口
         */
        public InputStream decrypt(InputStream is, String password, Map<String, Object> params) throws Exception {
            return AES.decrypt(is, password);
        }
    
        /**
         * 返回加密包装流
         *
         * @param is 待加密的文件流
         * @param password 取自文件路经的一段信息
         * @return 加密后的文件流
         * @throws Exception
         * @since 6.3.GA及以后使用该接口
         */
        @Override
        public InputStream encrypt(InputStream is, String password, Map<String, Object> params) throws Exception {
            return AES.encrypt(is, password);
        }
    
    //----------------这是分隔线以下两个方法为6.3.3 6.3.2  6.3.1版本请使用----------------------
       /**
         * 加密文件
         *
         * @return 文件大小
         * @params params
         */
        public Integer encryptFile(Map<String, Object> params) {
            // 平台传入的密码，根据需要使用
            String password = (String) params.get("password");
            // 需要加密的文件路径
            String path = (String) params.get("path");
            int fileSize = 0;
    
            File inFile = new File(path);
            FileInputStream in = null;
            try {
                //加密具体代码
                //TODO
                in = new FileInputStream(inFile);
                fileSize = in.available();
            } catch (Exception e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
    
            return fileSize;
    
            // 如果该方法不需要处理，则需要调用平台自身的处理机制，代码如下：
            // return AESSecurityProcessor.getInstance().encryptFile(params);
        }
    
    
      /**
         * 解密文件
         *
         * @return
         * @params params
         */
        public InputStream decryptFile(Map<String, Object> params) {
            String password = (String) params.get("password");
            // 需要解密的文件路径
            String path = (String) params.get("path");
            // DC存储控制器上下文对象
            DCContext context = (DCContext) params.get("context");
             FileInputStream in = null;
             try {
                    in = new FileInputStream(path);
                    int len = in.available();
                    if (len > 0) {
                        byte[] buf = new byte[len];
                        try {
                            in.read(buf, 0, len);
                            ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(buf);
    
                            //解密具体代码
                            //TODO
                            return byteArrayInputStream;
                        } finally {
                            try {
                                if (in != null)
                                    in.close();
                                context.setDCMessage(DCMessage.OK, I18nRes.findValue(AppsConst.SYS_APP_PLATFORM, "文件已读取完毕"));
                            } catch (Exception e) {
                                e.printStackTrace(System.err);
                            }
                        }
                    }
                    return null;
                } catch (Exception e) {
                    e.printStackTrace(System.err);
                    return null;
                } finally {
                    try {
                        if (in != null)
                            in.close();
                        in = null;
                    } catch (Exception e) {
                        e.printStackTrace(System.err);
                    }
                }
    
            // 如果该方法不需要处理，则需要调用平台自身的处理机制，代码如下：
            // return AESSecurityProcessor.getInstance().decryptFile(params);
        }
    
    
    //---------------------这是分隔线结束-----------------------------
    
    
        /**
         * 计算摘要
         * @param params data 需要摘要的数据
         * @return
         */
         //当重写该方法后，且`平台安全处理机制`配置为此处理机制时，AWS BO表将提供`加密摘要字段`按钮，详细参见以下`BO表数据摘要`章节
         //用户也可以在自己需要的场景调用该方法实现摘要防篡改功能
        public String calculateHashcode(Map<String, Object> params) {
            // 需要摘要数据
            String data = (String) params.get("data");
            // 具体摘要算法
            //TODO
            String hashCode = data;
            return hashCode;
        }
    
        /**
         * 判断安全处理器是否可用。如加密机制用到第三方服务，需要判断第三方服务是否可用，如果调用不成功的时候，则会阻止表单打开。
         * 该验证算法，要和加解密的算法保持一致，否则会导致数据加解密错误，导致数据丢失
         *
         * @param params
         * @return true，表示该处理器正常使用；否则不可用
         */
        public boolean isAvailable(Map<String, Object> params) {
            return true;
        }
    
        /**
        *用户登录密码的算法调整
        *
        */
        //当重写该方法后，需重新实现AWS PaaS平台登录适配器，详细参见下面`用户登录密码算法调整登录适配器`章节
        public String getPassword(String userId, String pwd) {
            // demo，仅返回不加密的密码，请不要应用到生产环境
            return pwd;
        }
    }
    

>   1. isAvailable方法返回false时，打开表单提示如下 [![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/security2.png)](<security2.png>)
> 

### 将SecurityProcessorDemo注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    public class Plugins implements PluginListener {
        @Override
        public List<AWSPluginProfile> register(AppContext appContext) {
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            list.add(new SecurityProcessorProfile("SECURITY-DEMO", "安全处理机制Demo", SecurityProcessorDemo.class.getName(), "安全处理机制Demo"));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

### 用户登录密码算法调整登录适配器

重写`AbstractSecurityProcessor`抽象类中的`getPassword`方法后，必须重新实现AWS PaaS平台登录适配器。

用户登录密码算法调整登录适配器示例代码如下：
    
    
    package com.actionsoft.apps.poc.plugin.adapter;
    
    import com.actionsoft.bpms.commons.login.LoginAdapterInterface;
    import com.actionsoft.bpms.commons.login.constant.LoginConst;
    import com.actionsoft.bpms.commons.login.control.LoginContext;
    import com.actionsoft.bpms.commons.login.control.LoginResult;
    import com.actionsoft.bpms.commons.security.processor.AESSecurityProcessor;
    import com.actionsoft.bpms.commons.security.processor.SecurityProcessorHelper;
    import com.actionsoft.bpms.org.cache.UserCache;
    import com.actionsoft.bpms.org.dao.OrgDaoFactory;
    import com.actionsoft.bpms.org.model.UserModel;
    
    public class PWDHashChangeLoginAdapterDemo implements LoginAdapterInterface {
        /**
         * 依据Context获取登录信息，进行登录检验
         *
         * @return 返回校验结果
         */
        public LoginResult validate(LoginContext context) {
            LoginResult lr = new LoginResult();
            // 确定uid
            String localUID = context.getUid();
            // 对应本地的AWS账户
            lr.setLocalUID(localUID);
            UserModel userModel = UserCache.getModel(localUID);
            if (userModel == null) {// 本地未发现该账户
                lr.setStatus(LoginConst.LOGIN_STATUS_ERR1);
                return lr;
            } else if (userModel.isClosed()) {
                // 账户已被注销
                lr.setStatus(LoginConst.LOGIN_STATUS_ERR2);
                return lr;
            }
    
            String pwd = context.getPwd();
            String oldPwdHash = AESSecurityProcessor.getInstance().getPassword(localUID, pwd);
            if (oldPwdHash.equals(userModel.getPassword())) {
                //旧版本的密码摘要值和数据库中的值一致，则说明用户登录的密码正确。
                //这时，需要修改数据库中的密码
                changePassword(localUID, pwd);//传入明文密码，内部会调用新算法计算密码摘要值
                lr.setStatus(LoginConst.LOGIN_STATUS_OK);
                return lr;
            } else {
                //如果不相等，则是已经处理过新算法了
                String newPwd = SecurityProcessorHelper.getPassword(localUID, pwd);
                if (newPwd.equals(userModel.getPassword())) {//新算法和数据库中的摘要比较
                    lr.setStatus(LoginConst.LOGIN_STATUS_OK);
                    return lr;
                } else {
                    // 密码不通过
                    lr.setStatus(LoginConst.LOGIN_STATUS_ERR1);
                    return lr;
                }
            }
        }
    
        //重写`AbstractSecurityProcessor`抽象类中的`getPassword`方法后会导致平台的密码摘要改变，所以需要将新的密码摘要内容存储到数据库中
        private void changePassword(String uid, String pwd) {
            UserModel model = UserCache.getModel(uid);
            if (model != null) {
                OrgDaoFactory.createUser().setPassWord(model.getUniqueId(), pwd);//pwd是明文的
            }
        }
    }
    

> 有关登录适配器详细介绍请参考[这里](<loginadapter.html>)

### BO表数据摘要

重写`AbstractSecurityProcessor`抽象类中的`calculateHashcode`方法后，且`AWS BPMS平台`的`安全处理机制(SecurityProcessorId)`参数配置为该插件注册名时，BO表将提供`加密摘要字段`按钮。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/zhaoyao2.png)](<zhaoyao2.png>)

按照提示说明，配置加密摘要字段后，在打开表单时将自动对被摘要字段进行安全检查，如果发现字段值被从数据库直接修改过，打开的表单将不可修改与办理，并有明显提示信息。 [![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/zhaoyao1.png)](<zhaoyao1.png>)