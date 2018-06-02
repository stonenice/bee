栈上分配
---
栈上分配时JVM提供的一项优化，基本思想是将线程私有的对象，打撒分配到栈上，而不是只要是对象都分配到堆的测试。判断对象的作用域是否可能
逃逸出函数体叫做逃逸分析。

栈上分配的好处是函数调用结束后自行销毁，而不需要垃圾回收器的接入，减少GC的次数，栈上分配速度快，访问快，从而提升系统性能。对于仅函数
块作用域下的大量零散小对象，栈上分配时一种很好的优化方式。

栈上分配依赖于逃逸分析和标量替换实现的，开启从功能需要同时开启-XX:+DoEscapeAnalysis和-XX:+EliminateAllocations两项。需要注意的是
逃逸分析只有在-server模式下才能生效。

TLAB上分配
---
TLAB为线程本地分配缓存，主要是加速对象内存的分配，堆为全局共享，多线程竞争激烈，会使性能下降。TLAB本身在Eden空间，JVM在其上为每个
线程分配独立的空间，检查线程冲突。

-XX:+UseTLAB 开启TLAB,在server模式下默认开启<br/>
-XX:+ResizeTLAB 开启自动调节TLAB的大小
-XX:TLABSize  人工指定TLAB的大小
-XX:TLABRefillWasteFraction  默认64，表示约1/64的TLAB空间作为refill_waste,既允许浪费的空间比例<br/>

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
-XX:PretenureSizeThreshold 直接进入老年代的阀值
-XX:MaxTretenuringThreshold 进入老年代的最大值

G1收集器配置
---
-XX:+UseG1GC 开启G1垃圾回收器<br/>
-XX:MaxGCPauseMillis 目标最大停顿时间，任何一次GC停顿时间超过该值，G1会尝试调整新生代和老年代的比例、堆大小、晋升年龄等。在
                     混合GC不行是会触发FullGC<br/>
-XX:ParallelGCThreads 垃圾回收器并发线程数<br/>
-XX:InitiatingHeapOccupancyPercent 内存使用率达到多少是触发并发标记<b/>

其它
---
-XX:+Inline 打开方法内联
-XX:FreqInlineSize 热点代码内联的大小阀值，超过该阀值的内联优化都不执行
-XX:ReservedCodeCacheSize 编译代码缓冲区大小，一但超过缓冲区JIT就停止工作
                     

