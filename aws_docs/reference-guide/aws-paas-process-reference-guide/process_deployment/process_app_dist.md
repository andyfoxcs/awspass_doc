# 分发流程应用 | AWS BPMN2 Process参考指南

# 分发流程应用

分发应用是指应用从当前AWS PaaS环境安装/升级到目标PaaS。分发流程应用和AWS PaaS其他类型应用相似，请关注以下建议

  * 不建议开启流程模型的`受管`选项，充分适应用户的流程差异

> 在AWS CONSOLE命令控制台，输入`dist app %appId%`可直接将打包应用输出至`%AWS-HOME%/apps/dist`下

## 延伸阅读

  * [受管应用](<https://docs.awspaas.com/reference-guide/aws-paas-env-guide/managed/README.html>)
  * [PaaS容器对应用的周期管理](<https://docs.awspaas.com/reference-guide/aws-paas-container-reference-guide/app_lifecycle/README.html>)
  * [打包下载应用](<https://docs.awspaas.com/getting-started-guide/aws-app-create-started-guide/step4/README.html>)
  * [安装应用](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_install/README.html>)
  * [升级应用](<https://docs.awspaas.com/user-manual/aws-pass-console-user-manual-amc/application_upgrade/README.html>)