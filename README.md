# FastDFS Client for Python

Server 版本：**6.04**

### How to Compile

编译环境：`Ubuntu 18.04`，以下步骤仅供参考：

1. 安装`libfastcommon`与`fastdfs`环境；

2. 安装`python3-dev`依赖（提供`Python.h`文件）；

3. 编译生成`FDFSPythonClient.so`文件。

一种可能的编译步骤：

```bash
readonly LIBFASTCOMMON_VERSION=1.0.42
readonly FASTDFS_VERSION=6.04

readonly LIBFASTCOMMON_DIR_NAME="libfastcommon-${LIBFASTCOMMON_VERSION}"
readonly FASTDFS_DIR_NAME="fastdfs-${FASTDFS_VERSION}"
readonly FASTDFS_CLIENT_DIR_NAME="FastDFSClient_Python"

## install requirements programmes
sudo apt install wget tar make gcc-4.8 -y
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 40
sudo update-alternatives --install /usr/bin/cc cc /usr/bin/gcc 40

# install libfastcommon
cd /usr/local/src/
sudo wget "https://github.com/happyfish100/libfastcommon/archive/V${LIBFASTCOMMON_VERSION}.tar.gz"
sudo tar xf "V${LIBFASTCOMMON_VERSION}.tar.gz"
cd "${LIBFASTCOMMON_DIR_NAME}"
sudo ./make.sh && sudo ./make.sh install

# install fastdfs
cd ../
sudo wget "https://github.com/happyfish100/fastdfs/archive/V${FASTDFS_VERSION}.tar.gz"
sudo tar xf "V${FASTDFS_VERSION}.tar.gz"
cd "${FASTDFS_DIR_NAME}"
sudo ./make.sh && sudo ./make.sh install

# install FastDFS Python Client
sudo apt install python3-dev g++-4.8 -y
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 40

cd ../
sudo git clone https://github.com/cosysun/FastDFSClient_Python.git --depth 1
cd FastDFSClient_Python/python_client
sudo make install
```

详细说明请看：[《FastDFS客户端(Python版)指南》](https://blog.csdn.net/lenyusun/article/details/44057139) 或[《接口说明文档》](./Interfaces.md)。

### Revision History

[HISTORY](./HISTORY)

