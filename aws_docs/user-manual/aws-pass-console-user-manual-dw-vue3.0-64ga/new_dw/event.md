# 自定义按钮 · AWS PaaS文档中心

# 自定义按钮

自定义按钮支持管理员将复复杂业务设计为一个按钮事件，成员可通过自定义按钮执行对应的操作，完成业务处理。自定义按钮可以为成员提供更便捷的业务操作，从而实现工作效率的全面提升

## 添加按钮

进入要设置按钮的视图，鼠标移动到`配置按钮`区域，点击`配置按钮` \- 添加`按钮`或`按钮组`或 `按钮菜单` ，进入自定义按钮的配置页面

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button1.png)](<button1.png>)

## 按钮配置

### 按钮样式

按钮样式即按钮的展示效果，包括按钮名称和样式设置

配置项 | 说明  
---|---  
按钮文字 | 按钮的显示名称，最多可设置 12个字符  
按钮类型 | 有两种：标准按钮、图标按钮  
标准按钮 | 有两种形式：文字或文字加图标  
图标按钮 | 只显示图标，鼠标滑过显示按钮文字，只支持PC端，移动端还是显示文字  
按钮颜色 | 选`默认`或`主要`等预制时，自动给出背景色、文字颜色（与平台UI色系相同）、； 选`其他`颜色时，能根据颜色深浅自动给出文字颜色  
按钮图标 | 设置按钮图标。当是标准按钮时，按钮图标颜色与文字一致自动与背景色反白显示；当是图标按钮时，可以在这设置图标颜色  
边框线 | 按钮颜色是`默认`时，有边框线该属性，否则隐藏，开启边框线，按钮有带边框的样式  
边框圆角 | 设置边框圆角大小  
标准按钮配置 | 标准按钮、按钮图标配置 | 图标按钮配置  
---|---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button2.png)](<button2.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button3.png)](<button3.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button4.png)](<button4.png>)  
运行效果 | 运行效果 | 运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button2.1.png)](<button2.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button3.1.png)](<button3.1.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button4.1.png)](<button4.1.png>)  
  
### 控制按钮显示开关

配置项 | 说明  
---|---  
勾选记录时出现 | 默认不开启。开启后，没有数据时不显示，需要有数据且勾选一条或多条数据后才显示  
显示在PC端 | 默认开启，关闭后在PC端不显示该按钮  
显示在移动端 | 默认开启关闭后在移动端不显示该按钮  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button5.png)](<button5.png>)  
---  
  
> `勾选记录时出现`只有在上方工具条上的按钮有该属性；数据按钮没有；底部按钮是必须勾选才显示，也没有该属性

### 按钮操作

提供了8种常规操作：`创建记录`、`打开视图`、`打开仪表盘`、`打开链接`、`打开表单`、`启动流程`、`触发前端脚本`、`触发后端程序`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button6.png)](<button6.png>)  
---  
  
#### 创建记录

选择按钮操作`创建记录`后,会显示与该操作相关的配置属性

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button7.png)](<button7.png>)  
---  
  
**点击需求确认**

默认关闭，开启后，可以自定义提示语、确定按钮、取消按钮

标准按钮配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button8.png)](<button8.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button8.1.png)](<button8.1.png>)  
  
**关联DW**

显示当前应用、父应用及关联应用的数据视图，除SQL数据视图

**表单默认值**

关联DW中对应表单字段添加默认值，不支持的组件在菜单中自动过滤掉了，默认值支持@公式，主表字段是直接通过手动输入或通过@公式赋值；子表字段是通过映射的方式给子表字段赋值

关联DW配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button9.gif)](<button9.gif>)  
添加表单默认值配置  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button9.1.png)](<button9.1.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button9.2.gif)](<button9.2.gif>)  
  
**交互方式**

三种交互方式：`信息` `侧边栏` `新窗口`,默认是`信息`，直接提示`创建成功`，如没有新建权限，操作后给出消失提示；`侧边栏` `新窗口`按操作动作以对应的交互方式成功打开表单

**关闭时是否刷新**

