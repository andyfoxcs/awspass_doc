# 按钮操作 · AWS PaaS文档中心

## 常规操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/info2.png)](<info2.png>)

项 | 说明  
---|---  
办理 | 完成任务，可修改名称,默认为`办理`。开启此项，显示`可自由跳转至`按钮，默认不开启;开启后，显示`批量办理任务`按钮，，默认不开启`禁用批量办理任务`选项   
批量办理 | 开启后， 在`流程中心`允许同时办理多个任务  
抄送 |  可抄送其他人阅读 ,可修改名称,默认为`抄送`。开启此项，显示`限制选人范围`和`请选择传阅模板`允许当前任务以内部传阅、邮件通知、钉钉、企业微信、飞书等方式传阅给指定人员阅读  
转办 | 可转交其他人处理，可修改名称,默认为`转办`。 开启此项，显示`限制选人范围`,可将当前执行的任务委托给其他人处理，默认不开启  
补签 | 动态创建一个补签流程，增加人员进行审批，只有路由设置为串/并签该属性才显示。 开启此项，显示`限制选人范围`,可将当前执行的任务给其他人处理，默认不开启  
特批 | 可跳转到任意节点，可上传特批文件 。开启此项，运行时表单工具栏提供`特事特办`按钮，允许办理者直接跳转到希望到达的节点，默认不开启  
加签 |  可动态创建一个自由加签分支流程，完成后再回到当前任务 ，默认不开启。 开启此项，显示`限制选人范围`，运行时，由办理者自由指定加签人员，为加签人员提供只读形式的表单数据。可应用`限制选人范围`  
会签 | 可动态创建一个同级部门会签分支流程，完成后再回到当前任务。开启此项，在办理人树形结构中展示与当前操作者部门平级的部门及子部门账户，双击部门可将该部门名称（该部门名称代表该部门【管理者】身份的账户）拾取到右侧，为会签人员提供只读形式的表单数据，默认不开启  
阅办 | 可动态创建一个部门内阅办分支流程，完成后再回到当前任务。开启此项，运行时在办理人树形结构中展示当前操作者部门，不包含子部门(阅办为当前办理人所在的部门账号,不包括子部门账户)，为阅办人员提供只读形式的表单数据，默认不开启  
协同 | 可动态创建一个自由协作分支流程(表单可编辑)，完成后再回到当前任务。开启此项，显示`限制选人范围`运行时，由办理者自由指定协同人员，为协同人员产生的任务允许在表单可修改状态下修改表单数据。可应用`限制选人范围`,默认不开启  
打印 | 用默认或指定的模板打印表单。开启此项，显示指定打印模板、页面宽度的选项及不限次数、审批记录控制属性，默认`不指定`和`默认页面宽度`，运行时，当前任务工具条出现"打印"按钮。注：打印次数限制是基于任务，如果当前节点为串/并签多人办理时，是每人分别打印的次数限制   
添加自定义按钮 | AWS工作流为人工交互任务提供了一组预封装的按钮，这些按钮会根据任务状态、节点策略动态显示  
  
### 自由跳转

办理按钮开启后显示自由跳转配置，办理该节点任务时，允许办理者动态指定到允许跳转的节点。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/tiaozhuan1.png)](<tiaozhuan1.png>)

> 该功能仅在单例任务时有效，当设置为串签或并签操作时，在运行时客户端不会出现自由节点选择窗口

### 批量办理

批量办理图1  
---  
[![undefined](https://docs.awspaas.com/apps/com.actionsoft.apps.workbench/function/workbench-pl.png)](<https://docs.awspaas.com/apps/com.actionsoft.apps.workbench/function/workbench-pl.png>)  
批量办理图2  
[![undefined](https://docs.awspaas.com/apps/com.actionsoft.apps.workbench/function/workbench-pl2.png)](<https://docs.awspaas.com/apps/com.actionsoft.apps.workbench/function/workbench-pl2.png>)  
  
### 限制选人范围

点击`限制选人范围`打开地址簿选项框，只能从地址簿选择，应用范围：`抄送、转办、补签、加签、协同、办理人-常用-任意指定中的参与者选项`

地址簿选项属性  
---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/info2.1.png)](<info2.1.png>)  
地址簿选项运行  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/zhidu1.png)](<zhidu1.png>)  
  
数据源过滤示例参数[UI-地址簿](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/zj/dzb.html>)

### 抄送

不影响流程主干执行的知会任务，任务传阅时，为当前节点任务工具条提供`抄送`按钮，允许办理者将当前节点的表单信息以只读方式传阅给指定范围人员阅读。

#### 选择抄送模板

支持邮件、短信、企业微信、钉钉、飞书模板，相关配置详见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process/manual_task/notice.html>

