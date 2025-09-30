# 地址簙 · AWS PaaS文档中心

# 地址簙

创建一个地址簿控件，这是一个私有封装。用于显示和修改被表单数据源绑定的数据，自动通过平台各类权限配置控制其读、写、隐藏状态。

## 运行

PC端  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdzb_pc.png)](<textdzb_pc.png>)  
移动端  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdzb_mobile.png)](<textdzb_mobile.png>)  
  
## 配置字段属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdzb1.png)](<textdzb1.png>)

**标题**

参见单行[标题](<text.html#title>)

**默认值**

参见单行[默认值](<text.html#mrz>)

**长度**

参见单行[长度](<text.html#length>)

**地址簿类型**

地址簿分为人员、部门、单位、角色、岗位、群组等六种类型

  * **人员**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdzb2.png)](<textdzb2.png>)  
---  

**分类维度** 组织、岗位、角色、群组，必须至少勾选一个分类维度

**显示兼任**

默认不开启，开启后，结构将显示组织模型添加兼职信息时，是否显示属性为是的兼职人员。有关兼职的设置请参见 <https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-org-vue/organization/usermap.html> 。 注： 兼职是否显示在6.3.1.0626 版本后提供一个总开关AWS Portal门户 应用参数地址薄显示兼职人员(addressDisplayMap) 详细见该参数说明

### 显示人员卡片

  * 开启后，鼠标放在回显的值上，显示人员卡片
  * 卡片上显示当前人的icon、部门、上线/离线、手机号码、电话号码
  * 安装了[个人主页](<https://awsappstore.com/apps/detail/com.actionsoft.apps.profile>)这个应用，卡片上还会显示`沟通`、`查看详情`操作
  * `沟通`在当前人的卡片中不显示，只在查看其他人卡片中显示

[![](https://helpcdn.awspaas.com/picture/picture/202312/f7a1ef47b75845a48503bb9343bdad95.png)](<https://helpcdn.awspaas.com/picture/picture/202312/f7a1ef47b75845a48503bb9343bdad95.png>)

> 只有类型是人员时，显示`显示兼任`、`显示人员卡片`属性

  * **部门**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdzb3.png)](<textdzb3.png>)  
---  
  
**分类维度** 只有组织一个维度，默认勾选且禁选

**选择范围** `全部`部门组织机构定义的全部部门;`所在部门`操作者所在部门及兼任部门;`所在虚拟部门`操作者所在虚拟部门

  * **单位**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdzb4.png)](<textdzb4.png>)  
---  

**分类维度** 只有组织一个维度，默认勾选且禁选

  * **角色**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdzb5.png)](<textdzb5.png>)  
---  

**分类维度** 组织、岗位、角色，必须至少勾选一个分类维度

  * **岗位**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdzb6.png)](<textdzb6.png>)  
---  

**分类维度** 组织、岗位、角色，必须至少勾选一个分类维度

  * **群组**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/textdzb7.png)](<textdzb7.png>)  
---  

**分类维度** 只有组织一个维度，默认勾选且禁选

### 换行

  * 默认不开启，人员地址簿input框一行的高度显示，内容超出一行的，鼠标滚动查看
  * 开启后，人员地址簿input框根据回显内容换行高度显示，不需要滚动查看
  * 只读时，换行与不换行，效果一样没区别，都是根据内容换行高度显示

**允许多选**

默认开启多选，允许选择多个值；不开启时，只允许选择一个值

  * **分隔符**

仅在开启`允许多选`时可用，多值之间可用`逗号`或`空格`分隔

**限制选人范围**

  * **根部门** 输入根部门ID，多个用竖线分隔，支持@公式

  * **部门层级** 只显示部门层级范围内的部门，例如【从1到3】

  * **群组** 输入群组ID，多个用竖线分隔，支持@公式

> 只有类型是人员、部门时，显示该属性

**限制单位范围**

