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