默认关闭，开启后关闭操作动作，会刷新当前页面。适应用对当前页面有影响的场景

**扫码创建**

默认不开启，仅移动端支持。开启后，显示`扫码结果到`某个字段的属性

**扫码结果到**

选择把扫码结果映射到关联DW对应表单字段的值，运行时点击按钮弹出扫码框，进行扫码，扫码获取的值映射给指定的字段

扫码配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button10.png)](<button10.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button10.1.png)](<button10.1.png>)  
  
**执行前JS脚本**

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button12.png)](<button12.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button12.1.png)](<button12.1.png>)  
  
**设置行样式示例**
    
    
    eventContext.DWApi.grid.setRowStyle(1,"color:red;background:blue;");
    

**设置单元格样式示例**
    
    
    eventContext.DWApi.grid.setCellStyle(1,"F_L7WKEXY0","color:red;background:blue;");
    

**获取选中数据示例**
    
    
    debugger;
    var data = eventContext.DWApi.grid.getCheckedData(true);
    var datalength = data.length;
    for(var i=0;i<datalength;i++){
      var data1 = data[i];
      var id = data1._ID;
      var bindid = data1._BINDID;
      var danhang1 = data1.F_L7WKEXY0;
      alert("id==="+id+"===bindid="+bindid+"==danhang1="+danhang1);
    }
    

**删除数据示例**
    
    
    debugger;
    var data = eventContext.DWApi.grid.getCheckedData(true);
    let ids = [];
    let bindids = [];
    var datalength = data.length;
    for(var i=0;i<datalength;i++){
      var data1 = data[i];
      ids.push(data1._ID);
        bindids.push(data1._BINDID);
    }
     eventContext.DWApi.data.removeData(ids,bindids,()=>{}, ()=>{});
    

**远程请求数据示例**
    
    
    DWApi.api.awsuiaxios.post({
          url: "jd",
          data: {
            sid: this.api.getSid(),
            cmd: 'com.actionsoft.apps.byod.helper_home',
            p1: "",
            p2: "",
          }
        }).then((r)=>{
         console.log("获取到的数据：",r)
         alert("打印信息请F12-console端查看");
        });
    

**打开指定的URL示例**
    
    
    const sid = eventContext.DWApi.sid;
          eventContext.DWApi.behavior.openUrl({
            url : "./w",
            data : {
                sid,
                cmd : "CLIENT_BPM_WORKLIST_PROCESSINST_CREATE_PREPARE", //平台某个请求
                processDefId : "obj_a6e92ef05f254e49abfb0e5a92d341e6",
                processGroupId : "obj_3c7ef304c6e44eceb81f3cd138e04236",
                title : "新建",
            },
            targetConfig : {
             type : "side",
             width : '90%',
             title : '新建',
            }
          });
    

**执行后JS脚本** 同执行前JS脚本

**禁用规则**

按钮被禁止点击

  * 公式返回TRUE，所有用户及所有数据上的按钮都是禁用的
  * 公式返回TRUE,且设置了限制范围，只有限定范围内的人看到的所有数据对应的按钮是禁用的
  * 规则条件中满足禁用条件，所有用户及规则条件中满足禁用条件的数据上的按钮都是禁用的
  * 规则条件中满足禁用条件,且设置了限制范围，只有限定范围内的人看到的及规则条件中满足禁用条件的数据上的按钮是禁用的
  * 其他情况均不禁用

公式  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button11.1.png)](<button11.1.png>)  
规则条件  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button11.png)](<button11.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button11.2.png)](<button11.2.png>)  
  
> 规则条件配置多个条件相同且满足的，规则效果按顺序最后一个显示

**显隐规则**

按钮被隐藏,配置同禁用规则

  * 公式返回false，所有用户及所有数据上的按钮都是隐藏的
  * 公式返回false,且设置了限制范围，只有限定范围内的人看到的所有数据对应的按钮是隐藏的
  * 规则条件中满足隐藏条件，所有用户及规则条件中满足禁用条件的数据上的按钮都是隐藏的
  * 规则条件中满足隐藏条件,且设置了限制范围，只有限定范围内的人看到的及规则条件中满足禁用条件的数据上的按钮是隐藏的
  * 其他情况均不隐藏