选择被传阅人  
---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/read1.png)](<read1.png>)  
被传阅人收到通知  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/read2.png)](<read2.png>)  
被传阅人收到邮件通知  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/read2-1.png)](<read2-1.png>)  
传阅任务跟踪  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/read3.png)](<read3.png>)  
  
被传阅人收到短信、企业微信、钉钉、飞书通知

短信 | 飞书  
---|---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/sms-read2.png)](<sms-read2.png>) | [![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/feishu-read2.png)](<feishu-read2.png>)  
企业微信 | 阿里钉钉信  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/weixin-read2.png)](<weixin-read2.png>) | [![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/dingding-read2.png)](<dingding-read2.png>)  
  
#### 用API创建传阅任务
    
    
    //创建传阅任务
    SDK.getTaskAPI().createUserCCTaskInstance( processInst,  parentTaskInstModel,  userContext,  participant,  title);
    

> 全部API文档，[参见这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)

### 转办

指将当前执行的转办给其他人处理。

设置转办  
---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/weituo1.png)](<weituo1.png>)  
转办留言跟踪  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/weituo2.png)](<weituo2.png>)  
  
#### 用API转办任务
    
    
    //转办任务
    SDK.getTaskAPI().delegateTask( taskInstId,uid,targetUID,delegateReason);
    

### 补签

动态创建一个补签流程，增加人员进行审批

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/bq.png)](<bq.png>)

> 补签添加人后，同时把当前任务办理完毕

### 特批

办理者在遇到紧急情况下，允许忽略下面的一些执行节点，直接跳转到希望到达的节点。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/base5.png)](<base5.png>)

> 使用该权限的人员需要仔细填写留言，当遇到重大责任决策时，有些企业必须由领导手写意见并传真给特事特办人员

### 动态活动节点

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/info4.png)](<info4.png>)

执行时，为当前节点任务工具条提供`沟通`按钮，允许当前办理者征求他人意见后继续办理；为被协同人任务工具条提供`完毕`和`沟通`按扭；当前办理者可等待沟通任务全部执行完毕后或通过沟通收回按钮收回未执行完的任务后，继续向下办理任务。

  * **`阅办`** 在办理人树形结构中展示当前操作者部门，不包含子部门(阅办为当前办理人所在的部门账号,不包括子部门账户)，为阅办人员提供只读形式的表单数据
  * **`会签`** 在办理人树形结构中展示与当前操作者部门平级的部门及子部门账户，双击部门可将该部门名称（该部门名称代表该部门【管理者】身份的账户）拾取到右侧，为会签人员提供只读形式的表单数据
  * **`加签`** 执行时，由办理者自由指定加签人员，为加签人员提供只读形式的表单数据。可应用`限制选人范围`
  * **`协同`** 执行时，由办理者自由指定协同人员，为协同人员产生的任务允许在表单可修改状态下修改表单数据。可应用`限制选人范围`

沟通  
---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/active2.png)](<active2.png>)  
协同人继续沟通或完毕  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/active3.png)](<active3.png>)  
当前办理者沟通收回  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/active4.png)](<active4.png>)  
沟通审批记录  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/active5.png)](<active5.png>)  
沟通跟踪  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/active6.png)](<active6.png>)  
  
#### 用API创建沟通任务
    
    
    //创建沟通任务
    SDK.getTaskAPI().createUserAdHocTaskInstance( processInstId, parentTaskInstId,uid,participant,adHocType,title);
    
    //完成沟通任务
    SDK.getTaskAPI().completeTask(...);
    

> 全部API文档，[参见这里](<https://docs.awspaas.com/reference-guide/aws-paas-api-guide/native/java_doc.html>)

### 打印表单

任务执行时，为当前节点任务工具条提供`打印`按钮，允许办理者打印当前节点的表单

打印图1  
---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/print0.png)](<print0.png>)  
打印图2  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/print2.png)](<print2.png>)  
  
  * 自定义表单模板需安装[PDF表单打印](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.formprint/admin/addtemplate.html>)，具体使用参见[PDF表单打印](<https://docs.awspaas.com/apps/com.actionsoft.apps.addons.formprint/admin/addtemplate.html>)
  * 当表单模板选择不指定,运行时在PDF预览页面右上角选择框中列出打印关联该表单的打印模板及没有打印模板的表单，有打印模板的表单模型不参与打印；当选择设计的关联该表单的打印模板，运行时在PDF预览页面直接显示选择的打印模板

### 添加自定义按钮

AWS工作流为人工交互任务提供了一组预封装的按钮，这些按钮会根据任务状态、节点策略动态显示。

  * `办理` 任务处于正常办理状态时
  * `保存` 表单允许修改时
  * `作废` 流程属性中允许出现作废按钮，并且当前处在第一个节点时
  * `传阅` 节点任务允许传阅时
  * `委托` 节点任务允许委托办理时
  * `特事特办` 节点任务允许特事特办时
  * `打印` 节点任务允许表单打印时
  * `沟通` 节点任务允许阅办、会签、加签、协同时
  * `接收办理` 节点任务处于并签状态，且设置允许个人抢先接收时

但是当处理一个较为复杂的业务流程时，上述默认的按钮可能是不够的，例如 _【当一个工单流程被执行时，用户希望通过点击"生成问题报告"按钮启动一个问题报告流程，或者提供一个自己实现的套打程序】_ ，扩展按钮提供了一个可配置的按钮扩展框架和Java、JavaScript事件接口。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/kz1.gif)](<kz1.gif>)

