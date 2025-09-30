# DAO封装 · AWS PaaS文档中心

## DAO封装

AWS的DAO基于对JDBC的直接封装，与当今流行的Hibernate、iBATIS相比，去除了O/R映射关系的直接依赖，并借鉴了Apache DBUtils设计思想，只在需要的场景完成O/R Mapping。

采用AWS MVC的DAO优势如下：

  * 代码简单、直接，性能高
  * 无需拼写SQL语句，自动提供表查询、删除和更新操作
  * 屏蔽分页技术，自动适应不同数据库的物理分页
  * 提供自定义的`RowMapper`，将JDBC对象转换成业务实体对象（`ModelBean`）
  * 提供操作复杂数据库操作的`DBSql`工具类
  * 所有操作受控于`AWS SLA`的质量和性能监控、告警

### DaoObject类和方法介绍

Dao(Data Access Object)是一个设计模式，它是对数据访问的一种抽象。`com.actionsoft.bpms.commons.mvc.dao.IDaoObject`是AWS设计的数据库访问接口，`DaoObject`是实现了`IDaoObject`接口用于访问AWS本地数据库的抽象父类，该类对单主键数据库表的查询/更新/删除等常规操作提供了实现。

### TestDao开发示例

  1. 继承`ModelBean`，实现业务实体对象
  2. 继承`DaoObject`，实现Dao处理对象
         
         public class TestDao extends DaoObject<TestModel> {
         
          public TestDao() {
          }
         
          /**
           * 插入一条测试记录
           */
          @Override
          public int insert(TestModel model) throws DataAccessException{
              model.setId(UUIDGener.getUUID());
              String sql = "INSERT INTO " + entityName() + "(ID,F1,F2)VALUES(:ID,:F1,:F2)";
              Map<String, Object> paraMap = new HashMap<>();
              paraMap.put("ID", model.getId());
              paraMap.put("F1", model.getF1());
              paraMap.put("F2", model.getF2());
              return DBSql.update(sql, paraMap);
          }
         
          /**
           * 更新一条测试记录
           */
          @Override
          public int update(TestModel model) throws DataAccessException{
              if (UtilString.isEmpty(model.getId())) {
                  throw new DataAccessException("Method getId() Does Not Allow Empty!");
              }
              Map<String, Object> paraMap = new HashMap<>();
              paraMap.put("F1", model.getF1());
              paraMap.put("F2", model.getF2());
              // 不需要写sql，可调用基类封装的update方法
              return update(model.getId(), paraMap);
          }
         
          /**
           * 封装测试
           *
           * @param id
           * @param f2
           * @return
           */
          public int updateF2(String id, double f2) throws DataAccessException{
              Map<String, Object> paraMap = new HashMap<>();
              paraMap.put("F2", f2);
              return update(id, paraMap);
          }
         
          /**
           * 封装DBSql测试
           *
           * @return
           */
          public long count() {
              return DBSql.getLong("SELECT COUNT(ID) AS C FROM " + entityName(), "C");
          }
         
          /**
           * 封装DBSql测试
           *
           * @param f2
           * @return
           */
          public List<TestModel> queryByF1(String f1) {
              return query("F1=?", f1).orderBy("F2").desc().list();
          }
         
          /**
           * 该Dao实现的表名称
           */
          @Override
          public String entityName() {
              return "TEST_DAO";
          }
         
          /**
           * 构建该Dao从一条记录转换成对象的映射对象
           */
          @Override
          public RowMapper<TestModel> rowMapper() {
              return new Mapper();
          }
         
          /**
           * TestDao Mapper
           */
          private class Mapper implements RowMapper<TestModel> {
              public TestModel mapRow(ResultSet rset, int rowNum) throws SQLException {
                  TestModel model = new TestModel();
                  try {
                      model.setId(rset.getString("ID"));
                      model.setF1(rset.getString("F1"));
                      model.setF2(rset.getDouble("F2"));
                  } catch (Exception e) {
                      e.printStackTrace();
                  }
                  return model;
              }
         
          }
         }
         

### 异常处理

当操作发生错误时，框架将抛出`uncheck`异常（如AWSDataAccessException），如果你的逻辑没有方案或需求去处理这个异常可以继续向外抛出。

当操作发生参数非法、执行非法等常见Dao处理逻辑场景时，建议抛出如下异常（详细请参见**异常处理** 章节）

  * **AWSIllegalArgumentException** 非法参数异常造成错误的访问请求，对应400错误
  * **AWSObjectNotFindException** 资源未找到异常，对应404错误
  * **AWSForbiddenException** 访问被拒绝异常，对应403错误

### 默认编码字符集

utf-8

### 事务处理与资源释放

Spring MVC自动接管了事务与资源释放，这是非常棒的编程体验。为提高性能，目前AWS DAO框架未接管JDBC事务和自动完成`Connection`释放。

当你的程序需要事务支持时，可以遵循标准的JDBC编程规范，对`Connection`对象进行事务的开启、回滚或提交。

如果你的程序获得了一个新的`Connection`(如通过`DBSql.open()`)，那么最终需要你的代码通过`DBSql.close()`释放这个连接。

### 物理表

建议使用AWS的`BO`模型设计和维护你的物理表结构，如果某些表必须由自己的sql创建（不推荐），那么需要遵循App开发规范中约定的表名前缀和sql安装/升级脚本规范。

### 数据库连接池

AWS MVC的数据库连接池使用了[tomcat-jdbc](<http://tomcat.apache.org/tomcat-7.0-doc/jdbc-pool.html>)，相关高级参数调优，可修改对应AWS安装目录`bin/conf/db_pool.properties`文件。

### DBSql类和方法介绍

`com.actionsoft.bpms.util.DBSql`是和AWS数据库交互的工具类，它基于`PreparedStatement`实现了数据库的查询、插入、更新、批处理，DBSql一般用于DaoObject中。

  * get方法用于简单类型查询
  * query方法用于自定义复杂查询
  * update方法用于数据库的更新/插入/删除
  * batch方法用于批处理
  * open/close数据库连接/释放
  * 其它工具方法

    
    
    // 查询单个字段
    String value_a = DBSql.getString("select a from table_test where id=?", new Object[]{"id1"});
    
    // 查询多个字段
    Map<String,Object> value_map = DBSql.getMap("select a,b,c from table_test where id=?", "id1");
    
    // 查询返回自定义对象，MyBean是java类
    List<MyBean> list = DBSql.query("select a,b,c from table_test where id=?", new RowMapper<MyBean>() {
    
        @Override
        public MyBean mapRow(ResultSet rs, int rowNum) throws SQLException {
            MyBean mybean = new MyBean();
            mybean.setA(rs.getString("a"));
            return mybean;
        }
    
    }, "id1");
    

> 详细请参见**aws-api-doc** 的`DBSql`