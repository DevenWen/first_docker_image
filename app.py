#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2021/06/05 23:18:50
@Author  :   wenkangqiang :)
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from flask import Flask
import socket
import os


app = Flask(__name__)

@app.route('/')
def hello():
    html = """
           <h3>Hello {name}!</h3>  
           <b>Hostname:</b> {hostname}<br/>
           """
    return html.format(name = os.getenv('NAME', "world"), hostname = socket.gethostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)