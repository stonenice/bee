介绍如何在Linux下安装部署jetty,其中操作系统为CentOS 7.2.0 64bit, JDK为1.8, Jetty位9.3.14

首先给出安装包的下载地址：
JDK:http://www.oracle.com/technetwork/java/javase/downloads/index.html
    进入页面后点击jdk下载按钮进入jdk下载页面，确认许可后下载对应的版本，由于是CentOS的原因这里有两种方法安装jdk。一种是使用rpm包，另一种是使用
    预编译好的tar.gz包。安装方式有所不同。
Jetty:http://www.eclipse.org/jetty/download.html
    Jetty所有的包都是预编译好的，直接解压便可使用
    

第一步，安装JDK
    下面介绍如何在Linux上安装JDK, 正如前面说到的一样有两种方式，两种方式都比较简单根据自己的情况进行选择。两种方式我都会进行介绍，但我个人比较
    倾向于直接解压便可用的方式，其原因是各种目录了然于胸可控性强。rpm包的默认安装目录可能因为版本的不同而发生变化，给你带来不必要的麻烦。
    
    1.RPM
    在官网上下载对应版本的rpm包，我这里使用的包名为jdk-8u111-linux-x64.rpm。在安装之前请先检查是否已经安装，命令如下：
        1）检查是否已经安装JDK  rpm -qa|grep jdk 或者 rpm -qa|grep java
        2）删除安装包    rpm -e [package]
        3）安装软件包    rpm -ivh [pachake]
    检查没有安装过jdk后，执行命令 rpm -ivh jdk-8u111-linux-x64.rpm 完成jdk的安装，执行完成可以在命令行中执行java -version进行检查。
    
    设置java的环境变量，可以在~/.bashrc 或 /etc/profile中进行设置，但这里推荐~/.bashrc。
    执行命令 vi ~/.bashrc 后再文件中加入以下信息：
    export JAVA_HOME=/usr/java/default
    export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
    export PATH=$JAVA_HOME/bin:$PATH
    
    输入wq结束编辑后一定要记住执行 source ~/.bashrc 是变量生效。
    
    2.预编译包(.tar.gz)
    在官网下载对应的软件包，我这里的包名是jdk-8u111-linux-x64.tar.gz。执行tar -xvf jdk-8u111-linux-x64.tar.gz将其解压到当前目录。
    最后执行mv jdk-8u111-linux-x64 /usr/local/java 将解压的目录移动到指定目录。很明显这里的JAVA_HOME就是/usr/local/java.
    
    如上设置JAVA的环境变量，具体如下：
    执行命令 vi ~/.bashrc 后再文件中加入以下信息：
    export JAVA_HOME=/usr/local/java
    export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
    export PATH=$JAVA_HOME/bin:$PATH
    
    输入wq结束编辑后执行 source ~/.bashrc 是变量生效。
    
    完成上述操作后执行 java -version命令检查是否安装成功。
    
第二步，安装Jetty
    该操作一定是在你成功安装Java运行环境之后执行。由于Jetty也是预编译的安装包，因此将你下载的安装解压的指定目录后，为其设置好环境变量便可使用。
    具体如下：
    执行tar -xvf jetty-distribution-9.3.14.v20161028.tar.gz解压到当前目录
    执行mv jetty-distribution-9.3.14.v20161028 /usr/local/jetty 移动到指定目录
    执行命令 vi ~/.bashrc 后再文件中加入以下信息，设置环境变量：
    export JETTY_HOME=/usr/local/jetty
    export PATH=$JETTY_HOME/bin:$PATH
    输入wq结束编辑后执行 source ~/.bashrc 是变量生效。
    
    执行jetty.sh start 启动服务,默认端口为8080,若能在浏览器中看到欢迎首页，则说明安装成功
    
    设置为系统自启动服务（可选操作）
    
    
    
