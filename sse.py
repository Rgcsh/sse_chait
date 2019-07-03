# coding:utf8
# 将程序转换成可以使用gevent框架的异步程序
# from gevent import monkey
#
# monkey.patch_all()

from flask import Flask, send_from_directory, redirect, url_for, request, jsonify
from flask_sse import sse

app = Flask(__name__)
# redis路径
app.config["REDIS_URL"] = "redis://localhost"
# app注册sse的蓝图,并且访问路由是/stream1
app.register_blueprint(sse, url_prefix='/stream1')


# 重定向到发送消息页面
@app.route('/')
def index():
    return redirect(url_for('.index', _external=True) + 'upload/' + 'send_messages.html')


# 接收send_messages.html文件中接口发送的数据，并且通过sse实时推送给用户
@app.route('/messages', methods=['POST'])
def send_messages():
    channel = request.values.get('channel')
    message = request.values.get('message')

    # 关于channel的使用==> http://flask-sse.readthedocs.io/en/latest/advanced.html
    # 如channel是channel_bob，则只有channel_bob.html才能接收数据
    # sse推送消息
    sse.publish({"message": message}, type='social', channel=channel)
    return jsonify({'code': 200, 'errmsg': 'success', 'data': None})


@app.route('/upload/<path:path>')
def send_file(path):
    return send_from_directory('upload/', path)


if __name__ == '__main__':
    app.run()
