# Flask + Vue 实现前后端分离个人博客

### 说在前面

这仅仅只是一个Demo，其中还有很多功能没有实现。

### 主要技术栈

* `Flask-Restful`，用于开发`Restful api`
* `Vue.js`, 实现前端页面
* `Bulma`, 前端UI框架

### 使用

你需要python3.7 和 node@14的运行环境。
将代码克隆到你的电脑，进入`flask-api`目录

以下操作在目录`flask-api`进行。终端命令：

1. `pip install -r requirements.txt`安装python依赖库
2. `flask init`按照提示初始化博客，包括用户名和密码。注意这是一个单用户的博客。
3. `flask fakedata -a 100 -c 10 -t 10` 虚拟100个文章，10个分类，10个标签。
4. `flask run`运行程序
你还可以使用`flask --help`查看其它命令。

进入`vue-page`目录，终端命令：
中国用户建议使用cnpm安装依赖库
1. `npm install`, 安装依赖库 
2. `npm run serve`

最后浏览器打开`127.0.0.1:8080`即可看到页面。`127.0.0.1:8080/admin`可进入后台管理页面，账号密码为`flask init`初始化的账号密码.


### demo截图

<img src="https://s1.ax1x.com/2020/03/24/8b7aZ9.png" alt="QQ20200324 110847@2x" border="0">
<img src="https://s1.ax1x.com/2020/03/24/8b7wI1.png" alt="QQ20200324 110909@2x" border="0">
<img src="https://s1.ax1x.com/2020/03/24/8b7NqJ.png" alt="QQ20200324 110924@2x" border="0">
<img src="https://s1.ax1x.com/2020/03/24/8b7tr4.png" alt="QQ20200324 111029@2x" border="0">
<img src="https://s1.ax1x.com/2020/03/24/8b7Man.png" alt="QQ20200324 111057@2x" border="0">
<img src="https://s1.ax1x.com/2020/03/24/8b7gqH.png" alt="QQ20200324 111045@2x" border="0">

