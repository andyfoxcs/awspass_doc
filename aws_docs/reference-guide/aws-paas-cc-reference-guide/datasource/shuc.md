# 输出 · AWS PaaS文档中心

# 输出

配置Data Service输出与SQL语句返回字段的映射关系。根据连接器操作类型选择的不同，输出参数显示会不同。 AWS平台会根据SQL自动生成输出参数并配置连线映射，一般使用者无需进行修改。

## 不同操作类型输出结果

输入结果中公共参数sla.inTimes(输入构建用时)、sla.outTimes(输出构建用时)、totalTimes(总耗时)，这三个参数属于引擎自处理的参数，实施人员无需修改。

### SELECT结果

操作类型为查询时，输出结果为SELECT结果，实施人员可勾选是否返回多行。 勾选返回多行后，输出参数将自动增加page.total参数，用于返回总记录数；测试一下将根据输入是否勾选允许分页返回对应多条数据。 当不勾选返回多行时，测试一下将自动随机返回 一条记录。 [![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds36.png)](<rds36.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds39.png)](<rds39.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds40.png)](<rds40.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds41.png)](<rds41.png>)

### INSERT结果/UPDATE结果/DELETE结果

INSERT结果/UPDATE结果/DELETE结果输出参数为result.rowCount(SQL影响的的记录数)。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds42.png)](<rds42.png>)

## 修改参数

输出页签右边Data Service输出项，参数可进行修改。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds44.png)](<rds44.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds43.png)](<rds43.png>)

项 | 说明  
---|---  
参数名 | 参数名，仅支持数字、字母、下划线、中划线  
标题 | 参数名标题，用于快速了解参数的意义  
描述 | 详细描述信息，用于快速了解参数的意义  
类型 | 参数类型，参见输入  
数据清选 | 对返回结果进行清洗操作，详细介绍参见下方  
  
### 数据清洗

数据清洗是指为输出数据项进行处理。例如：字典翻译（如1代表男，0代表女）、值转换（如将long的Timestamp值转换成日期）、复杂值处理（如脱敏手机号，只保留前后3位）、去重（如将无效记录剔除）等。数据清洗默认为无，表示不清洗，即原值返回。 清洗方式支持`公式`和`Java程序`两种。

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds45.png)](<rds45.png>)

#### 公式

通过@公式对输出数据进行处理。

  1. 仅支持简单类@公式
  2. 取普通字段值$[参数名]，参数名为右侧Data Service输入参数名

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds46.png)](<rds46.png>)

[![](https://docs.awspaas.com/reference-guide/aws-paas-cc-reference-guide/datasource/rds47.png)](<rds47.png>)

#### Java程序

通过Java事件对输出数据进行处理。 事件需要实现`com.actionsoft.bpms.cc.ds.ValueFunction`接口。

示例：
    
    
    import com.actionsoft.bpms.cc.ds.ValueFunction;
    import com.actionsoft.messaging.MessageContext;
    
    public class DataConvertDemo implements ValueFunction {
    
        /**
         * 示例：对用户名进行转换，追加该用户状态
         *
         * @param obj 当前字段值，对应类型的Java Object
         * @param ctx 当前引擎上下文，使用ctx.getProperty获取当前行其他字段值
         * @return 转换后的值
         */
        @Override
        public Object process(Object obj, MessageContext ctx) {
            String username = (String) obj;
            int closed = ctx.getProperty("closed", Integer.class); //从上下文获取其他字段值
            if (closed == 0) {
                return username + "（活跃中）";
            } else {
                return username + "（已注销）";
            }
        }
    }