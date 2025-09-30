# AWS UI 组件库文档

这是AWS UI组件库的文档集合，包含了界面设计规范、组件使用指南等内容。

## 文档结构

### 基础组件

- [颜色规范](basic/colors.md) - `#basic/colors`
- [通信组件](basic/communicate.md) - `#basic/communicate`
- [表单](basic/form.md) - `#basic/form`
- [图标库](basic/icon.md) - `#basic/icon`
- [交互组件](basic/interactive.md) - `#basic/interactive`
- [修饰符](basic/modifier.md) - `#basic/modifier`
- [快速开始](basic/quickstart.md) - `#basic/quickstart`
- [场景组件](basic/scene.md) - `#basic/scene`

### Component

- [Address](component/address.md) - `#component/address`
- [Atformula](component/atformula.md) - `#component/atformula`
- [Button](component/button.md) - `#component/button`
- [Chart](component/chart.md) - `#component/chart`
- [Checkbox](component/checkbox.md) - `#component/checkbox`
- [Datepicker](component/datepicker.md) - `#component/datepicker`
- [Datezone](component/datezone.md) - `#component/datezone`
- [Edithtml](component/editHtml.md) - `#component/editHtml`
- [Fileupload](component/fileupload.md) - `#component/fileupload`
- [Grid](component/grid.md) - `#component/grid`
- [Iconpicker](component/iconPicker.md) - `#component/iconPicker`
- [Input](component/input.md) - `#component/input`
- [Menu](component/menu.md) - `#component/menu`
- [Milestone](component/milestone.md) - `#component/milestone`
- [Numberbox](component/numberbox.md) - `#component/numberbox`
- [Radio](component/radio.md) - `#component/radio`
- [Select2](component/select2.md) - `#component/select2`
- [Slider](component/slider.md) - `#component/slider`
- [Switchbutton](component/switchbutton.md) - `#component/switchbutton`
- [Tabs](component/tabs.md) - `#component/tabs`
- [Toolbar](component/toolbar.md) - `#component/toolbar`
- [Tree](component/tree.md) - `#component/tree`

### 反馈组件

- [Barcode](feedback/barcode.md) - `#feedback/barcode`
- [Confirm](feedback/confirm.md) - `#feedback/confirm`
- [Dialog](feedback/dialog.md) - `#feedback/dialog`
- [Message](feedback/message.md) - `#feedback/message`
- [Messagepage](feedback/messagePage.md) - `#feedback/messagePage`
- [Notification](feedback/notification.md) - `#feedback/notification`
- [Popconfirm](feedback/popConfirm.md) - `#feedback/popConfirm`
- [Popbox](feedback/popbox.md) - `#feedback/popbox`
- [Progress](feedback/progress.md) - `#feedback/progress`
- [Qrcode](feedback/qrcode.md) - `#feedback/qrcode`
- [Scopednotifications](feedback/scopedNotifications.md) - `#feedback/scopedNotifications`
- [Sidebar](feedback/sidebar.md) - `#feedback/sidebar`
- [Spin](feedback/spin.md) - `#feedback/spin`
- [Tooltip](feedback/tooltip.md) - `#feedback/tooltip`
- [Wizard](feedback/wizard.md) - `#feedback/wizard`

### 布局组件

- [手风琴](layout/accordion.md) - `#layout/accordion`
- [盒子](layout/box.md) - `#layout/box`
- [列表单](layout/columForm.md) - `#layout/columForm`
- [列布局](layout/column.md) - `#layout/column`
- [布局](layout/layout.md) - `#layout/layout`
- [Other](layout/other.md) - `#layout/other`
- [分页](layout/pagination.md) - `#layout/pagination`
- [面板](layout/panels.md) - `#layout/panels`
- [Sidebarcollapse](layout/sidebarCollapse.md) - `#layout/sidebarCollapse`
- [表格](layout/table.md) - `#layout/table`

## 使用说明

### 查看在线文档

访问 [AWS UI 在线文档](https://docs.awspaas.com/help/commons/awsui/) 获取最新的交互式内容。

### 本地文档说明

- `index.md` - 主页面静态内容
- 各子目录包含对应模块的占位文档
- 每个文档都包含对应的在线访问链接

### 获取动态内容

由于AWS UI文档是单页应用(SPA)，动态内容需要JavaScript渲染。要获取完整内容：

1. 使用现代浏览器直接访问对应的hash路由链接
2. 使用Selenium等自动化工具进行内容抓取
3. 参考 `awsui_crawler.py` 中的完整爬虫实现

## 统计信息

- 发现路由数: 55
- 生成时间: 2025-09-30 15:16:36
- 源地址: https://docs.awspaas.com/help/commons/awsui/