> 规则条件配置多个条件相同且满足的，规则效果按顺序最后一个显示

**样式规则**

配置了样式规则，默认的样式规则不生效按配置的样式规则显示

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button13.png)](<button13.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button13.1.png)](<button13.1.png>)  
  
> 规则条件配置多个条件相同且满足的，规则效果按顺序最后一个显示

**校验规则**

配置校验规则，在按钮操作之前会按配置进行校验提示

警告并中断配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button14.png)](<button14.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button14.1.png)](<button14.1.png>)  
仅提示配置  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button15.png)](<button15.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button15.1.png)](<button15.1.png>)  
进行询问配置  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button16.png)](<button16.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button16.1.png)](<button16.1.png>)  
  
>   * 规则条件配置多个条件相同且满足的，规则效果按顺序最后一个显示  
> 
>   * `禁用规则` `显隐规则` `样式规则` `校验规则`只在数据列按钮中显示，视图工具条上方或下方都不显示这四个属性
>   * `禁用规则`、`显隐规则`如果admin没在AC限定范围内，与随AC限定范围的人规则一致
> 

#### 打开视图

**视图列表**

列出关联DW中的所有视图供选择，如果选择的视图当前用户没有权限，会显示第一个视图；如果只有一个视图，且没有权限访问，会给出没有权限访问的友好提示

**过滤条件**

根据视图数据来源显示对应的下拉选择字段，条件根据字段类型会不一样，当选择的字段是文本时，条件有`等于` `包含` `不包含` `开头是` `结尾是`;是数值或日期类型时，条件有`等于` `大于` `小于` `大于等于` `小于等于` `不等于`

**打开方式**

三种交互方式：`侧边栏` `对话框` `新窗口`,默认是`侧边栏`，如没有视图的查看权限，操作后给出没有访问权限的提示

**打码查询**

默认不开启，仅移动端支持。开启后，显示`扫码结果过滤`的属性

**扫码结果过滤**

选择字段及条件，运行时点击按钮弹出扫码框，进行扫码，扫码获取的值作为条件值，对视图数据进行过滤，打开视图最终显示的数据是过滤后的视图数据

>   * 在移动端，过滤条件与扫码结果过滤都配置后，两者是and关系  
> 
>   * 其他配置属性同创建记录
> 

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button17.png)](<button17.png>)  
PC运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button17.1.png)](<button17.1.png>)  
移动端运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button17.2.png)](<button17.2.png>)  
  
#### 打开仪表盘

**仪表盘**

显示当前应用、父应用、关联应用的仪表盘

> 没有`关闭时是否刷新`、`扫码`等属性，其他属性参见打开视图同打开视图

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button22.png)](<button22.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button22.1.gif)](<button22.1.gif>)  
  
#### 打开链接

**链接标题**

打开链接的标题

**链接地址**

链接地址，支持@公式
    
    
    ./w?sid=@sid&cmd=CLIENT_DW_PORTAL&processGroupId=obj_70bb907ec76a4c55b4f4cd158547a335&appId=com.awspaas.user.apps.shitu
    

**扫码创建**

扫码结果qrCode追加到URL链接参数上

示例1视图外链查询传参数
    
    
    http://XXXX:8088/portal/r/w?sid=@sid&cmd=CLIENT_DW_PORTAL&processGroupId=obj_ecb2ab39c08f44b4b3f431adcd306a40&appId=com.awspaas.user.apps.app20221214113953&dwViewId=obj_8f7c744336d54dfe843a6fff480cbc01&condition=[{tp:'BB',cp:'=',fd:'BBOBJ_F749DAD81B95440997A686359424FB2F',cv:'[qrcode]'}]
    

示例2URL地址追加参数
    
    
    http://www.baidu.com?q=[qrcode]
    

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button19.png)](<button19.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button19.1.png)](<button19.1.png>)  
  
