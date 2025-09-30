# 代码示例 · AWS PaaS文档中心

# 代码示例

## 后端JAVA组件注册
    
    
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
    

## 前端VUE

前端vue代码详细参见开发步骤中下载的项目包示例。