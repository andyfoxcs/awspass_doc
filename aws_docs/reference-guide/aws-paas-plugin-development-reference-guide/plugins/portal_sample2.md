# 匿名门户开发 · AWS PaaS文档中心

## 匿名门户开发

匿名门户是指网络用户在未录系统前，提供的站点内容。其特点是此刻无法获知用户身份，如果这些内容与访问AWS PaaS资源无关（如访问数据库、AWS SDK API），可忽略本章节。

  * 当用户访问登录页时，从数据库读取内部发布的某些通知公告
  * 构造一个与AWS PaaS资源密切相关的外网站点，当用户登录身份后再进入业务门户系统

> 如果要构造一个较为复杂的外网站点，且内容与AWS PaaS资源耦合度不高，建议网站通过AWS PaaS开放的ASLP服务接口(HTTP鉴权)进行集成

### 技术规格建议

请根据设计目标，考虑如下技术建议

目标 | 建议  
---|---  
访问AWS PaaS数据库 | App MVC开发，使用不含Session的Mapping编程注解  
访问其他数据库或服务 | 建议如上，后端使用CC进行连接  
调用AWS PaaS SDK | 如启动流程、查询任务状态。建议如上  
JSP/Servlet需要Session变量 | AWS MVC不推荐你的JSP/Servelt程序使用状态会话。如果匿名网站被部署在Web集群环境，需要你的技术团队自行解决J2EE Web会话缓存同步  
引入新的前端框架 | 如`bootstrap`，请将这类资源放入portal/%AppId%/lib下  
css、图片等资源文件 | 建议将这类资源放入portal/%AppId%/相关目录下，如img、css、file  
*开发自己的JSP | 除必要的文件允许放到Web应用根目录下（如重构了index.jsp，一个product.jsp介绍公司产品）之外，建议将JSP资源放入portal/%AppId%/jsp下，并记录你的差异清单  
*开发自己的Servlet | 将编译的jar包放入portal/WEB-INF/lib下 ，并记录你的差异清单  
*为Web应用增加三方jar类库 | 将第三方jar包放入portal/WEB-INF/lib下，并记录你的差异清单  
*自定义URL规则 | 如增加自己的url-pattern，可修改portal/WEB-INF/web.xml，并记录你的差异清单  
  
> 上述加星号的项目属于AWS PaaS私有部署能支持的定制部分，超出AWS App容器对应用安装/卸载的控制范围，当AWS PaaS平台自身进行升级时存在被覆盖的风险

### 注意事项

不含Session的cmd是一种匿名访问AWS PaaS资源的请求，开发团队应对这类访问的后端逻辑有充分的安全评估