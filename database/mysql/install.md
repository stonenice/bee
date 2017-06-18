MySQL安装笔记
===
>MySQL一直在更新，然而对应的文档确实很久以前的。就比如你想安装最新的MySQL5.7一样，网上的资料还停留在5.1的年代。
>抱着好东西就要分享的态度，也方便自己那天忘了有地方查找特将MySQL5.7的最新安装方法记录下来。本笔记会持续更新与MySQL
>的最新版本保持一致。

**操作系统：** CentOS7

YUM工具安装
---
1. 在百度、谷歌上搜索MySQL进入MySQL的官网, 在下载页面下载与你系统对应的安装包。我这里需要下载centos7的rpm安装包，
安装包名为mysql57-community-release-el7-11.noarch。如果使用wget不好下载，你可以先下载到你的windows机器上，再利用
linux命令rz上传到你的机器上。（如果机器上没有rz命令需要执行yum install lrzsz命令进行安装）

2. 在机器上找到的rpm安装包，然后执行rpm -ivh mysql57-community-release-el7-11.noarch安装到你的机器上，完后你才可以
执行yum进行安装。如果你不知道能安装那些可以执行命令yum list|grep mysql将其列出，最后执行命令进行安装，命令如下：
yum install mysql-community-client mysql-community-server mysql-community-devel

3. 完成安装后，执行命令mysql -V 检查是否安装成功，如果安装成功就可以执行命令：systemctl start mysqld(service mysqld start)
启动MySQL服务。

4. 相信很多人都会遇到，服务启动后不知道登录密码是多少。以前可能还可以看网上的说的的执行mysqld_safe --skip-grant-tables进行免密
登录。而MySQL5.7连mysqld_safe的命令都没有，唯一的解决方法还是去查看官方文档：https://dev.mysql.com/doc/refman/5.7/en/linux-installation-yum-repo.html 。具体方法是，MySQL5.7在第一服务启动时会将初始密码写到mysqld.log中，你需要执行命令：grep 'temporary password' /var/log/mysqld.log
查到登录密码。之后便可以愉快的执行mysql -u root -p啦。

5. 登录系统后，如果你执行show databases; 系统会报错， 报错的原因是让你修改密码。 这是你需要执行命令：
ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass4!'; 进行重置密码， 需要注意的是MySQL5.7对密码的强度进行限制，简单的密码
是不允许设置的，密码必须包含字母大小写与数字。

6. 执行命令添加一个远程用户，不然远程连接数据库是不行的。

7. 如果你远程用户创建好了但没有在防火墙中将3306端口对外开放也是不能连接的。CentOS7.x开放端口如下：
1）firewall-cmd --zone=public --add-port=3306/tcp --permanent
2）firewall-cmd --reload
