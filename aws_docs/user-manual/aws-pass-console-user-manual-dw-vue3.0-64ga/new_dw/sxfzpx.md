# 筛选/分组/排序 · AWS PaaS文档中心

# 筛选/分组/排序

  * 减少DW查询设置，结合Excel、表格类产品习惯，给用户开放自定义过滤功能
  * 解决点击列排序与排序方案冲突，结合表格类产品习惯，合并至现有自定义排序
  * 列去掉了上下排序图标，简洁整体界面
  * 这三个操作只能在运行端操作

鼠标滑过列时

鼠标未滑过时  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp1.png)](<sfp1.png>)  
鼠标滑过列时  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp2.png)](<sfp2.png>)  
鼠标滑过到下拉箭头时  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp3.png)](<sfp3.png>)  
  
## 筛选

当视图中数据量大，增加执行SQL耗时超过8秒，为降低数据库压力，不执行直接提取内容的操作，用户可点击按钮确认提取，或者使用自定义筛选

**筛选字段是文本、数值类型的**

  * 鼠标滑过时打开二级菜单
  * 字段为字典或列表、单选组、复选组等组件设置了显示规则，按规则显示值显示
  * 为避免性能卡顿，对内容筛选列，进行过滤、排序、计算百分比操作
  * 如「筛选」已存在该类型的「多选过滤条件值」，按此初始化Check框
  * 按名称排序时，空白在第一行
  * 为避免性能卡顿，应用当前DW排序，如果后台GROUP记录大于300，只返回前300条和总行数供前端使用。最后一行提示，如`剩余182项忽略提供...`

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp4.png)](<sfp4.png>)

  * 点「仅筛选此项」时，将该条件放入「筛选」的「等于」条件项并应用。如果「筛选」已有该字段，更新匹配的值并应用
  * 点「自定义筛选」时，打开「筛选」下拉框，将该字段添加到条件列表下方。如果「筛选」已有该字段，不重复添加
  * 全部勾选时表示未设置过滤条件
  * 勾选项不允许超过12个。否则，DW随点击应用过滤条件，用户可继续勾选或取消勾选。同时添加或更新到`筛选`配置

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp5.png)](<sfp5.png>)  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp6.gif)](<sfp6.gif>)  
  
**筛选字段是日期类型的**

  * 当仅筛选年、年月时，为期间
  * 日期类型支持：指定日期、指定年、指定月、今天、昨天、明天、上周、本周、下周、上月、本月、下月、过去7天内、未来7天内、过去30天内、未来30天内

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp7.png)](<sfp7.png>)  
---  
[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp8.png)](<sfp8.png>)  
  
**筛选按钮**

  * 各视图通用，工具条右侧第一个
  * 用户可以在这里自定义设置，也可以通过上述操作`仅筛选此项`菜单快捷添加到这里
  * 菜单里勾选的多选，在这里为多条记录，且类型为「任一」
  * 梳理不同字段类型提供的比较方式有所不同（全平台统一）
  * 匹配条件，对有数据源的UI，自动提供下拉框。对地址簿的支持地址簿选择；UI配置了取值显示值的，按显示值筛选

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp9.png)](<sfp9.png>)

## 排序

  * 各视图通用，工具条右侧的`分组`右侧
  * 当用户点击列菜单的排序时
    * 将该字段追加到`自定义排序`，若已追加，不做处理
    * 应用自定义排序
  * 当应用`自定义排序`时（用户点击列菜单的排序或点击`排序`按钮的`自定义排序`）

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp10.gif)](<sfp10.gif>)

## 分组

  * 仅`表格`视图支持分组，工具条右侧的`筛选`按钮右侧
  * 默认没有或使用管理员预设分组
  * `树形表格`时不提供该功能
  * 添加分组字段，最多添加三个，相关操作与表格分组配置一样

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-dw-vue3.0-64ga/new_dw/sfp11.png)](<sfp11.png>)

> 其他注意点
> 
>   * `筛选`与管理员配置的查询条件不冲突，当两者都存在时，是组合的AND关系
>   * 支持内容筛选的UI组件（不在该范围的，该菜单不提供 `>`箭头图标及二级菜单，点击等于 `自定义筛选`操作）
>     * 单行、数值、货币、列表、单选、多选、日期、日期时间、滑竿、打分、开关
>     * 所有字典类、地址簿
>   * 移动端不提供用户自定义`分组`的定义，仅PC
>   * 移动端支持`筛选`，将原DW查询条件+自定义筛选结合成一个页面场景
>   * 流程视图、表格导航树、日历不支持分组，数据来源是数据服务、数据流的也不支持分组
>   * 数据来源是数据服务、数据流的也不支持筛选、排序
>