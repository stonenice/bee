1.进行Spark开发时如何引用或安装库？
答：对于自学spark的人来说，可能会因为不知道如何打入spark的开发库，而不能完成自已的第一个HelloWorld. 若是MapReduce还好，Eclipse的hadoop
插件里就已经包含不需要你操心，或者能熟练使用maven的人也不用担心，因为差什么库就在pom.xml写上就好。但总是天工不作美啊！去网上搜spark引用库的
问题没有一个回复是正确的，最后只能自行研究。由我不会R语言，我就将java,scala,python语言的库引用写下（开发环境Eclipse）。
    java,scala: spark可以在windows下安装，将spark安装包解压后，在解压的目录下有个jars的目录，执行在Eclipse中的项目上点击右键，找到
        build path选项，将jars中的所有jar添加进去就好。
    python: 同上，解压的目录中有个python的目录，进入该目录，先找下是否存在setup.py文件，若存在执行命令python setup.py install安装。
        若文件不存在则直接将pyspark文件夹及里面的内容复制到$PYTHON_HOME/lib/site-packages. 如果你的机器上没有安装pip那么site-packages
        是不存在的，这事你可以复制到$PYTHON_HOME/lib目录下。老版本的spark中，Python库存在setup.py文件，而新版本中没有。所以存在差异。
        需要注意的是安装pyspark后还可能需安装py4j,psutil两个库才能正常运行，这里使用pip进行安装： pip install py4j , pip install psutil
