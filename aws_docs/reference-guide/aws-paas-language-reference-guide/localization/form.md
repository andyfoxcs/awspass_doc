# 表单多语言 | AWS PaaS多语言开发参考指南

# 表单多语言

表单国际化的标签格式为`[I18N#XXX]`。

流程表单存放在`%AWS_HOME%/apps/install/%APPID%/template/form/`目录下，该类文件国际化需要施人员手动修改htm文件，将需要国际化的信息使用`[I18N#]`标签括起来，然后将该信息作为国际化资源的key，在`%AWS_HOME%/apps/install/%APPID%/i18n`目录下进行多语言资源配置。例如：
    
    
    <!-- htm模板 -->
    <tr>
    <td>[I18N#会议室名称]</td>
    </tr>
    
    <!--i18n 资源配置-->
     <item key="会议室名称>
        <cn><![CDATA[会议室名称]]></cn>
        <en><![CDATA[Room Name]]></en>
        <big5><![CDATA[會議室名稱 ]]></big5>
    </item>
    

> 目前用户审批记录组织信息相关多语言需要用户手动在`%AWS_HOME%/apps/install/_bpm.platform/i18n/`目录下配置以部门名称、角色名称等为key的资源项，不支持组织类相关元数据在线配置的多语言资源。