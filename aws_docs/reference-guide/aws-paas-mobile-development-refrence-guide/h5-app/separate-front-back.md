# 前后端分离开发模式 | AWS 移动开发参考指南

# 前后端分离开发模式

开发模式:前后端代码完全分离。

  * 前端代码负责页面布局，通过ajax请求动态展示页面。
  * 后端负责接口和业务开发，不涉及任何前端页面布局相关的代码。

前后端分离模式下和模板模式下访问页面有何不同？

  * 请求页面时不再通过CMD，而是直接访问AWS Web服务器app目录下的html， 例如`http://127.0.0.1:8088/portal/apps/com.actionsoft.apps.poc.h5/index.html`

  * 如果在添加H5应用时选中了SSO， 移动端访问页面时会自动添加sid参数, 例如`http://127.0.0.1:8088/portal/apps/com.actionsoft.apps.poc.h5/index.html?sid=512292d0-2eb8-438f-b496-aa58dfcf1d19`