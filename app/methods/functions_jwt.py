from ast import Import
# from base64 import encode, decode
# from hashlib import algorithms_available, algorithms_guaranteed
from http.client import ImproperConnectionState
from datetime import datetime, timedelta
# from os import getenv
import jwt
import app.models as models
from fastapi.responses import JSONResponse
from sqlalchemy import true

def expire_date(days: int):
    return datetime.now() + timedelta(milliseconds=days)

secret = 'dnVvODY4Yzc2bzhzNzZqOG83czY4b2Nq'

def write_token(data: models.Cuenta):
    payload= {"cuenta_id":data.id, "exp": expire_date(1000)}
    token = jwt.encode(payload=payload, key=secret, algorithm="HS256")
    return token

'''
def write_token(data: dict):
    token_bytes = encode(data, secret, algorithm='HS256')
    return token_bytes
'''

def validate_token(token):
    try:
        jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)
    except jwt.InvalidTokenError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)

'''
def validate_token(token):
    try:
        response = decode(token, secret, algorithms=['HS256'])
        return response
    except exceptions.DecodeError:
        return "Token no valido"
'''