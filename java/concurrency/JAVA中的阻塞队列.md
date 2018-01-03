JAVA中的阻塞队列
===

阻塞队列(BlockingQueue):是一个支持两个附加操作的队列(FIFO),这两个附加操作是指以阻塞线程的方式对队尾插入和队首移除元素，这里对阻塞的理解为队列满
不能插入元素时阻塞当前线程直到队列有空，队列为空不能获取任何元素时阻塞当前线程直到队列有元素。

接口BlockingQueue中定义了4组方法，每组方法的区别如下：

|方法/处理方式|抛异常-不阻塞|返会true/false-不阻塞|一直阻塞|超时退出-不阻塞|
|---|---|---|---|---|
|插入|add(e)|offer(e)|put(e)|offer(e,time,unit)|
|移除|remove()|poll()|take|poll(time,unit)|
|检查|element()|peek()|无|无|

在JDK7中提供了7个阻塞队列：

- ArrayBlockingQueue: 基于数组结构的有界阻塞队列，默认情况下不保证线程公平的访问队列。
- LinkedBlockingQueue: 基于链表结构的有界阻塞队列，默认最大长度为Integer.MAX_VALUE
- LinkedBlockingDeque: 由链表组成的双端有界阻塞队列，既可以从队列的两端插入和移除元素，可以将竞争分摊到两端，也运用在“任务窃取”模式中。
- LinkedTransferQueue: 基于链表结构的无界阻塞队列,如果当前有线程在等待接收元素，调用transfer方法会直接给等待的线程，而不是插入队列后再通知
- PriorityBlockingQueue: 一个支持优先级的无界阻塞队列，默认情况下采取元素支持的升序排序。
- DelayQueue: 基于PriorityQueue实现的一个支持延时获取元素的无界阻塞队列。常用场景为缓存系统的有效期，定时任务调度。队列的元素必须实现Delayed接口
- DelayedWorkQueue: 多线程下特殊设计的延时队列，主要用于任务调度
- SynchronousBlockingQueue: 不存储元素的阻塞队列，作用类似于互斥锁


