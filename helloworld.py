# *** coding: utf-8 ***
#@Time   : 2020/11/30 20:42
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : helloworld.py

'''
pip install flask
请求
methods=['POST']
post: 请求参数json,接口如何获取这个参数值呢？request.get_json()  返回值是字典
form表单   request.form.to_dict()

get:
request.args.to_dict()
响应
1,2,4是必须要掌握的
1. return 字符串
2. jsonify()  返回json数据
3. redirect(url_for(获取资源的函数的名字))  重定向
4. 自己构造响应值 make_response()
5. 前后端不分离想写页面 render_template(xxx.html)

接口： 映射关系，一个url地址对应着一个资源，(资源所对应的函数叫视图)视图的名字不能重复
'''

# 导包
from flask import Flask, jsonify, request, redirect, url_for, make_response

# 创建APP 应用
app = Flask(__name__)

# 定义第一个接口 url：/index  返回的资源，也就是响应：字符串‘hello world’
# 通过@app.route(url, 请求参数)来定义URL地址
# 第一个参数是定义的URL，第二个参数时请求方法，不写默认是get方法
@app.route('/index')
def index():          # 定义一下/index这个url地址返回的资源是什么
    return 'hello world'

@app.route('/login', methods=['POST', 'GET'])  # 既支持post接口，也支持get接口
# @app.route('/login', methods=['POST'])  # 只支持post接口
def login():
    '''
    json类型的数据
    :return: 
    '''
    # data = request.get_json()  # 请求参数是json的数据
    # data = request.form.to_dict() # 请求参数是form-data的数据
    data = request.args.to_dict()  # get请求参数的数据
    # 主要做逻辑判断
    return jsonify({
        'code': 10001,
        'msg': 'success',
        'data': data
    })

@app.route('/demo')
def demo():
    return redirect(url_for('index'))

@app.route('/login2')
def login2():
    resp = make_response(redirect(url_for('index')))
    # 给响应设置cookie值，set_cookie进行一个设置
    # 响应.set_cookie(键，值)
    resp.set_cookie('testfan-id', '234354353434534')
    return resp

@app.route('/query')
def query():
    # request.cookies 类似字典，获取所有的cookie值
    data = request.cookies.get('testfan-id')
    return jsonify({
        'code': 10001,
        'msg': 'success',
        'data': data
    })

@app.route('/list')
def list():
    data = request.args.to_dict()
    return jsonify({
        'code': 1001,
        'data': data,
        'msg': 'success'
    })


if __name__ == '__main__':
    # http://127.0.0.1:5000/ 默认的端口号是5000
    # 启动，必须要写
    # app.run() # 这样启动，就是你更改的代码不会自动加载
    app.run(debug=True, port=8888)