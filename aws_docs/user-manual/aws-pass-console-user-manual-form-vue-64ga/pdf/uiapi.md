# UI组件相关的API · AWS PaaS文档中心

# UI组件相关的API

## 脚本配置入口

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/uiapi1.png)](<uiapi1.png>)  
---  
1添加动作 | 2选择触动时机 | 3选择脚本  
---|---|---  
**4编辑当前选择的脚本** | **5解绑脚本** | **6绑定脚本**  
  
## 脚本管理

在`表单设计器-表单属性`中点击`脚本管理`，弹出侧边栏，在侧边栏中对脚本进行增、删、改操作

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-form-vue-64ga/pdf/uiapi2.png)](<uiapi2.png>)  
---  
  
## 编程模式

**this关键字的使用说明**

this关键字用于定义函数的场景中，如果方法调用已经跳出当前函数，则不能直接使用this关键字 其他调用场景可以使用FormAPI来代替

**this.ui方法说明**

ui方法，可以获取表单中的字段，组件（非数据库字段），入参针对获取的信息有所不同，可以是字段名或字段id（boItemModel的id），可获取到对应的字段；可以是组件id，获取到对应的组件信息 ui方法，要控制一下组件不存在时候，链式调用不报错，返回值提供一个错误信息：字段/组件不存在 grid方法也需要做同样处理

表单的UI组件提供了一些常用的方法，可以获取值和控制UI组件

**获取当前字段**
    
    
    this.ui("字段名").getVal();//取值
    this.ui("字段名").setVal("新的值","新的显示值");//赋值，组件内容会处理显示规则，新的显示值可选
    this.ui("字段名").getObj();//获取字段对象
    

**获取主表字段（子表中）**
    
    
    this.parent("字段名").getVal();//获取父页面的或者父表的字段内容，仅限子表场景中使用，如果是字段子表场景，仅获取上一级的数据内容
    this.ui("字段名","表名").getVal();//获取指定表的字段内容，可以用于多层级的字段子表，直接获取某一层级的表的数据，“表名”不指定，获取当前的数据
    

**获取字段状态**
    
    
    this.ui("字段名").getStatus();//获取字段的状态，
    //返回：
    // normal 正常态，表单原始态，包括存储字段设置的状态、节点设置的状态
    // readonly 只读，后台设置的状态，所有前台设置后的结果
    // hidden 隐藏，后台设置的状态，所有前台设置后的结果
    
    this.ui("字段名").isExist();//获取字段是否存在，返回true/false
    this.grid("表名").isExist();//获取表格是否存在，返回true/false
    

**获取字段dom状态**
    
    
    this.ui("字段名").isVisible();//获取字段dom的显示状态
    this.grid("表名").isVisible();//获取字段
    

**修改字段状态**
    
    
    this.ui("字段名").setReadOnly(true/false);//设置是否只读
    this.ui("字段名").setHidden(true/false);//设置隐藏，true：隐藏；false：显示，注意同时隐藏标题
    this.ui("字段名").setRequired(true/false);//设置必填，true：必填；false：选填
    

**定位/滚动到组件**
    
    
    this.ui("字段名").locate()
    this.grid("表名").locate()
    

**刷新表单**
    
    
    this.api.refreshPage()// 刷新表单，数据重新加载
    this.api.reloadPage()// 刷新表单，整个页面重新加载
    

**刷新组件**

对有数据源的UI或者子表进行刷新，子表行选择，翻页
    
    
    this.ui("字段名").refresh()
    this.grid("表名").refresh(callback)
    this.grid("表名").gotoPage("页码")
    

**提供基本交互**

消息提示
    
    
    this.feedback.msg("消息内容","消息类型");//PC端，移动端对外暴露的都是这个API，内部采用对应的客户端来实现
    //示例
    
    this.feedback.msg("提示信息","success")
    
    this.feedback.msg("提示信息","warning")
    
    this.feedback.msg("提示信息","info")
    
    this.feedback.msg("提示信息","error")
    
    this.feedback.validateMsg("")
    this.feedback.bannerMsg([{"
    bgColor":"",
    "fontColor":"",
    "msg":""
    }])// 提供横幅提示效果，支持多条展示
    

