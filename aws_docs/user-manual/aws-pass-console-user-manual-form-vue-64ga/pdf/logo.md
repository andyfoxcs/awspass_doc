# 流程表单状态LOGO · AWS PaaS文档中心

# 流程表单状态LOGO

表单的流程状态信息，支持PC和移动表单，提高表单阅读效率，常规待办和打印状态的流程表单不显示这个状态。AWS Portal门户参数提供流程表单状态LOGO样式配置(processFormStateLogoCSS)全局开关

**配置** [![](https://helpcdn.awspaas.com/picture/picture/202311/93eb3941316c4b818329bbec29ee2c8a.png)](<https://helpcdn.awspaas.com/picture/picture/202311/93eb3941316c4b818329bbec29ee2c8a.png>)

**运行效果** [![](https://helpcdn.awspaas.com/picture/picture/202311/8e4538e4e15f421e852971ae934a9bb9.png)](<https://helpcdn.awspaas.com/picture/picture/202311/8e4538e4e15f421e852971ae934a9bb9.png>)

`mobileLogoPosition` `mobileLogoStyle`这两个参数可以没有，如果没有，PC、移动用一套配置；如果加上这两个参数，对移动端单独配置
    
    
    {"showProcessLogo":true,"logoPosition":{"x":"500px","y":"100%"},"mobileLogoPosition":{"x":"500px","y":"100%"},"logoStyle":{"width":"150","height":"150"},"mobileLogoStyle":{"width":"150","height":"150"},"stateCss":{"active":{"imgSrc":""},"suspend":{"imgSrc":""},"end":{"imgSrc":""},"terminate":{"imgSrc":""},"cancel":{"imgSrc":""}}}