# *** coding: utf-8 ***
#@Time   : 2020/12/2 17:23
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : server.py

from flask import Flask, request, jsonify
from logindemo.tools import write_csv, read_csv

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/login', methods=['POST'])
def login():
    '''
    登录接口
    :return: 
    '''
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({
            'code': 404,
            'message': '无效的参数:name',
            'data': data
        })
    if 'password' not in data or not data['password']:
        return jsonify({
            'code': 404,
            'message': '无效的参数:password',
            'data': data
        })
    name = data['name']
    pwd = data['password']
    try:
        if read_csv(name, pwd):
            return jsonify({
                'code': 200,
                'data': data,
                'message': '登录成功'
            })
        else:
            return jsonify({
                'code': 401,
                'data': data,
                'message': '用户不存在或密码错误'
            })
    except Exception as e:
        return jsonify({'data': data, 'message': "未知异常", 'code': 500})


@app.route('/register', methods=['POST'])
def register():
    '''
    注册接口
    :return: 
    '''
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({
            'code': 404,
            'message': '无效的参数:name',
            'data': data
        })
    if 'password' not in data or not data['password']:
        return jsonify({
            'code': 404,
            'message': '无效的参数:password',
            'data': data
        })
    name = data['name']
    pwd = data['password']
    try:
        write_csv(name, pwd)
        if read_csv(name, pwd):
            return jsonify({
                'code': 200,
                'data': data,
                'message': '注册成功'
            })
        else:
            return jsonify({
                'code': 401,
                'data': data,
                'message': '注册失败'
            })
    except Exception as e:
        return jsonify({
            'code': 204,
            'data': data,
            'message': e
        })

if __name__ == '__main__':
    app.run(debug=True, port=5001)