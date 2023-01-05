from flask import request,make_response,jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_jwt_extended import create_access_token
from app import app
from validation.Login import Login
from Database.connecting import db_validation
import datetime
from datetime import date
from datetime import datetime
import re
import mysql
import bcrypt
from dateutil.relativedelta import relativedelta





@app.route ('/Register',methods=["POST"])
def Register_data():
    data=request.get_json()
    First=data["First_name"]
    Last=data["Last_name"]
    Email=data["Email"]
    DOB=data["Dob"]
    Password=data["Password"]
    Confirm_password=data["Confirm_password"]
    Response=Register(First,Last,Email,DOB,Password,Confirm_password)
    return make_response(Response)


def Register(First,Last,Email,DOB,Password,Confirm_password):
     if not validate_name(First):
         return "enter the proper name"
     if not validate_lastname(Last):
         return "enter the proper last name"
     if not validate_Email(Email):
         return "enter the proper email id"
     if not validate_birth(DOB):
         return "Please enter the proper date of birth"
     if not validate_password(Password):
         return "please enter the proper password"
     if Password!=Confirm_password:
         return "password mismatch"
     return DB_query(First,Last,Email,DOB,Password)





def DB_query(first,last,email,dob,password):
    user_query="""INSERT INTO cloudpay_register_user (FirstName,LastName,Email,Dob,Password) VALUES (%s, %s, %s, %s,%s)"""
    user_params=[]
    user_params.extend([first,last,email,dob])
    var=bcrypt.gensalt(10)
    secured_password=bcrypt.hashpw(password.encode("utf8"),var)
    user_params.append(secured_password)
    db_res=db_validation(user_query,user_params)
    if "error" in db_res:
        return"some error happen"
    else:
        Access=create_access_token(identity=email)
        return (jsonify(Access))
def validate_name(first):
    if first.isnumeric():
        return False
    if " " in first:
        return False
    if first.isalnum():
        return True
def validate_lastname(Last):
    if Last.isnumeric():
        return False
    if " " in Last:
        return False
    if Last.isalnum():
        return True
def validate_Email(email):
    regex=regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.fullmatch(regex,email)
def validate_birth(birth):
    date_format = '%Y-%m-%d'
    dateobject=datetime.strptime(birth,date_format)
    return True
 
           
def validate_password(password):
    regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    return re.fullmatch(regex,password)

    







@app.route ('/login', methods=["POST","GET"])
def Login_data():
    data=request.get_json()
    Email=data["email"]
    Password=data["password"]
    response=Login(Email,Password)
    return make_response(response)
# def Login(Email,Password):
#     cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute("SELECT * FROM cloudpay_register_user WHERE = %s AND Password= %s",(Email,Password))
#     details=cursor.fetchone()
#     if details:
#         # session['loggedin']== True
#         # session['id']=details['Email']
#         return "Login Successfully done"
#     else:
#         return "Email or password incorrect"

@app.route ('/add', methods=["POST"])
def add_money():
    data=request.get_json()
    card_number=data["Add"]
    expiry=data["expiry"]
    cv=data["CVV"]
    amount=data["Amount"]
    m_number=data["Mobile_number"]
    # save=data["save_details"]
    is_validation=valid(card_number,expiry,cv,amount,m_number)
    return make_response(is_validation)
def valid(card_number,expiry,cv,amount,m_number):
    if not validate_card(card_number):
        return "Enter the valid card number"
    if not validate_expiry(expiry):
        return "your card is expired"
    if not validate_cv(cv):
        return "invalid cvv"
    if not validate_money(amount):
        return "you have insufficient balance"
    if not validate_mobile(m_number):
        return "mobile number invalid"
def validate_card(card):
     if card.isnumeric():
        return True
     if " " in card:
        return True
     if len(card)>=16:
        return True
     
def validate_expiry(date):
     date_format = '%m/%y'
     format=datetime.strptime(date,date_format)
     return True
    
def validate_cv(cv):
    if cv.isnumeric():
        return True
    if " " in cv:
        return True
    if len(cv)==3:
        return True
     
def validate_money(money):
    return True
def validate_mobile(number):
    regex="^\\+?[1-9][0-9]{7,14}$"
    return re.fullmatch(regex,number)  


@app.route ('/minus', methods=["POST"])
def withdraw_money():
    data=request.get_json()
    account=data['']
    ifsc=data['']
    a_name=data['']
    m_number=data['']
    amount=data['']
    is_validation=validation(account,ifsc,a_name,m_number,amount)
    if is_validation == True:
        db_insert=db_minus(amount)
        if db_insert==True:
            return "success"
def db_minus(amount):
    user_query="UPDATE details WHERE Amount=Amount-amount"
    user_params=[]
    user_params.extend([amount])
    db_response=db_validation(user_query,user_params)
    if "error" in db_response:
        return "error"
    else:
        return "success"

def validation(account,ifsc,a_name,m_number,amount):
    if len(account)<11:
        return "please enter the valid account number"
    if not ifsc.isalnum():
        return "IFSC code is mismatch"
    if a_name==int and len(a_name)<=2:
        return "Please enter the proper name"
    if not validate_number(m_number):
        return "mobile number is invalid"
    if not validate_amount(amount):
        return "Sorry unable to process you have minimum balance"
def validate_number(m_number):
    regex=re.compile("(0|91)?[6-9][0-9]{9}")
    return re.fullmatch(m_number,regex)
def validate_amount(amount):
    amount_1="SELECT amount FROM details WHERE amount=?"
    if amount_1>=amount:
        return True
@app.route ('/send', methods=["POST"])
def send_money():
    return True





    
        




    
    

# class valid(card_number,expiry,cv,amount,m_number,save):
#     # def __init__(self,card_number,expiry,cv,amount,m_number,save):
#     #     self.card=card_number
#     #     self.number=expiry
#     #     self.CV=cv
#     #     self.Amount=amount
#     #     self.M_number=m_number
#     #     self.Save=save