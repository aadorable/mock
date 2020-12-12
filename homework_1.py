# *** coding: utf-8 ***
#@Time   : 2020/12/1 17:42
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : homework_1.py

from flask import Flask, request, jsonify
from pass_through import passThrough

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/login/mock', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    if name == '不良用户':
        return jsonify({
            'data': data,
            'message': '该用户有不良记录，限制使用其他功能',
            'code': 1001
        })
    else:
        resp = passThrough(data)
        return resp

if __name__ == '__main__':
    app.run(debug=True, port=9090)