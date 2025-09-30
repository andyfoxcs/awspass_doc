# 事件 · AWS PaaS文档中心

# 事件

Java触发器是执行后端Java代码逻辑的容器，在客户端视图页面加载时被触发，由开发者通过Java程序影响视图页面显示内容。

**步骤**

  1. 打开视图配置界面
  2. 鼠标移动视图名称上，点击"高级选项"弹出侧边栏，点击"事件"页签
  3. 对事件实现类进行注册/删除

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/35.png)](<35.png>)

配置项 | 说明  
---|---  
触发器类型 | 各种事件名称，不同的事件要求开发人员实现的接口不同，每个事件只允许注册一个类  
Java类名 | 一个遵循AWS事件接口实现的Java程序，格式：类路径+类名  
注册 | 将指定的Java类注册到组件，多次为同一个组件执行【注册】等同修改  
删除 | 将Java类从一个事件中移走  
  
## 视图加载前的触发器

项 | 说明  
---|---  
接口 | DataWindowBeforeLoadEventInterface  
返回值 | 一个JSON结构  
  
### 常见使用场景

**１.针对不同用户是否可查看该视图 ２.实现参数处理**

[![](https://helpcdn.awspaas.com/picture/picture/202309/2aab8e91459949a6b627f2f7664ca29e.png)](<https://helpcdn.awspaas.com/picture/picture/202309/2aab8e91459949a6b627f2f7664ca29e.png>)

### 开发示例
    
    
    import java.util.HashMap;
    
    import com.actionsoft.bpms.dw.design.event.DataWindowBeforeLoadEventInterface;
    import com.actionsoft.bpms.dw.exec.component.DataView;
    import com.actionsoft.bpms.dw.exec.component.model.awsdw.ExecDataViewModel;
    import com.actionsoft.bpms.server.UserContext;
    import com.alibaba.fastjson.JSONObject;
    
    /**
     * 视图加载前的触发器
     *
     * @return 格式化好的sql语句 说明： 1.必须实现类 com.actionsoft.bpms.dw.design.event.DataWindowBeforeLoadEventInterface 2.此示例实现的是 : admin用户不能查看此视图
     */
    public class DataWindowBeforeLoadEvent implements DataWindowBeforeLoadEventInterface {
      public boolean excute(UserContext me, DataView view) {
        //1.可以实现判断权限的功能
        //    if (me.getUID().equals("admin")){
        //      return false;
        //    }
        //2.实现参数处理
        ExecDataViewModel execDataViewModel = (ExecDataViewModel) view.getDw().getExtendParams().get("ExecDataViewModel");
        JSONObject extendParams = execDataViewModel.getExtendConfig();
        //2.1.获取url自定义参数
        JSONObject urlConfig = extendParams.getJSONObject("urlConfig");
        if (urlConfig != null) {
          JSONObject stObj = (JSONObject) urlConfig.get("st");
          if (stObj != null) {
            //可以获取URL传入的自定义的参数（小心SQL注入）
            String urlParamA = stObj.getString("urlParamA");
          }
        }
        //2.2.把需要的业务参数放到请求参数中,前端页面可以通过DWApi.view.model.extendConfig.params获取相关参数
        JSONObject params = new JSONObject();
        params.put("typeA", 1);
        params.put("typeB", 2);
        params.put("id", 5566);
        extendParams.put("params", params);
        //3.可以操作部分属性，此示例会取消所有条件查询
        execDataViewModel.getSearcher().getLikecondition().clear();
        return true;
      }
    }
    

### 注册事件

进入视图模型配置页面，点击【视图名称 > 高级选项】，打开侧边栏切换至【事件】页签，注册事件。

[![](https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png)](<https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png>)

[![](https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png)](<https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png>)

### 调试运行

完成事件注册后，点编辑视图模型主页右上角【预览】按钮进行调试运行。

[![](https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png)](<https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png>)

## 格式化表格SQL语句的触发器

项 | 说明  
---|---  
接口 | DataWindowFormatSQLEventInterface  
返回值 | 一个SQL片段  
  
### 常见使用场景

**不同用户查看数据不同**

[![](https://helpcdn.awspaas.com/picture/picture/202309/2aab8e91459949a6b627f2f7664ca29e.png)](<https://helpcdn.awspaas.com/picture/picture/202309/2aab8e91459949a6b627f2f7664ca29e.png>)

### 开发示例
    
    
    import java.util.Map;
    import com.actionsoft.bpms.dw.design.event.DataWindowFormatSQLEventInterface;
    import com.actionsoft.bpms.dw.exec.component.DataView;
    import com.actionsoft.bpms.server.UserContext;
    
    public class DataWindowFormatSQLEvent implements DataWindowFormatSQLEventInterface {
    
    /**
     * 格式化SQL语句的触发器
     *
     * @param me 用户上下文
     * @param view dw视图对象
     * @param sql sql语句
     * @return 格式化好的sql语句
     * 说明:1.必须实现类 com.actionsoft.bpms.dw.design.event.DataWindowFormatSQLEventInterface
     *     2.示例说明:只有admin用户能够查询所有数据,其他用户只能查看自己创建的信息
     */
    
      public String formatSQL(UserContext me, DataView view, String sql) {
        if (!"admin".equals(me.getUID())) {
          sql = sql.replace("1=1", "createuser = '" + me.getUID() + "'");
        }
        // 如果需要改变查询条件的值
        Map<String, Object> sqlParam = view.getDatagrid().getSqlParams();
        sqlParam.put("NAME", "森林好小子");// 注意多个同名参数是以NAME,NAME0,NAME1,NAME2...做为key来存放值
        return sql;
      }
    }
    

### 注册事件

进入视图模型配置页面，点击【视图名称 > 高级选项】，打开侧边栏切换至【事件】页签，注册事件。

[![](https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png)](<https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png>)

[![](https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png)](<https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png>)

### 调试运行

完成事件注册后，点编辑视图模型主页右上角【预览】按钮进行调试运行。

[![](https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png)](<https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png>)

## 删除数据后的触发器

项 | 说明  
---|---  
接口 | DataWindowAfterDeleteInterface  
返回值 | 无  
  
### 常见使用场景

**一般用于刷新缓存**

### 开发示例
    
    
    import java.util.List;
    
    import com.actionsoft.apps.AppPlatformConfig;
    import com.actionsoft.apps.resource.AppTeam;
    import com.actionsoft.bpms.bo.engine.BO;
    import com.actionsoft.bpms.dw.design.event.DataWindowAfterDeleteInterface;
    import com.actionsoft.bpms.server.UserContext;
    
    /**
     * 数据删除后触发器
     *
     * 说明:1.必须实现类com.actionsoft.bpms.dw.design.event.DataWindowAfterDeleteInterface
     * 2.一般用于刷新缓存
     */
    public class DataWindowAfterDeleteEvent implements DataWindowAfterDeleteInterface {
    
      /**
       * @param me 用户上下文
       * @param boDatas 删除后的旧数据（用于逻辑处理）
       * @param boName 表名称
       */
      @Override
      public void excute(UserContext me, List<BO> boDatas, String boName) {
        //此示例实现删除该表数据后删除DEVTeam组中userid的成员
        for (BO formData : boDatas) {
          String userid = formData.getString("USERID");
          AppTeam team = AppPlatformConfig.getAppTeamById( "DEVTeam");
          team.getMembers().remove(userid);
        }
      }
    }
    

### 注册事件

进入视图模型配置页面，点击【视图名称 > 高级选项】，打开侧边栏切换至【事件】页签，注册事件。

[![](https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png)](<https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png>)

[![](https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png)](<https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png>)

### 调试运行

完成事件注册后，点编辑视图模型主页右上角【预览】按钮进行调试运行。

[![](https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png)](<https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png>)

## 格式化表格数据的触发器

项 | 说明  
---|---  
接口 | DataWindowFormatDataEventInterface  
返回值 | 无  
  
### 常见使用场景

**1\. 更改页面数据显示** **2\. 格式化导出数据**

### 开发示例
    
    
     import java.sql.ResultSet;
    import java.sql.SQLException;
    
    import com.actionsoft.bpms.dw.design.event.DataWindowFormatDataEventInterface;
    import com.actionsoft.bpms.dw.exec.component.Column;
    import com.actionsoft.bpms.dw.exec.data.DataSourceEngine;
    import com.actionsoft.bpms.server.UserContext;
    import com.alibaba.fastjson.JSONArray;
    import com.alibaba.fastjson.JSONObject;
    
    public class DataWindowFormatDataEvent implements DataWindowFormatDataEventInterface {
     /**
      * 格式化表格数据的触发器
      *
      * @param me 用户上下文
      * @param JSONArray 数据对象
      * 说明：1.必须实现类 com.actionsoft.bpms.dw.design.event.DataWindowFormatDataEventInterface
      *    2.此示例实现的是 : 如果字段"ZT",为0显示错误图标,为1显示正确图标,为其他显示警示图标
      *    3.如果需要在数据导出时应用格式化数据请实现formatGridExport方法（如果不需要则不实现）
      */
     public void formatData(UserContext me, JSONArray datas) {
      for (Object datao : datas) {
       JSONObject data = (JSONObject) datao;
       String columnValue = data.getString("ZT"); // 注意有些特殊组件的值为JSONObject，请根据情况使用getJSONObject获取相应值
       switch (columnValue) {
       case "0":
        columnValue = "<img src=../apps/_bpm.platform/img/model/form_designer/error.png border=0/>";
        break;
       case "1":
        columnValue = "<img src=../apps/_bpm.platform/img/model/form_designer/ok.png border=0/>";
        break;
       default:
        columnValue = "<img src=../apps/_bpm.platform/img/model/form_designer/warn.png border=0/>";
        break;
        }
       //虚拟字段VIRTUALBUTTON ，组件为按钮不显示
       //data.put("VIRTUALBUTTON" ,"");
       //data.put("COLUMNTYPE_VIRTUALBUTTON", "");
       data.put("ZT" + DataSourceEngine.AWS_DW_FIXED_CLOMUN_SHOW_RULE_SUFFIX, columnValue);
      }
     }
    
     /**
      * 格式化导出数据
      *
      * @param me 用户session
      * @param rs 数据库结果集
      * @param colModel 字段的相关配置模型
      * @param fieldId 字段名
      * @return null 时不执行
      */
     public String formatGridExport(UserContext me, ResultSet rs, Column colModel, String fieldId) {
      String ss = null;
      try {
       if (fieldId.equals("NAME")) { // 如果名字是NAME
        ss = rs.getString(fieldId) + "Helden sterben nicht!"; // 则执行
       }
      } catch (SQLException e) {
       e.printStackTrace();
      }
      return ss;
     }
    }
    

### 注册事件

进入视图模型配置页面，点击【视图名称 > 高级选项】，打开侧边栏切换至【事件】页签，注册事件。

[![](https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png)](<https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png>)

[![](https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png)](<https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png>)

### 调试运行

完成事件注册后，点编辑视图模型主页右上角【预览】按钮进行调试运行。

[![](https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png)](<https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png>)

## 自定义表格数据的触发器

项 | 说明  
---|---  
接口 | DataWindowCustomGridDataInterface  
返回值 | 一个JSON对象，代表一套完整的表格数据  
  
### 常见使用场景

**1\. 更改页面数据显示** **2\. 格式化导出数据**

### 开发示例
    
    
    import java.util.Map;
    import com.actionsoft.bpms.commons.mvc.view.ResponseObject;
    import com.actionsoft.bpms.dw.design.event.DataWindowCustomGridDataInterface;
    import com.actionsoft.bpms.dw.exec.component.DataView;
    import com.actionsoft.bpms.server.UserContext;
    import com.alibaba.fastjson.JSONArray;
    import com.alibaba.fastjson.JSONObject;
    
    public class DataWindowCustomGridDataEvent implements DataWindowCustomGridDataInterface {
      /**
       * 自定义表格数据的触发器
       *
       * @param me 用户上下文
       * @param view 当前视图对象
       * @param pageNow 要查询的页数
       * @param condition 查询条件
       * @param eventParams 附加属性
       * 说明:1.必须实现类com.actionsoft.bpms.dw.design.event.DataWindowCustomGridDataInterface
       *    2.示例说明:自定义返回一套数据(需要做好创建好数据列表)
       */
      @Override
      public JSONObject excute(UserContext me, DataView view, int pageNow, JSONObject condition, Map<String, Object> eventParams) {
        ResponseObject responseObject = ResponseObject.newOkResponse();
        // 数据源可以通过自定义代码进行获取例如从WebService获取的数据源但要符合相应的JSON格式
        //JSON格式如下
        JSONObject maindata = new JSONObject();
        maindata.put("identifier", "ID");//主键ID列名称
        maindata.put("pageCount", 5); //总页数
        maindata.put("pageNow", 1);//当前页
    
        //分页信息
        JSONObject pageInfo = new JSONObject();
        pageInfo.put("totalsum", new JSONObject());
        pageInfo.put("total", 12);//数据总条数
        pageInfo.put("from", 1); //当前页显示，从第几条起
        pageInfo.put("to", 4); //当前页显示，到第几条结束
        maindata.put("pageInfo", pageInfo);
    
        //数据信息
        JSONArray items = new JSONArray();
    
        //其中一条信息
        JSONObject item = new JSONObject();
        item.put("NUM", 26);
        item.put("TIME", "2018");
        item.put("PLACE", "日本东京>");
        item.put("NAME", "小怪兽>");
        item.put("TYPE", "动画>");
        item.put("ID", "8cb8d560-736d-4e24-aa3a-414f7e505acc");
        item.put("AWS_DW_SELECTED_ID", "8cb8d560-736d-4e24-aa3a-414f7e505acc");//这个参数值要与对应主键ID的值一致
    
        //一条信息的附加信息(防止空指针)
        JSONObject AWS_DW_FIXED_COLUMN_STYLE = new JSONObject();
        AWS_DW_FIXED_COLUMN_STYLE.put("statusImg", "");
        AWS_DW_FIXED_COLUMN_STYLE.put("fontColor", "");
        AWS_DW_FIXED_COLUMN_STYLE.put("priority", "");
        AWS_DW_FIXED_COLUMN_STYLE.put("isReaded", 1);
        AWS_DW_FIXED_COLUMN_STYLE.put("isCanDelete", 1);
        AWS_DW_FIXED_COLUMN_STYLE.put("h_s_l", 0);
        item.put("AWS_DW_FIXED_COLUMN_STYLE", AWS_DW_FIXED_COLUMN_STYLE);
        items.add(item);
        maindata.put("items", items);
    
        responseObject.put("maindata", maindata);
        //标签查询信息
        responseObject.put("ls", new JSONArray());
        return responseObject.toJSONObject();
      }
    }
    

### 注册事件

进入视图模型配置页面，点击【视图名称 > 高级选项】，打开侧边栏切换至【事件】页签，注册事件。

[![](https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png)](<https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png>)

[![](https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png)](<https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png>)

### 调试运行

完成事件注册后，点编辑视图模型主页右上角【预览】按钮进行调试运行。

## 导出事件的触发器

项 | 说明  
---|---  
接口 | DataWindowExportGridEventInterface  
返回值 | 无  
  
### 常见使用场景

**1\. 视图数据导出时，更改导出内容，如将表格中的附件一并导出**

### 开发示例
    
    
    import java.io.File;
    import java.io.InputStream;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    
    import org.apache.poi.hssf.usermodel.HSSFWorkbook;
    import org.apache.poi.xssf.streaming.SXSSFWorkbook;
    
    import com.actionsoft.apps.AppsConst;
    import com.actionsoft.apps.resource.plugin.profile.DCPluginProfile;
    import com.actionsoft.bpms.bo.design.model.BOItemModel;
    import com.actionsoft.bpms.commons.cache.iae.model.IAEModel;
    import com.actionsoft.bpms.commons.formfile.dao.FormFileDao;
    import com.actionsoft.bpms.commons.formfile.model.delegate.FormFile;
    import com.actionsoft.bpms.dw.design.event.DataWindowExportGridEventInterface;
    import com.actionsoft.bpms.dw.design.model.DWModel;
    import com.actionsoft.bpms.dw.exec.component.Column;
    import com.actionsoft.bpms.server.UserContext;
    import com.actionsoft.bpms.server.fs.DCContext;
    import com.actionsoft.bpms.server.fs.dc.DCConst;
    import com.actionsoft.bpms.server.fs.dc.DCProfileManager;
    import com.actionsoft.bpms.server.fs.dc.DCStoreUtil;
    import com.actionsoft.bpms.util.UtilFile;
    import com.actionsoft.i18n.I18nRes;
    import com.alibaba.fastjson.JSONArray;
    import com.alibaba.fastjson.JSONObject;
    import com.csvreader.CsvWriter;
    
    public class DataWindowExportGridEvent implements DataWindowExportGridEventInterface {
      /**
       * 示例：用于把DW数据中的附件与excel一同压缩后导出
       *
       * @param me 用户上下文
       * @param eventContext 事件上下文
       */
      @Override
      public void exportAfter(UserContext me, Map<String, Object> eventContext, CreateExportFile createExportFile) {
        DWModel dwModel = (DWModel) eventContext.get("DWModel");//dw模型对象(仅用于读取，禁止修改，否则后果自负)
        String cacheId = (String) eventContext.get("cacheId");//导出任务ID
        JSONObject configJson = (JSONObject) eventContext.get("configJson");//导出任务配置
        String viewId = (String) eventContext.get("viewId");//当前viewId
        List<Column> showColumnList = (List<Column>) eventContext.get("showColumnList");//导出字段列表
        JSONObject multiHeaderJson = (JSONObject) eventContext.get("multiHeaderJson");//多级表头配置（如果需要）
        JSONArray exportData = (JSONArray) eventContext.get("exportData");//导出的数据（包含ID和BINDID）
        String type = (String) eventContext.get("type");//导出格式
        if (type.equals("xlsx")) {
          SXSSFWorkbook wb = (SXSSFWorkbook) eventContext.get("workbook");//poi对象,按需获取避免报错
        }
        if (type.equals("xls")) {
          HSSFWorkbook wb = (HSSFWorkbook) eventContext.get("workbook");//poi对象,按需获取避免报错
        }
        if (type.equals("csv")) {
          CsvWriter wb = (CsvWriter) eventContext.get("workbook");//Writer,按需获取避免报错
        }
        //找出field字段配置
        Column fieldColumn = null;
        for (Column column : showColumnList) {
          //F_YXVFCZJY 是附件字段名称
          if (column.getField().equals("F_YXVFCZJY")) {
            fieldColumn = column;
            break;
          }
        }
        //找到bo配置
        BOItemModel boItemModel = (BOItemModel) fieldColumn.getExtendParams().get("boItemModel");
        String groupValue = "dw~temp~file";
        String zipDir = "tempzip";
        String fileValue = zipDir + "/" + cacheId;
        DCPluginProfile profile = DCProfileManager.getDCProfile(AppsConst.SYS_APP_PLATFORM, DCConst.REPOSITORY_TEMP);
        Map<String, Integer> msi = new HashMap<>();
        //遍历数据，找到该字段的所有文件，统一copy到同一路径下
        String appId = AppsConst.SYS_APP_PLATFORM;//;
        exportData.forEach(o -> {
          JSONObject rowData = (JSONObject) o;
          FormFileDao dao = new FormFileDao();// 查询当前表中 当前字段的所有文件
          List<FormFile> files = dao.queryByBoFieldName(rowData.getString("ID"), boItemModel.getName(), "FILENAME", true);
          for (FormFile fFile : files) {
            String fieldName = fFile.getFileName();
            DCContext fileDc = new DCContext(me, DCProfileManager.getDCProfile(dwModel.getAppId(), DCConst.REPOSITORY_UI_FILE), dwModel.getAppId(), fFile.getId(), fFile.getBoItemName(), fieldName);
            try {
              String toFieldName = fieldName;//防止重名
              if (msi.containsKey(fieldName)) {
                int count = msi.get(fieldName) + 1;
                toFieldName = fieldName + count; //注意：此处不提供处理后缀
                msi.put(fieldName, count);
              } else {
                msi.put(fieldName, 0);
              }
              InputStream in = DCStoreUtil.read(fileDc);
              DCStoreUtil.write(new DCContext(me, profile, appId, groupValue, fileValue, fieldName), in);
            } catch (Exception e) {
              e.printStackTrace();
            }
          }
        });
        //执行excel的文件写入
        //！！！注意如果执行 createExportFile.execute，则必须执行 eventContext.put("dc", exportFiledc);否则造成重复创建导出文件，并造成错误
        DCContext exportFiledc = createExportFile.execute();//此处进行创建导出的excel文件
        //重新命名excel文件名称
        String fileTitle = I18nRes.findValue(me.getLanguage(), dwModel.getTitle().getLabel() + "（" + dwModel.getViewById(viewId).getLabel() + "）");
        exportFiledc.setFileNameShow(fileTitle + "." + type);
        //复制excel文件到压缩目录
        try {
          InputStream in = DCStoreUtil.read(exportFiledc);
          DCStoreUtil.write(new DCContext(me, profile, appId, groupValue, fileValue, exportFiledc.getFileNameShow()), in);
        } catch (Exception e) {
          e.printStackTrace();
        }
        //压缩该目录的所有文件
        String zipFileName = "zip文件名" + ".zip";
        DCContext zipDcContext = new DCContext(me, profile, appId, groupValue, zipDir, zipFileName);
        zipDcContext.setFileNameShow(zipFileName);
        try {
          UtilFile.zipCompress(zipDcContext.getPath() + cacheId, new File(zipDcContext.getFilePath()));
        } catch (Exception e) {
          e.printStackTrace();
        }
        //！！！注意，如果在上下文参数中放入dc，程序会使用此dc作为文件下载入口，不再执行默认生成导出文件的行为
        eventContext.put("dc", zipDcContext);//放入zip文件让程序进行下载
      }
    
      /**
       * 导出前事件
       *
       * @param me 用户上下文
       * @param eventContext 事件上下文
       */
      @Override
      public void exportBefore(UserContext me, Map<String, Object> eventContext) {
        //无操作空实现即可
      }
    
      /**
       * 导出前准备事件
       * 示例：更改导出显示的名称
       *
       * @param me 用户上下文
       * @param eventContext 事件上下文
       */
      @Override
      public void exportPrepare(UserContext me, Map<String, Object> eventContext) {
        DWModel dwModel = (DWModel) eventContext.get("DWModel");//dw模型对象(仅用于读取，禁止修改，否则后果自负)
        String cacheId = (String) eventContext.get("cacheId");//导出任务ID
        JSONObject configJson = (JSONObject) eventContext.get("configJson");//导出任务配置
        String viewId = (String) eventContext.get("viewId");//当前viewId
        IAEModel iaeModel = (IAEModel) eventContext.get("iaeModel");//任务缓存
        iaeModel.setFileName("zip文件名" + ".zip");
      }
    }
    

### 注册事件

进入视图模型配置页面，点击【视图名称 > 高级选项】，打开侧边栏切换至【事件】页签，注册事件。

[![](https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png)](<https://helpcdn.awspaas.com/picture/picture/202309/aed0e4beeac34846b8b2130dc7fd79eb.png>)

[![](https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png)](<https://helpcdn.awspaas.com/picture/picture/202309/81ee19cac42c465097207c795ca0f860.png>)

### 调试运行

完成事件注册后，点编辑视图模型主页右上角【预览】按钮进行调试运行。

[![](https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png)](<https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png>)

[![](https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png)](<https://helpcdn.awspaas.com/picture/picture/202309/7193873895f14ae884666366425e9c60.png>)