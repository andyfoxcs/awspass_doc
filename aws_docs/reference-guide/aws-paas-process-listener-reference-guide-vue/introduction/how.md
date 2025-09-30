# 如何开发流程事件? | AWS 流程事件开发参考指南

## 如何开发流程事件？

  * 本地安装有DEV版AWS PaaS开发环境（有关开发工具参见<https://docs.awspaas.com/reference-guide/aws-paas-mvc-reference-guide/ide/README.html> ）
  * 继承事件[编程接口](<../introduction/interface.html>)，完成代码开发
  * 将jar打包到该App的资源目录（install/%appId%/lib）
  * 选择事件类型之后，自动查找该类型对应的实现类
  * 测试流程执行，在IDE调试代码

### 注册事件

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/introduction/2.png) ![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/introduction/3.png)

#### 事件触发器显示java类规则

  * 根据类中继承的抽象类进行匹配
  * 下拉列表的展示内容：类名，描述，版本号，开发商
  * 读取类的成员变量信息，自动生成扩展属性。key值格式：事件名_类名_成员变量名
  * 运行时刻使用填写的值给成员变量赋值
  * 支持已经注册的类的刷新动作，用于成员变量有变化时初始化扩展参数。

#### 成员变量

  * 事件触发器类提供成员变量的定义，运行时刻，会使用对应的值进行初始化，目前支持类型：String、Date、Integer、Long、Double、Boolean

> 使用成员变量功能要求AWS平台版本不低于6.2.12.0925版本。

##### 示例代码
    
    
    package com.actionsoft.FlowStepBiz;
    
    import java.util.Date;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExecuteListener;
    
    public class Form006AfterSave extends ExecuteListener {
        @Override
        public String getDescription() {
            // TODO Auto-generated method stub
            return "测试用例";
        }
    
        @Override
        public String getProvider() {
            // TODO Auto-generated method stub
            return "ActionSoft";
        }
    
        @Override
        public String getVersion() {
            // TODO Auto-generated method stub
            return "1.0";
        }
    
        //事件触发器类的成员变量定义开始----------
        private int num = 0;
        private Date date = new Date();
        private long long1 = (long) 12;
        private double double1 = 12.2;
        private boolean flag = true;
        private String name = "";
    
        public String getName() {
            return name;
        }
        public void setName(String name) {
            this.name = name;
        }
        public int getNum() {
            return num;
        }
        public void setNum(int num) {
            this.num = num;
        }
        public Date getDate() {
            return date;
        }
        public void setDate(Date date) {
            this.date = date;
        }
        public long getLong1() {
            return long1;
        }
        public void setLong1(long long1) {
            this.long1 = long1;
        }
        public double getDouble1() {
            return double1;
        }
        public void setDouble1(double double1) {
            this.double1 = double1;
        }
        public boolean isFlag() {
            return flag;
        }
        public void setFlag(boolean flag) {
            this.flag = flag;
        }
        //事件触发器类的成员变量定义结束----------
    
        @Override
        public void execute(ProcessExecutionContext ctx) throws Exception {
                info("事件被触发-->" + ctx.getProcessInstance());
        }
    }
    

##### 成员变量扩展属性展示

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/introduction/5.png)

### Debug断点调试代码

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/introduction/4.png)