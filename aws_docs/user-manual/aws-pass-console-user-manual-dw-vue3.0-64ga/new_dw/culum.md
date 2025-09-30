# 列属性/字段属性 · AWS PaaS文档中心

# 列属性/字段属性

属性项 | 说明  
---|---  
显示名称 | DW列标题，编辑后需按回车或点击[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/dg.png)](<dg.png>)图标  
样式 | 可修改客户端数据列表背景颜色、字体颜色、字体大小、列对齐方式。  
● **文本类型** 字段默认左对齐  
● **数值类型** 字段默认右对  
● **日期类型** 字段认居中对齐  
● **彩虹标签** 把字段值相同的通过颜色来分类标记  
请输入文字说明 | 给标题添加文字说明，在运行时显示  
规则 | ● **显示规则** 在客户端运行时刻可以将字段列值显示为指定内容，详细参见显示规则  
● **修改规则** 在客户端运行时刻可快速修改该字段列值，无权限控制，详细参见修改规则  
● **点击规则** 运行时DW列表点击行为，对附件、HTML排片、图片、条形/二维码等UI组件不支持 详细参见点击规则  
冻结到当前列 | 冻结到当前列，当前列前面的几列固定显示，后面可用横向滚动条来查看  
排序 | 设置后，在运行时DW列表显示当前页数据时将组装Order by语句自动排序  
隐藏 | 设置后，该列在客户端列表中默认将不显示  
其他 | ● **模糊查询** 设置后，对应字段将支持模糊搜索，数值、日期类型的字段不支持模糊查询  
● **表头排序** 设置后，该列表头将支持点击进行升序/降序排序，该排序采用字符串方式进行排序   
● **统计** 对数值类型字段进行平均值、最大值、最小值、单页求和、数据求和等统计  
● **导出** 设置后，在列表导出数据时会将选中的列自动列在显示导出列下  
● **支持HTML** 设置后内容中带HTML标签内容会被解析，否则不解析显示带标签的原值  
访问权限 | 设置该列可访问的用户范围，不设置默认所有用户均可访问  
  
> 部分属性不支持列表、卡片、时间轴模式  
> 

**彩虹标签**

如果已有业务数据再在样式中勾选配置`彩虹标签`，在列表字段值默认会以7种不同颜色循环标记展示，如果还没有业务数据，已勾选配置`彩虹标签`，添加业务数据后，默认彩虹标签上没有颜色标记，需要管理员针对不同值手动配置颜色

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18.5.png)](<18.5.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18.6.png)](<18.6.png>)

**隐藏**

同步到客户端`自定义配置-隐藏`,用户在客户端修改`自定义配置-隐藏`后只对自己生效，不会同步到字段属性的设置

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18.2.png)](<18.2.png>)

**统计**

统计功能配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18.3.png)](<18.3.png>)  
统计值显示配置  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18.3.1.png)](<18.3.1.png>)  
  
**运行示例**

右下方  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18.4.png)](<18.4.png>)  
表格底部  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18.4.1.png)](<18.4.1.png>)  
  
**支持HTML**

没配置支持HTML，内容显示HTML片断，不会被解析

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18.7.png)](<18.7.png>)

**配置支持HTML后，运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/18.8.png)](<18.8.png>)

> 修改规则与支持HTML这个配置互拆，配置了支持HTML 修改规则隐藏

## 显示规则

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.png)](<19.png>)

### 数据格式化

在运行时将DW列表对应字段值进行格式化显示，支持数值、日期、百分比、货币

  * **数值**

    * **小数位数** 最多能设置8位小数

**配置** BO存储中设置的是8位小数，原值9999000.12345678，小数位数配置2位

**运行结果**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.2.png)](<19.2.png>)

    * **数字分节** 按中国、国际两种来分节，默认国际

**配置** BO存储中设置的是8位小数，原值9999000.12345678，数字分节配置按中国或国际分节

**运行结果**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.4.png)](<19.4.png>)

    * **空值处理** 三种处理方式：显示为'--'、显示为'0'、 不显示

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.6.png)](<19.6.png>)

    * **单位换算** 两种方式。时间：不同单位之间的数值换算；自定义：自定义换算表达式

**配置** BO存储中设置的是8位小数，原值9999000.12345678

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.7.png)](<19.7.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.8.png)](<19.8.png>)

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.9.png)](<19.9.png>)

