# 调试SQL输出 | AWS LOG日志参考指南

# 调试SQL输出

AWS为开发者调试SQL提供了系统开关
    
    
    配置见%AWS-HOME%/bin/conf/aws-log4j.xml，默认关闭。
    
    //level值为OFF时不输出sql操作，为ALL时输出sql操作
    <Logger name="com.actionsoft.sql" additivity="false" level="OFF">
                <appender-ref ref="asyncAppender" />
    </Logger>