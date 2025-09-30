# 容器 | AWS PaaS应用容器与资源控制参考指南

# 容器

应用容器（App Container）是AWS PaaS的控制内核，在AWS PaaS中一切皆应用。应用容器是AWS PaaS架构思想中值得称赞的原创设计，完成于2013年8月。

AWS PaaS利用容器来运行AWS应用。每个应用的资源被容器独立的管理和调度，这些资源被应用Id（AppId）命名和隔离。

### 本地应用仓库

每个AWS PaaS实例的容器有特定的工作边界（应用仓库）。容器会根据应用所处的不同周期阶段，在特定的应用仓库间切换。

  * apps/upload _处于待安装/升级的应用介质文件_
  * apps/install _安装的应用资源_
  * apps/uninstall _被卸载的应用资源，处于该仓库的应用可以被还原或彻底删除_
  * apps/dist _存放打包成可分发的介质文件（.app后缀）_
  * apps/history _所有操作的历史资源文件_

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/basic_concept/concept-2.png)

> AWS PaaS应用容器采用业内广泛采纳的机制（如文件签名）和特殊机制来确保应用被完整的传输到容器，被成功的安装。如果中途发生意外（如文件损坏、安装或升级失败、中途物理宕机等），对应用仓库的所有操作被自动回滚到之前状态。

### 应用周期管理

应用周期主要包括：

  * 安装/升级
  * 卸载/还原
  * 彻底卸载

#### 通过控制台管理

AWS PaaS管理员可以访问实例console（控制台》应用管理）完成这些操作。

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/basic_concept/concept-3.png)

可以通过终端输出信息监控应用在容器的处理过程。如下图，用户试图在PaaS中安装`工作网络的安卓应用`，由于依赖的父应用`工作网络`尚未安装，给出错误提示

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/basic_concept/concept-4.png)

#### 通过命令行管理

对于有本地PaaS环境的开发者，也可以在AWS命令行控制台中通过如下命令完成同等操作：
    
    
    in aws //进入shell环境
    list app //列出当前PaaS的全部应用状态
    install app %AppId%,%AppId%.. //安装应用
    upgrade app %AppId%,%AppId%.. //升级应用
    dist app %AppId% //打包成分发的介质文件
    uninstall app %AppId% //卸载应用
    recovery app %AppId% //还原卸载的应用
    remove app %AppId% //彻底删除已卸载的应用（物理删除）
    

### 应用状态控制

应用状态受容器控制，状态间切换是动态的。每个应用在瞬间只存在一种状态，下面列出的八种状态有三种是中间状态（后缀ING）

  * READY（就绪）
  * STARTING（启动中）
  * ACTIVE（启动成功）
  * STOPPING（暂停中）
  * STOPPED（已暂停）
  * FAILED（已出错）
  * UNINSTALLING（卸载中）
  * UNINSTALLED（已卸载）

#### 通过控制台控制

AWS PaaS管理员可以访问实例console（控制台》应用管理）完成这些操作。

![](https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/basic_concept/concept-5.png)

#### 通过命令行控制

对于有本地PaaS环境的开发者，也可以在AWS命令行控制台中通过如下命令完成同等操作：
    
    
    in aws //进入shell环境
    start app %AppId% //启动应用
    stop app %AppId% //暂停应用
    restart app %AppId% //重启应用
    

### 应用间互操作

应用容器基于JVM，为每个应用平行分配一个相互隔离的classloader，避免了不同开发商应用间资源冲突问题。哪么，应用间的互操作该如何处理？

AWS PaaS为开发者提供了独有的ASLP 应用互操作接口协议(Application Service Locator Protocol)，这是个伟大的发明。开发者可以像访问一个互联网url地址那样，访问PaaS中其他应用的接口，看起来就这么简单：
    
    
    //获得订单信息
    aslp://com.actionsoft.apps.poc.api/getOrder
    

  * 在AWS PaaS中每个aslp服务都拥有一个唯一的访问地址,便于开发者学习和理解
  * 避开ClassLoader互依赖风险和加载风险,也通过简单协议串让开发者避开ClassLoader概念
  * 协议与应用具体位置和实现无关，任何授权的PaaS内部应用或外部系统（设备）都可以调用
  * 支持同步调用和异步调用
  * 高性能，普通计算资源配置下也可超过1万/TPS（每秒吞吐量）

> 有关ASLP接口封装，请访问<https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/aslp.html>

### 容器启动

AWS PaaS服务的启动过程，主要是容器完成各个应用资源绑定的过程，当容器操作未就绪或即将关闭时，为调用者返回的错误码如下：

  * **760 服务正在启动(Instance Starting)** _当服务器正在启动尚未就绪时，会返回该错误信息。遇到这种错误，请稍后执行_
  * **761 服务正在关闭(Instance Stoping)** _当服务器正在关闭时，会返回该错误信息。遇到这种错误，请不要再重复请求，服务器将被关闭_
  * **762 服务脱机(Instance Offline)** _当服务器处于运行中，由运维人员暂停客户端响应时，会返回该错误信息。遇到这种错误，请联系系统管理员_

### 容器日志与监控

  * 在控制台的应用管理（AMC），提供各应用运行状态和日志
  * AWS SLA服务为容器提供的监控和告警，见<https://docs.awspaas.com/reference-guide/aws-paas-sla-reference-guide/appendix1/resource_metric.html>