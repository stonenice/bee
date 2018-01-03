在JDK的并发包中提供了几个常用的并发工具类。CountDownLatch、CyclicBarrier、Semaphore和Exchanger等帮助简化编写并发程序。

**CountDownLatch**
CountDownLatch允许一个或多个线程等待其他线程完成，其作用类似于join方法。需要注意的是CountDownLatch需要指定等待计数器的值。其提供
await(time,unit)方法支持等待一定时间后就不阻塞当前线程。join也有类似方法。
<pre>
public static void main(String[] args){
    CountDownLatch latch=new CountDownLatch(2);
    new Thread(()->{
        System.out.println("1");
        latch.countDown();
        
        System.out.println("2");
        latch.countDown();
    }).start();
    
    latch.awit()
    System.out.println("finished");
}
</pre>

**CyclicBarrier**
CyclicBarrier就是一个可以循环使用的屏障，其做的事情主要是实现一组线程到达屏障是可以被阻塞，直到最后一个线程到屏障时，屏障才会开门，
所有被屏障拦截的线程才会继续运行。
<pre>
    public static void main(String[] args) throws Exception {
        CyclicBarrier barrier = new CyclicBarrier(2, () -> {
            System.out.println("all task is finished");
        });

        new Thread(() -> {
            try {
                System.out.println("1");
                barrier.await();
                System.out.println("finished");

            } catch (Exception e) {
                e.printStackTrace();
            }
        }).start();


        new Thread(() -> {
            try {
                System.out.println("waiting 3s");
                Thread.sleep(3000);
                barrier.await();

            } catch (Exception e) {
                e.printStackTrace();
            }
        }).start();

    }
</pre>

**CyclicBarrier和CountDownLatch的区别**
1. 第一个区别是理解逻辑上的区别，CountDownLatch是指领取任务，任务没完成之前阻塞主线程的过程。CyclicBarrier是指工作先做，做到一定程度到达屏障
处阻塞工作线程，当所有工作线程都到达屏障处时执行barrierAction.同时之前被阻塞的工作线程也可以继续执行。换个角度理解也可以是工作快的先到达屏障处
后等待工作慢的线程，都到达屏障时又可以继续执行。
2. CountDownLatch的计数器只能使用一次，而CyclicBarrier的计数器可以使用reset()方法重置后使用多次。除此之外，CyclicBarrier还提供
getNumberWaiting方法返回当前阻塞线程的数量，isBroken方法用来了解阻塞的线程是否被中断等。

**Semaphore**
Semaphore(信号量)是用来控制同时访问特定资源的线程数量，它通过协调各个线程以保证合理的使用公共资源。比如可以用于做流量控制。

**Exchanger**
Exchanger是一个用于线程间协作的工具类。可以实现线程间同步的彼此进行数据交换。如果一个线程先执行exchange()进行数据交换，他会等待另一个线程也执
行exchange()交换数据时才会继续往后执行，否则该线程会一直阻塞。


