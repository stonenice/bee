Executor是Java中的轻量级并发编程框架，如果可以你也可利用基本的线程实现同样的功能。Executor框架是指java 5中引入的一系列并发库中
与Executor相关的一些功能类，其中包括线程池，Executor，Executors，ExecutorService，CompletionService，Future，Callable等。
并发编程的一种编程方式是把任务拆分为一些列的小任务，即Runnable，然后在提交给一个Executor执行，Executor.execute(Runnalbe) 。
Executor在执行时使用内部的线程池完成操作。

ExecutorService继承于Executor接口，ExecutorService提供了管理Executor生命周期的各种方法。Executors提供了创建各种线程池的方法。
可以通过Executors创建下列类型的线程池,返回值得类型为ExecutorService:
1) CachedThreadPool(Executors.newCachedThreadPool):创建一个可缓存的线程池，调用execute 将重用以前构造的线程（如果线程可用）。
   如果现有线程没有可用的，则创建一个新线程并添加到池中。终止并从缓存中移除那些已有 60 秒钟未被使用的线程
   
2) FixedThreadPool(Executors.newFixedThreadPool):创建固定数目线程的线程池。

3) SchduleThreadPool(Executors.newSchduleThreadPool):创建一个支持定时及周期性的任务执行的线程池，多数情况下可用来替代Timer类。

4) SingleExecutor(Executors.newSingleExecutor):创建一个单线程化的Executor。

5) SingleSchduledExecutor(Executors.newSingleSchduleExecutor):创建一个单线程化的Executor,并支持定时及周期性的任务执行。

6) WorkStealingPool(Executors.newWorkStealingPool):创建一个拥有多个任务队列（以便减少连接数）的 ExecutorService。


Callable与Future(FutureTask)异步执行：
Future<V>代表一个异步执行的操作，通过get()方法可以获得操作的结果，如果异步操作还没有完成，则，get()会使当前线程阻塞。
FutureTask<V>实现了Future<V>和Runable<V>。Callable代表一个有返回值得操作。
//======================= Example ===============================================
    Callable<Integer> func = new Callable<Integer>(){  
        public Integer call() throws Exception {  
            System.out.println("inside callable");  
            Thread.sleep(1000);  
            return new Integer(8);  
        }         
    };  
    
    FutureTask<Integer> futureTask  = new FutureTask<Integer>(func);  
    Thread newThread = new Thread(futureTask);  
    newThread.start();  
      
    try {  
        System.out.println("blocking here");  
        Integer result = futureTask.get();  
        System.out.println(result);  
    } catch (Exception e) {  
    }  
