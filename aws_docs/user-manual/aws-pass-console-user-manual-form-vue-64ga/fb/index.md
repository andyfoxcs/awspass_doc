# 发布 · AWS PaaS文档中心

# 发布

## 已关联流程列表

绑定当前表单的所有流程，如果为空，点新建流程，去绑定当前表单

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/quickstart/glprocess.png)](<../quickstart/glprocess.png>)  
---  
  
## 已关联视图列表

绑定当前表单的所有视图，如果为空，点新建视图，去绑定当前表单

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/quickstart/glview.png)](<../quickstart/glview.png>)  
---  
  
## 公开发布

### 功能简介

公开发布即通过公开链接的形式将表单发布给外部成员进行数据的增、改。包括以下 2 种部分：

  * 外链填单
  * 查看数据

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link1.png)](<link1.png>)  
---  
  
### 外链填单

**使用场景**

  * 组织外人员提客服工单及后续的工单分配
  * 市场部门进行对外的市场调研
  * 活动限时报名

**设置步骤**

表单设计界面-发布-公开发布-开启-外链填单； 开启前，当前表单需要绑定流程或视图，否则即使开启了，表单链接也无法打开表单 开启后，可以将表单链接发送给好友，也可以分享到企业微信、钉钉、飞书等社交网络。同时也可以生成二维码，微信、钉钉、飞书扫码直接打开表单。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link.gif)](<link.gif>)  
---  
  
**外链填单**

用户无需登录便可通过链接访问，它提交数据，是采集外部数据的一种方式。

**分享链接**

开启后，可通过点击复制、二维码、或者预览打开，将表单填写链接/二维码发布给外部用户进行数据填报。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link5.png)](<link5.png>)  
---  
  
  * **配置二维码**

点击二维码图标，弹出配置二维码框，提供三种模板，默认`无`只展示一个二维码；模板一、模板二，可以配置主题色、标题、描述

无 | 模板一 | 模板二   
---|---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link2.png)](<link2.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link3.png)](<link3.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link4.png)](<link4.png>)  

  * **启用密码**

默认不打开，打开密码的开关设置好密码，也可以通过刷新来更新密码，访问表单时要输入密码方可访问。

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link6.png)](<link6.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link6.1.png)](<link6.1.png>)  
  * **限时提交**

默认不开启，链接永远有效；开启后设置时间，链接在设置的有效时间内有效

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link7.png)](<link7.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link7.1.png)](<link7.1.png>)  

**分享设置**

  * **提交提示语**

通过外链填单提交的提示语。默认为“信息已提交”，在这可以自定义

配置  | 运行   
---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link8.png)](<link8.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link8.1.png)](<link8.1.png>)  

  * **允许重复提交**

默认不开启，相同IP视为同一用户，开启后，表单数据允许重复提交

  * **允许分享单条数据**

默认不开启，开启后`查看已提交数据`页可对单条数据进行分享

**字段权限**

字段权限优先级高于存储中字段权限，设置了只读或隐藏、表单按设置的显示只读或隐藏

  * 字段被设置隐藏不影响查询及表格数据的展示，只影响表单字段的显示隐藏
  * 有些字段在表单中是强制只读展示的，即使字段权限中不设置只读，打开表单也是只读的，如组件是地址簿、网格字典、树形字典、分类字典、流程字典的字段
  * 有些在表单中是强制隐藏的，如流程里程碑、修改记录、表单二维码

**强制更新规则**

为字段设置预设值最多添加20条，设置预设值后，打开表单外链，预设值就在表单中显示了

### 查看已提交数据

**使用场景**

在使用过程中，往往会遇到需要非成员协作团队成员，去修改或补录某些字段数据的情况，比如业务员收集客户资料信息不完善，需要客户协作补录某字段数据。对外数据链接，可以帮助非成员更明确的修改补录数据。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/link9.png)](<link9.png>)  
---  
  
**查询**

  * 高级排版、手写签批、使用字典类、高级类UI组件的字段不提供查询  

  * 列表、单选组数据源为自定义时在查询显示列表，模糊查询，列表只支持单选查询  

  * 复选组数据源为自定义时显示为复选框构选的形式展示，模糊查询  

  * 日期类组件提供对应的UI组件，大于等于、小于等于进行范围查询  

  * 其他的组件都是文本UI进行模糊查询  

**表格数据**

  * 不支持的组件在查看已提交数据表格中不显示，如手写签批、HTML  

  * 有设置显示值、取值的组件，在表格中展示显示值，如单选组、复选组、列表、省市县、地址簿等组件  

  * 在表格中单选组、复选组、列表不支持颜色的样式  

**查看表单数据**

点击操作列`查看数据`，打开表单即可查看

**查看属性**

  * **提交时间** 外链表单提交时间
  * **提交设备** 外链表单提交时用的设备，支持电脑、手机
  * **用户IP** 外链表单提交时的用户IP
  * **数据分享** 在`外链填单`中开启`允许分享单条数据`后`数据分享`属性才显示，默认开启，外部人员可通过链接查看/修改当前表单记录
  * **启用密码** 开启数据分享才显示，默认关闭，启开后，查看/修改表单需要密码才能打开表单
  * **限时提交** 开启数据分享才显示，默认关闭，启开后，设置时间，打开表单链接有时间有效，否则失效

## 表单发布到应用商店

  * 计划将开发、实施的模型发布到AWS企业应用商店，需要有开发者账号，登录发开者账号才能发布
  * 开发者账号分`个人用户`，`企业用户`两类，都可以发布模型

  * **个人用户** 个人用户，通过平台端注册的用户

  * **企业用户** 通过[ISV申请](<https://docs.awspaas.com/reference-guide/aws-appstore-reference-guide/join_appstore/register.html>)，走完入驻流程的认证开发商。企业用户可以管理企业成员

  * 个人开发者发布表单对应的物理表名前缀是BO_EU开头的，企业开发者发布对应的物理表名前缀根据[申请开发者证书](<https://docs.awspaas.com/reference-guide/aws-appstore-reference-guide/join_appstore/register.html>)填写的一致

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/fbform.png)](<fbform.png>)  
---  
  
> 还可以用微信扫码登录

项 | 说明  
---|---  
名称 | 必填  
一句话描述 | 发布表单的描述,128字内  
行业 | 表单属于哪个行业  
标签 | 要发布表单添加标签，标签添加2到5个，每个标签12个文字内  
开发用时 | `半天` `一天` `两天` `三天` `一周`五个选项供选择  
  
**账号登录**

当前表单发布到应用商店，需要先登录开发者账号

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/quickstart/login.gif)](<../quickstart/login.gif>)  
---  
  
**账号解除绑定**

1.登录/注册开发者账号，显示`账号已绑定`  
2.点击三点图标再点`解除绑定`，弹出确认框，点`确定`，解除绑定

**表单发布到应用商店步骤：**

1.登录/注册开发者账号  
2.填写发布表单的相关属性  
3.点击`申请发布`后，发起`申请发布流程`,在应用商店端 品经理审核，在当前页面查看审核状态及在新建表单页面中[我的发布](<../create/mb.html#fb>)中看审核状态

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/fb/fbform1.png)](<fbform1.png>)  
---