#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, decode_token, get_jwt_identity
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import threading
import jwt, os
from config import *

# Setup flask
app = Flask(__name__)
 
app.config['JWT_SECRET_KEY'] = "TEST"
FLAG = os.getenv('FLAG')
jwtmanager = JWTManager(app)
blacklist = set()
lock = threading.Lock()
 
# Free memory from expired tokens, as they are no longer useful
def delete_expired_tokens():
    with lock:
        to_remove = set()
        global blacklist
        for access_token in blacklist:
            try:
                jwt.decode(access_token, app.config['JWT_SECRET_KEY'],algorithm='HS256')
            except:
                to_remove.add(access_token)
       
        blacklist = blacklist.difference(to_remove)
 
@app.route("/")
def index():
    return "POST : /login <br>\nGET : /admin"
 
# Standard login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
    except:
        return jsonify({"msg":"""Bad request. Submit your login / pass as {"username":"username","password":"password"}"""}), 400
 
    if len(username) > 15:
        return jsonify({"msg":"Username is too long"}), 400
    isTempUser = True
    if username == 'admin' and password == FLAG:
        isTempUser = False
    else:
        username = username + "_temp"

    access_token = create_access_token(identity=username,expires_delta=datetime.timedelta(minutes=3))
    ret = {
        'access_token': access_token,
    }
   
    if isTempUser:
        with lock:
            blacklist.add(access_token)

    return jsonify(ret), 200
 
# Standard admin endpoint
@app.route('/admin', methods=['GET'])
@jwt_required()
def protected():
    access_token = request.headers.get("Authorization").split()[1]
    username = get_jwt_identity().lower()
    # If username is too long, just cut it!
    if len(username) > 20:
        username = username[:20]
    with lock:
        if access_token in blacklist:
            return jsonify({"msg":"Token is revoked"})
        else:
            if (username[-5:]) == '_temp':
                return jsonify({'message:': 'Hi Temporary User: ' + username[:-5]})
            else:
                return jsonify({'Welcome back, here your flag!:': FLAG})
 
 
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(delete_expired_tokens, 'interval', seconds=3*60)
    scheduler.start()
    app.run(debug=False, host='0.0.0.0', port=5000)