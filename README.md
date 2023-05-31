# intelligent-system

Deterministic inference 
简易的确定性推理机实现 

1. 定义准备支持的产生式语法规范；
2. 设计知识库的外部存储机制；
3. 设计事实库的内部数据结构；
4. 绘制推理机工作流程图；
5. 编码实现推理机；
6. 设计并实现相关软件界面；
7. 推理机的运行调试；

# 开发日志（碎碎念）

## 5月30日

第一次实现带UI的PY程序，有点找不到方向，调研+需求分析

## 5月31日

决定先实现UI，因为个人认为在没有UI设计基础的情况下，容易把内核写成一个命令行的版式，后面反攻，开销太大。 

鼓捣了一天UI最终选择了**<u>PYQT</u>**，看上的是可以直接进行图形设计导出UI进而生成PY文件。不过最终也走了很多曲折的路：

1. 直接的pyqt安装不可行（MacOS ，版本12.5Monterey，M2）：我编译器用的Vscode，不知道什么原因，首先是pyqt的下载，不知道怎怎么配置Qt for python 插件，后来看了经验贴，换成了pyside6，还是不行，design打不开。于是我后来意识到：“**<u>为什么我不直接下QT design</u>呢？**”，于是直接下载使用，效果看着和帖子里面配置成功的效果一样。 

这里我指出一点，我的PY版本是3.10.9，但是我看官网的PYQT5貌似最高至支持就是到3.8（貌似），如果有想要尝试的（MacOS M2），可以使用PYQT6，反正我最后放弃了。

2. UI的图形创建：第一天大概熟悉了基本操作，以及不同窗口的操作。事实上来说，我觉得从UI开始是正确的决定，因为其中的编程确实有别与之前熟悉的命令行操作，就比如你要操作一个命令行，你肯定使用不同的字符编码操作，但是变成UI，落实成对象就是另一个思路了

