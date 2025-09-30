# 开发步骤 · AWS PaaS文档中心

# 开发步骤

  1. 平台注册组件
     * 后端Java注册组件
     * 平台应用管理中注册
  2. 前端项目搭建
     * 代码开发
     * 打包到app
     * 注意事项

在开始前点击[这里](<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/form-user-custom-extend.zip>)您需要下载项目包和示例代码。

## 1\. 平台注册组件

### 1.1后端Java注册组件

在您下载的项目包 `readme-help/java-example.zip`中提供了一个基本示例。
    
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.devformui.ui.CustomFormUI;
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.FormUIPluginProfile;
    import com.actionsoft.bpms.form.design.constant.FormRuleControlEnum;
    
    /**
     * 自定义vue UI组件。  应用ID:com.actionsoft.apps.devformui
     */
    
    public class Plugins implements PluginListener {
    
        public Plugins() {
        }
    
        @Override
        public List<AWSPluginProfile> register(AppContext context) {
            List<AWSPluginProfile> list = new ArrayList<>();
            // ---------------------注册自定义组件-----------------------------
            /**
             * @param id UI名，建议英文
             * @param clazz 实现类
             * @param title 简要说明
             * @param desc 详细说明
             * @param isSetting 是否有组件专有属性
             * @param isSetColumnWidth 是否允许设置显示宽度属性（表格列）
             * @param isSetWidth 是否允许设置可编辑时宽度属性
             * @param isSetHeight 是否允许设置可编辑时高度属性
             * @param isSetExtendCode 是否允许设置扩展代码属性
             * @param isSetAltText 是否允许设置鼠标提醒属性
             * @param isSupportGrid 是否支持子表
             * @param isSupportMobile 是否支持手机表单
             * @param isSetDisplayRule 是否支持显示规则属性
             */
            list.add(new FormUIPluginProfile("常规",
                    "AWSUI.Custom.text", //必须与前端一致
                    CustomFormUI.class.getName(),
                    "自定义组件", //名称必须与前端一致
                    "",
                    true,
                    true,
                    true,
                    false,
                    true,
                    true,
                    true,
                    true,
                    true
            )
                    .setSupportRuleControl(FormRuleControlEnum.SUBMIT)
                    .setSupportRuleControl(FormRuleControlEnum.CHANGE)
                    .setSupportRuleControl(FormRuleControlEnum.CALC)
                    .setSupportRuleControl(FormRuleControlEnum.EDIT)
                    .setSupportRuleControl(FormRuleControlEnum.REQUIRED)
                    .setIconFont("awsui-iconfont", "&#xe86b;", "#0c6e9f")
                    .setColumnWidth(150)
                    .setEngineVersion(2) //vue组件版本
            );
            return list;
        }
    }
    

### 1.2 平台应用管理中注册

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/uivue1.png)](<uivue1.png>)

注意：必须将注册的Java代码打成jar包，放在app的lib路径下（若该app安装路径下没有lib文件夹可以新建一个）。

## 2\. 前端项目搭建

### 2.1 准备工作（安装VUE开发环境，详细教程可自行VUE相关网站查找）

  1. 需要安装node.js，官网最新版本即可
  2. 安装yarn： npm install -g yarn
  3. 命令进入上面下载的项目包路径，在项目包路径位置运行： yarn install
  4. 修改配置文件 AWSDevServiceParams.js [![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/uivue2.png)](<uivue2.png>)
  5. 运行vue程序

    
    
    npm run dev
    

### 2.2 代码开发

  1. 项目使用VUE3、typeScript、vite、Element Plus（pc端）、Vant UI(移动端)开发
  2. 项目包form-user-custom-extend\packages\ui-components\custom\test-item\src\packages\custom\test-item 目录是此项目的一个测试组件示例（用于参考）
  3. PC端默认引用全局的Element Plus（可参考 <https://element-plus.org/zh-CN/）>
  4. 移动端默认引用全局的Vant UI（可参考 <https://vant-contrib.gitee.io/vant/#/zh-CN）ui>

**项目结构简介：** [![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/uivue3.png)](<uivue3.png>)

**如何测试一个现有表单？**

  1. 设计时刻测试URL：拿到表单Id与开发地址进行拼凑一个开发URL。 例如：[http://localhost:3000/#/?formDefId=ea082958-95d3-42ca-b606-b979f8c1e9a7&appId=com.actionsoft.apps.tpl.rework&categoryName=返工](<http://localhost:3000/#/?formDefId=ea082958-95d3-42ca-b606-b979f8c1e9a7&appId=com.actionsoft.apps.tpl.rework&categoryName=返工>) 其中formDefId是表单ID，appId是应用ID，categoryName是应用下所属分类名
  2. 运行时刻（PC端）测试URL，此时需要把表单挂载到流程里，启动流程后： 例如：[http://localhost:3000/runtime-pc/index.html?processInstId=539da0b6-5667-4280-8aaf-4a0a4a7a586b&taskInstId=fea49365-ec0b-4c05-a2f8-b2d0bdab8df0&openState=1](<http://localhost:3000/runtime-pc/index.html?processInstId=539da0b6-5667-4280-8aaf-4a0a4a7a586b&taskInstId=fea49365-ec0b-4c05-a2f8-b2d0bdab8df0&openState=1>) 其中processInstId是流程实例ID，taskInstId是任务实例ID，openState打开状态，1为默认
  3. 运行时刻（移动端）测试URL，此时需要把表单挂载到流程里，启动流程后： 例如：[http://localhost:3000/runtime-mobile/index.html?processInstId=539da0b6-5667-4280-8aaf-4a0a4a7a586b&taskInstId=fea49365-ec0b-4c05-a2f8-b2d0bdab8df0&openState=1](<http://localhost:3000/runtime-mobile/index.html?processInstId=539da0b6-5667-4280-8aaf-4a0a4a7a586b&taskInstId=fea49365-ec0b-4c05-a2f8-b2d0bdab8df0&openState=1>) 其中processInstId是流程实例ID，taskInstId是任务实例ID，openState打开状态，1为默认

### 2.2 打包到app

开发完毕后在package.json中右键运行：  
vite build --config vite-config/vite.config.packages.design.ts  
打包设计资源包到app中  
vite build --config vite-config/vite.config.packages.pc.ts  
打包电脑端资源包到app中  
vite build --config vite-config/vite.config.packages.mobile.ts  
打包移动端资源包到app中  
最后随平台分发应用功能分发即可。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/uivue5.png)](<uivue5.png>)

### 2.3 注意事项

  1. 表单正常打包需要Java端已经注册自定义组件并且前端已打包到app中，否则会导致表单无法打开
  2. java资源需要打包到apps/install/appid/lib目录下，前端VUE资源运行命令完成打包后，需要重启应用升效
  3. 自定义UI组件程序是在某个应用内，但自定义的UI组件是AWS PaaS平台内可用，不区分应用