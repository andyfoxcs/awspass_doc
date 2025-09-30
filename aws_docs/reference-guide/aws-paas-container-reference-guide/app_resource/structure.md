# 资源结构 | AWS PaaS应用容器与资源控制参考指南

# 资源结构

以下清单列出了AWS应用约定的根文件夹和文件

文件夹或文件 | 说明 | 是否必须  
---|---|---  
%appId%/repository/ | 存放各种模型文件版本（如流程模型），由建模工具维护和管理 | 否  
%appId%/lib/ | 存放开发者编写的java程序库或第三方jar库 | 否  
%appId%/template/ | 存放页面模板文件，由建模工具维护和管理 | 否  
%appId%/i18n/ | 存放多语言资源配置 | 否  
%appId%/mobile/ | 存放移动应用程序包 | 否  
%appId%/method/ | 存放扩展到建模方法定义（PAL应用专用） | 否  
%appId%/db/ | 存放与业务数据相关的数据库脚本 | 否  
**manifest.xml** | 应用描述文件 | **是**  
%appId%/icon16.png | 应用小图标 | 否  
%appId%/icon64.png | 应用中图标 | 否  
%appId%/icon96.png | 应用大图标 | 否  
portal/apps/%appId% | 应用在Web层的资源，如css、js | 否  
  
### 说明

  * 当创建新应用时，上述结构被自动初始化
  * repository目录下的模型文件禁止非专业级人员修改或转移

> 在每个app根目录下，至少存在一个manifest.xml文件，其他部分都不是必要资源