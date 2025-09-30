# 地址簿 | AWS UI组件参考指南

## 地址簿

创建一个地址簿控件，这是一个私有封装。用于显示和修改被表单数据源绑定的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。

### 运行

PC端  
---  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addressR1.png)  
移动端  
![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addressR1_m.png)  
  
> 只显示最近的10条记录

**预置校验**

  * 参见单行[预置校验](<text.html#check>)

  * 若输入一个非法的账户名，不允许保存

  * 支持键盘模糊提示(liveSearch)

### 设计

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addressD3.png)

**基本属性**

  * **_查询列宽_**

参见单行[查询列宽](<text.html#searchwidth>)

  * **_显示规则_**

参见单行[显示规则](<text.html#displayrule>)

  * **_帮助说明_**

参见单行[帮助说明](<text.html#tooltip>)

  * **_扩展代码_**

    * 参见单行[扩展代码](<text.html#componentExtendCode>)

    * readonly仅控制文本框不可输入，但按钮还是可以点击

    * disabled控制文本框和按钮均不可使用

**扩展属性**

  * **_空值提示_**

参见单行[空值提示](<text.html#nulltip>)

  * **_地址簿类型_**

地址簿分为人员地址簿和部门地址簿两种

    * **人员地址簿**

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addressD1.png)

> 1.**模式** 普通模式和高级模式两种。以下属性项仅在高级模式时可用
> 
> 2.**叶子节点类型** `用户`树节点显示到用户;`部门`树节点仅显示到部门；`团队`树节点仅显示到团队
> 
> 3.**分类方式** 仅在`叶子节点类型`为`用户`时可用，可选范围：部门、角色、团队
> 
> 4.**兼任** 勾选`显示`后树结构将显示组织模型添加兼职信息时，`是否显示`属性为`是`的兼职人员。有关兼职的设置请参见 <https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-org/organization/usermap.html> 。 _注： 兼职是否显示在6.3.1.0626 版本后提供一个总开关`AWS Portal门户` 应用参数`地址薄显示兼职人员(addressDisplayMap)` _ 详细见该参数说明
> 
> 5.**选择模式** `单选`,只允许选择一个值;`多选`,允许选择多个值
> 
> 6.分隔符 仅在`选择模式`为`多选`时可用，多值之间的分隔符
> 
> 7.**取值字段** 指定取值字段，多个值用","隔开
> 
> 8.**回填字段** 指定回填字段，多个值用","隔开，【取值字段】和【回填字段】个数和次序必须匹配
> 
> 10.**过滤范围** `部门层级`,只显示部门层级范围内的部门，例如【从1到3】 `隐藏作为公司的子部门` 该属性仅当部门来源于HR组织管理应用时有效
> 
> 11.**过滤事件** 一个实现com.actionsoft.bpms.ui.dict.address.base.AddressUIFilterInterface接口的类，由自定义的Java程序控制树形节点的显示，例如【根据当前人的身份过滤掉不允许显示的部门、角色人员】  
> 
          
          import com.actionsoft.bpms.org.model.DepartmentModel;
          import com.actionsoft.bpms.org.model.UserModel;
          import com.actionsoft.bpms.server.UserContext;
          import com.actionsoft.bpms.ui.dict.address.base.AddressUIFilterInterface;
          import com.actionsoft.bpms.ui.dict.address.model.AdvancedAddressModel;
          
          /**
          * 地址本UI组件的过滤事件
          * @author Administrator
          *
          */
          public class AddressUIFilterTest implements AddressUIFilterInterface {
          
           @Override
            public boolean addressUIFlexCompanyFilter(UserContext uc, CompanyModel model, AdvancedAddressModel advancedAddressModel) {
                if(model.getName().equals("炎黄盈动")){
                    return true;
                }else{
                    return false;
                }
            }
          
             @Override
              public boolean addressUIFlexDepartmentFilter(UserContext uc, DepartmentModel model,AdvancedAddressModel advancedAddressModel) {
                  if (model.getName().equals("总裁办")) {
                      String choiceType = advancedAddressModel.getChoiceType();
                      advancedAddressModel.setLeafType("department");
                      return true;
                  }
                  return true;
              }
          
              @Override
                 public boolean addressUIFlexUserFilter(UserContext uc, UserModel userModel, AdvancedAddressModel aa) {
                if (HighSecurity.isON()) { //判断是否开启密级设置
                    int currSecurityLevel = uc.getUserModel().getSecurityLevel();
                    if (currSecurityLevel <= userModel.getSecurityLevel()){
                        if (userModel.getUserName().equals("测试用户")) {
                            return false;
                        }else{
                            return true;
                        }
                        }
                    return false;
                } else {
                    if (userModel.getUserName().equals("测试用户")) {
                            return false;
                        }else{
                            return true;
                    }
                }
            }
          }
          

> 12.**单位列表** 如果不配置该属性，默认显示自己所在实体单位及有权限访问的实体单位；如果配置该属性，显示配置的并且有权限的单位（包括实体单位和虚拟单位）  
>  13.**数据源接口** 一个继承com.actionsoft.bpms.ui.dict.address.base.AddressUISourceDataAbs的类，由自定义的Java程序控制树形节点的内容  
> 

    
    
        package com.actionsoft.bpms.ui.dict.address.base;
    
        import com.actionsoft.bpms.server.UserContext;
        import com.alibaba.fastjson.JSONArray;
        import com.alibaba.fastjson.JSONObject;
    
        public abstract class AddressUISourceDataAbs implements AddressUISourceDataInterface {
            /**
             * 获取地址簿树跟节点
             *
             * @param appId 应用id
             * @param filter 地址簿配置
             * @param context 用户上下文
             * @return
             */
            public abstract JSONArray getOrgTreeData(String appId, JSONObject filter, UserContext context);
    
            /**
             * 获取地址簿树子节点  移动端时从根目录开始pid=='' && pType == ''时是根目录
             *
             * @param appId 应用id
             * @param filter 地址簿配置
             * @param context 用户上下文
             * @param pid 父节点id
             * @param pType 父节点类型
             * @return
             */
            public abstract JSONArray getSubJsonData(String appId, JSONObject filter, UserContext context, String pid, String pType);
    
            /**
             * 查询地址簿
             *
             * @param appId 应用id
             * @param filter 地址簿配置
             * @param context 用户上下文
             * @param sourceField 地址簿回填字段
             * @param type 查询类型 同地址簿叶子节点
             * @param keyWord 查询关键字
             * @param limit 每页条数
             * @param start 起始条数
             * @return 包含 总数量 totalNum 总数量 ； 查询列表 list(JSONArray)
             */
            public abstract JSONObject search(String appId, JSONObject filter, UserContext context, String sourceField, String type, String keyWord, int limit, int start);
    
            /**
             * 地址簿显示值（主要是返回值中有uid 或deptid 或 teamID 显示值需要具体信息用来显示）
             *
             * @param appId 应用id
             * @param filter 地址簿配置
             * @param context 用户上下文
             * @param value 用户账号或部门id
             * @return 包含 id ：用户账号或部门id ；name： 用户名称或部门名称
             */
            public abstract JSONObject addressDisplayValue(String appId, JSONObject filter, UserContext context, String value);
            /**获取父节点 移动端使用
             * @param appId 应用id
             * @param filter 地址簿配置
             * @param context 用户上下文
             * @param nodeId 当前节点id
             * @param nodeType 当前节点类型
             * @return
             */
            public abstract JSONObject getParentTreeNode(String appId, JSONObject filter, UserContext context, String nodeId, String nodeType);
        }
    
    
    
         import java.util.ArrayList;
         import java.util.Collections;
         import java.util.HashMap;
         import java.util.Iterator;
         import java.util.List;
         import java.util.Map;
    
         import com.actionsoft.apps.AppsConst;
         import com.actionsoft.bpms.commons.security.high.HighSecurity;
         import com.actionsoft.bpms.commons.security.high.model.HighSecurityModel;
         import com.actionsoft.bpms.commons.security.mgtgrade.util.GradeSecurityUtil;
         import com.actionsoft.bpms.org.cache.CompanyCache;
         import com.actionsoft.bpms.org.cache.DepartmentCache;
         import com.actionsoft.bpms.org.cache.TeamCache;
         import com.actionsoft.bpms.org.cache.UserCache;
         import com.actionsoft.bpms.org.cache.UserMapCache;
         import com.actionsoft.bpms.org.model.CompanyModel;
         import com.actionsoft.bpms.org.model.DepartmentModel;
         import com.actionsoft.bpms.org.model.TeamModel;
         import com.actionsoft.bpms.org.model.UserMapModel;
         import com.actionsoft.bpms.org.model.UserModel;
         import com.actionsoft.bpms.org.util.AddressBookUserMapComparator;
         import com.actionsoft.bpms.org.util.SecurityUtil;
         import com.actionsoft.bpms.server.UserContext;
         import com.actionsoft.bpms.server.conf.ConfigConst;
         import com.actionsoft.bpms.ui.dict.address.base.AddressUISourceDataAbs;
         import com.actionsoft.bpms.ui.dict.address.util.AdvancedAdrressUtil;
         import com.actionsoft.bpms.util.UtilSerialize;
         import com.actionsoft.bpms.util.UtilString;
         import com.actionsoft.sdk.local.SDK;
         import com.alibaba.fastjson.JSONArray;
         import com.alibaba.fastjson.JSONObject;
    
         public class AddressUISourceDataTest extends AddressUISourceDataAbs {
             /**
              * 获取地址簿树跟节点
              *
              * @param filter
              * @return
              */
             public JSONArray getOrgTreeData(String appId, JSONObject filter, UserContext context) {
                 JSONArray treeData = new JSONArray();
                 //单位列表
                 String companyList = filter.getString("companyList");
                 JSONObject addressSetting = filter.getJSONObject("addressSetting");
                 //部门根目录，多个用|隔开
                 String rootDetpId = addressSetting.getString("rootDetpId");
                 //部门层级
                 int layerFrom = -1;
                 int layerTo = 9999;
                 String layerFromStr = addressSetting.getString("layerFrom");
                 if (!UtilString.isEmpty(layerFromStr)) {
                     layerFrom = Integer.parseInt(layerFromStr);
                 }
                 String layerToStr = addressSetting.getString("layerTo");
                 if (!UtilString.isEmpty(layerToStr)) {
                     layerTo = Integer.parseInt(layerToStr);
                 }
                 //取值字段
                 String sourceField = filter.getString("sourceField");
                 //叶子节点
                 String leafType = addressSetting.getString("leafType");
                 /*//返回单位json
                 JSONObject json = new JSONObject();
                 json.put("id", "单位id");
                 json.put("name", "单位名称");
                 json.put("iconCls", "company");
                 json.put("iconFont", "&#xe6ff;");
                 json.put("open", "是否展开 true|false");
                 json.put("nocheck", true);
                 json.put("type", "company");
                 //以下内容用来回填数据
                 json.put("COMPANYNAME", "单位名称");
                 json.put("COMPANYID", "单位id");
                 json.put("COMPANYNO", "单位编码");
                 treeData.add(json);*/
                 //返回部门json
                 /*JSONObject json = new JSONObject();
                 json.put("iconCls", "dept");
                 json.put("iconFont", "&#59318;");
                 json.put("pid", "父节点id");
                 json.put("type", "dept");
                 if (leafType.equals("dept")) {
                     json.put("leaf", true);//是否叶子节点
                 }
                 json.put("open", false);
                 json.put("layer", "部门层级");
                 json.put("size", "部门下人员个数");
                 json.put("sourceId", "部门id");
                 json.put("id", "部门id");
                 json.put("name", "部门名称");
                 json.put("type", "dept");
                 json.put("fullPathName", "部门全路径");
                 //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                 if (!UtilString.isEmpty(sourceField)) {
                     JSONObject temp = new JSONObject();
                     temp.put("COMPANYNAME", "公司名称");
                     temp.put("COMPANYID", "公司id");
                     temp.put("COMPANYNO", "公司编码");
                     temp.put("DEPTNAME", "部门名称");
                     temp.put("DEPTID", "部门id");
                     temp.put("DEPTFULLPATHID", "部门id全路径");
                     temp.put("DEPTFULLPATHNAME", "部门名称全路径");
                     temp.put("DEPTNO", "部门代码");
                     temp.put("DEPTZONE", "区域划分");
                     temp.put("DEPTTYPE", "部门类型");
                     temp.put("EXT1", "扩展标记1");
                     temp.put("EXT2", "扩展标记2");
                     temp.put("EXT3", "扩展标记3");
                     temp.put("EXT4", "扩展标记4");
                     temp.put("EXT5", "扩展标记5");
                     String[] sourceFields = sourceField.split(",");
                     for (String field : sourceFields) {
                         json.put(field, temp.getString(field));
                     }
                 }*/
                 /*//返回人员的json
                 JSONObject json = new JSONObject();
                 json.put("sourceId", "用户帐号");
                 json.put("id", "用户帐号");
                 json.put("name", "用户姓名");
                 json.put("type", "user");
                 json.put("USERNAMEALIAS", "用户全名");
                 //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                 if (!UtilString.isEmpty(sourceField)) {
                     JSONObject temp = new JSONObject();
                     temp.put("COMPANYNAME", "单位名称");
                     temp.put("COMPANYID", "单位id");
                     temp.put("COMPANYNO", "单位编码");
                     temp.put("EMAIL", "邮箱");
                     temp.put("USERNAME", "用户姓名");
                     temp.put("DEPTID", "部门id");
                     temp.put("DEPTFULLPATHID", "部门id全路径");
                     temp.put("DEPTFULLPATHNAME", "部门名称全路径");
                     temp.put("DEPTFULLPATHNAMEWITHCOMPNAY", "部门全路径名称(含单位)");
                     temp.put("DEPTNAME", "部门名称");
                     temp.put("DEPTNO", "部门编码");
                     temp.put("ROLEID", "角色id");
                     temp.put("UID", "用户帐号");
                     temp.put("USERID", "用户ID");
                     temp.put("USERNO", "员工代码");
                     temp.put("USERNAME", "用户姓名");
                     temp.put("USERNAMEALIAS", "用户全名");
                     temp.put("EMAIL", "邮箱");
                     temp.put("OFFICETEL", "电话");
                     temp.put("MOBILE", "手机");
                     temp.put("OFFICEFAX", "传真");
                     temp.put("POSITIONNAME", "职位名称");
                     temp.put("POSITIONNO", "职位编码");
                     temp.put("POSITIONLAYER", "职位等级");
                     temp.put("EXT1", "扩展标记1");
                     temp.put("EXT2", "扩展标记2");
                     temp.put("EXT3", "扩展标记3");
                     temp.put("EXT4", "扩展标记4");
                     temp.put("EXT5", "扩展标记5");
                     String[] sourceFields = sourceField.split(",");
                     for (String field : sourceFields) {
                         json.put(field, temp.getString(field));
                     }
                 }*/
    
                 return treeData;
             }
    
             /**
              * 获取地址簿树子节点 移动端时从根目录开始pid=='' && pType == ''时是根目录
              *
              * @param filter
              * @return
              */
             public JSONArray getSubJsonData(String appId, JSONObject filter, UserContext context, String pid, String pType) {
                 JSONArray treeData = new JSONArray();
                 //单位列表
                 String companyList = filter.getString("companyList");
                 JSONObject addressSetting = filter.getJSONObject("addressSetting");
                 //部门根目录，多个用|隔开
                 String rootDetpId = addressSetting.getString("rootDetpId");
                 //部门层级
                 int layerFrom = -1;
                 int layerTo = 9999;
                 String layerFromStr = addressSetting.getString("layerFrom");
                 if (!UtilString.isEmpty(layerFromStr)) {
                     layerFrom = Integer.parseInt(layerFromStr);
                 }
                 String layerToStr = addressSetting.getString("layerTo");
                 if (!UtilString.isEmpty(layerToStr)) {
                     layerTo = Integer.parseInt(layerToStr);
                 }
                 //取值字段
                 String sourceField = filter.getString("sourceField");
                 //叶子节点
                 String leafType = addressSetting.getString("leafType");
    
                 /*//返回单位json
                 JSONObject json = new JSONObject();
                 json.put("id", "单位id");
                 json.put("name", "单位名称");
                 json.put("iconCls", "company");
                 json.put("iconFont", "&#xe6ff;");
                 json.put("open", "是否展开 true|false");
                 json.put("nocheck", true);
                 json.put("type", "company");
                 json.put("fullPathName", "公司全路径");
                 //以下内容用来回填数据
                 json.put("COMPANYNAME", "单位名称");
                 json.put("COMPANYID", "单位id");
                 json.put("COMPANYNO", "单位编码");
                 treeData.add(json);*/
                 //返回部门json
                 /*JSONObject json = new JSONObject();
                 json.put("iconCls", "dept");
                 json.put("iconFont", "&#59318;");
                 json.put("pid", "父节点id");
                 json.put("type", "dept");
                 if (leafType.equals("dept")) {
                     json.put("leaf", true);//是否叶子节点
                 }
                 json.put("open", false);
                 json.put("layer", "部门层级");
                 json.put("size", "部门下人员个数");
                 json.put("sourceId", "部门id");
                 json.put("id", "部门id");
                 json.put("name", "部门名称");
                 json.put("type", "dept");
                 json.put("fullPathName", "部门全路径");
                 //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                 if (!UtilString.isEmpty(sourceField)) {
                     JSONObject temp = new JSONObject();
                     temp.put("COMPANYNAME", "公司名称");
                     temp.put("COMPANYID", "公司id");
                     temp.put("COMPANYNO", "公司编码");
                     temp.put("DEPTNAME", "部门名称");
                     temp.put("DEPTID", "部门id");
                     temp.put("DEPTFULLPATHID", "部门id全路径");
                     temp.put("DEPTFULLPATHNAME", "部门名称全路径");
                     temp.put("DEPTNO", "部门代码");
                     temp.put("DEPTZONE", "区域划分");
                     temp.put("DEPTTYPE", "部门类型");
                     temp.put("EXT1", "扩展标记1");
                     temp.put("EXT2", "扩展标记2");
                     temp.put("EXT3", "扩展标记3");
                     temp.put("EXT4", "扩展标记4");
                     temp.put("EXT5", "扩展标记5");
                     String[] sourceFields = sourceField.split(",");
                     for (String field : sourceFields) {
                         json.put(field, temp.getString(field));
                     }
                 }*/
                 /*//返回人员的json
                 JSONObject json = new JSONObject();
                 json.put("pid", pid);
                 if (部门主管) {
                     json.put("iconFont", UtilSerialize.parseObject("{'code':'&#58939;','color':'#DA2912'}"));
                 } else {
                     json.put("iconFont", "&#58939;");
                 }
                 json.put("sourceName", "用户姓名");
                 json.put("type", "user");
                 json.put("leaf", true);
                 json.put("sourceId", "用户帐号");
                 json.put("id",  "用户帐号"+ "_" + pid);
                 json.put("name", "用户姓名");
                 json.put("type", "user");
                 json.put("USERNAMEALIAS", "用户全名");
                 json.put("fullPathName", "所在部门全路径");
                 //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                 if (!UtilString.isEmpty(sourceField)) {
                     JSONObject temp = new JSONObject();
                     temp.put("COMPANYNAME", "单位名称");
                     temp.put("COMPANYID", "单位id");
                     temp.put("COMPANYNO", "单位编码");
                     temp.put("EMAIL", "邮箱");
                     temp.put("USERNAME", "用户姓名");
                     temp.put("DEPTID", "部门id");
                     temp.put("DEPTFULLPATHID", "部门id全路径");
                     temp.put("DEPTFULLPATHNAME", "部门名称全路径");
                     temp.put("DEPTFULLPATHNAMEWITHCOMPNAY", "部门全路径名称(含单位)");
                     temp.put("DEPTNAME", "部门名称");
                     temp.put("DEPTNO", "部门编码");
                     temp.put("ROLEID", "角色id");
                     temp.put("UID", "用户帐号");
                     temp.put("USERID", "用户ID");
                     temp.put("USERNO", "员工代码");
                     temp.put("USERNAME", "用户姓名");
                     temp.put("USERNAMEALIAS", "用户全名");
                     temp.put("EMAIL", "邮箱");
                     temp.put("OFFICETEL", "电话");
                     temp.put("MOBILE", "手机");
                     temp.put("OFFICEFAX", "传真");
                     temp.put("POSITIONNAME", "职位名称");
                     temp.put("POSITIONNO", "职位编码");
                     temp.put("POSITIONLAYER", "职位等级");
                     temp.put("EXT1", "扩展标记1");
                     temp.put("EXT2", "扩展标记2");
                     temp.put("EXT3", "扩展标记3");
                     temp.put("EXT4", "扩展标记4");
                     temp.put("EXT5", "扩展标记5");
                     String[] sourceFields = sourceField.split(",");
                     for (String field : sourceFields) {
                         json.put(field, temp.getString(field));
                     }
                 }*/
    
                 return treeData;
             }
    
             public JSONObject search(String appId, JSONObject filter, UserContext context, String sourceField, String type, String keyWord, int limit, int start) {
                 JSONObject result = new JSONObject();
                 String companyList = filter.getString("companyList");
                 JSONObject addressSetting = filter.getJSONObject("addressSetting");
                 //部门根目录，多个用|隔开
                 String rootDetpId = addressSetting.getString("rootDetpId");
                 //部门层级
                 int layerFrom = -1;
                 int layerTo = 9999;
                 String layerFromStr = addressSetting.getString("layerFrom");
                 if (!UtilString.isEmpty(layerFromStr)) {
                     layerFrom = Integer.parseInt(layerFromStr);
                 }
                 String layerToStr = addressSetting.getString("layerTo");
                 if (!UtilString.isEmpty(layerToStr)) {
                     layerTo = Integer.parseInt(layerToStr);
                 }
                 //叶子节点
                 String leafType = addressSetting.getString("leafType");
                 JSONArray array = new JSONArray();
                 String currentCompanyId = context.getCompanyModel().getId();
                 String uid = context.getUID();
                 int listSize = 0;
                 /*//返回人员json
                 JSONObject json = new JSONObject();
                 json.put("id", "用户帐号");
                 json.put("text", "用户姓名");
                 json.put("showtextsuffix", "显示后缀");
                 json.put("sourceId", "用户帐号");
                 json.put("name", "用户姓名");
                 json.put("type", "user");
                 json.put("USERNAMEALIAS", "用户全名");
                 json.put("deptId", "所属部门ID");  移动端使用
                json.put("deptName", "所属部门名称");  移动端使用
                json.put("deptFullName", "所属部门全路径");  移动端使用
                 //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                 if (!UtilString.isEmpty(sourceField)) {
                     JSONObject temp = new JSONObject();
                     temp.put("COMPANYNAME", "单位名称");
                     temp.put("COMPANYID", "单位id");
                     temp.put("COMPANYNO", "单位编码");
                     temp.put("EMAIL", "邮箱");
                     temp.put("USERNAME", "用户姓名");
                     temp.put("DEPTID", "部门id");
                     temp.put("DEPTFULLPATHID", "部门id全路径");
                     temp.put("DEPTFULLPATHNAME", "部门名称全路径");
                     temp.put("DEPTFULLPATHNAMEWITHCOMPNAY", "部门全路径名称(含单位)");
                     temp.put("DEPTNAME", "部门名称");
                     temp.put("DEPTNO", "部门编码");
                     temp.put("ROLEID", "角色id");
                     temp.put("UID", "用户帐号");
                     temp.put("USERID", "用户ID");
                     temp.put("USERNO", "员工代码");
                     temp.put("USERNAME", "用户姓名");
                     temp.put("USERNAMEALIAS", "用户全名");
                     temp.put("EMAIL", "邮箱");
                     temp.put("OFFICETEL", "电话");
                     temp.put("MOBILE", "手机");
                     temp.put("OFFICEFAX", "传真");
                     temp.put("POSITIONNAME", "职位名称");
                     temp.put("POSITIONNO", "职位编码");
                     temp.put("POSITIONLAYER", "职位等级");
                     temp.put("EXT1", "扩展标记1");
                     temp.put("EXT2", "扩展标记2");
                     temp.put("EXT3", "扩展标记3");
                     temp.put("EXT4", "扩展标记4");
                     temp.put("EXT5", "扩展标记5");
                     String[] sourceFields = sourceField.split(",");
                     for (String field : sourceFields) {
                         json.put(field, temp.getString(field));
                     }
                     array.add(json);
                 }*/
                 //返回部门JSON
                 /*JSONObject json = new JSONObject();
                 json.put("id", "部门id");
                 json.put("text", "部门名称");
                 json.put("showtextsuffix", "显示后缀");
                 json.put("sourceId", "部门id");
                 json.put("id", "部门id");
                 json.put("name", "部门名称");
                 json.put("type", "dept");
                 json.put("fullPathName", "部门全路径");
                 //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                 if (!UtilString.isEmpty(sourceField)) {
                     JSONObject temp = new JSONObject();
                     temp.put("COMPANYNAME", "公司名称");
                     temp.put("COMPANYID", "公司id");
                     temp.put("COMPANYNO", "公司编码");
                     temp.put("DEPTNAME", "部门名称");
                     temp.put("DEPTID", "部门id");
                     temp.put("DEPTFULLPATHID", "部门id全路径");
                     temp.put("DEPTFULLPATHNAME", "部门名称全路径");
                     temp.put("DEPTNO", "部门代码");
                     temp.put("DEPTZONE", "区域划分");
                     temp.put("DEPTTYPE", "部门类型");
                     temp.put("EXT1", "扩展标记1");
                     temp.put("EXT2", "扩展标记2");
                     temp.put("EXT3", "扩展标记3");
                     temp.put("EXT4", "扩展标记4");
                     temp.put("EXT5", "扩展标记5");
                     String[] sourceFields = sourceField.split(",");
                     for (String field : sourceFields) {
                         json.put(field, temp.getString(field));
                     }
                 }*/
                 //返回团队json
                 /*JSONObject json = new JSONObject();
                 json.put("id", "团队ID");
                 json.put("text","团队名称");
                 json.put("showtextsuffix", "显示后缀");
                 json.put("sourceId", "团队ID");
                 json.put("id", "团队ID");
                 json.put("name", "团队名称");
                 json.put("type", "team");
                 json.put("TEAMID", "团队ID");
                 json.put("TEAMNAME", "团队名称");*/
                 result.put("totalPageNum", listSize);
                 result.put("list", array);
                 return result;
             }
    
             /**
              * 地址簿显示值（主要是返回值中有uid 或deptid 或 teamID 显示值需要具体信息用来显示）
              *
              * @param appId 应用id
              * @param filter 地址簿配置
              * @param context 用户上下文
              * @param value 用户账号或部门id
              * @return 用户或部门信息
              */
             public JSONObject addressDisplayValue(String appId, JSONObject filter, UserContext context, String value) {
                 JSONObject addressSetting = filter.getJSONObject("addressSetting");
                 //叶子节点
                 String leafType = addressSetting.getString("leafType");
                 //地址簿回填字段
                 String[] sourceFields = filter.getString("sourceField").split(",");
                 boolean hasUID = false; //是否是员工账号
                 boolean hasDeptId = false; //是否是部门id
                 boolean hasTeamId = false; //是否是团队id
                 JSONObject json = new JSONObject();
                 for (int i = 0; i < sourceFields.length; i++) {
                     if (leafType.equals("user") && ("UID".equals(sourceFields[i]) || "USERNAMEALIAS".equals(sourceFields[i]))) {
                         hasUID = true;
                     } else if (leafType.equals("dept") && "DEPTID".equals(sourceFields[i])) {
                         hasDeptId = true;
                     } else if ("TEAMID".equals(sourceFields[i])) {
                         hasTeamId = true;
                     }
                 }
                 if (hasUID) {//value 是 uid
                     json.put("sourceId", "xinren1");
                     json.put("id", "xinren1");
                     json.put("name", "新人1");
                     json.put("type", "user");
                     json.put("USERNAMEALIAS", "新人1");
                     //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                     if (!UtilString.isEmpty(filter.getString("sourceField"))) {
                         JSONObject temp = new JSONObject();
                         temp.put("COMPANYNAME", "单位名称");
                         temp.put("COMPANYID", "单位id");
                         temp.put("COMPANYNO", "单位编码");
                         temp.put("EMAIL", "邮箱");
                         temp.put("DEPTID", "部门id");
                         temp.put("DEPTFULLPATHID", "部门id全路径");
                         temp.put("DEPTFULLPATHNAME", "部门名称全路径");
                         temp.put("DEPTFULLPATHNAMEWITHCOMPNAY", "部门全路径名称(含单位)");
                         temp.put("DEPTNAME", "部门名称");
                         temp.put("DEPTNO", "部门编码");
                         temp.put("ROLEID", "角色id");
                         temp.put("UID", "xinren1");
                         temp.put("USERID", "55555");
                         temp.put("USERNO", "员工代码");
                         temp.put("USERNAME", "新人1");
                         temp.put("USERNAMEALIAS", "新人1");
                         temp.put("EMAIL", "邮箱");
                         temp.put("OFFICETEL", "电话");
                         temp.put("MOBILE", "手机");
                         temp.put("OFFICEFAX", "传真");
                         temp.put("POSITIONNAME", "职位名称");
                         temp.put("POSITIONNO", "职位编码");
                         temp.put("POSITIONLAYER", "职位等级");
                         temp.put("EXT1", "扩展标记1");
                         temp.put("EXT2", "扩展标记2");
                         temp.put("EXT3", "扩展标记3");
                         temp.put("EXT4", "扩展标记4");
                         temp.put("EXT5", "扩展标记5");
                         for (String field : sourceFields) {
                             json.put(field, temp.getString(field));
                         }
                     }
                 } else if (hasDeptId) {
                     DepartmentModel dept = DepartmentCache.getModel(value);
                     if (dept != null) {
                         json.put("id", dept.getId());
                         json.put("name", dept.getPathNameI18NOfCache());
                     } else {
                         json.put("id", value);
                         json.put("name", value);
                     }
                 }
                 //      返回用户信息
                 //      JSONObject json = new JSONObject();
                 //      json.put("sourceId", "用户帐号");
                 //        json.put("id",  "用户帐号");
                 //        json.put("name", "用户姓名");
                 //        json.put("type", "user");
                 //        json.put("USERNAMEALIAS", "用户全名");
                 //        //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                 //        if (!UtilString.isEmpty(sourceField)) {
                 //            JSONObject temp = new JSONObject();
                 //            temp.put("COMPANYNAME", "单位名称");
                 //            temp.put("COMPANYID", "单位id");
                 //            temp.put("COMPANYNO", "单位编码");
                 //            temp.put("EMAIL", "邮箱");
                 //            temp.put("USERNAME", "用户姓名");
                 //            temp.put("DEPTID", "部门id");
                 //            temp.put("DEPTFULLPATHID", "部门id全路径");
                 //            temp.put("DEPTFULLPATHNAME", "部门名称全路径");
                 //            temp.put("DEPTFULLPATHNAMEWITHCOMPNAY", "部门全路径名称(含单位)");
                 //            temp.put("DEPTNAME", "部门名称");
                 //            temp.put("DEPTNO", "部门编码");
                 //            temp.put("ROLEID", "角色id");
                 //            temp.put("UID", "用户帐号");
                 //            temp.put("USERID", "用户ID");
                 //            temp.put("USERNO", "员工代码");
                 //            temp.put("USERNAME", "用户姓名");
                 //            temp.put("USERNAMEALIAS", "用户全名");
                 //            temp.put("EMAIL", "邮箱");
                 //            temp.put("OFFICETEL", "电话");
                 //            temp.put("MOBILE", "手机");
                 //            temp.put("OFFICEFAX", "传真");
                 //            temp.put("POSITIONNAME", "职位名称");
                 //            temp.put("POSITIONNO", "职位编码");
                 //            temp.put("POSITIONLAYER", "职位等级");
                 //            temp.put("EXT1", "扩展标记1");
                 //            temp.put("EXT2", "扩展标记2");
                 //            temp.put("EXT3", "扩展标记3");
                 //            temp.put("EXT4", "扩展标记4");
                 //            temp.put("EXT5", "扩展标记5");
                 //            String[] sourceFields = sourceField.split(",");
                 //            for (String field : sourceFields) {
                 //                json.put(field, temp.getString(field));
                 //            }
                 //        }
                 //返回部门信息
                 /*JSONObject json = new JSONObject();
                 json.put("sourceId", "部门id");
                 json.put("id", "部门id");
                 json.put("name", "部门名称");
                 json.put("type", "dept");
                 json.put("fullPathName", "部门全路径");
                 //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                 if (!UtilString.isEmpty(sourceField)) {
                     JSONObject temp = new JSONObject();
                     temp.put("COMPANYNAME", "公司名称");
                     temp.put("COMPANYID", "公司id");
                     temp.put("COMPANYNO", "公司编码");
                     temp.put("DEPTNAME", "部门名称");
                     temp.put("DEPTID", "部门id");
                     temp.put("DEPTFULLPATHID", "部门id全路径");
                     temp.put("DEPTFULLPATHNAME", "部门名称全路径");
                     temp.put("DEPTNO", "部门代码");
                     temp.put("DEPTZONE", "区域划分");
                     temp.put("DEPTTYPE", "部门类型");
                     temp.put("EXT1", "扩展标记1");
                     temp.put("EXT2", "扩展标记2");
                     temp.put("EXT3", "扩展标记3");
                     temp.put("EXT4", "扩展标记4");
                     temp.put("EXT5", "扩展标记5");
                     String[] sourceFields = sourceField.split(",");
                     for (String field : sourceFields) {
                         json.put(field, temp.getString(field));
                     }
                 }*/
                 return json;
             }
             /**
             * @param appId 应用id
             * @param filter 地址簿配置
             * @param context 用户上下文
             * @param nodeId 当前节点id
             * @param nodeType 当前节点类型
             * @return
             */
            public JSONObject getParentTreeNode(String appId, JSONObject filter, UserContext context, String nodeId, String nodeType) {
                JSONObject result = null;
                if ("company".equals(nodeType)) {
                } else if ("dept".equals(nodeType)) {
                    if ("dept1".equals(nodeId) || "dept2".equals(nodeId)) {//上一级是公司
                        result = new JSONObject();
                        result.put("id", "comppany1");
                        result.put("name", "公司1");
                        result.put("type", "company");
                        result.put("fullPathName", "/公司1");
                    } else if ("dept3".equals(nodeId)) {//上一级是部门
                        result = new JSONObject();
                        result.put("id", "dept1");
                        result.put("name", "研发");
                        result.put("type", "dept");
                        result.put("fullPathName", "/研发");
                    }
                }
                return result;
            }
    
         }
    

  * **部门地址簿**  

![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addressD2.png)

>   * **分类方式** `全部部门`组织机构定义的全部部门;`操作者所在部门及兼任部门`操作者所在部门及兼任部门;`操作者所在虚拟部门`操作者所在虚拟部门
> 
>   * **取值字段** 指定取值字段，多个值用","隔开
> 
>   * **回填字段** 指定回填字段，多个值用","隔开,【取值字段】和【回填字段】个数和次序必须匹配
> 
> 

>   * **选择模式** 单选或 多选   
>   
> 
> 
>     1. 默认组织树是部门显示在上，人员显示在下，系统管理员可以修改%AWS_HOME%/bin/conf/aws-portal.xml文件中people-list-priority属性值，修改部门与人员的显示顺序
> 
>     2. AWS Portal门户为地址簿提供了一系列运行时参数设置 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addressD4.png)
> 
> 3.AWS平台进行模式为SaaS模式时，地址薄所有场景仅允许查看显示自己主职身份所在单位的组织信息，且优先级高于该组件相关属性的配置 ![](https://docs.awspaas.com/reference-guide/aws-paas-ui-reference-guide/list/addressD5.png)
> 
>   * 部分扩展属性不支持移动端
> 
>   * 不显示注消状态的单位、部门、人员
>