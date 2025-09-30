# 输入 · AWS PaaS文档中心

# 输入

配置SQL语句执行时的输入参数，DS引擎在执行时会有一层转换，因此此处需要配置Data Service输入与SQL参数的映射关系。 AWS平台会根据SQL自动生成输入参数并配置连线映射，一般使用者无需进行修改，但当SQL语句较复杂时，使用者可进一步手动完成相关配置。

> RDS DS的输入参数必须全部连线。 [![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds20.png)](<rds20.png>)

## Data Service输入

Data Service输入参数配置，即SQL语句中`:变量名`部分。

配置连接器后，AWS PaaS平台会自动生成输入输出参数并进行映射，一般无需更改，如有特殊复杂场景用户可手动修改配置。

### 修改参数

为参数增加标题和默认值信息。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds21.png)](<rds21.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds22.png)](<rds22.png>)

项 | 说明  
---|---  
参数名 | 参数名，仅支持数字、字母、下划线、中划线  
标题 | 参数名标题，用于快速了解参数的意义  
描述 | 详细描述信息，用于快速了解参数的意义  
类型 | 参数类型，详见下方介绍  
来源 | 支持调用方给定和系统给定，详见下方介绍  
默认值 | 参数默认值。来源为系统给定时，必填。DS引擎将自动将该值作为默认值传入  
  
[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds23.png)](<rds23.png>)

#### 参数类型

参数类型，支持字符串、数值、布尔。

  * 字符串类型，数据库字段为日期型的，选择相应字符串类型即可
  * 数值类型，支持Integer、Long、BigDecimal、Double
  * 布尔类型，布尔类型true 或 false

#### 参数来源

  * `调用方给定`，该参数在DS引擎执行时，参数值由调用者传入。
  * `系统给定`，参数来源为系统给定时，默认值必填。指该参数在DS引擎执行时，不会使用由调用者传入的值，DS引擎自动以配置的默认值执行。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds33.png)](<rds33.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds34.png)](<rds34.png>)

#### 必填

必填是指在DS引擎执行时，如果判断该参数传入的值为NULL 或者没有为该参数传入值，则DS引擎直接抛出错误，不向接口发送请求。 勾选必填后， 测试一下页面相应参数将显示红* ，且不允许勾选设置为null和删除。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds35.png)](<rds35.png>)

## SELECT参数/UPDATE参数/INSERT参数/DELETE参数

根据连接器操作类型选择的不同，输入右侧参数显示会不同。 相关参数为SQL语句自动解析，不允许修改。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds24.png)](<rds24.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds25.png)](<rds25.png>)

### SELECT参数

连接器操作类型为`查询`时，为SELECT参数。 此时可勾选是否支持分页，勾选支持分页后，输入参数将自动增加page.size 和 page.index 参数，测试一下时可以输入参数值。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds26.png)](<rds26.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds37.png)](<rds37.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds38.png)](<rds38.png>)

### UPDATE参数

连接器操作类型为`更新`时，为UPDATE参数。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds27.png)](<rds27.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds28.png)](<rds28.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds55.png)](<rds55.png>)

### INSERT参数

连接器操作类型为`插入`时，为INSERT参数。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds29.png)](<rds29.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds30.png)](<rds30.png>)

### DELETE参数

连接器操作类型为`查询`时，为DELETE参数。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds31.png)](<rds31.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds32.png)](<rds32.png>)