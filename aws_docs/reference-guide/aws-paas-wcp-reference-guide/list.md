# 概览 | AWS 流程引擎对WCP的支持评估

## 概览

  * 注1:Workflow Control-flow Patterns(简称 WCP),由 <http://www.workflowpatterns.com> 在 2006 年,从学术 角度提出的43个工作流控制模式,WCP 可以被理解成一组高度抽象的工作流业务场景

  * 注2:如果工具通过可视化的工具配置方式得到直接支持,被评估为+;如果模式不直接支持,但通过已存在的标准API 封装得到支持,被评估为+/-;需要通过特定程序编码或不能得到支持的,被评估为-

(一) | [Basic Control Flow Patterns(基本控制流模式)](<./part1/README.html>) | 评估  
---|---|---  
1 | [Sequence(顺序流)](<./part1/wcp-1.html>) | +  
2 | [Parallel Split(并行分支)](<./part1/wcp-2.html>) | +  
3 | [Synchronization(同步)](<./part1/wcp-3.html>) | +  
4 | [Exclusive Choice(排他选择)](<./part1/wcp-4.html>) | +  
5 | [Simple Merge(简单汇聚)](<./part1/wcp-5.html>) | +  
(二) | [Advanced Branching and Synchronization Patterns(高级分支和同步模式)](<./part2/README.html>) | 评估  
---|---|---  
6 | [Multi-Choice(多选择)](<./part2/wcp-6.html>) | +  
7 | [Structured Synchronizing Merge(结构化同步汇聚)](<./part2/wcp-7.html>) | +  
8 | [Multi-Merge(多例汇聚)](<./part2/wcp-8.html>) | +  
9 | [Structured Discriminator(结构化鉴别器)](<./part2/wcp-9.html>) | +  
28 | [Blocking Discriminator(阻塞鉴别器)](<./part2/wcp-28.html>) | -  
29 | [Cancelling Discriminator(取消鉴别器)](<./part2/wcp-29.html>) | +  
30 | [Structured Partial Join(结构化部分合并)](<./part2/wcp-30.html>) | +  
31 | [Blocking Partial Join(阻塞部分合并，M选N)](<./part2/wcp-31.html>) | -  
32 | [Cancelling Partial Join(取消部分合并，M选N)](<./part2/wcp-32.html>) | +  
33 | [Generalised AND-Join(一般并行合并)](<./part2/wcp-33.html>) | +  
37 | [Local Synchronizing Merge(本地化同步汇聚)](<./part2/wcp-37.html>) | +  
38 | [General Synchronizing Merge(通用同步汇聚)](<./part2/wcp-38.html>) | +  
41 | [Thread Merge(线程汇聚)](<./part2/wcp-41.html>) | +  
42 | [Thread Split(线程分支)](<./part2/wcp-42.html>) | -  
(三) | [Iteration Patterns(模迭代模式)](<./part3/README.html>) | 评估  
---|---|---  
10 | [Arbitrary Cycles(任意循环)](<./part3/wcp-10.html>) | +  
21 | [Structured Loop(结构化循环)](<./part3/wcp-21.html>) | +  
22 | [Recursion(递归)](<./part3/wcp-22.html>) | +  
(四) | [Termination Patterns(终止模式)](<./part4/README.html>) | 评估  
---|---|---  
11 | [Implicit Termination(隐式终止)](<./part4/wcp-11.html>) | +  
43 | [Explicit Termination(显式终止)](<./part4/wcp-43.html>) | +  
(五) | [Multiple Instance Patterns(多实例模式)](<./part5/README.html>) | 评估  
---|---|---  
12 | [Multiple Instances without Synchronization(异步多例)](<./part5/wcp-12.html>) | +  
13 | [Multiple Instances with a Priori Design-Time Knowledge(设计期确定多例)](<./part5/wcp-13.html>) | +  
14 | [Multiple Instances with a Priori Run-Time Knowledge(运行期确定多例)](<./part5/wcp-14.html>) | +  
15 | [Multiple Instances without a Priori Run-Time Knowledge(运行期无法确定多例)](<./part5/wcp-15.html>) | +/-  
34 | [Static Partial Join for Multiple Instances(静态多例合并)](<./part5/wcp-34.html>) | -  
35 | [Cancelling Partial Join for Multiple Instances(取消部分多例合并，M选N)](<./part5/wcp-35.html>) | +  
36 | [Dynamic Partial Join for Multiple Instances(动态多例合并)](<./part5/wcp-36.html>) | +/-  
(六) | [State-based Patterns(状态模式)](<./part6/README.html>) | 评估  
---|---|---  
16 | [Deferred Choice(延迟选择)](<./part6/wcp-16.html>) | +  
17 | [Interleaved Parallel Routing(并行交叉路由)](<./part6/wcp-17.html>) | +  
18 | [Milestone(里程碑)](<./part6/wcp-18.html>) | +/-  
39 | [Critical Section(独占)](<./part6/wcp-39.html>) | +/-  
40 | [Interleaved Routing(交叉路由)](<./part6/wcp-40.html>) | +/-  
(七) | [Cancellation and Force Completion Patterns(取消模式)](<./part7/README.html>) | 评估  
---|---|---  
19 | [Cancel Task(取消任务实例)](<./part7/wcp-19.html>) | +  
20 | [Cancel Case(取消流程)](<./part7/wcp-20.html>) | +  
25 | [Cancel Region(取消区域)](<./part7/wcp-25.html>) | +/-  
26 | [Cancel Multiple Instance Activity(取消多例)](<./part7/wcp-26.html>) | +  
27 | [Complete Multiple Instance Activity(完成多例)](<./part7/wcp-27.html>) | +/-  
(八) | [Trigger Patterns(触发器模式)](<./part8/README.html>) | 评估  
---|---|---  
23 | [Transient Trigger(瞬间触发)](<./part8/wcp-23.html>) | +  
24 | [Persistent Trigger(持久触发)](<./part8/wcp-24.html>) | -