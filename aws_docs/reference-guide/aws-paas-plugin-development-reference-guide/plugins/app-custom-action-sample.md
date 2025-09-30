# 代码示例 · AWS PaaS文档中心

## 代码示例

### AppCustomAction
    
    
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Map;
    
    import com.actionsoft.apps.AppsConst;
    import com.actionsoft.apps.lifecycle.dist.DistContext;
    import com.actionsoft.apps.lifecycle.event.AppCustomActionInterface;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.bpms.bpmn.engine.cache.ProcessDefCache;
    import com.actionsoft.bpms.bpmn.engine.model.def.ProcessDefinition;
    import com.actionsoft.bpms.commons.security.ac.AccessControlAPI;
    import com.actionsoft.bpms.commons.security.ac.cache.AccessControlCache;
    import com.actionsoft.bpms.commons.security.ac.model.AccessControlModel;
    import com.actionsoft.bpms.commons.security.ac.model.ProcessStartACCM;
    import com.actionsoft.bpms.util.UtilFile;
    import com.alibaba.fastjson.JSON;
    import com.alibaba.fastjson.JSONArray;
    
    /**
     * 用于应用分发时将流程启动权限导出、应用安装或者升级时写入流程启动权限
     */
    public class AppCustomAction implements AppCustomActionInterface {
        @Override
        public void dist(AppContext app, DistContext distCtx) {
            Map<String, ProcessDefinition> listByApp = ProcessDefCache.getInstance().getListByApp(app.getId());
            List<String> versionIds = new ArrayList<>();
            for (ProcessDefinition processDefinition : listByApp.values()) {
                if (!versionIds.contains(processDefinition.getVersionId())) {
                    versionIds.add(processDefinition.getVersionId());
                }
            }
    
            JSONArray arr = new JSONArray();
            for (String versionId : versionIds) {
                List<AccessControlModel> accessModelListByResource = AccessControlAPI.getInstance().getAccessModelListByResource(ProcessStartACCM.resourceType, versionId, ProcessStartACCM.VISIT.getType());
                for (AccessControlModel accessControlModel : accessModelListByResource) {
                    Object object = JSON.toJSON(accessControlModel);
                    arr.add(object);
                }
            }
            if (arr.size() > 0) {
                UtilFile file = new UtilFile(AppsConst.APPS_ROOT + AppsConst.FOLDER_DIST + "/" + app.getId() + "/process.start.ac.json");
                file.canWrite();
                file.writeUTF8(arr.toString());
            }
        }
    
        @Override
        public void install(AppContext newApp) {
            UtilFile file = new UtilFile(AppsConst.APPS_ROOT + AppsConst.FOLDER_INSTALL + "/" + newApp.getId() + "/process.start.ac.json");
            if (file.exists()) {
                JSONArray array = JSON.parseArray(file.readStrUTF8());
                for (Object o : array) {
                    AccessControlModel model = JSON.parseObject(o.toString(), AccessControlModel.class);
                    Object acModel = AccessControlCache.getACModel(model._resourceType, model._resourceId, model._assignmentType, model._assignmentId, model._accessModel);
                    if (acModel == null) {
                        AccessControlAPI.getInstance().appendACResource(model._resourceId, model._resourceType, model._accessModel, model._assignmentId, model._assignmentType);
                    }
                }
                // 安装数据完毕
                UtilFile.removeFile(file);
            }
        }
    
        @Override
        public void upgrade(AppContext newApp) {
            install(newApp);
        }
    
    }
    

### 将类注册至PluginListener监听器

> com.actionsoft.apps.poc.plugin.Plugins
    
    
    package com.actionsoft.apps.poc.plugin;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import com.actionsoft.apps.listener.PluginListener;
    import com.actionsoft.apps.poc.plugin.at.MyLenExpression;
    import com.actionsoft.apps.resource.AppContext;
    import com.actionsoft.apps.resource.plugin.profile.AWSPluginProfile;
    import com.actionsoft.apps.resource.plugin.profile.AtFormulaPluginProfile;
    
    /**
     * 注册插件
     */
    public class Plugins implements PluginListener {
        public Plugins() {
        }
    
        public List<AWSPluginProfile> register(AppContext context) {
            // 存放本应用的全部插件扩展点描述
            List<AWSPluginProfile> list = new ArrayList<AWSPluginProfile>();
            // 注册
            list.add(new AppCustomActionPluginProfile(AppCustomAction.class.getName()));
            return list;
        }
    }
    

注意：在AWS CONSOLE的`应用管理 > 应用开发 > 配置应用`或AWS Developer中配置该App的`扩展插件`选项为`com.actionsoft.apps.poc.plugin.Plugins`

该测试代码是将流程的实例代码启动权限AC授权部分在分发时导出，在安装的时候进行导入。

**适用于组织结构测试机和正式机完全同步且一致的场景，仅供参考**