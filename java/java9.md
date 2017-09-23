安装java9
---
1. 在官网下载java9的安装包后安装到自己的计算上，在cmd中执行java -version 等正确显示则证明安装成功。
2. java9安装后默认会将C:\ProgramData\Oracle\Java\javapath的目录加到PATH环境变量中，因此安装后直接执行java -version能生效。
但是为了方便后续使用，还是应该配置JAVA_HOME的方式来使用。在配置JAVA_HOME的时候一定要放在PATH的最前面，否则可能会出现
“ could not find java.dll”的错误，这个是安装java9与之前版本的一点小差异
