1、复制文件夹

复制ClientForPython到FastDFS源代码client目录下


2、复制json库
cp json/lib/* /usr/local/lib/
ldconfig


3、接入client目录下 执行Make

make

4、进入ClientForPython，生成.so文件
