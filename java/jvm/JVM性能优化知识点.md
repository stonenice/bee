栈上分配
---
栈上分配时JVM提供的一项优化，基本思想是将线程私有的对象，打撒分配到栈上，而不是只要是对象都分配到堆的测试。判断对象的作用域是否可能
逃逸出函数体叫做逃逸分析。

栈上分配的好处是函数调用结束后自行销毁，而不需要垃圾回收器的接入，减少GC的次数，栈上分配速度快，访问快，从而提升系统性能。对于仅函数
块作用域下的大量零散小对象，栈上分配时一种很好的优化方式。

栈上分配依赖于逃逸分析和标量替换实现的，开启从功能需要同时开启-XX:+DoEscapeAnalysis和-XX:+EliminateAllocations两项。需要注意的是
逃逸分析只有在-server模式下才能生效。

GC日志相关的JVM参数
---
-XX:+PrintGC  简单的GC日志<br/>
-XX:+PrintGCDetails 详细的GC日志，包含GC的类型（Minor GC/Full GC）,GC收集器的类型，导致GC的原因等<br/>
-XX:+PrintHeapAtGC 在GC时打印当前堆信息<br/>
-XX:+PrintGCTimeStamps 如果要分析GC发生的时间，需要打印GC的时间戳<br/>
-XX:+PrintGCApplicationStoppedTime 打印因GC停顿的时间<br/>
-Xloggc:log.gc 指定GC信息输出的文件位置<br/>

跟踪类加载和卸载
---
-XX:TraceClassLoding 追踪类加载<br/>
-XX:TraceClassLoding 追踪类卸载<br/>

堆溢出参数
---
-XX:+HeapDumpOnOutOfMemoryError 发生OOM时Dump堆信息<br/>
-XX:HeapDumpPath 堆信息Dump的保存位置<br/>

堆栈相关参数
---
-Xmx8G JVM最大可用内存<br/>
-Xms8G JVM最小可用内存<br/>
-Xss
-Xmn3G 新生代大小<br/>
-XX:PermSize=64M 方法区（永久代）内存大小<br/>
-XX:MaxPermSize=64M 方法区（永久代）最大内存大小<br/>
-XX:MaxMetaspaceSize=64M JDK1.8后只有元数据区，默认为系统内存限制，也可进行限制<br>
-XX:ServivorRatio 新生代中Eden区与Servivor区的比值<br/>
-XX:NewRatio=老年代/新生代   新生代与老年代的比例 <br/>
