# 应用场景 · AWS PaaS文档中心

## 应用场景

这是一种应用与应用间关联的高级开发模式，可以为你的`主应用`定义扩展点，绑定该应用扩展点的`关联应用`提供具体实现。

  * `主应用`从`关联应用`接收参数
  * `主应用`提供框架，具体逻辑处理由`关联应用`实现

**为了便于文档阅读，对词汇约定下**

  * `主应用`，指A应用提供扩展点，通过开放这个接口接收`关联应用`的注册或实现
  * `关联应用`，指与A应用发生关联的B应用，这种附加的关联特性随着B应用的存在而自动提供
  * `扩展点`，指A应用封装的一个任意`ASLP`服务。 B应用在启动时调用一次A应用的该`ASLP`服务。当B应用发生重启或资源重新加载时，AWS PaaS应用容器会以B应用的身份重新进行一次`绑定`

### `主应用`从`关联应用`接收参数

这是一种最简单的应用场景，`主应用`提供一个由`ASLP`维护的静态List队列，当有`关联应用`绑定该扩展点时，将参数传递给`主应用`。

如下代码是某个应用通过绑定`通知中心`的扩展点，向`通知中心`注册参数配置。当各种应用发送通知消息时，`通知中心`就能够根据事先绑定的配置去处理这个消息。
    
    
    Map<String, Object> params1 = new HashMap<String, Object>();
    params1.put("systemName", AppNotificationAPITest1.systemName);
    params1.put("icon", "");
    list.add(new AppExtensionProfile("通知中心->API测试-简单消息", "aslp://com.actionsoft.apps.notification/registerApp", params1));
    

### `主应用`提供框架，具体逻辑处理由`关联应用`实现

`主应用`提供一个由`ASLP`维护的静态List队列，当有`关联应用`绑定该扩展点时，将参数传递给`主应用`。参数中包含`关联应用`的实现类，该类在`主应用`的恰当场景被调用。

如下代码是某个应用通过绑定CoE`报告生成器`的扩展点，向`报告生成器`注册参数配置。`报告生成器`本身是个空壳，各种报告的实现就可以由开发者自己去实现。

[![](https://docs.awspaas.com/reference-guide/aws-paas-plugin-development-reference-guide/plugins/app-extend-1.png)](<app-extend-1.png>)
    
    
    Map<String, Object> params1 = new HashMap<String, Object>();
    params1.put("groupName", "RACI模型分析");
    params1.put("title", "RACI流程说明");
    params1.put("targetMethodScope", "process.bpmn2,process.epc,process.flowchart");// 建模大类、建模方法，多个用逗号隔开，如果为空表示全部
    params1.put("relationMethodScope", "-");// 如果设置-，表示不需要用户选择关联范围，向导页被忽略
    params1.put("lang", "cn");// 该App支持的语言，多个用逗号隔开
    params1.put("optionClass", Report1WizardOption.class.getName());// 附加的报表选项，如果该值没有，向导页被忽略
    params1.put("generClass", Report1Gener.class.getName());// 生成报告
    list.add(new AppExtensionProfile("PAL报告->RACI流程说明", "aslp://_bpm.coe/registerOutputApp", params1));