# Flask + Vue 实现前后端分离个人博客

### 注意

这仅仅只是一个Demo，其中还有很多问题没有解决。另外，前端界面所显示的内容，并不代表后端已经实现了。

### 主要技术栈

* `Flask-Restful`，用于开发`Restful api`
* `Vue.js`, 实现前端页面
* `Bulma`, 前端UI框架

### 使用

将代码克隆到你的电脑，进入`flask-api`目录，使用`requirements.txt`安装`python`库后

以下操作在目录`flask-api`进行。终端命令：

1. `flask init`按照提示初始化博客，包括用户名和密码。注意这是一个单用户的博客。
2. `flask fakedata -a 100 -c 10 -t 10` 虚拟100个文章，10个分类，10个标签。
3. `flask run`运行程序

进入`vue-page`目录，终端命令：

1. `npm run serve`

最后浏览器打开`127.0.0.1:8080`即可看到页面。

### demo截图

[](https://github.com/laodiaoyadashu/flask-vue-blog/blob/master/images/QQ20200324-110847%402x.png)



