# RDS · AWS PaaS文档中心

# RDS

对连接器中[RDS(连接关系型数据库服务)](<../tech-adapters/rds.html>)进行数据转换处理。

## 快速上手

以查询AWS PaaS数据库用户表中姓名包含管理员并且创建日期在2020年的数据，并将部门ID显示成部门名称为例，进行演示。

  1. 新建RDS连接
  2. 新建RDS数据
  3. 配置SQL(以mysql为例)
  4. 配置输入输出信息
  5. 配置数据清洗(将部门ID显示成部门名称)
  6. 测试

### 1\. 新建RDS连接

在 `连接服务>连接`页签，创建`RDS(连接关系型数据库服务)`，详细步骤参见[这里](<../tech-adapters/rds.html>)。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds1.png)](<rds1.png>)

### 2\. 新建RDS数据

在 `连接服务>数据`页签，创建`RDS(连接关系型数据库服务)`

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds2.png)](<rds2.png>)

### 3\. 配置SQL(以mysql为例)

SQL语句可通过SQL向导配置后再编辑，也可直接手动录入 `SELECT USERID,USERNAME,DEPARTMENTID FROM orguser WHERE USERNAME like :USERNAME AND (CREATEDATE>=:CREATEDATE and CREATEDATE<=:CREATEDATE1)`

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds3.gif)](<rds3.gif>)

### 4\. 配置输入输出信息

确认输入输出参数连线已连通。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds4.png)](<rds4.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds5.png)](<rds5.png>)

### 5\. 配置数据清洗(将部门ID显示成部门名称)

在输出页签右侧Data Service输出，配置DEPAETMENTID参数数据清洗类型为@公式，值为`@departmentName(org,$[DEPARTMENTID])`

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds6.png)](<rds6.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds7.png)](<rds7.png>)

### 6\. 测试

点击保存按钮，保存后，点击`测试一下`，输入查询条件 USERNAME 值为 `%管理员%`，CREATEDATE值为`2020-01-01 00:00:00` ，CREATEDATE1值为`2020-12-31 23:59:59` 点击执行按钮进行显示查询结果。

> 实际结果以所查询数据库的记录为准。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds8.png)](<rds8.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds9.png)](<rds9.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds10.png)](<rds10.png>)