> 1.开启小数位数，如果单位换算结果也带小数位数，先执行单位换算，后执行小数位数  
>  2.没开启小数位数，如果单位换算结果带小数，按单位换算结果显示，如果单位换算结果中不带小数位数，直接显示数据库原值的小数位数

    * **前缀后缀** 字段值说明的更清楚明白

**配置** BO存储中设置的是8位小数，原值9999000.12345678 前缀配置：销售金额；后缀配置：万元

**运行结果**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.11.png)](<19.11.png>)

    * **日期**

      * **当前格式** 只有BO存储字段类型为文本时显示`当前格式`,为日期时不显示`当前格式`
      * **目标格式** 列表中显示的格式

**配置** BO存储中都设置的UI组件是日期

**运行结果**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.14.png)](<19.14.png>)

**配置** BO存储中都设置的UI组件是日期时间

**运行结果**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.17.png)](<19.17.png>)

    * **百分比**

**配置** BO存储中设置的是8位小数，原值9999000.12345678，配置百分比、三位小数

**运行结果**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.19.png)](<19.19.png>)

    * **货币**

**配置** 配置不同的货币种类，显示不同的货币符号

**运行示例**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.21.png)](<19.21.png>)

### 数据映射

  * **常量** 支持HTML语言，如`重要:<img src=../aws_img/red.gif>|不重要:<img src=../aws_img/white.gif>`需勾选支持HTML。值可手动输入常量值，也可选择 已有的列表数据;显示输入要显示的名称,支持@公式；高级在高级框中输入一个简单的常量串，语法格式：值1:显示1|值2:显示2...。高级与上面添加的值，显示相互同步

> 不支持的包括系统字段，字段的UI组件是日期 日期时间的及sql数据源中的所有字段

  * **SQL数据** sql语句支持@公式

  * **组织** 运行时，自动将值与组织信息进行匹配显示

  * **键值字典** 该属性需要基础字典应用支持，详细参见<https://docs.awspaas.com/reference-guide/aws-paas-dict-reference-guide/reference/dw.html>

  * **BO数据** 通过外键值进行匹配显示

    * **数据源** 下拉选择列出的是当前应用、当前应用关联的应用、当前应用的父应用的所有BO存储
    * **值/显示** 下拉选择显示的数据源BO存储的字段,值建议用值不能重复的字段

**配置**

数据源BO_ACT_EXBO，字段名`账号（ZH）`的值`hanqq` 字段名`姓名（NAME）`的值`韩东`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.22.png)](<19.22.png>)

**运行示例**

DW数据源BO_ACT_LOUDOU2，字段名`责任人（NAME）`的值`hanqq` 与配置中的`账号（ZH）`的值相同，根据配置在列表中的显示值就是`韩东`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/19.23.png)](<19.23.png>)

### UI组件

该配置仅在DW中添加的计算字段和数据源BO存储中是虚拟字段时可见，在运行时显示为按钮

  * 展示方式分为平铺
  * 按钮行为来自于字段属性自定义的点击规则
  * 按钮样式为CSS HTML片段

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/20.png)](<20.png>)

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/20-1.png)](<20-1.png>)

> 计算字段配置显示规则是按钮时，点击规则没有意义被隐藏，显示规则配置的不是按钮时，显示点击规则

## 修改规则

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/21.png)](<21.png>)

### UI组件

**只读** 不允许修改

**文本** 针对修改文本类型字段

**日期** 日期控件选择框

**数值** 针对修改数值类型字段

**下拉框** 列表形式选择

**必填** 修改时，会校验必填

> 同一字段配置`修改规则`，`点击规则`不显示之前的配置也失效，建议这两种不要实施同一字段  
>  只有交互风格为表格的支持`修改规则`，其它风格不支持修改规则  
>  当前字段支持哪些类型，下面的表格
> 
> BO字段类型 | BOUI组件类型 | 修改规则的类型  
> ---|---|---  
> 只读 | 文本 | 日期 | 数值 | 列表  
> 时间格式 | 日期格式 | 日期时间格式  
> 文本  
> 时间 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>)  
> 日期 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>)  
> 日期时间 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>)  
> 其它组件 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>)  
> 日期  
> 日期 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>)  
> 日期时间 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>)  
> 数值 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>)  
  
  * [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) 表示支持
  * [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) 表示不支持

