from Database.connecting import db_validation
from flask import jsonify


def Login(Email,password):
    verify_details_query="SELECT EMAIL, PASSWORD FROM REGISTER WHERE EMAIL= %S"
    verify_detail_params=[]
    verify_detail_params.append(Email,password)
    user_login=db_validation(verify_details_query,verify_detail_params).fetchone()
    if not user_login:
        return "username and password  is incorrect"
    else:
        return "Login successful for",user_login(Email)








