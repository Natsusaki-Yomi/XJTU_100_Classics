# XJTU“一百本书”自动填写脚本

此脚本能够爬取nsa系统中对书籍的描述，自动将其填入“评价”一栏并保存提交。下图展示了脚本的运行效果。

![Description](https://p.inari.site/guest/23-04/06/642ed878a1b28.png)

![Result](https://p.inari.site/guest/23-04/06/642ed88f7c88c.png)

## 使用方法

##### 0. 安装Selenium：

```sh
pip install selenium
```

##### 1. 安装Chrome及其驱动：

安装Chrome后，在地址栏中输入

```
chrome://settings/help
```

查询Chrome版本。例如下图的Chrome版本为112.0.5615.50。

![Chrome_Ver.](https://p.inari.site/guest/23-04/06/642ed8c764efe.png)

根据查到的版本号，到[Chrome驱动网站](https://chromedriver.storage.googleapis.com/index.html)下载对应的驱动文件，并将解压后的路径加入系统环境变量。

##### 2. 运行脚本

```sh
python 100_Classics.py
```
