# Multiple Instance Patterns(多实例模式) | AWS 流程引擎对WCP的支持评估

# Multiple Instance Patterns(多实例模式)

多实例模式描述的是，在一个流程实例中，同一个活动的有多个活动的线程（因此共享相同的实现定义）。多实例可以在三种情况下出现：

  1. 一个活动在触发的时候可以启动自己的多个实例（这种形式的活动是一个多实例活动）；
  2. 一个给定的活动，接收多个独立的触发命令后，可以启动多次；
  3. 在一个流程实例中的两个或两个以上的活动共享相同的实现定义。就一个多实例活动来说这可能是相同的活动或者就一个活动块来说是一个共同的子过程定义。这些活动中的两个（或多个）被触发，使得它们的执行重叠（部分或全部）。

  * [WCP12-Multiple Instances without Synchronization(异步多例)](<./wcp-12.html>)
  * [WCP13-Multiple Instances with a Priori Design-Time Knowledge(设计期确定多例)](<./wcp-13.html>)
  * [WCP14-Multiple Instances with a Priori Run-Time Knowledge(运行期确定多例)](<./wcp-14.html>)
  * [WCP15-Multiple Instances without a Priori Run-Time Knowledge(运行期无法确定多例)](<./wcp-15.html>)
  * [WCP34-Static Partial Join for Multiple Instances(静态多例合并)](<./wcp-34.html>)
  * [WCP35-Cancelling Partial Join for Multiple Instances(取消部分多例合并，M选N)](<./wcp-35.html>)
  * [WCP36-Dynamic Partial Join for Multiple Instances(动态多例合并)](<./wcp-43.html>)