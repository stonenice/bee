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
    1.对于使用service启动的服务的系统
        1) ln -s /usr/local/jetty/bin/jetty.sh /etc/init.d/jetty 或 cp /usr/local/jetty/bin/jetty.sh /etc/init.d/jetty
        将启动脚本复制一份到init.d 目录, 上面两个命令的区别在于一个只是复制了文件的链接而不是文件本身，一个则直接是文件本身。前者的好处
        就是系统中只存在一份真实的文件，节省存储空间
        2) chkconfig --add jetty  添加服务
        3) service jetty start 启动服务，若失败可能是各种文件权限的问题，若是启动脚本的权限可以执行 chmod 755 /etc/init.d/jetty
        解决，若是其它文件或目录的权限就需要自己去发现。
        
    2.使用systemctl启动服务的系统
        1）启动脚本由原来的/etc/init.d迁移到/usr/lib/systemd下面，开机即启动的服务放在/usr/lib/systemd/system目录下。
        2）启动脚本以.service作为后缀，如jetty.service. 执行vi /usr/lib/systemd/system/jetty.service创建文件，内容
        如下：
        [Unit]
        Description=jetty - A NIO JAVA Web Server
        After=network.target remote-fs.target nss-lookup.target
 
        [Service]
        Type=forking     #指定为后台运行  
        PIDFile=/run/jetty.pid  #socket文件路径
        ExecStart=/usr/local/jetty/bin/jetty.sh start  #启动命令
        ExecReload=/bin/kill -s HUP $MAINPID
        ExecStop=/bin/kill -s QUIT $MAINPID
        PrivateTmp=true
 
        [Install]
        WantedBy=multi-user.target
        
        3）systemctl enable jetty 启用jetty服务
        4）systemctl start jetty 或 systemctl start jetty.service启动服务，启动失败则需要耐心解决
        
第三步，Web部署
    部署网站的时候可能因为不同需求需要不同的配置，如更改默认端口，将访问路径由www.example.com/helo改为www.example.com等各种要求。
    在进行部署之前先了解jetty中如何解决上面的问题是非常有用的。
    1）修改默认端口
    在jetty中有很多种方法能够修改默认端，不同的版本可能有所不同。我介绍常用的两种，如果你的目录中有${JETTY_HOME}/etc/jetty-http.xml
    文件. 你可以在文件搜索port或8080将其改为指定的端口，如80端口。若你的目录中有${JETTY_HOME}/start.ini文件，找到
    # jetty.http.port=8080的配置，取消注释，将其改为你指定的端口。如jetty.http.port=80
    
    2)修改访问路径
    在jetty中每个网站都存在一个配置文件，如在webapps里面有个网站hello,那么在${JETTY_HOME}/webapps或${JETTY_HOME}/context中
    存在一个配置文件hello.xml. 内容如下
    <Configure id="helloWebapp" class="org.eclipse.jetty.webapp.WebAppContext">
        <Set name="contextPath">/hello</Set>
        <Set name="war"><Property name="jetty.webapps" default="."/>/hello.war</Set>
    </Configure>
    
    从配置文件中可以看出contextPath就是网址的前缀或者说虚拟目录，若设为"/",则访问网站变为www.example.com/. 若设为"/hello"则
    访问地址为www.example.com/hello
    
    网站部署：
    在JavaWEB中部署可以是压缩包和目录的形式，比如需要部署hello项目。可以将hello.war或hello直接放在webapps中。两种形式的都可以。
    这里以目录的形式介绍：
    将项目hello复制到webapps中，并在其同目录下创建配置文件hello.xml.内容如下：
    <Configure id="helloWebapp" class="org.eclipse.jetty.webapp.WebAppContext">
        <Set name="contextPath">/hello</Set> 
        <Set name="war"><Property name="jetty.webapps" default="."/>/hello</Set>
    </Configure>
    
    contexPath为项目访问地址的虚拟目录，war为项目的位置，这里可以是压缩包也可以是目录.
    仔细研究war配置项可以发现配置项目部署的位置为<Property name="jetty.webapps" default="."/>/hello其可以等同于
    ${jetty.webapps}/hello来理解。由此可以看出，如果你想将项目部署在其它目录，如/var/jetty/www. 那么你的项目目录
    应该设置为<Set name="war">/var/jetty/www/hello</Set>
    
    执行脚本jetty.sh start 启动服务完成部署


    
    
    
