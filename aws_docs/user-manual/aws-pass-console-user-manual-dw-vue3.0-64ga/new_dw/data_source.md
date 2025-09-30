# 配置数据源 · AWS PaaS文档中心

# 配置数据源

## 表单数据源

适用于所有视图类型，数据来自当前AWS连接的本地数据库BO表模型。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/14.png)](<14.png>)

属性项 | 说明  
---|---  
数据源 | 列出当前设计者可访问的BO数据源，包括关联应用、父应用、当前应用中的BO数据源   
`流程应用视图`列出的是绑定流程组的第一个流程绑定第一个表单主表对应的BO数据源，支持搜索  
添加字段 | 添加运行时DW列表允许显示的字段  
添加计算字段 | 即在DW列表中添加虚拟字段，一般应用在DW列表通过显示规则自定义按钮  
高级 | 强制过滤条件，不含WHERE的SQL语句，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)  
同步结构变化 | 当BO数据源字段的长度、类型发生变化，点`同结构变化`，会同步到当前视图中  
  
> 添加的字段，实体字段蓝色，虚拟字段黑色的，隐藏字段蓝色背景色置灰[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/14.3.png)](<14.3.png>)

**_字段菜单选择卡_**

  1. 打开数据源配置界面
  2. 添加字段，鼠标移动到字段名称就能显示`菜单选项卡`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/14.1.png)](<14.1.png>)

属性项 | 说明  
---|---  
修改字段名 | 点击字段名，进行修改，按回车或点击[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/dg.png)](<dg.png>)图标，完成修改操作,改的 字段名同步到数据列表  
设置唯一标识 | 选取数据源中的主键字段或者设置了唯一约束的字段，SQL数据源要求SQL语句变更后，必须由添加字段按钮获取相应字段列表  
排序 | 配置后，该列表头将支持点击进行升序/降序排序，该排序采用字符串方式进行排序，与字段列表中的配置一致  
隐藏 | 配置后，该列在客户端列表中默认将不显示  
删除 | 配置后，运行时DW列表将不再显示该字段  
列名 | 显示字段名，鼠标移到列名悬浮显示列名及列名ID  
  
### 添加计算字段

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/14.2.png)](<14.2.png>)

## SQL数据源

仅适用于普通视图分类，数据支持来自当前AWS连接的本地数据库和来自`连接服务 > RDS 连接关系型数据库服务`连接的外部数据库两种。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/14-1.png)](<14-1.png>)

属性项 | 说明  
---|---  
数据源 | `本地数据源` 数据来自当前AWS连接的本地数据库   
`CC数据源`数据来自`连接服务 > Database组件`连接的外部数据库  
测试数据源 | SQL数据源显示测试数据源,测试CC数据源是否连通  
SQL语句 | 完整的SELECT查询语句，支持[@公式](<https://docs.awspaas.com/reference-guide/aws-paas-at-reference-guide/index.html>)，  
如`select * from orguser where departmentid='@departmentId()'  
高级 | 自定义COUNT SQL默认会反向解析SQL查询语句生成COUNT SQL，用于构建表格总记录数和翻页，支持@公式  
如`select count(*) from orguser where departmentid='@departmentId()'，高级中的sql条件要与SQL语句中的一致  
  
> ● 创建数据用户视图BO数据源建议用主表对应的BO,不建议用子表对应的BO  
>  ● `数据应用视图`、`流程 应用视图-普通视图`中类型可选表单数据源、sql数据源，其他视图只显示表单数据源