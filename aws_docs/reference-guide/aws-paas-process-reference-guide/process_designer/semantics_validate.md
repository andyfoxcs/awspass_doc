# 语法校验 | AWS BPMN2 Process参考指南

# 语法校验

业务系统需要确保逻辑结构的准确性，而流程设计器需要更友好、易用的傻瓜化操作。

AWS流程设计器在三个层面对流程结构进行自动化校验，确保流程引擎的准确执行和业务完整性：

  * 加载前合法性校验（level 0 validation）
  * 操作前合法性校验（level 1 validation）
  * 保存前合法性校验（level 2 validation）

## 加载前合法性校验（level 0 validation）

加载BPMN XML文件时的合法性校验。这是最底层的校验机制，主要通过`BPMN20.xsd`、`aws-bpmn-extensions-6.0.xsd`等系列Sechma定义，对模型结构进行校验。如不符合BPMN2规范、文件被损坏、缺失AWS扩展描述等，将抛出[异常日志](<https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/system_log/README.html>)。

  * `level 0`检查不通过，禁止在AWS PaaS里执行。

## 操作前合法性校验（level 1 validation）

设计器会基于当前[流程版本](<versions.html>)类型，对结构性调整的操作进行检查控制，防止用户犯错误。

  * `level 1`检查不通过，禁止相关操作。

#### 1\. 防止结构破坏

通常是指删除流程对象（如节点、事件）。这种场景在任何流程版本都会校验（如设计状态、运行状态），如果要删除的流程对象已经实例化，该流程对象不允许从画布上删除。

**如删除如下节点时，设计器抛出合法性校验警告** ![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/31.png)

**解决方案**

  1. 在`实例运行管理`中，删除该流程产生的实例
  2. 基于创建的新版本进行大结构调整

#### 2\. 保护正式`运行`版本主体结构的稳定性

流程版本处于`运行`类型时，可以修改所有的配置，新增规则等。但是对如下操作被检查和阻止

  * 禁止删除、增加活动类节点
  * 禁止删除所有流程对象
  * 禁止删除规则连线

**解决方案**

  * 基于创建的新版本进行大结构调整

## 保存前合法性校验（level 2 validation）

当用户修改流程结构保存时，自动进行一次结构合法性检查。设计器会友好的导航错误位置（点击错误提示），给出改进解决方案提示。例如

  * 断线
  * 自连接
  * 结构不合法（如无开始、无结束）
  * 场景不合法（如边界事件未吸附、各种符号用错场景）

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_designer/22.png)

  * `level 2`检查不通过，禁止保存。

## 延伸阅读

  * [流程建模规范](<../appendix/definition_spec.html>)
  * [流程引擎规范](<../appendix/engine_spec.html>)
  * [AWS LOG日志参考指南](<https://docs.awspaas.com/reference-guide/aws-paas-log-reference-guide/index.html>)