**对话框交互**
    
    
    this.feedback.dialog(options:dialogOption|"close");//对话框，参数内容可以和elementui的保持一致，内容支持text、html、支持调用awsui组件,传入close字符串时可以调用关闭
    
    
    declare interface DialogButtonModel {
        text: string;
        click: () => void;
        type?: "primary" | "danger"
    }
    
    declare interface DialogConfig {
        title?: string;
        /**
         * 扩展参数（详细参见elementui-dialog）
         */
        extendParams?: any;
        /**
         * render方法优先
         */
        contextRender?: any;
        /**
         * 支持html
         */
        html?:string;
        /**
         * dialog按钮
         */
        buttons?: DialogButtonModel[]
    }
    
    
    //示例代码1（弹出dialog里一个地址簿）：
    const config = {
        filter: {
            addressType: "user",//固定值
            isAdvMode: true,//固定值
            addressSetting: {
                range: "department|position|role|team",//固定值
                delimiter: " ",//分隔符，根据实际情况使用，通常是空格，可以是半角逗号，竖线
                choiceType: "single",//single：单选；multiple：多选
                leafType: "user"//叶子节点类型，现在固定为user
            },
            sourceField: "UID",//固定值
            targetField: "address",//固定值
            deptTargetField: ""//留空
        },
        separator: " "//分隔符和上面的delimiter一致
    }
    const testConfig = {
        data: {
            value: "zhf",
            address: JSON.stringify(config),
            sid: settingParam.sessionId,
            appId: "",
            addressDomId: "address",
            formData: "",
            cmd: "CLIENT_AWSUI_ADDRESSBOOK",
        },
        title: "人员",
        height: 556,
        disabled: false,//是否禁用
        readonly: false,//是否只读
        maxRowNumber: false,//设置是否一行显示，如果一行展示，选多后不会挤高度，否则自适应选择的内容撑高
    }
    
    
    this.feedback.dialog({
        title: "测试标题3333",
        extendParams: {width: "500px"},
        contextRender: ({h, resolve}) => {
            return [
                h("span", () => "分配人员："),
                h(resolve("AwsuiAddress"),
                    {
                        propsOptions: testConfig,
                        modelValue: "admin",
                        'onUpdate:modelValue': value => alert("设置的值：" + value),
                    }
                ),
                h(resolve("AwsuiButton"), {onClick: e => alert(231)}, () => "按钮示例")
            ]
        },
        buttons: [{
            text: "关闭此按钮", click: () => {
                alert("点击此按钮就关闭");
                window.formApi.behavior.dialog.closeDialog()
            }, type: "danger"
        }]
    })
    
    //示例代码2（弹出dialog里一个html页面）：
    this.feedback.dialog({
        title: "测试标题",
        extendParams: {width: "500px"},
        html:"<div>这是一段html</div><br><p>这是一段html</p>",
        buttons: [{
            text: "关闭此按钮", click: () => {
                alert("点击此按钮就关闭");
                this.feedback.dialog("close")
            }, type: "danger"
        }]
    })
    

**侧边栏交互**
    
    
    this.feedback.drawer({"参数"});//弹出侧边栏，参数内容可以和elementui的保持一致，内容支持text、html、支持调用awsui组件,传入close字符串时可以调用关闭，同时参照elementui和vant
    
    //示例1，类似于dialog，style用于mobile，size用于pc
    this.feedback.drawer({
        extendParams:{size:"70%",position:"right",style:{height:"100%",minWidth:'80%'}},
        contextRender: ({h, resolve}) => {
            return [
                h("span","分配人员222："),
                h(resolve("AwsuiButton"), {onClick: e => alert(231)}, ()=>"按钮示例333")
            ]
        }
    })
    

**消息确认框交互**
    
    
    this.feedback.msgBox({"参数"});//消息确认框，参数内容可以和elementui的保持一致
    //示例
    
    {
        title: string;
        message: string;
        ok?: () => void;
        cancel?: () => void;
        /**
         * 是否显示取消按钮 false,
         */
        "showCancelButton"?: boolean;
        /**
         * 是否显示确定按钮 true,
         */
        "showConfirmButton"?: boolean;
        /**
         * 是否显示取消按钮false,
         */
        "cancelButtonText"?: string;
        /**
         * 是否显示取消按钮false,
         */
        "confirmButtonText"?: string;
    }
    
    formUserApi.feedback.msgBox({
        title: "标题",
        message: "内容"
    })