#!/usr/bin/env python
from flask import Flask, render_template


from OpenSSL import SSL
# context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')

import urllib
import json
import os

import pdb,json
from random import randint
import ast
from flask import Flask
from flask import request
from flask import make_response
import requests, json
import datetime
from flask_simple_ui import UI

# Flask app should start in global layout
app = Flask(__name__)
ui = UI(app)

# db = pymysql.connect('localhost','root','','umd')
# client = base.Client(('localhost', 11211))
# days = {0:"%%M%", 1:"%Tu%", 2:"%%W%", 3:"%Th%", 4:"%%F%", 5:"%%Sa%", 6:"%%Su%"}
@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')


@app.route('/loan_predictor', methods=['GET'])
def loan_predictor():
    return render_template('/Readme.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    suggestion=[]
    app.run(debug=True, port=port, host='0.0.0.0')