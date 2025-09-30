# 流程版本 · AWS PaaS文档中心

## 流程版本

在AWS平台中，流程版本与状态由流程版本管理工具进行自动管理，流程模型各个版本的实例控制数据相互隔离、互不影响。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/version/version2.png)](<version2.png>)

_流程版本状态及状态转换过程参考如下：_

[![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/41.png)](<https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/41.png>)

  * **DESING-设计状态**  
新建的流程模型、创建的流程新版本为`设计`状态，处在该状态下的流程设计器允许随意进行流程设计，无约束性保护。处于设计状态的流程可以参与客户端执行，但在启动时会给出`设计`字样，表示该流程处于测试阶段。

[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/version/version3.png)](<version3.png>)

  * **RUN-运行状态**  
流程模型一旦被发布，被标记为`运行`状态，处在该状态下的流程设计器不允许删除、增加节点和子流程模型，但可以修改流程相关属性和规则。处于运行状态的流程属于经过测试，正式使用的流程模型。

[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/version/version4.png)](<version4.png>)

  * **CLOSED-停用状态**  
当发布流程模型时，该流程处于`运行`状态的流程版本将被标记为`停用`状态，处在该状态下的流程设计器只读。

[![undefined](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/version/version5.png)](<version5.png>)`

> 启动流程对版本的选择参见[这里](<https://docs.awspaas.com/reference-guide/aws-paas-process-event-reference-guide/appendix/process_model_version.html>)

### 创建新版本

这是一个较为灵活的版本操作，通常会选择一个当前最新的版本作为下个新版本的设计底稿。作为一个可回溯版本的操作，设计人员也可选择一个更早期版本，然后点击`创建新版本`按钮。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/version/version7.png)](<version7.png>)

### 发布

可选择最新版本或历史版本作为正式运行的流程，同时另外一个`运行`状态的版本将被标记为`停用`状态。 [![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/version/version9.png)](<version9.png>)

> 流程模型一旦被标记为`运行`状态，将永远不能转换成`设计`状态，只能通过`创建新版本`获得一个新版本

### 复制

这是一个辅助操作，允许设计人员复制一个流程成为与之毫不相关的另外一个新流程，被复制的新流程与当前流程无版本关系。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/version/copy1.png)](<copy1.png>)

### 另存为

与复制操作一样，把原流程模型另外存一个新流程，被另存的新流程与当前流程无版本关系

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/version/copy1.1.png)](<copy1.1.png>)

### 删除

如果该流程尚未产生实例，可执行该功能删除该流程模型。删除模型后，系统会自动重新计算版本号规则，保持正常的流水号。

[![](https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-process-64ga/version/version10.png)](<version10.png>)

### 延伸阅读

  * [流程版本差异](<https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/versions.html>)