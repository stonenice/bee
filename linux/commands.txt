命令:ps
常用参数：
1.ps -aux 查看系统中正在运行的进程

命令:netstat
常用参数:
1.netstat -tunlp 查看系统中正在监听的所有端口

命令:kill
常用参数:
1.kill -s 9 1023 向进程号(pid)1023的进程发送中止的信号

命令:killall
常用参数:
1.killall mysql 结束所有名为mysql的进程

tar
---
> 需要注意的是，在进行压缩时如果只想包含相对路径而不是绝对路径，必须使用-C的选项。在解压*.tar.gz2时，需要检查系统是否按照了bzip2，如果没有按照-j选项将不可用。

1) *.tar.gz或*.tgz都是gzip的压缩算法，压缩命令为:tar -cvf test.tar.gz -C /opt test/ 解压命令为: tar -xvf test.tar.gz
2) *.tar.bz2 在解压前需要安装bzip2. 压缩命令为:tar -jcvf test.tar.gz2 -C /opt test/ 解压命令为: tar -jxvf test.tar.gz2 (bzip2 test.tar.gz2)
3) *.tar.xz, 压缩命令为:tar -Jcvf test.tar.xz -C /opt test/ 解压命令为: tar -Jxvf test.tar.xz

