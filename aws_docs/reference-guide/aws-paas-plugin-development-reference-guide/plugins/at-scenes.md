# 应用场景 · AWS PaaS文档中心

# 应用场景

@公式(又称为@命令/AT公式)是一个预先定义，服务器端解析执行的函数公式（例如获得当前服务器日期，可使用`@date`）。

## 使用

在AWS PaaS中@公被普遍的应用，如BO字段默认值、流程实例标题。为了便于技术人员识别，通常字体加粗绿色显示，并在编辑组件的右上角提供标识：

[![编辑@公式](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/at-1.png)](<at-1.png>)

## 嵌套与组合

所有@公式都允许被无限深度的嵌套和组合使用。 嵌套是指某个@公式的值（输出）是另外一个@公式参数的输入。
    
    
    @rmb(@numAdd(100.06,200))
    

上述规则由`@rmb`和`@numAdd`嵌套，表示将100.06和200的和，然后作为`@rmb`的输入，输出人民币大写。下图解释嵌套组合的逻辑处理顺序：

[![逻辑处理顺序](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/at-2.png)](<at-2.png>)

组合是指将常量字符串与@公式合并成最终输出的值，成为一段脚本。

## 公式编辑器

如果@公式参数或嵌套复杂、难以理解，也可以使用AWS提供的公式编辑器，可视化每个公式的输入参数和输出参数，通过拖拽完成嵌套参数的编辑。作为AT公式开发者，对那些声明为公式必填的参数被显著提示。

[![公式编辑器](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/at-3.png)](<at-3.png>)

> 从应用场景不难看出，你开发的AT公式将通过平台各种方式场景提供给应用配置人员。如果有一个合理规范的命名、参数说明和分类，将降低使用者的学习门槛。