>   * 待办 已办 发起这三类流程视图不支持修改规则  
> 
>   * 修改规则与支持HTML这两配置互拆，配置了修改规则 支持html隐藏
> 

  * **Java事件接口**

一个实现AbstractDataWindowQuickChangedBeforeEvent接口的JAVA类，示例：

    
    
    import java.sql.Connection;
    import java.sql.SQLException;
    import java.sql.Statement;
    import java.util.Map;
    
    import net.sf.json.JSONObject;
    
    import com.actionsoft.bpms.dw.design.event.AbstractDataWindowQuickChangedBeforeEvent;
    import com.actionsoft.bpms.server.UserContext;
    import com.actionsoft.bpms.util.DBSql;
    
    /**
     * 示例说明（java类必须继承 AbstractDataWindowQuickChangedBeforeEvent）
     */
    public class DataWindowQuickChangedBeforeEvent extends AbstractDataWindowQuickChangedBeforeEvent {
    
      /**
       * 必须实现 updateBeforeEvent方法
       *
       * @param me 当前上下文对象
       * @param cellName 修改单元格名称
       * @param dataSource 数据源
       * @param changedBeforeCellRow 修改前行的json数据对象(可获得整行数据)
       * @param changedAfterCellMap 修改后行的值（如果需要返回自定义的值，需要重新Put）
       * @return // 返回 1：表示成功 0：表示失败 true：表示校验通过(针对BO数据源) false：表示校验失败(针对BO数据源) 字符串消息：表示向前台返回提示信息
       */
      public String updateBeforeEvent(UserContext me, String cellName, String dataSource, JSONObject changedBeforeCellRow, Map changedAfterCellMap) {
        // 获取数据库连接
        Connection conn = getSqlConn(dataSource);
        // 获取数据表名称
        String tableName = getTableName(dataSource);
        String identifier = changedBeforeCellRow.getString("DV_IDENTIFIER");
        String changedAfterCellValue = (String) changedAfterCellMap.get(cellName);
        // 写自己的业务方法
        String sql = "update " + tableName + " set " + cellName + "='" + changedAfterCellValue + "' where ID  ='" + changedBeforeCellRow.getString(identifier) + "'";
        Statement st = null;
        try {
          st = conn.createStatement();
          st.executeUpdate(sql);
        } catch (SQLException e) {
          e.printStackTrace();
        } finally {
          DBSql.close(conn, st, null);
        }
        // changedAfterCellMap.put(cellName, changedAfterCellValue); //如果需要改变值 需要执行此行代码
        return "true";
      }
    }
    

> 当前数据源不是BO数据源时，该规则的Java事件必填

## 点击规则

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/16.png)](<16.png>)

属性项 | 说明  
---|---  
操作 | 运行时DW列表点击行为，对附件、HTML排片、图片、条形/二维码等UI组件不支持  
目标 | 点击规则触发后页面的打开方式，仅适用于`操作`选择`默认（打开表单`、`修改表单`、`只读表单`选项时  
标题 | 仅在`行为打开目标`为`弹出新Tab页`、`弹出层窗口`时可见，支持@公式  
宽度 | 仅在`行为打开目标`为`弹出层窗口`、`弹出侧边栏`时可见，指定弹出层窗口的宽度，支持像素(px)或百分比(%)  
高度 | 仅在`行为打开目标`为`弹出层窗口`、`内嵌下方`时可见，指定弹出层窗口的高度，支持像素(px)或百分比(%)  
  
`默认（打开表单）`、`修改表单`、`只读表单`是系统内置操作，仅支持BO数据源，不允许删除。

  * **默认（打开表单）** 由流程引擎自动控制表单字段状态

  * **修改表单** 提供修改状态的表单和"保存"按钮，其权限低于BO模型字段【允许显示】【允许编辑】选项，高于流程表单应用的【字段权限】，该行为仅对数据应用视图有效

  * **只读表单** 只读显示该表单

  * **自定义点击规则** 自定义点击事件

在弹出"点击规则"窗口，在操作中选择`自定义`，填写相关信息，点击"确定"按钮，完成操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/17.png)](<17.png>)

属性项 | 说明  
---|---  
名称 | 自定义行为的方案名称  
事件 | ● `onclick` 鼠标点击事件   
● `ondblclick`鼠标双击事件  
JavaScript事件脚本 | 合法的JavaScript函数,参见页面示例