## 使用说明(简陋版)
### 推送更新
* 在本地编写好rst文件后通过make clean->make html编译出html文件
* 将build/html内所有内容复制到docs文件夹内
* 将所有内容push到github中publish分支即可完成更新

### 子目录or子子目录
* 创建source/subdir_name/xxx.rst
* 在source/index.rst文件中添加子目录的相对路径(具体可查看index.rst中实例)
* 子子目录即在source/subdir_name/xxx.rst中添加子子目录的路径(套娃操作)
