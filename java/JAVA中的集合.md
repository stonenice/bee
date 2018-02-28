![JAVA Collection Framework](https://raw.githubusercontent.com/stonenice/bee/master/statics/images/JAVA%20Collections%20Framework.jpg)

## 系统整理JAVA集合框架
>Java集合框架包含了大部分Java开发中用到的数据结构，主要包括List列表、Set集合、Map映射、迭代器（Iterator、Enumeration）、
>工具类（Arrays、Collections）几个部分。

集合框架被设计成要满足以下几个目标：

- 该框架必须是高性能的。基本集合（动态数组，链表，树，哈希表）的实现也必须是高效的。
- 该框架允许不同类型的集合，以类似的方式工作，具有高度的互操作性。
- 对一个集合的扩展和适应必须是简单的。

为此，整个集合框架就围绕一组标准接口而设计。完整的集合框架中除了Collection外还包括Map，Map里存储的是键/值对。尽管Map没有继承Collection接口，
但是它们完全整合在集合中。 这种理解源自数据结构，计算机中的数据结构有：集合、线性结构、树型结构、图。 集合的基本内容如下：

- 集合类存放于Java.util包中。
- 集合类型主要有3种：set(集）、list(列表包含Queue）和map(映射)。
- Collection：Collection是集合的基本接口，List、Set、Queue的最基本的接口。
- Iterator：迭代器，使你能够通过循环来得到或删除集合的元素。ListIterator 继承了Iterator，以允许双向遍历列表和修改元素。
- Map：是映射表的基础接口

**要点总览：**
<pre>
1. 集合是一个对象，可容纳其他对象的引用。集合接口声明对每一种类型的集合可以执行的操作。
2. 任何对象加入集合类后，自动转变为Object类型，所以在取出的时候，需要进行强制类型转换。
3. 常见的理解中说Set是无序的，List是有序的。我理解这里的有序和无序是指集合是否能确保元素插入的先后顺序，因为TreeSet的实现就是元素自然有序。
</pre>

## Set
Set直接继承自Collection接口,存储的是**无序、不重复**的数据。 Set接口常见的两个实现类为HashSet和TreeSet, 两个底层实现的算法有所不同，因此
在使用是需要非常小心。 其主要特点为：

1. Set集合不允许出现重复数据
2. 允许包含值为null的元素，但最多只能有一个null元素。不过这条规则得根据具体实现类来看，HashSet就支持null元素，因为底层实现是HashMap。
TreeSet底层是TreeMap的实现，因此TreeSet实现的Set就不支持插入null元素。

|类名|算法|描述|
|---|---|---|
|HashSet|Hash散列算法，利用hashCode()算出元素位置后使用equals()判断当前元素和已有元素是否相等，相等则舍弃以实现元素不重复|只要是Hash算法就必须确保hashCode()和equals()方法逻辑的正确性。<br/>HashSet特点是元素无序。<br/>JDK1.8中HashSet的具体实现是使用HashMap进行改造的，支持dummy参数的是使用LinkedHashMap改造而来，因此HashSet允许null,且最多只有一个null|
|TreeSet|利用平衡二叉树(红黑树算法)的特征实现元素不重复，主要是利用compareTo()对所有元素进行二分查找，如果元素已存在就舍弃|必须确保compareTo()方法逻辑正确.<br/>元素自然有序.<br/>TreeSet是利用TreeMap进行改造而来，不过由于null不能提供compareTo()方法因此TreeSet不支持null元素|

## List
List是有序的Collection，使用此接口能够精确的控制每个元素插入的位置。用户能够使用索引的位置来访问List中的元素其特点是**有序,可重复类**，
似于Java数组。List关注的是索引，拥有一系列和索引相关的方法，查询速度快。往list集合里插入或删除数据时，会伴随着后面数据的移动，
所有插入删除数据速度慢（需要根据底层使用的数据结构来定，如果是连续内存块则会这样，如果是链表结构则插入和删除都很快）。

- List允许有相同的元素存在。
- 除了具有Collection接口必备的的iterator()方法外，还提供了listIterator()方法，放回一个 ListIterator接口。
- 实现List接口的常用类有ArrayList、LinkedList、Vector(Stack)、CopyOnWriteArrayList

|类名|内容|
|---|---|
|ArrayList|底层数据结构是数组，查询快、支持随机访问、增删慢、线程不安全、效率高，其正好与LinkedList互为补充。<br/>ArrayList底层就是Object[] elementData的数据进行实现，因此**实际的类型为Object,对元素的插入获取都会进行拆箱和装箱**。**使用new实例化时容量为零**，只有在添加第一个元素时才分配默认的**容量大小10**。当容量不够需要扩容是，会使用**oldCapacity + (oldCapacity >> 1)的新容量进行扩容，既原容量的1.5倍**。|
|LinkedList|底层数据结构是双向链表并实现了Deque接口,查询慢,不支持随机访问、增删快、线程不安全、效率高，与ArrayList互为补充。<br/>LinkedList的结构是一个size,first指针,last指针构成的双向链表(双端队列).|
|Vector(Stack)|Vector是基于Object[] elementData的实现，支持随机访问，使用new实例化时默认大小就是10和ArrayList第一次添加元素时为10不同。扩容时按如下公式进行扩容**oldCapacity + ((capacityIncrement > 0) ?capacityIncrement : oldCapacity),既原来的2倍**进行扩容. 由于使用了synchronized关键字修饰了方法，因此Vector是线程安全的。 Stack直接继承自Vector，只是对元素的访问顺序进行了限制，限制后为后进先出LIFO。|
|CopyOnWriteArrayList|线程安全，**COW（Copy On Write）**是一种读写分离的思想。新增元素时不直接修改原来数组而是直接复制一份进行修改，修改后再加锁根据数据指针。实现的效果是get方法做到无锁并发，**写时使用ReentryLock进行互斥更新**。具体内容如下：|

**CopyOnWriteArrayList:**<br/>
CopyOnWrite容器即写时复制的容器。通俗的理解是当我们往一个容器添加元素的时候，不直接往当前容器添加，而是先将当前容器进行Copy，复制出一个新的容器，然后新的容器里添加元素，添加完元素之后，再将原容器的引用指向新的容器。这样做的好处是我们可以对CopyOnWrite容器进行并发的读，而不需要加锁，因为当前容器不会添加任何元素。所以CopyOnWrite容器也是一种读写分离的思想，读和写不同的容器。

优点：

- CopyOnWrite并发容器用于读多写少的并发场景。比如白名单，黑名单，商品类目的访问和更新场景
- 实现高性能的无锁并发读取

缺点：

- 内存占用问题  因为CopyOnWrite的写时复制机制，所以在进行写操作的时候，内存里会同时驻扎两个对象的内存。很有可能造成频繁的Yong GC和Full GC
- 数据一致性问题  CopyOnWrite容器只能保证数据的最终一致性，不能保证数据的实时一致性。所以如果你希望写入的的数据，马上能读到，请不要使用CopyOnWrite容器。

## Map
## Queue



