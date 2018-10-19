此项目通过flask_see实现了SSE功能

SSE:服务器发送事件，传统http请求中，服务方都是被动的接受请求，然后发送数据。但是无法做到服务端主动发送请求给客户端，然而有些时候需要此功能。因此有了SSE或者Websocket技术来实现。SSE实现方式的是半双工，只能在连接建立后服务端发送数据给客户端，相反不行。（Websocket可以）

flask_sse官方文档: http://flask-sse.readthedocs.io/en/latest/index.html

博客网址: http://www.cnblogs.com/rgcLOVEyaya/p/RGC_LOVE_YAYA_624days.html

开启服务方法：

  第一种方法：通过gevent+uWSGI服务器
            运行 start_project.sh 脚本

  第二种方法: 通过gevent+gunicorn服务器
             进入到sse.py目录,输入  gunicorn sse:app --worker-class gevent --workers 4 --bind 127.0.0.1:5000  运行

项目使用方法：

打开 127.0.0.1:5000/ 跳转到send_messages.html页面
接着打开 channel_bob.html,channel_public.html,channel_tom.html页面
在send_messages.html页面输入channel和message后，点击按钮，会发现对应的channel页面会显示发送的信息。

由此证明SSE正常工作!