#### 打开表单

**关联表单**

显示当前应用、父应用及关联应用的表单

**表单标题**

打开的表单，默认显示表单的标题，在这可以自定义表单标题，支持@公式

**匹配条件**

  * 通过对关联表单主子表添加匹配条件，找到要打开的表单，匹配条件与打开视图中的过滤条件一样

  * 子表只是匹配找到要打开的表单，不在子表中进行数据过滤

**表单操作**

常规、只读两种操作，常规是根据表单当前所在的流程节点是只读还是可编辑来显示；只读打开表单始终是只读状态

>   * 在移动端，匹配条件与扫码查询到过滤都配置后，两者是and关系  
> 
>   * 其他配置属性同[创建记录](<..#cjjl>)
> 

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button20.png)](<button20.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button20.1.gif)](<button20.1.gif>)  
  
#### 启动流程

**关联流程**

显示当前应用、父应用及关联应用的流程，显示设计、运行状态的流程，停用的流程不显示

**执行人**

执行人多个用空格分开，若不指定，第一个节点需要设置路由

配置  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button21.png)](<button21.png>)  
运行效果  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button21.1.gif)](<button21.1.gif>)  
  
> 其他属性同创建记录

#### 触发前端脚本

同执行前JS脚本

#### 触发后端程序

**执行Java类**

需继承`com.actionsoft.bpms.bpmn.engine.listener.ValueListener`类，目前只支持Ajax方式这一种

**示例代码**
    
    
    package com.actionsoft.apps.poc.form.event;
    
    import java.util.HashMap;
    import java.util.Map;
    
    import com.actionsoft.apps.AppsConst;
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ValueListener;
    import com.actionsoft.bpms.commons.htmlframework.HtmlPageTemplate;
    import com.actionsoft.bpms.commons.mvc.view.ResponseObject;
    import com.actionsoft.bpms.server.UserContext;
    
    public class MyBtnActionImpl extends ValueListener {
    
        @Override
        public String execute(ProcessExecutionContext ctx) throws Exception {
            //参数获取
            //记录ID
            String boId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BOID);
            //表单ID
            String formId = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_FORMID);
            //BO表名
            String boName = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_BONAME);
            //视图场景获取选中行数据
             String rowData = ctx.getParameterOfString("$SOURCEDATA");
            // Ajax方式
            ResponseObject ro = ResponseObject.newOkResponse();
            boolean r = true;// 针对业务进行处理
            // 处理业务逻辑成功时
            if (r) {
                ro.msg("成功");// 返回给服务器的消息
                ro.put("key1", "value1").put("key2", "value2");// 放入前端需要的参数
                return ro.toString();
            } else {
                // 错误时
                ro = ResponseObject.newErrResponse();
                ro.msg("错误");
                return ro.toString();
            }
        }
    }
    

> 在流程节点、表单自定义按钮触发后端获取记录ID、表单ID、BO表名，在视图自定义按钮触发后端获取选中行数据，根据获取参数，分场景使用

### 按钮排序

按钮支持拖动排序

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button25.gif)](<button25.gif>)  
---  
  
**自定义按钮支持一览表**

数据按钮 | 底部按钮  
---|---  
表格 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>)  
相册 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>)  
看板 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>)  
时间轴 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>)  
表单 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>)  
甘特图 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/yes.png)](<../base_def/yes.png>)  
日历视图 | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/base_def/no.png)](<../base_def/no.png>)  
  
> 移动端只显示上方工具条上的按钮，数据按钮及底部按钮不显示

**按钮类型**

按钮类型分为三类：`按钮` `按钮组` `按钮菜单`三种，移动端不支持 `按钮组` `按钮菜单`的样式，统一显示成按钮

按钮 | 按钮组 | 按钮菜单  
---|---|---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button25.png)](<button25.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button23.png)](<button23.png>) | [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/button24.png)](<button24.png>)  
  
>   * 按钮组中的当添加自定义按钮后，按钮类型不能在修改
>   * 按钮组、按钮菜单中的配置与按钮一样
>