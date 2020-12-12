# *** coding: utf-8 ***
#@Time   : 2020/12/1 17:11
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : api_mock.py
'''
todo 1 做一个mock服务的挡板，增加了黑名单的功能，返回值要返回{'data':请求参数携带的数据，‘msg’:’您已经被我们公司加入黑名单‘,'code':1001}
todo 2 透传 ---保留原来的功能，保留原来登录成功的一些功能(被测项目现有登录接口的功能是要保留,...)
'''

from flask import Flask, request, jsonify
from pass_through import passThrough, passThroughRe

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/login/mock', methods=['POST'])
def login():
    '''
    实现黑名单功能，为了让流程走的通，eg:为了
    让下订单接口对于黑名单用户不开放(根据你的登录接口的返回值做判断)
    :return:
    '''
    data = request.get_json()
    name = data.get('name')
    if name == '黑名单':
        return jsonify({
            'code': 1001,
            'message': '您已被加入黑名单，无法登录！',
            'data': data
        })
    else:
        resp = passThrough(data)
        return resp

## 透传注册功能
##url保存，port号不一样没有关系,最好url是要保存之前/register
###新知识点:获取动态路由<变量> 默认变量是字符串类型  <int:变量>  变量是int类型
@app.route('/<func>', methods=['POST'])
def register(func):
    data = request.get_json()
    if func == 'register':
        resp = passThroughRe(data)
        return resp

if __name__ == '__main__':
    app.run(debug=True, port=9999)