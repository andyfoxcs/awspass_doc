# View视图 · AWS PaaS文档中心

## View视图

不建议直接在处理控制器中完成业务处理过程。

在AWS MVC框架中，View层负责实现具体的业务逻辑，组织处理结果。View提供客户端用户会话、身份及设备等信息，通过继承`ActionWeb`，完成View的开发。

### 开发示例
    
    
    public class ABCWeb extends ActionWeb {
        public ABCWeb (UserContext uc) {
            super(uc);
        }
        public String getMainPage(String p2) {
            return “Hi,p2=”+p2;
        }
    }
    

### 异常处理

当操作发生错误时，框架将抛出`uncheck`异常（如AWSDataAccessException），如果你的逻辑没有方案或需求去处理这个异常可以继续向外抛出。

当操作发生参数非法、执行非法等常见View层处理逻辑场景时，建议抛出如下异常（详细请参见**异常处理** 章节）

  * **AWSIllegalArgumentException** 非法参数异常造成错误的访问请求，对应400错误
  * **AWSObjectNotFindException** 资源未找到异常，对应404错误
  * **AWSForbiddenException** 访问被拒绝异常，对应403错误

### 框架范围之外的util或service层

如果业务处理逻辑相对复杂，建议将逻辑操作封装成util类或service类

### 识别访问者设备类型

通常你在为PC端浏览器的界面交互编程。如果需要你的程序能够更好的服务于其他移动设备，可以调用`UserContext.getDeviceType()`方法获取到当前用户的设备类型。

  * **LoginConst.DEVICE_PC** PC桌面电脑
  * **LoginConst.DEVICE_TABLET** 平板电脑
  * **LoginConst.DEVICE_MOBILE** 智能手机

### 与View相关的常见开发

  * Server端开发
    * 模版渲染(HTML静态文件+标签）
    * ModelBean封装
    * DAO封装
    * Cache封装
  * Web端开发
    * JavaScript
    * CSS
    * 熟悉portal/commons下的各种组件资源，如AWS UI、JQuery Mobile