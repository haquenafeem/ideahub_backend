from flask import Blueprint, request, jsonify
from passlib.hash import sha256_crypt
from ideahub import app
from ideahub.db import db
from ideahub.users.models import User
import jwt


users = Blueprint('users',__name__,url_prefix='/users')

@users.route('/')
def user():
    return ('user route123')

@users.route('/api')
def api():
    return 'HelloWorld'

@users.route('/login', methods=['POST'])
def login():

    content = request.get_json()

    email = content['email']
    passwordi = content['password']

    user = User.query.filter_by(email=email).first()

    if user:
        val = sha256_crypt.verify(passwordi, user.password)
        if val:
            payload = {
            'username' : user.email
            }
            token = jwt.encode( payload, app.config.get('SECRET_KEY'),algorithm='HS256' )
            return jsonify({"token": token.decode('UTF-8')})
        else :
            return jsonify({"Wrong Login":"Password Incorrect"})    
    else :
        return jsonify({"Sorry" : "no user found"})  


@users.route('/signup', methods=['POST'])
def signUp():
    content = request.get_json()

    username = content['username']
    email = content['email']
    password = sha256_crypt.encrypt(content['password'])
    admin= False

    push = User(username=username,email=email,password=password, is_admin=admin)

    db.session.add(push)
    db.session.commit()

    payload = {
        'username' : email
     }
    token = jwt.encode( payload, app.config.get('SECRET_KEY'),algorithm='HS256' )
    return jsonify({"token": token.decode('UTF-8')})        
 