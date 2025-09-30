# Form Submit提交 · AWS PaaS文档中心

## Form Submit提交

这是普通表单提交处理方式。下面，我们模拟了一个数值运算场景，由浏览器提交两个数值和运算类型，经过前端控制器传参和后端控制器的接参，最终抵达你的逻辑区。

  * HTML示例
  * JavaScript提交
  * 前端传参配置
  * 后端接参处理

### HTML示例
    
    
    <!doctype html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>数据计算</title>
        <!-- JQuery -->
        <script type="text/javascript" src="../commons/js/jquery/scripts/jquery.js"></script>
        <!-- AWS UI -->
        <link rel="stylesheet" type="text/css" href="../commons/css/awsui.css">
        <script type="text/javascript" src="../commons/js/awsui.js"></script>
    </head>
    <body>
        <form id="editForm" method="post" action="./jd?sid=<#sid>&cmd=%AppId%_calculation">
            <table class="awsui-ux">
                <tr>
                    <td class="awsui-ux-title">计算</td>
                    <td class="required">
                        <input id="number1" name="number1" class="awsui-textbox" />
                        <select id="sign" name="sign" class="awsui-select">
                            <option value="+">+</option>
                            <option value="-">-</option>
                            <option value="*">*</option>
                            <option value="/">/</option>
                        </select>
                        <input id="number2" name="number2" class="awsui-textbox" />
                        <span> = </span>
                        <input id="results" name="results" class="awsui-textbox" />
                    </td>
                </tr>
                <tr>
                    <td class="awsui-ux-title" colspan="2" style="text-align: center; ">
                        <span id="submitBtn" class="button blue">提交</span>
                    </td>
                </tr>
            </table>
        </form>
    </body>
    </html>
    

> 上述源码中，`<#sid>`在实际运行中由实际的用户会话Id替代

### JavaScript提交
    
    
    $('#submitBtn').click(function(e) {
        // 提交表单
        $('#editForm').submit();
    });
    

### 前端传参配置（Web层action.xml配置文件）
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <aws-actions>
        <cmd-bean name="%AppId%_calculation">
            <param name="number1" />
            <param name="number2" />
            <param name="sign" />
        </cmd-bean>
    </aws-actions>
    

>   * 声明`%AppId%`_calculation命令，`%AppId%`是你实际的应用Id
>   * 该命令接收`number1`,`number2`,`sign`三个参数
> 

### 后端接参处理

#### 方式1**（推荐）**
    
    
    /**
     * 数值计算
     *
     * @param me 用户上下文
     * @param number1 数字1
     * @param number2 数字2
     * @param sign 运算符
     * @return
     */
    @Mapping("%AppId%_calculation")
    public String calculation(UserContext me, int number1, int number2, @Param(defaultValue = "+")String sign) {
        TestWeb web = new TestWeb(me);
        return web.calculation(number1, number2, sign);
    }
    

>   * 显示定义与变量名匹配的方法参数
>   * `UserContext`是AWS MVC内置对象，获得当前操作者上下文信息
> 

#### 方式2
    
    
    /**
     * 数值计算
     *
     * @param me 用户上下文
     * @param params 参数值
     * @return
     */
    @Mapping("%AppId%_calculation")
    public String calculation(UserContext me, RequestParams params) {
        // 参数接收
        int number1 = params.getInt("number1");        // 获取整数类型
        int number2 = params.getInt("number2");        // 获取整数类型
        String sign = params.get("sign", "+");         // 获取字符串类型，第二个参数为默认值，以下方式相同
    //    Boolean bool = params.getBoolean('paramsName');   // 获取Boolean类型
    //    Double number = params.getDouble('paramsName');   // 获取浮点型参数
    
        TestWeb web = new TestWeb(me);
        return web.calculation(number1, number2, sign);
    }
    

>   * 不定义方法参数，动态从`RequestParams`对象中读取变量
>   * 这种方式可以让你的代码更灵活，但不利于重构
> 

### View层逻辑处理
    
    
    public class TestWeb extends ActionWeb {
    
        public TestWeb() {
        }
    
        public TestWeb(UserContext ctx) {
            super(ctx);
        }
    
        public String calculation(int number1, int number2, String sign) {
            ResponseObject ro = ResponseObject.newOkResponse();
            // 处理逻辑
            // ……
            // ro.put("newNum",newNum);
            return ro.toString();
        }
    }