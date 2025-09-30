# 应用状态 | AWS PaaS应用容器与资源控制参考指南

# 应用状态

每个应用在瞬间只存在一种状态，下面列出的八种状态有三种是中间状态（后缀ING）

  * READY（就绪）
  * STARTING（启动中）
  * ACTIVE（启动成功）
  * STOPPING（暂停中）
  * STOPPED（已暂停）
  * FAILED（已出错）
  * UNINSTALLING（卸载中）
  * UNINSTALLED（已卸载）

这里主要介绍几个结果类状态。

## READY（就绪）

介质已被成功安装到PaaS容器，但什么都没做。是所有其他状态的前置状态。

## ACTIVE（启动成功）

应用资源已经绑定完成，处于可访问状态。

**状态转换路径**

  1. READY->STARTING->ACTIVE
  2. STOPPED->STARTING->ACTIVE
  3. FAILED->STARTING->ACTIVE

## STOPPED/FAILED（暂停）

由于启动发生严重错误或外部执行了暂停操作，应用资源的实例已经销毁完成，处于不可访问状态。

**状态转换路径**

  1. READY->STARTING->STOPPING->FAILED
  2. ACTIVE->STOPPING->STOPPED

## UNINSTALLED（卸载）

应用已被卸载。

**状态转换路径**

  1. STOPPED->UNINSTALLING->UNINSTALLED
  2. FAILED->UNINSTALLING->UNINSTALLED
  3. ACTIVE->UNINSTALLING->UNINSTALLED