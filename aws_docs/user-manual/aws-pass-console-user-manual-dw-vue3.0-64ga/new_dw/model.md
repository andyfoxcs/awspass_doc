# 交互模式 · AWS PaaS文档中心

# 交互模式

可分别配置PC和移动端的展示样式。

  * [PC端](<pc.html>)展示模式支持：表格、看板、相册、时间轴、表格、甘特图、URL、嵌套DW 、导航树、日历表格、日历时间轴
  * [移动端](<mobile.html>)展示模式支持：列表、看板、时间轴、URL、嵌套DW、日历列表、日历时间轴

## 快速预览

在配置时刻，点击右上角的`预览`按钮可快速预览PC端、移动端效果

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/yulan1.png)](<yulan1.png>)

## 移动端视图部署

移动端视图部署有两种方式：

  * 将视图发布后在`导航服务-移动入口`开启移动入口应用中的标准首页，添加视图，作为当前应用对应的移动应用的视图在移动端展示

  * 将视图URL地址添加到`导航服务-移动入口`开启移动入口应用中的自定义URL，作为H5应用在移动端展示,部署步骤：

**1\. 获取视图URL地址**

鼠标移动到移动端视图，点击`高级选项-URL外链`或通过`发布`把视图发布至导航菜单获取URL地址

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/h5-1.png)](<h5-1.png>)

**2\. 获取的URL地址添加到`导航服务-移动入口`开启移动入口应用中的自定义URL**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/h5-3.png)](<h5-3.png>)

> URL地址只需写cmd及其它参数信息，不需要填写sid参数。更多信息参见<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_develop/README.html>

**3\. 创建应用**

进入`应用管理>创建应用`创建应用，且给应用授维护权限

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/h5-2.png)](<h5-2.png>)

**4\. 给应用授权**

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/h5-4.png)](<h5-4.png>)

**5\. 在移动门户进行访问**

用移动设备登录移动门户添加该应用进行访问。