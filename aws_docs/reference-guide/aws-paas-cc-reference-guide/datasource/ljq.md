# 连接器 · AWS PaaS文档中心

# 连接器

用于配置RDS DS要操作的连接器和SQL语句等信息。

项 | 说明  
---|---  
名称 | 一个简要名称  
描述信息 | 描述信息  
连接器 | 可从当前应用及关联应用的连接器中选择  
操作类型 | 支持查询、更新、插入、删除  
SQL向导 | 当连接器可连通时，点击可打开窗口选择操作的表和字段等信息，确定直接回填相应的SQL，  
自动生成的SQL条件均为=匹配，如需其它复杂匹配规则或复杂SQL可手动输入 ，  
字段仅支持简单的数值、文本、日期类型，比如大文本、BLob、Clob等非简单类型不会显示  
SQL语句 | 根据操作类型，可填写对应的SQL语句，支持通过SQL向导回填和手动输入  
受管信息 | 参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>)  
  
[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds11.png)](<rds11.png>)

## SQL语句支持范围与要求

  1. SQL语句支持`:变量名`格式定义变量，且变量名不能重复，例如： `UPDATE orguser SET CLOSED=:CLOSED,EMAIL=:EMAIL,EXT1=:EXT1,EXT2=:EXT2,EXT3=:EXT3,UPDATEDATE=:updatedate,SESSIONTIME=:SESSIONTIME WHERE USERID=:USERID or username like :username1 or (orderindex >=:orderindex2 and orderindex <:orderindex )`
  2. 查询类，SQL语句必须以SELECT开头，且不支持SELECT *，查询结果必须是固定的字段
  3. 更新类，SQl语句必须以UPDATE开头
  4. 插入类，SQL语句必须以INSERT开头，且必须给出固定的插入字段名称
  5. 删除类，SQl语句必须以DELETE开头
  6. 仅支持单表查询、更新、插入、删除操作，不支持多表联合
  7. 仅支持简单的as别名、order by 、group by语法
  8. like后:变量名 必须在`like` 与 `:变量名`中间有空格隔开
  9. oracle 当字段类型为日期字段时，SQL语句中包含to_date函数时，则Data Service输入字段类型应为`String` ，如果SQL语句中不包含to_data函数，则Data Service输入字段类型应为`Timestamp`类型

**oracleSQL语句包含to_data函数**

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds12.png)](<rds12.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds13.png)](<rds13.png>)

**oracleSQL语句不包含to_data函数**

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds14.png)](<rds14.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds15.png)](<rds15.png>)