自定义按钮中的配置及操作与[数据窗口-自定义按钮](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/event.html>)一样。

**与[数据窗口-自定义按钮]不同的地方有：**

  * 这里多了一个`复制表单`操作，`复制表单`的相关配置参见(../basic_info.html#cp)
  * 没有按钮组和按钮菜单的样式
  * 不支持按钮拖动排序

配置  
---  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/kz1.gif)](<kz1.gif>)  
运行效果  
[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/manual_task/kz2.png)](<kz2.png>)  
  
有关自定义按钮`触发后端程序`操作的详细介绍参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide-vue/form_event/form_toolbar_build.html>)。

## 调整按钮顺序

调整按钮顺序需注意的事项：

  1. 表单是VUE的才支持，否则不支持排序
  2. 有些按钮在设计端是需要配置，才显示出来的
  3. 在没进行按钮调整之前，按钮顺序还是按程序默认的来显示
  4. 调整按钮顺序后，可点击恢复默认排序，还原成程序默认的顺序
  5. PC和移动端分别设置排序
  6. 移动端排序中【更多】按钮只能在前面四个位置之间拖动排序，第四个以下的按钮会在更多中显示
  7. 自定义按钮、设置在工具栏或工具栏和办理窗口显示的审核菜单也参与排序，PC端中的跟踪不参与排序
  8. 流程文档，当没排序前按程序默认显示成icon,排序后显示成流程文档字样的按钮

按钮排序入口

[![](https://helpcdn.awspaas.com/picture/picture/202310/6d8c62518e204a678167aad8c9307830.png)](<https://helpcdn.awspaas.com/picture/picture/202310/6d8c62518e204a678167aad8c9307830.png>)

点击【调整按钮顺序】，进入到按钮排序界面，如下图：

[![](https://helpcdn.awspaas.com/picture/picture/202310/930a16e4eb904aefb65adf0462bb7d2d.png)](<https://helpcdn.awspaas.com/picture/picture/202310/930a16e4eb904aefb65adf0462bb7d2d.png>)

  * 支持拖动排序
  * 按钮较多时，支持设置间距、取消间距，设置的间距有两个或超过两个，会显示取消全部间距的操作。该功能只支持PC端
  * 在设计端拖动调整顺序后，在运行端看对应的顺序。PC端设计端从上到下与运行端匹配的顺序是从右到左；移动端设计端从上到下与运行端匹配是从左到右，在更多里的匹配与设计端一致是从上到下

效果展示

PC端配置

[![PC配置](https://helpcdn.awspaas.com/picture/picture/202310/89c983892d8f4c3d8ee9d1e1da40bf16.png)](<https://helpcdn.awspaas.com/picture/picture/202310/89c983892d8f4c3d8ee9d1e1da40bf16.png>)

PC运行效果

[![PC效果](https://helpcdn.awspaas.com/picture/picture/202310/1f13bdc5b2b94bacaeed3aea7d2bba76.png)](<https://helpcdn.awspaas.com/picture/picture/202310/1f13bdc5b2b94bacaeed3aea7d2bba76.png>)

移动端配置

[![移动配置](https://helpcdn.awspaas.com/picture/picture/202310/389b5618080f4c799aefb6b634a8191b.png)](<https://helpcdn.awspaas.com/picture/picture/202310/389b5618080f4c799aefb6b634a8191b.png>)

移动端运行效果

[![移动端效果](https://helpcdn.awspaas.com/picture/picture/202310/c9974c4d7f94416dbd02c4684b51e1e8.png)](<https://helpcdn.awspaas.com/picture/picture/202310/c9974c4d7f94416dbd02c4684b51e1e8.png>)

> 调整按钮顺序该功能在数据视图中也支持，使用方法与之相同 [![](https://helpcdn.awspaas.com/picture/picture/202310/f0d7e6fd621c4bbeb93bb73297761e77.png)](<https://helpcdn.awspaas.com/picture/picture/202310/f0d7e6fd621c4bbeb93bb73297761e77.png>)