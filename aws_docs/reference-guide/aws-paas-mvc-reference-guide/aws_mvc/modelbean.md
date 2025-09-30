# ModelBean封装 · AWS PaaS文档中心

## 业务对象封装

与其他MVC开发框架一样，编写出结构清晰的程序代码，需要对业务实体对象进行属性封装（概念如`POJO`、`JavaBean`）。

AWS MVC提供了设计业务实体对象的父类`ModelBean`和`IModelBean`接口，采用`ModelBean`封装的业务实体对象，还有以下优势：

  * 提供方法转换成JSON数据结构
  * 提供方法转换成XML数据结构
  * 作为DAO处理的实体表结构对象
  * 作为集群Cache的数据结构对象

### TestModel开发示例
    
    
    public class TestModel extends ModelBean implements IModelBean {
    
        private String id;
        private String f1;
        private double f2;
    
        public TestModel() {
        }
    
        public String getId() {
            return id;
        }
    
        public void setId(String id) {
            this.id = id;
        }
    
        public String getF1() {
            if (f1 == null) {
                f1 = "";
            }
            return f1;
        }
    
        public void setF1(String f1) {
            this.f1 = f1;
        }
    
        public double getF2() {
            return f2;
        }
    
        public void setF2(double f2) {
            this.f2 = f2;
        }
    }
    

### IModelBean接口声明
    
    
    /**
     * AWS MVC框架中，表示实体业务对象接口
     */
    public interface IModelBean extends Serializable {
    
        /**
         * 将当前对象转换成json处理对象
         */
        public JSONObject toJsonObject();
    
        /**
         * 将当前对象转换成json串
         */
        public String toJson();
    
        /**
         * 将当前对象转化成XML片段
         */
        public String toXML();
    }