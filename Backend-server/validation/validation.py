from flask import jsonify
import re
import datetime
from datetime import date
from Database.connecting import db_validation


def Register(First,Last,Email,Password,Confirm_password):
    user_data_validation=Valid(First,Last,Email,Password,Confirm_password)
    if user_data_validation == True:
        db_insert=add_database(First,Last,Email,Password)
        return db_insert
       
    else:
        return "invalid"
def add_database(First,Last,Email,Password):
    user_query="""INSERT INTO Register (FirstName, LastName, Email,DOB,CREDENTIALS) VALUES (%s, %s, %s, %s, %s)"""
    user_params=[]
    user_params.extend([First,Last,Email,Password])
    db_res=db_validation(user_query,user_params)
    print(db_res)
    if "error" in db_res:
        return "error"
    else:
        return "success"
    



def Valid(First,Last,Email,Password,Confirm_password):

    if not validate_First_name(First):
        return "enter the first name"
    if not validate_Last_name(Last):
        return "enter the Last name"
    # if not validate_DOB(DOB):
    #     return "your are below the age of our Requirements"
    if not validate_email(Email):
        return f"Please enter {'Email'} email id"
    if not validate_password(Password):
        return f"Please enter valid {'Password'} password"
    if Password!=Confirm_password:
        return "password mismatch"
    return True




def validate_First_name(First):
    if(len(First)>5):
        return True
def validate_Last_name(Last):
    if(len(Last)>5):
        return True
# def validate_DOB(DOB):
#       today = date.today()
#       age = today.year - DOB.year -((today.month, today.day) <(DOB.month, DOB.day))
#       if age>=18:
#         return True
def validate_email(Email_id):
    regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.fullmatch(regex,Email_id)

def validate_password(Password):
    if (len(Password)>10):
        return True
   
