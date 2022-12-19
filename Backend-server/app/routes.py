from flask import request,make_response
from app import app
from validation.validation import Register
from validation.Login import Login
from Database.connecting import db_validation
from Database.connecting import db_valid
from Database.connecting import db_validation_withdraw
import datetime
from datetime import date
import re




@app.route ('/Register',methods=["POST"])
def Register_data():
    data=request.get_json()
    First=data["First_name"]
    Last=data["Last_name"]
    Email=data["Email"]
    # DOB=data["Dob"]
    Password=data["Password"]
    Confirm_password=data["Confirm_password"]
    Response=Register(First,Last,Email,Password,Confirm_password)

    return make_response(Response)


@app.route ('/login', methods=["POST"])
def Login_data():
    data=request.get_json()
    Email=data["email"]
    Password=data["password"]
    response=Login(Email,Password)
    return make_response(response)

@app.route ('/add', methods=["POST"])
def add_money():
    data=request.get_json()
    card_number=data["Add"]
    expiry=data["expiry"]
    cv=data["CVV"]
    amount=data["Amount"]
    m_number=data["Mobile_number"]
    save=data["save_details"]
    is_validation=valid(card_number,expiry,cv,amount,m_number,save)
    if is_validation == True:
        db_insert=valid(amount)
def valid(amount):
    user_query="""ALTER TABLE details(amount=amount+amount) VALUES (%d)"""
    user_params=[]
    user_params.extend([amount])
    db_insert=db_valid(user_query,user_params)
    if "error" in db_insert:
        return "error"
    else:
        return "success"
    
def valid(card_number,expiry,cv,amount,m_number,save):
    if len(card_number)<=15:
        return "enter the valid card details"
    today=date.today()
    if today.year<=expiry.year:
        return "your card is expired"
    if len(cv)<3 and len(cv)>3:
        return "enter the proper cv"
    if amount==0:
        return "enter the amount"
    regex=re.compile("(0|91)?[6-9][0-9]{9}")
    if not re.fullmatch(regex,m_number):
        return "enter valid mobile number"
    return True


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
    db_response=db_validation_withdraw(user_query,user_params)
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





    
        




    
    

