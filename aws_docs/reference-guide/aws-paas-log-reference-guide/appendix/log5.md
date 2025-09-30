# 自定义日志路径 | AWS LOG日志参考指南

# 自定义日志路径

AWS PaaS平台支持开发者输出的日志信息自定义到指定文件目录。步骤：

## 1.配置文件

配置bin/conf/aws-log4j.xml文件，增加如下信息：
    
    
    <!--name唯一标识，调用LogAPI.getLogger时，会传入该值; filename定义日志文件目录及名称; filePatternpg-定义滚动日志文件名->
    <RollingFile name="userlog" fileName="../logs/user/my.log" append="true" filePattern="../logs/user/my.log.%i">
        <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss}--%m%n"/>
            <Policies>
                <SizeBasedTriggeringPolicy size="20000KB" />
            </Policies>
        <DefaultRolloverStrategy max="5"/>
    </RollingFile>
    
    .....
    
        <Logger name="actionsoft.userlog" additivity="false" level="ALL">
            <appender-ref ref="userlog" />
        </Logger>
    

![](https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/appendix/log1.png)

## 2.代码输出日志
    
    
    //包名
    import com.actionsoft.sdk.local.api.LogAPI;
    import com.actionsoft.sdk.local.api.Logger;
    
    ......
    
    //模拟代码
    Logger logger = LogAPI.getLogger("actionsoft.userlog");
    logger.error("这是错误日志");
    logger.warn("这是警告日志");
    logger.info("这是信息日志");
    logger.debug("这是调试日志");
    

## 3.查看日志

当代码运行后，可在`logs/user/my.log`查看日志信息。

![](https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/appendix/log2.png)