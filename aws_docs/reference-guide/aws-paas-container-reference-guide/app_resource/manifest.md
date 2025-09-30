# manifest配置 | AWS PaaS应用容器与资源控制参考指南

# manifest配置

manifest.xml是一个UTF-8（无BOM）格式的XML文件，为容器描述了应用的基本配置信息，位置在该应用的根目录下
    
    
    %appId%/manifest.xml
    

主要配置项说明如下

项 | 说明  
---|---  
name | 应用名称  
version | 版本号，格式为`数值.数值` 。如1.0  
buildNo | 打包流水号，每执行一次dist操作顺序加1  
developer | 应用开发者信息  
categoryVisible | 是否提供建模服务  
description | 应用一句话简述  
details | 应用详细说明  
reloadable | 是否支持热部署  
depend | 父应用（直接依赖）  
requires | 应用依赖声明（间接依赖）  
properties | 应用配置属性  
deployment | 应用自动化部署配置  
installListener | 应用安装事件  
startListener | 应用启动事件  
stopListener | 应用停止事件  
upgradeListener | 应用升级事件  
uninstallListener | 应用卸载事件  
... | ...  
  
### 注意事项

  * 该文件由PaaS提供的各种工具自动维护，禁止非专业级人员手工修改
  * depend有versions属性，支持若该应用兼容多个父应用的版本，可使用半角逗号隔开

### 例子
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    
    <app xmlns="http://www.actionsoft.com.cn/app">
      <name>工作网络</name>
      <version>2.0</version>
      <buildNo>12</buildNo>
      <developer id="776cca9a287c8b4d63b9cad216aa3859" tablePrefix="ACT" url="http://www.actionsoft.com.cn">北京炎黄盈动科技发展有限责任公司</developer>
      <productId/>
      <categoryVisible>false</categoryVisible>
      <releaseDate/>
      <description><![CDATA[以人为中心连接员工与工作信息，提供独立、安全、高效的企业级内网工作沟通平台。]]></description>
      <details><![CDATA[工作网络的主题是你在忙什么工作。这是一种协作引导，让你发布工作状态，组织同事来讨论创意、问问题、分享链接和其他信息。从这个角度，相当于为每个企业建立一个内部高度协作的知识库，这里保存了所有员工档案和问题对答记录。工作网络不仅仅用于沟通和讨论，还提供了丰富的扩展应用，帮助你如何完成工作。
    
    <b>主要功能</b>
    - 建立和管理一个或多个工作网络，每个工作网络是信息流动的边界
    - 建立和管理多个小组，小组间的信息相互隔离
    - 提供小组通讯录和小组介绍，可以充分个性化小组信息
    - 支持文字、文档、链接、投票、表扬、公告等类型的动态，提供对图片、Office文件缩略预览
    - 符合用户社交沟通习惯，支持赞、回复、转发、收藏和@
    - 支持#话题#汇聚信息流
    - 不断丰富的小组应用，安装即使用
    - 开放小组应用编程接口，允许开发者通过API向小组发送动态，通过小组应用扩展点开发特定需求的小组应用
    
    <b>特点</b>
    - 基于AWS PaaS的私有部署，安全可靠
    - 高性能缓存设计，支持大中型企业用户群
    
    
    <b>**特别说明</b>
    - 该应用依赖“通知中心”应用，对加入小组申请进行审核
    ]]></details>
      <installDate>2014-05-29 11:12:00</installDate>
      <upgradeDate/>
      <installListener/>
      <pluginListener>com.actionsoft.apps.network.Plugins</pluginListener>
      <startListener/>
      <stopListener/>
      <upgradeListener/>
      <uninstallListener/>
      <reloadable>true</reloadable>
      <upgradeRollback/>
      <requires>
        <require appId="com.actionsoft.apps.notification" notActiveHandler="error"/>
        <require appId="com.actionsoft.apps.favorite" notActiveHandler="none"/>
        <require appId="com.actionsoft.apps.jod" notActiveHandler="none"/>
        <require appId="com.actionsoft.apps.profile" notActiveHandler="none"/>
        <require appId="com.actionsoft.apps.mydriver" notActiveHandler="none"/>
        <require appId="com.actionsoft.apps.entaddress" notActiveHandler="none"/>
        <require appId="com.actionsoft.apps.vote" notActiveHandler="none"/>
      </requires>
      <properties>
        <property action="edit" group="表扬徽章定义" name="love" title="有爱" type="input" isSystem="false" desc="有爱">爱心满满。</property>
        <property action="edit" group="表扬徽章定义" name="trophy" title="奖杯" type="input" isSystem="false" desc="奖杯">取得了胜利。</property>
        <property action="edit" group="表扬徽章定义" name="cake" title="蛋糕" type="input" isSystem="false" desc="蛋糕">生日快乐。</property>
        <property action="edit" group="工作网络" name="isShowNum" title="小组应用工具栏显示个数" type="input" isSystem="false" desc="小组应用工具栏显示个数">3</property>
        <property action="edit" group="表扬徽章定义" name="flag" title="礼物" type="input" isSystem="false" desc="礼物">谢谢你做出的贡献！</property>
        <property action="edit" group="团队协作" name="storeMyDriver" title="是否启用转存到个人网盘" type="combox" isSystem="false" desc="是否启用将附件转存到个人网盘功能（true/false）" ref="true|false">true</property>
        <property action="edit" group="表扬徽章定义" name="good-news" title="喜报" type="input" isSystem="false" desc="喜报">付出总会有回报！</property>
        <property action="edit" group="表扬徽章定义" name="coffee" title="咖啡" type="input" isSystem="false" desc="咖啡">休息一下。</property>
        <property action="edit" group="表扬徽章定义" name="to-force" title="给力" type="input" isSystem="false" desc="给力">给力。</property>
        <property action="edit" group="表扬徽章定义" name="team" title="团队" type="input" isSystem="false" desc="团队">成功是一个团队运动。谢谢你的参与!</property>
        <property action="edit" group="工作网络" name="titleBgColor" title="标题背景颜色" type="input" isSystem="false" desc="标题背景颜色">#00CC99</property>
        <property action="edit" group="团队协作" name="usingVote" title="是否启用投票调查" type="combox" isSystem="false" desc="是否启用投票调查功能（true/false）" ref="true|false">true</property>
      </properties>
      <depend versions="6.1">_bpm.portal</depend>
      <deployment>
        <system id="obj_00093403df6a17ed729913d64f48f930" icon16="../commons/img/home_16.png" icon64="../commons/img/home_64.png" icon96="../commons/img/home_96.png" notifier="" name="%u9996%u9875" target="mainFrame" url="/" deployUrlType="2" source="1">
          <directory id="obj_633411ff934543c29cd68f6f0e24c614" icon16="../commons/img/home_16.png" icon64="../commons/img/home_64.png" icon96="../commons/img/home_96.png" notifier="" name="%u56E2%u961F" target="mainFrame" url="/" deployUrlType="2" source="0">
            <function id="obj_39c53a01a09c4097a3c0d86cb796f76f" icon16="../apps/com.actionsoft.apps.network/img/icon16.png" icon64="../apps/com.actionsoft.apps.network/img/icon64.png" icon96="../apps/com.actionsoft.apps.network/img/icon96.png" notifier="com.actionsoft.apps.network.metro.NetworkPortletNotifier" name="%u5DE5%u4F5C%u7F51%u7EDC" target="mainFrame" url="./w?sid=@sid&amp;cmd=com.actionsoft.apps.network_home" deployUrlType="2" source="0"/>
          </directory>
        </system>
      </deployment>
    </app>