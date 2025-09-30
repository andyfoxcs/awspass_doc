# 设计即执行 | AWS BPMN2 Process参考指南

# 设计即执行

秉承`设计即执行`的技术路线，可以将用户从需求提出到部署缩短到分秒之内。这个过程由内部一套复杂机制自动进行检查和处理，大大减少甚至无需测试。`设计即执行`让企业的商业流程以最小的成本、最高的效率、最快的速度拥抱变化。

AWS采取如下措施保障`设计即执行`达到生产环境对业务完整性的苛刻要求：

  * 识别BPM PaaS的[运行环境](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/version/README.html>)和[流程版本状态](<../process_designer/versions.html>)，通过`level 1,2 validation`校验，避免用户错误的设计操作
  * 通过`level 0 validation`校验保证有效的设计结构被持久化到磁盘，避免内存失效

![](https://docs.awspaas.com/reference-guide/aws-paas-process-reference-guide/process_deployment/11.png)

处理过程如上图。

  * **步骤1.** 用户在前端对X流程进行设计操作前，同步等待`level 1 validation`校验，在提交设计前进行`level 2 validation`校验。1-2校验通过，继续执行步骤2
  * **步骤2.** AWS的`BPMNIO`层对接收到的流程模型进行`level 0 validation`校验，检查模型结构的完整性和语义合法性。0校验通过，以BPMN2规范的文件保存至磁盘
  * **步骤3.** 准备新缓存对象，依次切换本地和集群节点缓存
  * **步骤4.** 引擎执行生效的缓存流程模型

## 延伸阅读

  * [语法校验](<../process_designer/semantics_validate.html>)
  * [多人编辑](<../process_designer/locked.html>)
  * [流程版本](<../process_designer/versions.html>)