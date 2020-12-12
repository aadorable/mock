# *** coding: utf-8 ***
#@Time   : 2020/12/1 17:11
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : pass_through.py

import requests
from flask import  make_response

def passThrough(data):
    url = 'http://127.0.0.1:5000/login'
    resp = requests.post(url, json=data)
    resp = make_response(resp.json())
    return resp

def passThroughRe(data):
    url = 'http://127.0.0.1:5000/register'
    resp = requests.post(url, json=data)
    resp = make_response(resp.json())
    return resp