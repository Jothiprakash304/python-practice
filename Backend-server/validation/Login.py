from Database.connecting import db_validation
from flask import jsonify
from flask_jwt_extended import create_access_token
import bcrypt




def Login(Email,Password):
    user_query=('SELECT * FROM cloudpay_register_user WHERE Email=%s AND Password=%s,(Email,Password)')
    user_params=[]
    user_params.append(Email)
    user=db_validation(user_query,user_params)
    hashed=user[1]
    check=bcrypt.hashpw(Password.encode("utf8"),hashed)
    if not user or (user and not check):
        return "username and password are incorrect"
    else:
        user_query="SELECT Email FROM cloudpay_register_user INNER JOIN cloudpay_account ON cloudpay_register_user.Email=cloudpay_acount.Email"
        access=create_access_token(identity=Email)
        return{
            "Token":access,
            "message":f"login succesfully done"
        }
     










# def Login(Email,Password):
#     user_query=('SELECT * FROM cloudpay_register_user WHERE Email=%s AND Password=%s',(Email,Password))
#     user_params=[]
#     user_params.append(Email)
#     user_login=db_validation(user_query,user_params)
#     credentials=user_login[1]
#     matching_credentials=bcrypt.checkpw(Password.encode("utf8"), credentials)
#     if not user_login or (user_login and not matching_credentials) :
#         return "username and password  is incorrect"
#     else:
#         access=create_access_token(identity=Email)
#         return {
#             "Token": access,
#             "message":f"login succesfull done",

#         }



 

# or (user_login and not matching_credentials)