默认不开启，开启后显示选择`限制单位范围`属性，如果不选择选项，默认显示自己所在实体单位及有权限访问的实体单位；如选择了，显示配置的并且有权限的单位（包括实体单位和虚拟单位）且必须选择自己所在的单位

> 只有类型是人员、部门时，显示该属性

**自定义数据回显**

默认不开启，不开启则默认回显至当前字段；开启后显示取值字段、回填字段这两属性

  * **取值字段** 指定取值字段

  * **回填字段** 指定回填字段，`取值字段`和`回填字段`个数和次序必须匹配

**高级**

  * **数据源接口** 一个继承com.actionsoft.bpms.ui.dict.address.base.AddressUISourceDataAbs的类，由自定义的Java程序控制树形节点的内容

    
    
      import com.actionsoft.bpms.org.cache.DepartmentCache;
    import com.actionsoft.bpms.org.model.DepartmentModel;
    import com.actionsoft.bpms.server.UserContext;
    import com.actionsoft.bpms.ui.dict.address.base.AddressUISourceDataAbs;
    import com.actionsoft.bpms.util.UtilSerialize;
    import com.actionsoft.bpms.util.UtilString;
    import com.alibaba.fastjson.JSONArray;
    import com.alibaba.fastjson.JSONObject;
    
    public class TestDataSource extends AddressUISourceDataAbs {
        /**
         * 获取地址簿树跟节点
         *
         *
         *
         * @param filter
         * @return
         */
        public JSONArray getOrgTreeData(String appId, JSONObject filter, UserContext context) {
            JSONArray treeData = new JSONArray();
            //单位列表
            String companyList = filter.getString("companyList");
            //部门根目录，多个用|隔开
            String rootDetpId = filter.getString("rootDetpId");
            //部门层级
            int layerFrom = -1;
            int layerTo = 9999;
            String layerFromStr = filter.getString("layerFrom");
            if (!UtilString.isEmpty(layerFromStr)) {
                layerFrom = Integer.parseInt(layerFromStr);
            }
            String layerToStr = filter.getString("layerTo");
            if (!UtilString.isEmpty(layerToStr)) {
                layerTo = Integer.parseInt(layerToStr);
            }
            //取值字段
            String sourceField = filter.getString("sourceField");
            //叶子节点
            String leafType = filter.getString("leafType");
            //返回单位json
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
            treeData.add(json);
            //返回部门json
               /*  JSONObject json = new JSONObject();
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
                 }
                 //返回人员的json
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
    
            //部门根目录，多个用|隔开
            String rootDetpId = filter.getString("rootDetpId");
            //部门层级
            int layerFrom = -1;
            int layerTo = 9999;
            String layerFromStr = filter.getString("layerFrom");
            if (!UtilString.isEmpty(layerFromStr)) {
                layerFrom = Integer.parseInt(layerFromStr);
            }
            String layerToStr = filter.getString("layerTo");
            if (!UtilString.isEmpty(layerToStr)) {
                layerTo = Integer.parseInt(layerToStr);
            }
            //取值字段
            String sourceField = filter.getString("sourceField");
            //叶子节点
            String leafType = filter.getString("leafType");
            if("company".equals(pType)){
                JSONObject json = new JSONObject();
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
                }
                treeData.add(json);
            }else if("dept".equals(pType)){
                JSONObject json = new JSONObject();
                json.put("pid", pid);
                if (true) {
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
                }
                treeData.add(json);
            }
    
    
            return treeData;
        }
    
        public JSONObject search(String appId, JSONObject filter, UserContext context, String sourceField, String type, String keyWord, int limit, int start) {
            JSONObject result = new JSONObject();
            String companyList = filter.getString("companyList");
            //部门根目录，多个用|隔开
            String rootDetpId = filter.getString("rootDetpId");
            //部门层级
            int layerFrom = -1;
            int layerTo = 9999;
            String layerFromStr = filter.getString("layerFrom");
            if (!UtilString.isEmpty(layerFromStr)) {
                layerFrom = Integer.parseInt(layerFromStr);
            }
            String layerToStr = filter.getString("layerTo");
            if (!UtilString.isEmpty(layerToStr)) {
                layerTo = Integer.parseInt(layerToStr);
            }
            //叶子节点
            String leafType = filter.getString("leafType");
            JSONArray array = new JSONArray();
            String currentCompanyId = context.getCompanyModel().getId();
            String uid = context.getUID();
            int listSize = 0;
            if("user".equals(leafType)){
                if("用户姓名".contains(keyWord)){
                    JSONObject json = new JSONObject();
                    if (true) {
                        json.put("iconFont", UtilSerialize.parseObject("{'code':'&#58939;','color':'#DA2912'}"));
                    } else {
                        json.put("iconFont", "&#58939;");
                    }
                    json.put("sourceName", "用户姓名");
                    json.put("sourceId", "用户帐号");
                    json.put("type", "user");
                    json.put("text", "用户姓名");
                    json.put("id",  "用户帐号");
                    json.put("name", "用户姓名");
                    json.put("type", "user");
                    json.put("value", "用户帐号");
                    json.put("USERNAMEALIAS", "用户全名");
                    json.put("showtextsuffix", "");
                    json.put("deptPath", "");
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
                    }
                    array.add(json);
                    listSize = 1;
                }
            }
    
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
    
            //叶子节点
            String leafType = filter.getString("leafType");
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
                if (true) {
                    json.put("iconFont", UtilSerialize.parseObject("{'code':'&#58939;','color':'#DA2912'}"));
                } else {
                    json.put("iconFont", "&#58939;");
                }
                json.put("sourceName", "用户姓名");
                json.put("type", "user");
                json.put("value", "用户帐号");
    
                json.put("sourceId", "用户帐号");
                json.put("id",  "用户帐号");
                json.put("name", "用户姓名");
                json.put("type", "user");
                json.put("USERNAMEALIAS", "用户帐号");
                //以下内容用来回填数据，根据sourceField值确定返回哪些数据
                if (!UtilString.isEmpty(filter.getString("sourceField"))) {
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
    

  * **过滤事件**

一个实现com.actionsoft.bpms.ui.dict.address.base.AddressUIFilterInterface接口的类，由自定义的Java程序控制树形节点的显示，例如【过滤掉包含对应字段符串的人员、部门、单位】
    
    
    import com.actionsoft.bpms.org.model.CompanyModel;
    import com.actionsoft.bpms.org.model.DepartmentModel;
    import com.actionsoft.bpms.org.model.UserModel;
    import com.actionsoft.bpms.server.UserContext;
    import com.actionsoft.bpms.ui.dict.address.base.AddressUIFilterInterface;
    import com.actionsoft.bpms.ui.dict.address.model.AdvancedAddressModel;
    
    public class Test
      implements AddressUIFilterInterface
    {
      public boolean addressUIFlexUserFilter(UserContext uc, UserModel model, AdvancedAddressModel addressUIFlexModel)
      {
        if (model.getUserName().contains("aws"))
          return false;
        return true;
      }
    
      public boolean addressUIFlexDepartmentFilter(UserContext uc, DepartmentModel model, AdvancedAddressModel addressUIFlexModel)
      {
        if (model.getName().contains("测试2")) {
          return false;
        }
        return true;
      }
    
      public boolean addressUIFlexCompanyFilter(UserContext uc, CompanyModel model, AdvancedAddressModel addressUIFlexModel)
      {
        if ((model.getName().contains("同步微信单位12")) || (model.getName().contains("新单位"))) {
          return false;
        }
        return true;
      }
    }
    

**控制属性**

参见单行[控制属性](<text.html#control>)

**不允许重复录入**

参见单行[不允许重复录入](<text.html#nocopy>)

**宽度**

参见单行[宽度](<text.html#wigth>)

**提示文字**

参见单行[提示文字](<text.html#tip>)

**帮助说明**

参见单行[帮助说明](<text.html#help>)

**字段规则**

参见单行[字段规则](<text.html#zdgz>)