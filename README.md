# 使用说明(简陋版)
## 推送更新
* 在本地编写好rst文件后通过make clean->make html编译出html文件
* 将build/html内所有内容复制到docs文件夹内
* 将所有内容push到github中publish分支即可完成更新

## 子目录or子子目录
* 创建source/subdir_name/xxx.rst
* 在source/index.rst文件中添加子目录的相对路径(具体可查看index.rst中实例)
* 子子目录即在source/subdir_name/xxx.rst中添加子子目录的路径(套娃操作)

## 注意
* 请在docs文件夹内创建.nojekyll文件！！！！(非常重要)
* 请先将测试内容推送到master分支，通过gitpage渲染后检查没有问题，再推送到publish稳定分支并更新gitpage分支位置
* 如果通过git clone到本地进行开发记得在source文件夹下创建_static和_templates两个文件夹后再进行make html

```
$ cd source
$ mkdir _static
$ mkdir _templates
$ cd ..
$ make clean
$ make html
$ rm -rf docs/*
$ touch docs/.nojekyll
$ cp -r build/html/* docs/
```



# 文档编辑帮助文档：

## 1.准备编辑/管理工具：

需要准备的工具/程序有：`GitHub Desktop`，`Typora`，`Pandoc`， `Anaconda`

下载链接如下(有的资源可能需要科学上网)：

`GitHub Desktop`：[Download GitHub Desktop | GitHub Desktop](https://desktop.github.com/download/)

`Typora`：提供阿里云盘链接：https://www.alipan.com/s/scBVDTNhKJ7   提取码：w6d0

`Pandoc`：[Pandoc - Installing pandoc](https://pandoc.org/installing.html)   提供阿里云盘链接：https://www.alipan.com/s/scBVDTNhKJ7   提取码：w6d0

`Anaconda`: [Download Anaconda Distribution | Anaconda](https://www.anaconda.com/download) 提供云盘：https://www.alipan.com/s/scBVDTNhKJ7   提取码：w6d0

`Anaconda环境`：[Download Anaconda Distribution | Anaconda](https://www.anaconda.com/download) 提供云盘：https://www.alipan.com/s/scBVDTNhKJ7   提取码：w6d0

## 2.配置工作环境：

### a. GitHub Desktop:

​		按照安装程序自带指导安装即可

### b. Typora:

​		按照安装引导程序安装即可

### c. Pandoc:

​		按照安装引导程序安装即可。安装完成后需要重启一次电脑

### d. Anaconda:

​		参考链接：[Anaconda超详细安装教程（Windows环境下）_conda安装-CSDN博客](https://blog.csdn.net/fan18317517352/article/details/123035625)

使用下面命令导入环境：

```powershell
conda create --name new_environment_name --file env.tar
#[环境压缩包见上面网盘链接]
```

### e. Sphinx

​		打开`Anaconda Prompt`，新建一个`conda`环境：

```cmd
conda create -n HITSCC python=3.10
#----------等待安装完成-------------
conda activate HITSCC
pip install sphinx -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
pip install furo -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

至此，我们已经很快速的完成了环境的准备工作，下面进入开发环节。

## 3.`github`仓库同步：

​		GitHub仓库的管理可以使用`Git Bash`，`VSCode中的Git插件`，`GitHhub Desktop `。为了方便直观地使用这里使用`GitHhub Desktop `。

​		接下来，我们将HIT-SCC社团的仓库代码克隆到本地，此后我们在本地进行编辑之后将内容提交到GitHub仓库。

1. 直接将仓库内容克隆下来

   ```powershell
   git clone https://github.com/HIT-SCC/scc.hit.edu.cn.git
   ```

2. 进入工作目录下，第一层级目录有如下文件结构：

   ```
   Mode                 LastWriteTime         Length Name
   ----                 -------------         ------ ----
   d-----         2024/7/27     21:47                build
   da----         2024/7/27     21:47                docs
   d-----         2024/7/27     21:47                source
   -a----         2024/7/27     21:47             54 init.bat
   -a----         2024/7/27     21:46            804 make.bat
   -a----         2024/7/27     21:46            658 Makefile
   -a----         2024/7/27     21:55           4581 README.md
   -a----         2024/7/27     21:10            108 run.bat
   -a----         2024/7/27     21:10             94 run.sh
   ```

3. 尝试运行一次编译：

   ```powershell
   make clean
   make html
   ```

4. 将build/html中内容复制到/docs中并进行提交

## 4.编辑页面并发布：

  	   编辑页面使用`typora`对`Markdown`文件进行编辑，然后导出为`reStructuredText`文本，将文本至于`source`对应目录下。接着执行上述步骤3与步骤4。

## 5.本地预览：

1.命令行进入`./docs`目录，然后运行下面命令在本地开启网页服务：

```powershell
python -m http.server --directory ./docs
```

​         默认在本地`8000`端口会部署该网页服务，使用`http://localhost:8000`即可进行访问

2.直接用`Microsoft Edge`打开`index.html`文件

## 6.自动运行：

完成编辑将新的`.rst`文件添加到对应文件目录，然后在工作目录下运行脚本`run.bat`

# Appendix:

## 1.多目录文件结构：

- 创建source/subdir_name/xxx.rst
- 在source/index.rst文件中添加子目录的相对路径(具体可查看index.rst中实例)
- 子子目录即在source/subdir_name/xxx.rst中添加子子目录的路径(套娃操作)