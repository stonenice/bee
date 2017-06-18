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
执行yum进行安装。如果你不知道能安装那些可以执行命令yum list|grep mysql将其列出，结果如图：
