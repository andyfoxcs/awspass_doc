# 封装CC的流程服务 | AWS BPMN2 Activity参考指南

# 封装CC的流程服务

  1. 实现[BizBeanInterface](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/listener/BizBeanInterface.html>)接口
  2. 继承[HelperService](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/servicetask/HelperService.html>)抽象类
  3. 注册到CC的流程服务
  4. 场景模拟，调试

## 开发注意事项

  1. 定位到执行方法
  2. 用注解定义参数的输入
  3. 用注解定义结构的输出
  4. 获取流程上下文对象
  5. 为实施人员扩展参数配置
  6. 设置版本和服务说明

#### 1\. 定位到执行方法

为更灵活的自定义接口参数结构和结果值类型，AWS未对该Java类的method进行接口声明。采用如下规则来动态查询适当的method方法并执行，当以下规则被命中多个时只取第1个：

  * 方法是`public`类型
  * 方法不是`static`类型
  * 方法名前缀不是`get`、`set`

**例如**
    
    
    public void executeAbc() throws SQLException {
        xxx
    }
    

#### 2\. 用注解定义参数的输入

使用@[MappingField](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/servicetask/MappingField.html>)对类变量的参数进行注解

**语法说明**

语法 | 说明  
---|---  
name | 变量名，非必须  
title | 变量标题，必须  
desc | 变量描述，非必须  
notNull | 是否不允许为空，默认允许  
primitive | 是否原始类型，默认是。如果false将根据类型判断  
  
**示例1**
    
    
    @MappingField(title="会议主题")
    private String title;
    
    @MappingField(title="登录密钥")
    private String token;
    
    //标准的Java Setter命名约定
    
    //供引擎赋值时调用
    public void setTitle(String title) {
        this.title = title;
    }
    
    //供引擎赋值时调用
    public void setToken(String token) {
        this.token = token;
    }
    

**示例2**
    
    
    public void abc(
    @MappingField(title="会议主题") String title,
    @MappingField(title="登录密钥") String token){
        ...
    }
    

#### 3\. 用注解定义结果的输出

使用@[MappingField](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/servicetask/MappingField.html>)对返回结果进行注解

**示例**
    
    
    //假设该类完成一个会议的创建，成功返回一个String类型的会议ID
    
    @MappingField(title="会议ID")
    public String createMeeting(){
        ...
    }
    

#### 4\. 获取流程上下文对象

开发者可以通过定义[ProcessExecutionContext](<https://docs.awspaas.com/api/aws-api-javadoc/com/actionsoft/bpms/bpmn/engine/core/delegate/ProcessExecutionContext.html>)类变量，获得当前流程实例的上下文对象。
    
    
    @Resource
    private ProcessExecutionContext ctx;
    

#### 5\. 为实施人员扩展参数配置

这是一种内部高级用法，不熟悉AWS平台开发的开发者勿用。

**定义示例**
    
    
    //重载这个方法
    @Override
    public List<BOItemModel> getConfig(){
        //自定义构造属性页面的组件模型
        List<BOItemModel> list = new ArrayList<BOItemModel>();
        BOItemModel p1 = new BOItemModel();
        p1.setComponentId(BOItemConst.AWSUI_TEXT);
        p1.setColumnWidth(360);
        p1.setName("这是属性名称");
        p1.setTitle("这是属性标题");
        p1.setNullable(true);
        p1.setComponentSetting("{\"placeholder\":\"这是空值提示\"}");
        list.add(p1);
        return list;
    }
    

**运行效果如下** ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/appendix/21.png)

**读值示例**
    
    
    ...
    //程序读实施人员的配置
    Map<String, String> vs = getConfigValues();
    String v1 = vs.get("这是属性名称");
    ...
    

#### 6\. 设置版本和服务说明

父类内置的方法，开发者可以重构或在构造函数内重设

  * setDescription，设置描述
  * setVersion，设置版本号
  * setProvider，设置供应商名称

## SampleCode
    
    
    public class CreateMeetingService extends HelperService {
    
        @MappingField(title="会议主题")
        private String title;
    
        @MappingField(title="会议日期", desc="预计会议开始的日期")
        private String meetingdate;
    
        @MappingField(title="会议时长", desc="预计会议持续的时长，分钟为单位")
        private String meetingtime;
    
        @MappingField(title="登录密钥")
        private String token;
    
        @MappingField(title="会议ID")
        public String createMeeting() throws ApiException, ParseException {
            //这里调用ctrix的API
            ...
            return meetingId;
        }
    
        public void setTitle(String title) {
            this.title = title;
        }
    
        public void setMeetingdate(String meetingdate) {
            this.meetingdate = meetingdate;
        }
    
        public void setMeetingtime(String meetingtime) {
            this.meetingtime = meetingtime;
        }
    
        public void setToken(String token) {
            this.token = token;
        }
    
    }
    

## 注册服务

进入`AWS CONSOLE > 连接服务`，点击`新建`并完成注册操作

新建 | 配置  
---|---  
![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/appendix/22.png) | ![](https://docs.awspaas.com/reference-guide/aws-paas-process-activity-reference-guide/appendix/23.png)  
  
> 注意：程序员开发的Java服务类，编译后的jar包资源必须存在于新建时指定的应用内(`%AWS-HOME%/apps/install/%APPID%/lib`)