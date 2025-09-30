# 复杂拆分 | AWS BPMN2 Gateway参考指南

## 复杂拆分

高级开发者可以通过实现ComplexGatewayInterface接口，编写branchOutgoing()方法来决定后继的分支路径。该方法会将引擎上下文对象和该网关所有后继连线作为参数提供给开发者，要求开发者返回自己决定的分支路径。如果开发者返回了null或一个空的List集合且该网关定义了一个默认的连线，那么该默认分支将被执行。

下图给出一个使用复杂网关进行拆分路径的例子。当网关B执行时，基于当前的流程变量num值确定后继路径：

  * 如果num值在1-5之间，激活“输出num个金币”的路径，并再生成新num数
  * 如果num值在6-7之间，激活“输出num个钻石”的路径，并再生成新num数
  * 如果num值在8-10之间，结束流程

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/complex_gateway/1.png)

该示例采用了随机数，实际执行的循环次数是未知的。以下示意了一次模拟执行的结果：“生成随机数”节点共执行了3次，复杂网关的branchOutgoing()方法也被执行了三次，在第3次时num为10，结束了流程。
    
    
    由JavaScript脚本在[1-10]选择一个随机数=7
    7个钻，快接近啦
    由JavaScript脚本在[1-10]选择一个随机数=2
    2个币，还不够
    由JavaScript脚本在[1-10]选择一个随机数=10
    

为了进一步了解这个示例是如何完成工作的，我们就关键场景做一下简单的说明。

> 完整实现可安装“AWS SDK API接口验证”应用，在Process API>Gateway网关>复杂网关流程(自定义branchOutgoing)中得到相关模型和源码示例。

#### 生成随机数

这是一个脚本节点(Script Task)，我们在这里使用JavaScript脚本生成一个随机数并赋值给流程变量num，如下：

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/complex_gateway/2.png)

#### 输出num个金币

这又是一个脚本节点，在这里使用JavaScript脚本将num变量打印输出，如下：

![](https://docs.awspaas.com/reference-guide/aws-paas-process-gateway-reference-guide/complex_gateway/3.png)

#### 复杂网关（网关B）代码实现

这是重点要介绍的部分。在示例中，该网关开发了一个名为“ComplexGateway1Test”的Java类，针对这一特殊场景对branchOutgoing()方法进行了实现，代码如下：
    
    
    /**
     * 复杂网关-Split Sample
     */
    public class ComplexGateway1Test implements ComplexGatewayInterface {
    
        /**
         * 汇聚前置分支
         *
         * @param ctx 引擎上下文
         * @param incomingSequenceFlows 前置分支定义
         * @param finishedSequenceFlows 已完成的前置分支
         * @return 符合聚合条件返回true
         */
        public boolean mergeIncoming(final BehaviorContext ctx, final List<SequenceFlowModel> incomingSequenceFlows, final List<SequenceFlowModel> finishedSequenceFlows) {
            return true;// 不适用
        }
    
        /**
         * 评估，返回后继分支路径
         *
         * @param ctx 引擎上下文
         * @param outgoingSequenceFlows 后继分支定义
         * @return 要激活的后继分支连线，如果返回了null或一个空的List集合且该网关定义了一个默认的连线，那么该默认分支将被执行
         */
        public List<SequenceFlowModel> branchOutgoing(final BehaviorContext ctx, final List<SequenceFlowModel> outgoingSequenceFlows) {
            List<SequenceFlowModel> branch = new ArrayList<SequenceFlowModel>();
            ProcessNode processNode = (ProcessNode) ctx.getProcessElement();
            // 判断流程变量num
            int num = 0;
            Object str1 = ctx.getVariable("num");
            try {
                if (str1 != null) {
                    num = Integer.parseInt(str1.toString());
                }
            } catch (NumberFormatException e) {
                // 抛出格式非法异常，流程分支将中断于该网关
                throw new AWSIllegalArgumentException("num", AWSIllegalArgumentException.FORMAT);
            }
            if (num > 0 && num < 6) {
                branch.add(processNode.findOutgoingTransition("obj_c6011922a2100001b6fb778063c61d39"));
            } else if (num > 5 && num < 8) {
                branch.add(processNode.findOutgoingTransition("obj_c60119282c3000015be93187785c18e3"));
            } else {
                branch.add(processNode.findOutgoingTransition("obj_c6011926812000016f557dcd5f2e14da"));
            }
            return branch;
        }
    }
    

> 关于该代码的ComplexGatewayInterface 接口说明，可参见AWS SDK API的JavaDoc文档 <https://docs.awspaas.com/api/aws-api-javadoc/index.html>