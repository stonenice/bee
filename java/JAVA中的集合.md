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
## Map
## Queue



